from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView, TemplateView
from django.urls import reverse_lazy
import calendar

from datetime import date, datetime
from Pacientes.models import Patients, Consultations
from Ventas.models import Order, Product
from Usuarios.models import UserModuleProfile

months = {
    1: 'Enero',
    2: 'Febrero',
    3: 'Marzo',
    4: 'Abril',
    5: 'Mayo',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre',
}

class Reports(TemplateView):
    template_name = 'Reportes/reports.html'


class Patient_Asist_Gerency_list(ListView):
    model = Patients
    template_name = 'Reportes/patient_asist.html'
    context_object_name = 'patients'

    def get_queryset(self):
        """
        Se buscan los pacientes que asistieron a la consulta
        """
        users = UserModuleProfile.objects.all()
        id_patients = []
        consultations = Consultations.objects.all()
        for consultation in consultations:
            if consultation.attended:
                id_patients.append(consultation.patient.pk)
        queryset = Patients.objects.filter(id__in=id_patients)
        return queryset

    def get_context_data(self, **kwargs):
        """
        Filtra por fecha específica, último mes o última semana
        """
        context = super(Patient_Asist_Gerency_list,
                        self).get_context_data(**kwargs)
        users = UserModuleProfile.objects.all()
        id_patients = []
        consultations = Consultations.objects.all()
        # Fecha específica
        if self.request.GET.get('date_ref'):
            date_insert = self.request.GET.get('date_ref')
            consultations = consultations.filter(date=date_insert)
            context['mensaje_filtro'] = 'Pacientes filtrados al  {}:'.format(
                date_insert)
        if self.request.GET.get('choice_ref'):
            period = self.request.GET.get('choice_ref')
            # Última semana
            if period == 'semana':
                today = date.today()
                day = today.day
                days = []
                for i in range(day-6, day+1):
                    if i > 0:
                        days.append(
                            '{}-{}-{}'.format(today.year, today.month, i))
                consultations = consultations.filter(date__in=days)
                context['mensaje_filtro'] = 'Pacientes filtrados a la última semana:'
            # +Último mes
            if period == 'mes':
                today = date.today()
                days = []
                for i in range(1, 32):
                    days.append('{}-{}-{}'.format(today.year, today.month, i))
                consultations = consultations.filter(date__in=days)
                context['mensaje_filtro'] = 'Pacientes filtrados al mes en curso:'
        # Filtro por asistencia
        for consultation in consultations:
            if consultation.attended:
                id_patients.append(consultation.patient.pk)
        context['patients'] = Patients.objects.filter(id__in=id_patients)
        return context


class Patient_notAsist_Gerency_list(ListView):
    model = Patients
    template_name = 'Reportes/patient_not_asist.html'
    context_object_name = 'patients'

    def get_queryset(self):
        """
        Se buscan los pacientes que no asistieron a la consulta
        """
        users = UserModuleProfile.objects.all()
        id_patients = []
        consultations = Consultations.objects.all()
        for consultation in consultations:
            if not consultation.attended:
                id_patients.append(consultation.patient.pk)
        queryset = Patients.objects.filter(id__in=id_patients)
        return queryset

    def get_context_data(self, **kwargs):
        """
        Filtra por fecha específica, último mes o última semana
        """
        context = super(Patient_notAsist_Gerency_list,
                        self).get_context_data(**kwargs)
        users = UserModuleProfile.objects.all()
        id_patients = []
        consultations = Consultations.objects.all()
        # Fecha específica
        if self.request.GET.get('date_ref'):
            date_insert = self.request.GET.get('date_ref')
            consultations = consultations.filter(date=date_insert)
            context['mensaje_filtro'] = 'Pacientes filtrados al  {}:'.format(
                date_insert)
        if self.request.GET.get('choice_ref'):
            period = self.request.GET.get('choice_ref')
            # Última semana
            if period == 'semana':
                today = date.today()
                day = today.day
                days = []
                for i in range(day-6, day+1):
                    if i > 0:
                        days.append(
                            '{}-{}-{}'.format(today.year, today.month, i))
                consultations = consultations.filter(date__in=days)
                context['mensaje_filtro'] = 'Pacientes filtrados a la última semana:'
            # +Último mes
            if period == 'mes':
                today = date.today()
                days = []
                for i in range(1, 32):
                    days.append('{}-{}-{}'.format(today.year, today.month, i))
                consultations = consultations.filter(date__in=days)
                context['mensaje_filtro'] = 'Pacientes filtrados al mes en curso:'
        # Filtro por inasistencia
        for consultation in consultations:
            if not consultation.attended:
                id_patients.append(consultation.patient.pk)
        context['patients'] = Patients.objects.filter(id__in=id_patients)
        return context


class Patient_Order_Gerency_list(ListView):
    model = Patients
    template_name = 'Reportes/patient_order.html'
    context_object_name = 'patients'

    def get_queryset(self):
        """
        Se buscan los pacientes que hicieron pedidos
        """
        users = UserModuleProfile.objects.all()
        id_patients = []
        orders = Order.objects.all()
        for order in orders:
            id_patients.append(order.client.pk)
        queryset = Patients.objects.filter(id__in=id_patients)
        return queryset

    def get_context_data(self, **kwargs):
        """
        Filtra por último mes o última semana
        """
        context = super(Patient_Order_Gerency_list,
                        self).get_context_data(**kwargs)
        users = UserModuleProfile.objects.all()
        id_patients = []
        orders = Order.objects.all()

        if self.request.GET.get('choice_ref'):
            period = self.request.GET.get('choice_ref')
            # Última semana
            if period == 'semana':
                today = date.today()
                day = today.day
                days = []
                for i in range(day-6, day+1):
                    if i > 0:
                        days.append(
                            '{}-{}-{}'.format(today.year, today.month, i))
                orders = orders.filter(date__in=days)
                context['mensaje_filtro'] = 'Pacientes filtrados a la última semana:'
            # +Último mes
            if period == 'mes':
                today = date.today()
                days = []
                for i in range(1, 32):
                    days.append('{}-{}-{}'.format(today.year, today.month, i))
                orders = orders.filter(date__in=days)
                context['mensaje_filtro'] = 'Pacientes filtrados al mes en curso:'
        # Filtro por asistencia
        for order in orders:
            id_patients.append(order.client.pk)
        context['patients'] = Patients.objects.filter(id__in=id_patients)
        return context


class Product_Most_Selled(TemplateView):
    template_name = 'Reportes/product_most_selled.html'

    def get_context_data(self, **kwargs):
        context = super(Product_Most_Selled, self).get_context_data(**kwargs)

        orders = Order.objects.all()
        today = date.today()
        days = []
        for i in range(1, 32):
            days.append('{}-{}-{}'.format(today.year, today.month, i))
        orders = orders.filter(date__in=days)
        product = {}
        for order in orders:
            key = order.article.pk
            if key in product:
                product[key]+=order.units
            else:
                product[key]=order.units
        #Ordenar según cantidad vendida
        import operator
        product_sort = sorted(product.items(), key=operator.itemgetter(1), reverse=True)
        #Buscar nombre del producto
        products = Product.objects.all()
        product = []
        for i in range(len(product_sort)):
            temp = [products.filter(id=product_sort[i][0]).first().name]
            temp.append(product_sort[i][1])
            product.append(list(temp))

        context['products'] = product
        return context


class Sales_Month_Seller(TemplateView):
    template_name = 'Reportes/sales_month_seller.html'

    def get_context_data(self, **kwargs):
        context = super(Sales_Month_Seller, self).get_context_data(**kwargs)
        if self.request.GET.get('choice_month'):
            mes = int(self.request.GET.get('choice_month'))
            orders = Order.objects.all()
            today = date.today()
            sales_year = {}
            for m in range(1, mes+1):
                days = []
                for d in range(1, calendar.monthrange(today.year, m)[1]+1):
                    days.append('{}-{}-{}'.format(today.year, m, d))
                order_m = orders.filter(date__in=days)
                sales_year[m]=order_m

            sellers = UserModuleProfile.objects.filter(rol='VEN')
            sellers_count = {}
            sellers_month_count = {}
            for seller in sellers:
                sellers_count[seller]=0
                for month, sales_month in sales_year.items():
                    for sale in sales_month:
                        if sale.seller.pk == seller.pk:
                            sellers_count[seller]+=1
                fullName_seller = '{} {}'.format(seller.first_name,seller.last_name)

                if months[month] in sellers_month_count:
                    aux = sellers_month_count[months[month]]
                    aux[fullName_seller] = sellers_count[seller]
                    sellers_month_count[months[month]] = aux
                else:
                    aux = {}
                    aux[fullName_seller] = sellers_count[seller]
                    sellers_month_count[months[month]] = aux

            context['sales'] = sellers_month_count
        return context