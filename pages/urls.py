from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('design/<str:client>', views.item , name='item'),
    path('designer/<str:designer_name>', views.designer , name='designer')
] 

