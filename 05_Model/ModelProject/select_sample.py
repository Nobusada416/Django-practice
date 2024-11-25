import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Person

# すべて取得
persons = Person.objects.all()

# print(persons)
for person in persons:
    print(person.pk, person.salary, person)

# 1件取得
# person = Person.objects.get(first_name='Jiro')
person = Person.objects.get(pk=1)
print(person)

# filter(絞り込み、エラーにならない、複数取得可)
print('-' * 100)
persons = Person.objects.filter(first_name='Jiro').all()
print(persons)

for person in persons:
    print(person, person.salary, person.web_site)
