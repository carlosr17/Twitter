from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import loader, Context
from django.http import HttpResponse
from search.models import Palabra
from django.core import serializers
import time
import twitter
import json

# Create your views here.
def index(request):
	miTemplate = loader.get_template("search/index.html")
	params= Context({})
	return HttpResponse(miTemplate.render(params))

#Metodo Para conultar los ultimos tweets
def test(key):
	api = twitter.Api(consumer_key='BrHuCVxSO8sjvaEb7wJA3tt9f',
		consumer_secret='a5Fes71Zguqlet9X8ZPfGYGFHGR1IhiVZr8lOLeag3cZHCkxJa',
		access_token_key='596615153-FpsQWMsEDGySHbQxuB48FBFQd7VKLZx3wRqDVCz1',
		access_token_secret='agWBoqHlnIdpZ3z6eJUQySm7uMqYTTvA8CYJCDbDbVzpU')
	tweets=api.GetSearch(term=key,count=10, lang='es',result_type="recent")
	retorno=[]
	for tweet in tweets:
		retorno.append({"text":tweet.text, 'user':tweet.user.name,'creacion':tweet.created_at})
	return retorno

class SearchAjaxView(TemplateView):

	def get(self, request, *args, **kwargs):
		key=request.GET['key']
		try:
			aux = Palabra()
			palabra = Palabra.objects.get(nombre=key)
			palabra.save()
		except Palabra.DoesNotExist:
			palabra = Palabra(nombre=key)
			palabra.save()
		keys= Palabra.objects.order_by('-time')
		data= serializers.serialize('json',keys,fields=('nombre'))
		datos= {"historial":data,'tweets':test(key)}
		return HttpResponse(json.dumps(datos))
