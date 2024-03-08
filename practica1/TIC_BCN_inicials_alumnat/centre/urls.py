from django.urls import path
from . import views

urlpatterns = {
    path('', views.index, name='index'),
    path('prof', views.proff, name='proff'),
    path('users', views.users, name='users')
}