from django.db import models
from django.contrib.auth.models import User

# Create your models here.
	
class Firma(models.Model):
    nazwa = models.CharField(max_length=50)
	
class Wniosek(models.Model):
	data_sporzadzenia = models.DateField() # 0
	wnioskodawca = models.ForeignKey(Firma, blank = True, null = True) # 1
	nazwa_zakupu = models.CharField(max_length=100) # 2
	opis = models.CharField(max_length=100, blank = True) # 3
	uzasadanienie = models.CharField(max_length=100, blank = True) # 4
	szacunkowa_wartosc = models.FloatField() # 5
	podstawa_wyliczenia = models.CharField(max_length=100) # 6
	planowany_termin = models.DateField() # 7
	tryb_udzielenia = models.CharField(max_length=100, blank = True) # 8
	proponowane_kryteria_oceny = models.CharField(max_length=100, blank = True) # 9
	proponowane_warunki_udzialu = models.CharField(max_length=100, blank = True) # 10
	
