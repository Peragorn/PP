from django import forms

from .models import User
from .models import Wniosek

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		
class WniosekForm_Wnioskodawca(forms.ModelForm): # WNIOSKODAWCA
		class Meta:
			model = Wniosek
			fields = ['jednostka_organizacyjna_uczelni',
			'wnioskodawca', 
			'wnioskodawca_tel',
			'osoba_dokonujaca_opisu',
			'osoba_dokonujaca_opisu_tel',
			'osoba_dokonujaca_opisu_email',
			'przedmiot_zamowienia',
			'przedmiot_zamowienia_okreslono_na_okres',
			'merytoryczne_uzasadnienie_celowosci',
			'termin_realizacji_zamowienia',
			'kwota_przeznaczona_na_sfinansowanie_zamowienia_brutto',
			'zrodlo_finansowania_oraz_zgodnosc_z_planem_rzeczowo_finansowym'
			]