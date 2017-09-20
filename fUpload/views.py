from django.shortcuts import render
from fUpload.forms import ProfileForm
from fUpload.models import DataModel
from django.http import HttpResponseRedirect
from django.contrib import messages 
# Create your views here.

def fUpload(request):
	form = ProfileForm(request.POST, request.FILES)
	file_uploaded = False
	if request.method == 'POST':
		print("POST metod")
		
		print(form)

		if form.is_valid():
			# print('forma validna /fUpload.views.fUpload')
			# form.save()
			# print("Snimljeno")
			file_name, file_size, read_file = manipulacija_file(request.FILES['datoteka'])

			instance = DataModel(datoteka=request.FILES['datoteka'])
			#print(DataModel.datoteka.name)
			#instance.save()
			form.save()
			file_uploaded = True
			
			print("Iz form valid")
			print(read_file)
			return render(request, 'fUpload/fUpload.html', {'form': form,
															'file_name': file_name,
															'file_size': file_size,
															'file_uploaded': file_uploaded,
															'read_file': read_file})

		else:
			print('Forma nije validna')
			a=form.errors
			print(a)
			messages.error(request, "Error")
			
			form = ProfileForm()

	return render(request, 'fUpload/fUpload.html', {'form': form, 'file_uploaded': file_uploaded})


#FUNKCIJA ZA MANIPULACIJU FAJLOM
def manipulacija_file(f):
	file_name = f.name
	file_size = f.size
	read_file = f.read()
	print(read_file)
	read_file=brisanje_zareza(read_file)

	print(read_file)
	return file_name, file_size, read_file



def brisanje_zareza(linija):
	dekodovano=str(linija, 'utf-8')
	#splitovano=linija.split(b' ')
	dekodovano=dekodovano.replace('.','ALEKSA')
	return dekodovano




from django.views.generic.list import ListView


class FajloviListView(ListView):
	model = DataModel
	template_name = 'fUpload/lista_fajlova.html'
	context_object_name = 'lista_fajlova'
