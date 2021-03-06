from django.shortcuts import render

# Create your views here.

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db import models

from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, HttpResponse

from .forms import UserForm
from .models import Wniosek, Firma
from django.utils import timezone

def home(request):

	#category_list = Movie.objects.order_by('-question')[:5]
	#context_dict = {'Moviees': category_list}


	form = UserForm()
	context = {"form": form}
	template = "home.html"
	return render(request,template,context)
	
def register(request):
	form = UserForm()
	context = {"form": form}
	template = "register.html"
	return render(request,template,context)
	
def search(request):

	#category_list = Movie.objects.order_by('-question')[:5]
	#context_dict = {'Moviees': category_list}
	form = UserForm()
	search_list = Game.objects.order_by('-name')[:5]
	context = {'search_list': search_list}
	template = "search.html"
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
	
class FirmaDetailView(DetailView):

	model = Firma
	slug_field = 'id'

	def get_context_data(self, **kwargs):
		context = super(FirmaDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context
