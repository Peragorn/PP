from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ranga(models.Model):
    user = models.OneToOneField(User)
	
	#0 - User
	#1 - Admin
	#2 - Rektor
	#3 - ?
	#4 - ?
	
    type = models.IntegerField(default=0, null=False)

    def getType(self):
        return self.type

    def __str__(self):
        return self.user.username
	
class Wniosek(models.Model):
	#nr_rej_wniosku = models.IntegerField(null=True, blank=True)
	
	#1.
	jednostka_organizacyjna_uczelni = models.CharField(max_length=255, null=True, blank=True)
	
	#1.1
	#wnioskodawca_imie_i_nazwisko = models.CharField(max_length=255, null=True, blank=True)
	wnioskodawca_imie_i_nazwisko = models.ForeignKey(User, related_name = 'wn_user_imie', null=True, blank=True)
	wnioskodawca_tel = models.CharField(max_length=255, null=True, blank=True)

	#1.2
	osoba_dokonujaca_opisu = models.ForeignKey(User, related_name = 'wn_user_osoba_dokonujaca_opisu', null=True, blank=True)
	#osoba_dokonujaca_opisu_tel = models.CharField(max_length=255, null=True, blank=True)
	#osoba_dokonujaca_opisu_email = models.CharField(max_length=255, null=True, blank=True)
	
	#2
	przedmiot_zamowienia = models.CharField(max_length=255, null=True, blank=True)
	przedmiot_zamowienia_okreslono_na_okres = models.CharField(max_length=255,null=True, blank=True)
		
	#3
	merytoryczne_uzasadnienie_celowosci = models.CharField(max_length=255, null=True, blank=True)
		
	#3.1
	termin_realizacji_zamowienia = models.CharField(max_length=255,null=True, blank=True)
	
	#4
	szacunkowa_wartosc_zamowienia_netto = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
	ustalenia_szacunkowej_wartosci_zamowienia_dokonano_na_podstawie = models.CharField(max_length=255, null=True, blank=True)
	osoba_dokonujaca_ustalenia_wartosci_szacunkowej_zamowienia = models.ForeignKey(User, related_name = 'wn_user_osoba_szacujaca', null=True, blank=True)
	
	#4.1
	kwota_przeznaczona_na_sfinansowanie_zamowienia_brutto = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
		
	#4.2
	zrodlo_finansowania_oraz_zgodnosc_z_planem_rzeczowo_finansowym = models.CharField(max_length=255, null=True, blank=True)
	##_4_Data = models.DateField()
	## PIECZEC?
	## PODPIS?
	
	
	#5
	potwierdzenie_pokrycia_finansowego_ze_srodkow_na_prace_naukowo_badawcze = models.CharField(max_length=255, null=True, blank=True)
	#_5_Data = models.DateField()
	## PODPIS?
	
	
	#6
	kontrasygnata_finansowa_uwagi = models.CharField(max_length=255, null=True, blank=True)
	#_6_Data = models.DateField()
	## PODPIS?
	
	## WYPELNIA DZIAL ZAMOWIEN PUBLICZNYCH:
	
	#7
	data_zlozenia_wniosku_w_dziale_zamowien_publicznych = models.CharField(max_length=255,null=True, blank=True)
	## PODPIS?
	
	#8
	uwagi_dzialu_zamowien_publicznych_dotyczace_wniosku = models.CharField(max_length=255, null=True, blank=True)
	
	#9
	komisja_przetargowa = models.CharField(max_length=255, null=True, blank=True)
	dzial_aparatury_badawczej_i_dydaktycznej = models.CharField(max_length=255, null=True, blank=True)
	wnioskodawca_w_uzgodnieniu_z_dzialem_nauki = models.CharField(max_length=255, null=True, blank=True)
	wnioskodawca = models.CharField(max_length=255, null=True, blank=True)
	
	# Osoby decydujace
	Szef_pionu = models.ForeignKey(User, related_name = 'wn_us_szef', null=True, blank=True)
	Decyzja_szefa_pionu = models.BooleanField(default=False, blank=True)
	
	Osoba_reprezentujaca_komisje_przetargowa = models.ForeignKey(User, related_name = 'wn_user_komisja_przetargowa' , null=True, blank=True)
	Decyzja_komisji_przetargowej = models.BooleanField(default=False, blank=True)
	
	Kierownik_Biura_Rozwoju_i_Programow_Miedzynarodowych = models.ForeignKey(User, related_name = 'wn_user_biuro_rozwoju' , null=True, blank=True)
	Decyzja_kierownika_Biura_Rozwoju_i_Programow_Miedzynarodowych = models.BooleanField(default=False, blank=True)
	
	Kierownik_Dzialu_Nauki = models.ForeignKey(User, related_name = 'wn_user_dzial_nauki' , null=True, blank=True)
	Decyzja_kierownika_Dzialu_Nauki = models.BooleanField(default=False, blank=True)
	
	Kierownik_Biura_Wspolpracy_Miedzynarodowej = models.ForeignKey(User, related_name = 'wn_user_biuro_wspolpracy' , null=True, blank=True)
	Decyzja_kierownika_Biura_Wspolpracy_Miedzynarodowej = models.BooleanField(default=False, blank=True)
	
	def __str__(self):              # __unicode__ on Python 2
		return "%d - %s" % (self.id, self.wnioskodawca)
	
	
class Przedmiot_Zamowienia(models.Model):
	nazwa = models.CharField(max_length=50)
	jednostka_miary = models.CharField(max_length=255)
	wniosek = models.ForeignKey(Wniosek, related_name = 'pz_wn')
	ilosc = models.IntegerField()
	Kwota_na_realizacje_brutto = models.DecimalField(max_digits=6, decimal_places=2)
	Pozycja_w_planie_zamowien = models.IntegerField()
	Opinia_trybu_zamowienia = models.CharField(max_length=255)
		
	# Nazwa wiersza w tabeli numeru 9
	postepujacy = models.CharField(max_length=255)
	
	def __str__(self):              # __unicode__ on Python 2
		return "%s" % (self.nazwa)