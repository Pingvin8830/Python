from django.shortcuts import render
from django.http import HttpResponse
from page.models import Category, Good

# Create your views here.

def index(request, cat_id):
  if cat_id == None:
    cat = Category.objects.first()
  else:
    cat = Category.objects.get(pk = cat_id)
  goods = Good.objects.filter(category = cat).order_by ("name")
  s = "Категория: " + cat.name + "<br><br>"
  for good in goods:
    s = s + "(" + str(good.pk) + ") " + good.name + "<br>"
  return HttpResponse(s)

