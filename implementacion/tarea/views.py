from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task_UNEDepartamento,Task_UNEMunicipio,Task_Status_Name,Task_TaskTypeCategory_Name  # Modelo que contiene los datos a mostrar
from django.http import HttpResponse

#Arg_Task = {}

# Create your views here.
@login_required
def tablero(request):
    Departamentos = Task_UNEDepartamento.objects.all()  # Obtén todos los estados de la base de datos
    Municipios = Task_UNEMunicipio.objects.all()
    Estados = Task_Status_Name.objects.all()
    Categorias = Task_TaskTypeCategory_Name.objects.all()

    return render(request,"tarea/tablero.html",{'Departamentos': Departamentos,'Municipios':Municipios,'Estados':Estados,'Categorias':Categorias})

@login_required
def process_task(request):
    if request.method == 'POST':
        status_ids = request.POST.getlist('states[]')  # Obtiene los IDs seleccionados
        category_ids = request.POST.getlist('categoris[]')
        #name = request.POST.getlist('name')
        name = request.POST.get('name', '')  # Valor por defecto vacío si no se envía
        selected_status = []
        selected_categorys = []

        for status_id in status_ids:
            try:
                status = Task_Status_Name.objects.get(id=status_id)  # Busca la categoría por ID
                selected_status.append(status.name)  # Agrega el nombre a la lista
            except Task_Status_Name.DoesNotExist:
                continue  # Manejo si no se encuentra la categoría

        for category_id in category_ids:
            try:
                category = Task_TaskTypeCategory_Name.objects.get(id=category_id)  # Busca la categoría por ID
                selected_categorys.append(category.name)  # Agrega el nombre a la lista
            except Task_Status_Name.DoesNotExist:
                continue  # Manejo si no se encuentra la categoría

        # Aquí puedes hacer algo con los IDs y nombres seleccionados
        # return HttpResponse(f"IDs seleccionados: {', '.join(selected_ids)}<br>Nombres seleccionados: {', '.join(selected_names)}")
        # Arg_Task['STATUS'] =selected_status
        # Arg_Task['CATEGORI'] =selected_categoris
        Arg_Task={'STATUS':selected_status,
                 'CATEGORY':selected_categorys,
                 'NAME':name}
        
        print(Arg_Task)
    return HttpResponse('Método no permitido', status=405)

    
    
    