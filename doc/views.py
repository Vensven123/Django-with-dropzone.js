from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Doc
# Create your views here.

class MainView(TemplateView):
    template_name  = 'doc/main.html'

def upload_phot_view(request):
     if request.method == 'POST':
         my_file = request.FILES.get('file') 
         Doc.objects.create(upload = my_file)
         return HttpResponse('')
     return JsonResponse*({'post':'false'})     
           