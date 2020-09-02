from django.urls import path

from . import views

urlpatterns = [
    path('',views.order_form,name='order'),
    path('ordered',views.ordered,name='ordered')
] 
