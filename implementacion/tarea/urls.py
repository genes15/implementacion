from django.urls import path
from . import views
from implementacion.tarea.views import tablero

urlpatterns = [
    
    path("",view=tablero,name ="tablero"),
    # path('get_municipios/', views.get_municipios, name='get_municipios'),
    path('process_task/', views.process_task, name='process_task'),
]
