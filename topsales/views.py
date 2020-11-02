from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TopSales

def TableView(request):


    query_results = TopSales.objects.all()
    template = loader.get_template('topsales/table.html')
    context = {
        'query_results': query_results,
    }
    return HttpResponse(template.render(context, request))