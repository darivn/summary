from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
import datetime
from mainApp.models import Background, Experience

header=[['Главная страница', '/'],['Опыт работы', '/experience'],['Образование','/education'],['Контакты', '/contacts']]

# Create your views here.
def index(request):
    return render(request, 'mainApp/mainPage.html', {
                                                        'header': header,
                                                        'page': '/',
                                                         'year': datetime.date.today().year
                                                    })

def contacts(request):
    return render(request, 'mainApp/contacts.html',
                  {
                      'header': header,
                      'values': [
                          ['phone.svg', 'Номер телефона: ', '8(919)942-54-42'],
                          ['email.svg','Почта: ', 'darivn@mail.ru'],
                          ['vk.svg', 'Страница в ВКонтакте', 'https://vk.com/nikdashav']
                                ],
                      'page': '/contacts',
                      'year': datetime.date.today().year
                  })

def experience(request):
    return render(request, 'mainApp/experience.html',
                  {
                      'header': header,
                      'object_list': Experience.objects.all(),
                      'page': '/experience',
                      'year': datetime.date.today().year
                  })

def element(request, pk):
    try:
        id=int(pk)
        r = render(request, 'mainApp/element.html',
                  {
                      'header': header,
                      'background': Background.objects.get(id_background=id),
                      'page': '/education',
                      'year': datetime.date.today().year
                  })
    except ValueError:
        raise Http404()
    except ObjectDoesNotExist:
        raise Http404()
    return r

def elements(request):
    return render(request, 'mainApp/elements.html',
                  {
                      'header': header,
                      'object_list': Background.objects.all(),
                      'page': '/education',
                      'year': datetime.date.today().year
                  })