import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Person

# person = Person(
#     first_name='Taro',
#     last_name='Sato',
#     birthday='2000-01-01',
#     email='aa@mail.com',
#     salary=10000,
#     memo='memo taro',
#     web_site='http://google.com',
# )

# person.save()

person = Person(
    first_name='Jiro',
    last_name='Sato',
    email='aa@mail.com',
    salary=None,
    memo='memo taro',
    web_site=None,
)

# person.save()

# create
# Person.objects.create(
#     id=4,
#     first_name='Jiro',
#     last_name='Ito',
#     email='bb@mail.com',
#     salary=20000,
#     memo='create method 実行',
#     web_site=None,
# )

# get_or_create
obj, created = Person.objects.get_or_create(
    id=6,
    first_name='Jiro',
    last_name='Ito',
    email='bb@mail.com',
    salary=20000,
    memo='create method 実行',
    web_site=None,
)
print(obj)
print(created)