from django.shortcuts import render

from django.views.generic import TemplateView

def index(request):
  return render(request, 'jinki/index.html', None)

def base(request):
  return render(request, 'jinki/base.html', None)

def Fpage(request):
  return render(request, 'jinki/Fpage.html', None)

class Cpage(TemplateView):
  template_name = 'jinki/Cpage.html'
