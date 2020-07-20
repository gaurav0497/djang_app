from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Product, Contact, Order,UpdateOrder
from math import ceil
import json
from datetime import datetime

# Create your views here.

def index(request):
    allprod = []
    catprod=Product.objects.values('category', 'id')
    categories = {item['category'] for item in catprod}
    for categry in categories:
        product = Product.objects.filter(category=categry)
        n = len(product)
        nSlides = n // 4 + ceil((n / 4) - n // 4)
        allprod.append([product, range(1, nSlides), nSlides])
    params = {'allprod' : allprod}
    return render(request, 'shoopeasy/index.html', params)

def Match_result(a,b):
    if a in b.desc.lower() or a in b.name.lower() or a in b.category.lower() or a in b.subcategory.lower():
        return True
    else:
        return False


def search(request):
    q = request.GET.get('search').lower()
    allprod = []
    catprod = Product.objects.values('category', 'id')
    categories = {item['category'] for item in catprod}
    for categry in categories:
        products = Product.objects.filter(category=categry)
        product = [items for items in products if Match_result(q, items)]
        n = len(product)
        nSlides = n // 4 + ceil((n / 4) - n // 4)
        if len(product) != 0:
            allprod.append([product, range(1, nSlides), nSlides])
    params = {'allprod': allprod, 'msg': ""}

    if ((len(allprod) == 0) or (len(q) <= 3)):
        params = {'msg': "Do not mess with me.Please use valid search."}
    return render(request, 'shoopeasy/search.html', params)


def about(request):
    return render(request, 'shoopeasy/about.html')


def contact(request):
    thnk = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contacts = Contact(cust_name=name, cust_email=email, cust_phone=phone, cust_desc=desc)
        if(name != "") and (email != "") and (phone != "") and (desc != ""):
            thnk = True
            contacts.save()
    return render(request, 'shoopeasy/contact.html', {'thk': thnk})


def productview(request, pdid):
    products = Product.objects.filter(id=pdid)
    return render(request, 'shoopeasy/prodview.html', {'products': products[0]})


def checkout(request):

    thank = False
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address1')+" "+request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')
        data = request.POST.get('data')
        order = Order(json_data=data, name=name, email=email, city=city, state=state, zip_code=zip_code, phone=phone,
                      address=address)

        if name != " " and email != " " and address != " " and phone != " ":
            thank = True
            order.save()
            update = UpdateOrder(order_id=order.order_id, update_desc="The order has been placed successfully.")
            update.save()

        order_id = order.order_id
        params = {"thank": thank, "id": order_id}
        return render(request, 'shoopeasy/checkout.html', params)
    return render(request, 'shoopeasy/checkout.html' )


def tracker(request):
    if request.method == 'POST':
        ord_id = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=ord_id, email=email)
            if(len(order) > 0):
                update = UpdateOrder.objects.filter(order_id=ord_id)
                updates = []
                for i in update:
                    updates.append({'text': i.update_desc, 'time': i.time})
                    response = json.dumps([updates[::-1], order[0].json_data], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{ }')

        except Exception as e:
            print(e)

    return render(request, 'shoopeasy/tracker.html')