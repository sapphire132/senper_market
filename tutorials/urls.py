from django.urls import path
from . import views

urlpatterns = [
    path('/',views.tutorials,name='tutorials'),
    path('/<int:course_id>',views.tutorial,name='tutorial')

]