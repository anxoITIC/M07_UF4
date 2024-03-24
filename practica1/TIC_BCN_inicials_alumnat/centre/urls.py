from django.urls import path
from . import views


#differents rutes de la aplicació
urlpatterns = [
    path('', views.index, name='index'),
    path('prof', views.proff, name='proff'),
    path('users', views.users, name='users'),
    path('info_user/<int:user_id>/', views.info_user, name='info_user'),
    path('info_prof/<int:professor_id>/', views.info_prof, name='info_prof'),
    path('formulari', views.formulari, name='formulari')
]
