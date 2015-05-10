from django import forms

from .models import User
from .models import Wniosek

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		
class WniosekForm_Wnioskodawca(forms.ModelForm):
		class Meta:
			model = Wniosek
			fields = ['nr_rej_wniosku',
			'jednostka_organizacyjna_uczelni',
			'wnioskodawca', 
			'wnioskodawca_tel',
			'osoba_dokonujaca_opisu',
			'osoba_dokonujaca_opisu_tel',
			'osoba_dokonujaca_opisu_email',
			'przedmiot_zamowienia',
			'przedmiot_zamowienia_okreslono_na_okres',
			'merytoryczne_uzasadnienie_celowosci',
			'termin_realizacji_zamowienia',
			'szacunkowa_wartosc_zamowienia_netto',
			'ustalenia_szacunkowej_wartosci_zamowienia_dokonano_na_podstawie',
			'osoba_dokonujaca_ustalenia_wartosci_szacunkowej_zamowienia',
			'kwota_przeznaczona_na_sfinansowanie_zamowienia_brutto',
			'zrodlo_finansowania_oraz_zgodnosc_z_planem_rzeczowo_finansowym'
]