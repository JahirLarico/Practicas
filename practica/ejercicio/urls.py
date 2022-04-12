from unicodedata import name
from django.urls import path
from . import views
app_name='ejercicio'

urlpatterns=[
    path('',views.index,name='index'),
    path('crear/',views.crear,name='crear'),
    path('guardar/',views.guardar,name='guardar'),
    path('<int:estudiante_id>/',views.info,name='info'),
    path('<int:estudiante_id>/editar/',views.editar,name='editar'),
    path('<int:estudiante_id>/modificar/',views.modificar,name='modificar'),
    path('<int:estudiante_id>/eliminar/',views.eliminar,name='eliminar')
]