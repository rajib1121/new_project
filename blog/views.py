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
    return render(request, 'blog/index.html', {})


def hint(request):
    return render(request, 'blog/hint.html', {'data': name_list})


def hw(request):
    return render(request, 'blog/hw.html', {
        'data': name_list,
        'c_list': country_list,
    })
    # return render(request, 'blog/index.html', {'data': name_list})


def country_page(request):
    return render(request, 'blog/country.html', {
        'c_list': country_list
    })

def modal_page(request):
    return render(request,'blog/modal.html', {

    })

def form_page(request):
    return render(request, 'blog/form.html', {
        
    })

def result(request, keyword):
    print(keyword)
    search_result = ""
    keyword_lo_case = keyword.lower()
    for name in name_list:
        name_lower = name.lower()
        if name_lower.startswith(keyword_lo_case):
            # search_result.append(name)
            if len(search_result) < 1:
                search_result += f'{name}'
            else:
                search_result += f', {name}'
    # data = {'names': search_result}
    
    print(search_result)
    # res = JsonResponse({'result':search_result})
    # return JsonResponse({'names': search_result})
    return HttpResponse(search_result)


@csrf_exempt
def get_data(request):
    # keyword = request.Get['keyword']
    search_result = ""
    if request.method == "POST":
        keyword = request.POST['text']
        print(keyword)
        if keyword == "":
            search_result = ""
        else:
            for name in name_list:
                name_lower = name.lower()
                if name_lower.startswith(keyword):
                    # search_result.append(name)
                    if len(search_result) < 1:
                        search_result += f'{name}'
                    else:
                        search_result += f', {name}'
            # data = {'names': search_result}
    
    print(search_result)
    msg = {'message': search_result}
    return JsonResponse(msg)