from django.urls import path
from django.contrib.auth.decorators import login_required
from Reportes import views


urlpatterns = [
    path('report/', login_required(views.Reports.as_view()), name="report"),
    path('report/patient_asist/', login_required(views.Patient_Asist_Gerency_list.as_view()), name="patient_asist"),
    path('report/patient_not_asist/', login_required(views.Patient_notAsist_Gerency_list.as_view()), name="patient_not_asist"),
    path('report/patient_order/', login_required(views.Patient_Order_Gerency_list.as_view()), name="patient_order"),
    path('report/product_most_selled/', login_required(views.Product_Most_Selled.as_view()), name="product_most_selled"),
    path('report/sales_month_seller/', login_required(views.Sales_Month_Seller.as_view()), name="sales_month_seller"),
]
