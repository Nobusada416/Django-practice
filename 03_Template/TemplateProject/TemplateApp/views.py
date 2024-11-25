from django.shortcuts import render


def index(request):
    value = "Good Bye"
    return render(request, 'TemplateApp/index.html', context={"value": value})

def home(request, first_name, last_name):
    my_name = f'{first_name} {last_name}'
    favorites = ['Apple', 'Grape', 'Banana']
    my_info = {
        'name': first_name,
        'age': 36
    }
    status = 10
    return render(request, 'TemplateApp/home.html', context={
          'my_name': my_name,
          'favorites': favorites,
          'my_info': my_info,
          'status': status
        })


def sample1(request):
    return render(request, 'sample1.html')

def sample2(request):
    return render(request, 'sample2.html')

def sample(request):
    name = 'ichiro yamada'
    height = 175.5
    weight = 72
    bmi = weight / (height / 100) ** 2
    page_url = 'ホームページ: https://www.google.com'
    favorite_fruits = [
        'Apple',
        'Grape',
        'Lemon',
    ]
    msg = """hello
    my name is
    ichiro
    """
    msg2 = '1234567890'
    return render(request, 'sample.html', context={
        'name': name,
        'bmi': bmi,
        'page_url': page_url,
        'fruits': favorite_fruits,
        'msg': msg,
        'msg2': msg2
    })


class Country:

    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital

    def __str__(self):
        return f'{self.name}, {self.population}, {self.capital}'

    def capital_and_population(self):
        return f'capital: {self.capital}, population: {self.population}'

def sample3(request):
    country = Country('Japan', 100000000, 'Tokyo')
    return render(request, 'sample3.html', context={
        'country': country
    })