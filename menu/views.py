from django.shortcuts import render
from .models import Category

# Create your views here.
def menu_list(request):
  categories = Category.objects.prefetch_related("items").all()
  context = {"categories": categories }
  return render(request, "menu/list.html", context)