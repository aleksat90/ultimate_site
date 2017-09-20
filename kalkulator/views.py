
from kalkulator.forms import KalkulatorForm
from django.views.generic import FormView
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.template import Context, Template, Engine
from django.shortcuts import render
from kalkulator import forms
import numpy as np

def rezultat(request):
	form_class = KalkulatorForm
	
			# return render(request,'kalkulator/rezultat.html', {'rezultat': rezultat})
	
def kalkulator_forma(request):
	form = forms.KalkulatorForm()
	resenje1 = 0
	resenje2 = 0
	if request.method == 'POST':
		form = forms.KalkulatorForm(request.POST)
		if form.is_valid():
			sabirak1 = form.cleaned_data['sabirak1']
			sabirak2 = form.cleaned_data['sabirak2']
			sabirak3 = form.cleaned_data['sabirak3']
			resenje1 = kvadratna_jednacina(sabirak1, sabirak2, sabirak3)[0]
			resenje2 = kvadratna_jednacina(sabirak1, sabirak2, sabirak3)[1]
			print(rezultat)
			#kvadratna jed

	return render(request, 'kalkulator/kalkulator.html', {'form': form,
															'resenje1': resenje1,
															'resenje2': resenje2})

#kvadratna jednacina
def kvadratna_jednacina(a,b,c):
	print("pozvan sam :)")
	r1=(-b+np.sqrt(b*b-4*a*c))/(2*a)
	r2=(-b-np.sqrt(b*b-4*a*c))/(2*a)
	print(r1)
	print(r2)
	return r1,r2

# class KalkulatorView(generic.edit.FormView):
# 	form_class = KalkulatorForm
# 	template_name= 'kalkulator/kalkulator.html'
# 	success_url = reverse_lazy('kalkulatorapp:kalkulator')

# 	# def form_valid(self, form):
# 	# 	sabirak1 = form.cleaned_data['sabirak1']
# 	# 	sabirak2 = form.cleaned_data['sabirak2']

# 	# 	self.rezultat = sabirak1 + sabirak2

# 	# 	template = Template('Rezultat je: {{rezultat}}')

# 	# 	context = Context({'rezultat' : self.rezultat})
# 	# 	template.render(context)

# 	# 	return super(KalkulatorView, self).form_valid(form)