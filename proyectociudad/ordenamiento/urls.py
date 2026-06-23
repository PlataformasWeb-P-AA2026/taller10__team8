from django.urls import path
from . import views

app_name = 'ordenamiento'

urlpatterns = [
    path('parroquias/', views.parroquias_list, name='parroquias_list'),
    path('parroquias/crear/', views.parroquia_create, name='parroquia_create'),
    path('parroquias/<int:pk>/editar/', views.parroquia_edit, name='parroquia_edit'),
    path('barrios/', views.barrios_list, name='barrios_list'),
    path('barrios/crear/', views.barrio_create, name='barrio_create'),
    path('barrios/<int:pk>/editar/', views.barrio_edit, name='barrio_edit'),
]