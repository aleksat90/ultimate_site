from django import forms

class KalkulatorForm(forms.Form):
	sabirak1=forms.FloatField(label='Parametar a:')
	sabirak2=forms.FloatField(label='Parametar b:')
	sabirak3=forms.FloatField(label='Parametar c:')