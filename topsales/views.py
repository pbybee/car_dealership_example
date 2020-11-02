from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Sales, Cars
from django.db.models import Max
from collections import defaultdict

def TableView(request):

    all_sales = Sales.objects.all()
    car_db = Cars.objects.all().values()

    reps = defaultdict()
    max_car = -1
    max_num = -1
    for car in car_db:
        new_max = all_sales.filter(car__car_id=car['car_id']).count()
        if max_num < new_max:
            max_num = new_max
            max_car = car['car_id']

    max_sales = all_sales.filter(car__car_id=max_car).values()
    for sale in max_sales:
        if sale['sale_rep'] not in reps.keys():
            reps[sale['sale_rep']] = 1
        else:
            reps[sale['sale_rep']] = reps[sale['sale_rep']] + 1

    car_model = ''
    for car in car_db:
        if car['car_id']==max_car:
            car_model = f"{car['car_make']} {car['car_model']}"

    template = loader.get_template('table.html')
    context = {
        'query_results': reps,
        'car_model': car_model
    }
    return HttpResponse(template.render(context, request))