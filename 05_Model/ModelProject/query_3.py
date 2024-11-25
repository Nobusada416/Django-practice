import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Students

# 件数
print(Students.objects.count())
print(Students.objects.filter(name='太郎').count())

# 件数、最大、最小、平均、合計
from django.db.models import Count, Max, Min, Avg, Sum
print(Students.objects.aggregate(
    Count('pk'), Max('pk'), Min('pk'), Avg('pk'), Sum('pk')
))

aggregate_value = Students.objects.aggregate(
    Count('pk'), Max('pk'), Min('pk'), Avg('pk'), Sum('pk')
)
print(aggregate_value['pk__avg'])
print(Students.objects.aggregate(
    count_pk=Count('pk'),
    max_pk=Max('pk'),
    min_pk=Min('pk'),
    avg_pk=Avg('pk'),
    sum_pk=Sum('pk')
))

# Group BY
print(Students.objects.values('name', 'age').annotate(
    Max('pk'), Min('pk')
).order_by('pk__max'))

for student in Students.objects.values('name').annotate(
    max_id=Max('pk'), min_id=Min('pk')
):
    print(student['name'], student['max_id'])