from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainApp/mainPage.html')

def contacts(request):
    return render(request, 'mainApp/contacts.html',
                  {
                      'values': [
                          ['phone.svg', 'Номер телефона: ', '8(919)942-54-42'],
                          ['email.svg','Почта: ', 'darivn@mail.ru']
                                ]
                  })
