from django.shortcuts import render
from django.http import Http404
import datetime
from mainApp.models import Background, Experience

# Create your views here.
def index(request):
    return render(request, 'mainApp/mainPage.html', {'year': datetime.date.today().year})

def contacts(request):
    return render(request, 'mainApp/contacts.html',
                  {
                      'values': [
                          ['phone.svg', 'Номер телефона: ', '8(919)942-54-42'],
                          ['email.svg','Почта: ', 'darivn@mail.ru']
                                ],
                      'year': datetime.date.today().year
                  })

def experience(request):
    return render(request, 'mainApp/experience.html',
                  {
                      'object_list': Experience.objects.all(),
                      'year': datetime.date.today().year
                  })

def element(request, pk):
    try:
        id=int(pk)
    except ValueError:
        raise Http404()
    return render(request, 'mainApp/element.html',
                  {
                      'background': Background.objects.get(pk=id),
                      'year': datetime.date.today().year
                  })

def elements(request):
    return render(request, 'mainApp/elements.html',
                  {
                      'object_list': Background.objects.all(),
                      'year': datetime.date.today().year
                  })