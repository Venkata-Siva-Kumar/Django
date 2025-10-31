from django.shortcuts import render,redirect,get_object_or_404
from .models import Plant_Details
from .forms import PlantDetailsForm

# Create your views here.
def insert_plant(request):
    if request.method == 'POST':
        form  = PlantDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_plants')
            
    else:
        form = PlantDetailsForm()
    return render(request,'insert.html',{'form':form})
    
def update_plant(request,id):
    plant = get_object_or_404(Plant_Details,id=id)
    if request.method == 'POST':
        form = PlantDetailsForm(request.POST,instance = plant)
        if form.is_valid():
            form.save()
            return redirect('show_plants')
    else:
        form = PlantDetailsForm(instance=plant)
    return render(request,'update.html',{'form':form,'plant':plant})
    
    
def show_plants(request):
    plants = Plant_Details.objects.all()
    return render(request, 'show.html', {'plants': plants})