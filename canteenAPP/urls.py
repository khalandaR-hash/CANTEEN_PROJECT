
from django.urls import path
from canteenAPP import views

urlpatterns = [

    path('',views.home_view,name='home'),
    path('employe/',views.employe_view,name='employee'),
    path('order/',views.order_book,name='order'),
    path('contact/',views.contact_view,name='contact'),

]
