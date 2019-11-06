from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from foodapp.models import Profile,FoodCourt,Store,Category,MenuCatalog,Item,Cart
from django.http import JsonResponse

def home(request):
    return render(request, "home.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/foodcourts/') 
        else:
            # Return an 'invalid login' error message.
            return HttpResponse('invalid user') 

    return render(request, "signin.html")


def signup(request):
    if request.method == "POST":
        name=request.POST['name']
        username= request.POST['username']
        email= request.POST['email']
        dob=request.POST['dob']
        phoneno=request.POST['phoneno']
        empid=request.POST['empid']
        password=request.POST['password']
        # cnfpassword=request.POST['cnfpassword']

        exists= User.objects.filter(username=username).exists()

        if not exists:
            user = User.objects.create_user(username,email,password)
            profile=Profile.objects.create(name=name,phone_number=phoneno,empid=empid,dob=dob,user=user)
            return redirect("/signin/")

    return render(request,"signup.html")

def signout(request):
    logout(request)
    return redirect("/home/")

def foodcourt(request):
    foodcourts = FoodCourt.objects.all()
    return render(request, "foodcourts.html",{"foodcourts" : foodcourts})

def stores(request,fc_id):
    foodcourt = FoodCourt.objects.get(fc_id = fc_id)
    stores = Store.objects.filter(foodcourt = foodcourt)
    return render(request, "stores.html",{"stores":stores, "foodcourt":foodcourt})

def store_menu(request,fc_id,number):
    foodcourt = FoodCourt.objects.get(fc_id = fc_id)
    store = Store.objects.get(number = number)
    items = Item.objects.filter(store = store)
    menu = MenuCatalog.objects.filter(store = store)
    # print(items)
    # print(menu)
    return render(request, "menu.html",{"items":items, "menu":menu ,"store":store})

def order_summary(request):
    user = request.user
    cart = Cart.objects.filter(user = user)
    total_price=0
    for item in cart:
        q = item.quantity
        p = item.item.price
        price = p*q
        total_price+= price
    return render(request, "summary.html",
                            {"user":user,"cart":cart,"total_price":total_price,
                            "foodcourt":cart[0].item.store.foodcourt.name, 
                            "storename":cart[0].item.store.name})

def invoice(request):
    return render(request, "invoice.html")

def add_to_cart(request):
    if request.method == "POST":
        quantity = request.POST.get("quantity")
        item_id = request.POST.get("item_id")

        user = request.user
        print(user)
        item = Item.objects.get(pk=int(item_id))
        cart_item = Cart.objects.create(user=user, quantity=quantity, item=item)
        return JsonResponse({"message":"Successfully add to the cart"})