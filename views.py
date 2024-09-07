from django.http import HttpResponse
from django.shortcuts import render, redirect
import csv
from phones.models import Phone


def index(request):
    return redirect('catalog')





def create_db(request):
    with open('phones.csv', encoding='UTF-8') as file:
        file_reader = csv.DictReader(file, delimiter=';')
        count = 0
        st_list = []
        for row in file_reader:
            phone = Phone(id=row['id'],
                  name=row['name'],
                  image=row['image'],
                  price=row['price'],
                  release_date=row['release_date'],
                  lte_exists=row['lte_exists'])
            phone.save()

    return HttpResponse('done')




def show_catalog(request):
    template = 'catalog.html'
    with open('phones.csv', encoding='UTF-8') as file:
        file_reader = csv.DictReader(file, delimiter=';')
        count = 0
        phones = []
        for row in file_reader:
            phones.append(row)
    context = {'phones': phones}
    print(context)
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
