from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza
# Create your views here.






def index(request):
    # pizzas = Pizza.objects.all()
    # pizza_names_and_price = [pizza.nom + " Prix : " + str(pizza.prix) + "€" for pizza in pizzas]
    # pizza_names_and_price_str = ", ".join(pizza_names_and_price)
    # return HttpResponse("Les Pizzas : " + pizza_names_and_price_str)
    return render(request, 'menu/index.html')
