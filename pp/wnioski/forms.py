from django import forms

from .models import User
from .models import Wniosek

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		
class WniosekForm_All(forms.ModelForm):
		class Meta:
			model = Wniosek
			fields = ['jednostka_organizacyjna_uczelni', #1
			'wnioskodawca', 
			'wnioskodawca_tel', 
			'osoba_dokonujaca_opisu',
			'osoba_dokonujaca_opisu_tel', 
			'osoba_dokonujaca_opisu_email',
			'przedmiot_zamowienia', #2
			'przedmiot_zamowienia_okreslono_na_okres',
			'merytoryczne_uzasadnienie_celowosci', #3
			'termin_realizacji_zamowienia',
			'szacunkowa_wartosc_zamowienia_netto', #4
			'ustalenia_szacunkowej_wartosci_zamowienia_dokonano_na_podstawie',
			'osoba_dokonujaca_ustalenia_wartosci_szacunkowej_zamowienia',
			'kwota_przeznaczona_na_sfinansowanie_zamowienia_brutto', 
			'zrodlo_finansowania_oraz_zgodnosc_z_planem_rzeczowo_finansowym',
			'potwierdzenie_pokrycia_finansowego_ze_srodkow_na_prace_naukowo_badawcze', #5
			'kontrasygnata_finansowa_uwagi', #6
			'data_zlozenia_wniosku_w_dziale_zamowien_publicznych', #7
			'uwagi_dzialu_zamowien_publicznych_dotyczace_wniosku', #8
			'dzial', #9
			'puste'
			]
		
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
			
class WniosekForm_Step2(forms.ModelForm): # KOLES OD SZACOWANIA WARTOSCI
		class Meta:
			model = Wniosek
			fields = ['szacunkowa_wartosc_zamowienia_netto'
			]