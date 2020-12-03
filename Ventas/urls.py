from django.urls import path
from django.contrib.auth.decorators import login_required
from Ventas import views


urlpatterns = [
    path('product/', login_required(views.Product_list.as_view()), name="product"),
    path('product/new/', login_required(views.Product_new.as_view()),
         name="product_new"),
    path('product/<int:pk>', login_required(views.Product_edit.as_view()),
         name="product_edit"),
    path('product/delete/<int:pk>',
         login_required(views.Product_delete.as_view()), name="product_delete"),
    path('order/', login_required(views.Order_list.as_view()), name="order"),
    path('order/workshop', login_required(views.Order_Workshop_list.as_view()),
         name="order_workshop"),
    path('order/new/', login_required(views.Order_new.as_view()), name="order_new"),
    path('order/<int:pk>', login_required(views.Order_edit.as_view()),
         name="order_edit"),
    path('order/delete/<int:pk>',
         login_required(views.Order_delete.as_view()), name="order_delete"),
]
