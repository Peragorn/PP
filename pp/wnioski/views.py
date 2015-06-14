from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db import models
from django import forms
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from django.db.models import Q

from .forms import UserForm
from .forms import WniosekForm_All, WniosekForm_Wnioskodawca, WniosekForm_New, WniosekForm_Szacujacy, WniosekForm_Dzial_Nauki, WniosekForm_Kwestor, WniosekForm_Rektor, WniosekForm_Kierownik_Dzialu_Zamowien_Publicznych,PrzedmiotZamowieniaForm
from .models import Wniosek, Przedmiot_Zamowienia, User, Ranga
from django.utils import timezone

def home(request):

	#category_list = Movie.objects.order_by('-question')[:5]
	#context_dict = {'Moviees': category_list}


	form = WniosekForm_Wnioskodawca()
	context = {"form": form}
	template = "home.html"
	return render(request,template,context)
	
### WNIOSEK
	
def wniosek_submit_wnioskodawca(request, id):
	if request.method == 'POST':
		instance = get_object_or_404(Wniosek, id=id)
		form=WniosekForm_All(request.POST or None, instance=instance)
		if form.is_valid():
			form.save()
			#return HttpResponseRedirect(reverse('pp:'))
	return  render(request, 'wniosek_submit_wnioskodawca.html', {
		'form': WniosekForm_Wnioskodawca(),
	})
	
def wniosek_submit_szacujacy(request):
	if request.method == 'POST':
		instance = get_object_or_404(MyModel, id=id)
		form=WniosekForm_Szacujacy(request.POST or None, instance=instance)
		if form.is_valid():
			form.save()
			#return HttpResponseRedirect(reverse('pp:'))
	return  render(request, 'wniosek_submit_szacujacy.html', {
		'form': WniosekForm_Szacujacy(),
	})
	
def wniosek_moje(request):
	current_user = request.user
	#category_list = Movie.objects.order_by('-question')[:5]
	#context_dict = {'Moviees': category_list}
	#(Item.objects.filter(Q(creator=owner) | Q(moderated=False))
	#wnioski = Wniosek.objects.filter('-id')[:3]
	
	#TODO Dla rektora kwestora ETC ETC
	wnioski = Wniosek.objects.filter(Q(wnioskodawca_imie_i_nazwisko=current_user.id) | 
	Q(osoba_dokonujaca_ustalenia_wartosci_szacunkowej_zamowienia=current_user.id) | 
	Q(Kierownik_Dzialu_Nauki=current_user.id) |
	Q(Kwestor=current_user.id) |
	Q(Rektor=current_user.id) |
	Q(Kierownik_Dzialu_Zamowien_Publicznych=current_user.id)
	)
	#Q(Szef_pionu=current_user.id) | 
	#Q(Szef_pionu=current_user.id) | 
	#Q(Szef_pionu=current_user.id) | 
	#Q(Szef_pionu=current_user.id) | 
	#Q(Szef_pionu=current_user.id) | ) 
	

	
	context_dict = {'wnioski': wnioski}
	
	form = UserForm()
	template = "wniosek_moje.html"
	return render(request,template,context_dict)
	
def wniosek_new(request):
	if request.method == 'POST':
		form=WniosekForm_New(request.POST)
		if form.is_valid():
			form.save()
			#return HttpResponseRedirect(reverse('pp:'))
		return  render(request, 'home.html', {
		'form': WniosekForm_New(),
	})

	form = WniosekForm_New()
	context = {"form": form}
	template = "wniosek_new.html"
	return render(request,template,context)
		
def wniosek_dzial_nauki(request):
	form = WniosekForm_Biuro_Wspolpracy()
	context = {"form": form}
	template = "wniosek_dzial_nauki.html"
	return render(request,template,context)
				
def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            ut = Ranga(user=user, type=0)
            ut.save()

            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()


    return render_to_response(
            'register.html',
            {'user_form': user_form, 'registered': registered}, context)

def about(request):
	form = UserForm()
	context = {"form": form}
	template = "about.html"
	return render(request,template,context)
	
def contact(request):
	form = UserForm()
	context = {"form": form}
	template = "contact.html"
	return render(request,template,context)
	
def example(request):
	form = WniosekForm_All()
	context = {"form": form}
	template = "example.html"
	return render(request,template,context)
	
def przedmiot_zamowienia(request):
	form = PrzedmiotZamowieniaForm()
	context = {"form": form}
	template = "przedmiot_zamowienia.html"
	return render(request,template,context)
		
def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('login.html', {}, context)

#@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/')

	
# ITEM VIEWS



class WniosekDetailView(DetailView):

	model = Wniosek
	slug_field = 'id'
			
	def get_context_data(self, **kwargs):
		context = super(WniosekDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context
		
def my_model_view(request, mymodel_id):
	class MyModelForm(forms.ModelForm):
		class Meta:
			model = Wniosek

	model = get_object_or_404(Wniosek, pk=mymodel_id)
	
	current_user = request.user
	instance = get_object_or_404(Wniosek, pk=mymodel_id)
	#(Item.objects.filter(Q(creator=owner) | Q(moderated=False))
	#form = myModelForm(instance=model)
	
	template = "wniosek_generic.html"
	
	if current_user == getattr(model, 'osoba_dokonujaca_ustalenia_wartosci_szacunkowej_zamowienia'):
		form = WniosekForm_Szacujacy(request.POST or None, instance=instance)
		
	if current_user == getattr(model, 'Kwestor'):
		form = WniosekForm_Kwestor(request.POST or None, instance=instance)
		
	if current_user == getattr(model, 'Rektor'):
		form = WniosekForm_Rektor(request.POST or None, instance=instance)
		
	if current_user == getattr(model, 'Kierownik_Dzialu_Zamowien_Publicznych'):
		form = WniosekForm_Kierownik_Dzialu_Zamowien_Publicznych(request.POST or None, instance=instance)
	
	if request.method == 'POST':

		if form.is_valid():
			form.save()
			#return HttpResponseRedirect(reverse('pp:'))
			form = MyModelForm(instance=model)
			template = "wniosek_detail.html"
			return  render(request, 'home.html', {
				'form': WniosekForm_Wnioskodawca(),
		})
		else:		
			return render(request, 'about.html', context)
			
	else:	
		form = MyModelForm(instance=model)
		template = "wniosek_generic.html"
	
		if current_user == getattr(model, 'osoba_dokonujaca_ustalenia_wartosci_szacunkowej_zamowienia'):
			form = WniosekForm_Szacujacy(request.POST or None, instance=instance)
			
		if current_user == getattr(model, 'Kwestor'):
			form = WniosekForm_Kwestor(request.POST or None, instance=instance)
			
		if current_user == getattr(model, 'Rektor'):
			form = WniosekForm_Rektor(request.POST or None, instance=instance)
			
		if current_user == getattr(model, 'Kierownik_Dzialu_Zamowien_Publicznych'):
			form = WniosekForm_Kierownik_Dzialu_Zamowien_Publicznych(request.POST or None, instance=instance)

		context = {"form": form}
		return render(request, template, context)
	

	
class Przedmiot_ZamowieniaDetailView(DetailView):

	model = Przedmiot_Zamowienia
	slug_field = 'id'

	def get_context_data(self, **kwargs):
		context = super(Przedmiot_ZamowieniaaDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context
