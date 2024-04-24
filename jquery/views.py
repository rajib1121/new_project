from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

name_list = [
    "Adams",
"Baker",
"Clark",
"Davis",
"Evans",
"Frank",
"Ghosh",
"Hills",
"Irwin",
"Jones",
"Klein",
"Lopez",
"Mason",
"Nalty",
"Ochoa",
"Patel",
"Quinn",
"Reily",
"Smith",
"Trott",
"Usman",
"Valdo",
"White",
"Xiang",
"Yakub",
"Zafar",
'Blake',
'Harvey',
'Antonio',
'Connor',
'Julian',
'Aidan',
'Harold',
'Conner',
'Peter',
'Hunter',
'Eli',
'Alberto',
'Carlos',
'Shane',
'Aaron',
'Marlin',
'Paul',
'Ricardo',
'Hector',
'Alexis',
'Adrian',
'Kingston',
'Douglas',
'Gerald',
'Joey',
'Johnny',
'Charlie',
'Scott',
'Martin',
'Tristin',
'Troy',
'Tommy',
'Rick',
'Victor',
'Jessie',
'Neil',
'Ted',
'Nick',
'Wiley',
'Morris',
'Clark',
'Stuart',
'Orlando',
'Keith',
'Marion',
'Marshall',
'Noel',
'Everett',
'Romeo',
'Sebastian',
'Stefan',
'Robin',
'Clarence',
'Sandy',
'Ernest',
'Samuel',
'Benjamin',
'Luka',
'Fred',
'Albert',
'Greyson',
'Terry',
'Cedric',
'Joe',
'Paul',
'George',
'Wade',
'Dave',
'Seth',
'Ivan',
'Riley',
'Gilbert',
'Jorge',
'Dan',
'Brian',
'Roberto',
'Ramon',
'Miles',
'Liam',
'Nathaniel',
'Ethan',
'Lewis',
'Milton',
'Claude',
'Joshua',
'Glen',
]

country_list = ["Bangladesh", "India", "Pakistan", "Srilanka", "Nepal", "Bhutan", "Maldives"]




def index(request):
    return render(request, 'jquery/index.html', {
        
    })

def hw(request):
    return render(request, 'jquery/hw.html', {
        
    })

def modal(request):
    return render(request, 'jquery/modal.html', {

    })

def form(request):
    return render(request, 'jquery/form.html', {

    })

def country(request):
    return render(request, 'jquery/country.html', {
        'c_list': country_list,
    })

def hint(request):
    return render(request, 'jquery/hint.html', {
        
    })


@csrf_exempt
def get_data(request):
    # keyword = request.Get['keyword']
    search_result = ""
    if request.method == "POST":
        keyword = request.POST['text'].lower()
        print(keyword)
        if keyword == "":
            search_result = ""
        else:
            for name in name_list:
                name_lower_case = name.lower()
                if name_lower_case.startswith(keyword):
                    # search_result.append(name)
                    if len(search_result) < 1:
                        search_result += f'{name}'
                    else:
                        search_result += f', {name}'
            # data = {'names': search_result}
    
    print(search_result)
    msg = {'result': search_result}
    return JsonResponse(msg)