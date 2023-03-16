from django.shortcuts import render

# Create your views here.
def price(request, name, cnt):
    item = {
        'iphone' : 100,
        'ipad' : 200,
        'ipod' : 50,
        'applewatch' : 70,
        'macbook' : 500
    }
    price = item[name]
    sum = price * cnt
    context = {
        'item' : item,
        'price' : price,
        'cnt' : cnt,
        'name' : name,
        'sum' : sum
    }
    return render(request, 'price.html', context)
    