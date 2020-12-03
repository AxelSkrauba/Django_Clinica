from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from Pacientes.models import Patients
from .models import Product, Order
from Usuarios.models import UserModuleProfile

from .forms import ProductForm, ProductGlassesForm, OrderForm
# Create your views here.


class Product_new(CreateView):
    ver = True
    model = Product
    form_class = ProductForm
    template_name = 'Ventas/product_new.html'
    success_url = reverse_lazy('product')


class Product_edit(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'Ventas/product_edit.html'
    success_url = reverse_lazy('product')

    def get_context_data(self, **kwargs):
        """
        Si se califica como Lente, se tienen las demás opciones solicitadas.
        """
        context = super(Product_edit, self).get_context_data(**kwargs)
        if self.request.POST:
            if self.object.is_glasses:
                context['form'] = ProductGlassesForm(
                    self.request.POST, instance=self.object)
            else:
                context['form'] = ProductForm(
                    self.request.POST, instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form = context['form']
        if form.is_valid():
            self.object = form.save()
            form.instance = self.object
            form.save()
        if self.object.is_glasses and (self.object.side is None):
            return self.render_to_response(self.get_context_data(form=form))
        else:
            return super().form_valid(form)


class Product_delete(DeleteView):
    model = Product
    success_url = reverse_lazy('product')


class Product_list(ListView):
    model = Product
    template_name = 'Ventas/products.html'
    context_object_name = 'products'


class Order_new(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'Ventas/order_new.html'
    success_url = reverse_lazy('order')

    def form_valid(self, form):
        """
        Se calcula el precio total. Se establece como vendedor al de la actual sesión
        """
        context = self.get_context_data()
        form = context['form']
        if form.is_valid():
            self.object = form.save()
            form.instance = self.object
            id_article_form = form.instance.article.id
            article_price = Product.objects.filter(
                id=id_article_form).first().price
            total = form.instance.units * article_price
            form.instance.total = total
            form.instance.seller = UserModuleProfile.objects.filter(
                id=self.request.user.pk).first()
            form.save()
        return super().form_valid(form)


class Order_edit(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'Ventas/order_edit.html'
    success_url = reverse_lazy('order')

    def form_valid(self, form):
        """
        Se vuelve a calcular el precio total por si se edita el artículo o la cantidad.
        El estado de vendedor se mantiene al que creó el pedido.
        """
        context = self.get_context_data()
        form = context['form']
        if form.is_valid():
            self.object = form.save()
            form.instance = self.object
            id_article_form = form.instance.article.id
            article_price = Product.objects.filter(
                id=id_article_form).first().price
            total = form.instance.units * article_price
            form.instance.total = total
            form.save()
        return super().form_valid(form)


class Order_delete(DeleteView):
    model = Order
    success_url = reverse_lazy('order')


class Order_list(ListView):
    model = Order
    template_name = 'Ventas/orders.html'
    context_object_name = 'orders'

class Order_Workshop_list(ListView):
    model = Order
    depth = 1
    template_name = 'Ventas/orders_workshop.html'
    context_object_name = 'orders'
