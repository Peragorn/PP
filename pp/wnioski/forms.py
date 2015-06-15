from django import forms

from .models import User
from .models import Wniosek, Przedmiot_Zamowienia

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		
class WniosekForm_All(forms.ModelForm):
		class Meta:
			model = Wniosek
			
			
			
class WniosekForm_Rektor(forms.ModelForm):
		class Meta:
			model = Wniosek
			fields = ['zatwierdzenie_pod_wzgledem_merytorycznym',
			'zatwierdzenie_do_realizacji',
			'zatwierdzenie_przedmiotow_zamowienia'
			]
			
class WniosekForm_Kwestor(forms.ModelForm):
		class Meta:
			model = Wniosek
			fields = ['kontrasygnata_finansowa_uwagi'
			]
			
class WniosekForm_Kierownik_Dzialu_Nauki(forms.ModelForm):
		class Meta:
			model = Wniosek
			fields = ['potwierdzenie_pokrycia_finansowego_ze_srodkow_na_prace_naukowo_badawcze'
			]
			
class WniosekForm_osoba_dokonujaca_opisu(forms.ModelForm):
		class Meta:
			model = Wniosek
			fields = ['zatwierdzenie_przedmiotow_zamowienia_przez_osobe_dokonujaca_opisu'
			]
			
class WniosekForm_New(forms.ModelForm): # NEW
		class Meta:
			model = Wniosek
			fields = ['wnioskodawca_imie_i_nazwisko', #
			'osoba_dokonujaca_opisu', #
			'osoba_dokonujaca_ustalenia_wartosci_szacunkowej_zamowienia', #
			'Kierownik_Dzialu_Nauki', #
			'Kwestor', #
			'Rektor', #
			'Kierownik_Dzialu_Zamowien_Publicznych' #
			
			]
			
class WniosekForm_Kierownik_Dzialu_Zamowien_Publicznych(forms.ModelForm): # NEW
		class Meta:
			model = Wniosek
			fields = ['data_zlozenia_wniosku_w_dziale_zamowien_publicznych', #
			'uwagi_dzialu_zamowien_publicznych_dotyczace_wniosku', #
			'Przedmioty_zamowienia_Komisja_przetargowa', #
			'Przedmioty_zamowienia_Dzial_aparatury_badawczej_i_dydaktycznej', #
			'Przedmioty_zamowienia_wnioskodawca_w_uzgodnieniu_z_dzialem_nauki', #
			'Przedmioty_zamowienia_Wnioskodawca',
			'Decyzja_kierownika_Zamowien_Publicznych'
			
			]
			
class WniosekForm_Wnioskodawca(forms.ModelForm): # WNIOSKODAWCA
		class Meta:
			model = Wniosek
			fields = ['jednostka_organizacyjna_uczelni',
			'przedmiot_zamowienia',
			'przedmiot_zamowienia_okreslono_na_okres',
			'merytoryczne_uzasadnienie_celowosci',
			'termin_realizacji_zamowienia',
			'kwota_przeznaczona_na_sfinansowanie_zamowienia_brutto',
			'zrodlo_finansowania_oraz_zgodnosc_z_planem_rzeczowo_finansowym',
			]
			
class WniosekForm_Szacujacy(forms.ModelForm): # KOLES OD SZACOWANIA WARTOSCI
		class Meta:
			model = Wniosek
			fields = ['szacunkowa_wartosc_zamowienia_netto',
			'ustalenia_szacunkowej_wartosci_zamowienia_dokonano_na_podstawie'
			]
						
class PrzedmiotZamowieniaForm(forms.ModelForm): # Przedmiot Zamowienia
		class Meta:
			model = Przedmiot_Zamowienia