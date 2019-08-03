from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  if request.method == 'POST':
    a = request.POST.get('a', None)
    b = request.POST.get('b', None)
    c = int(a) + int(b)
    return render(request, 'index.html', locals())
  return render(request, 'index.html', locals())
