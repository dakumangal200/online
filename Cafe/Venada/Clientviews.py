from django.shortcuts import render,redirect
from Cafe_admin.models import Area, Product,Contactus,Customer,Category,Feedback,CartTable,Order,Order_Item
from django.contrib import messages
import sys,random
from django.conf import settings
from django.core.mail import send_mail
from Venada.clientform import ContactForm,RegistrationForm,TablebookingForm,FeedBackForm
from datetime import date
from .cart import client_Cart
from django.views.decorators.csrf import csrf_exempt


def ClientIndex(request):
    c=Product.objects.all()
    re=Product.objects.all().order_by('-Product_id')[:4]
    cat=Category.objects.all()
    return render(request,'client_Index.html',{"cmenu":c,'cate':cat,'recent':re})

def ClientMenu(request,id):
    if id==0:
        c=Product.objects.all()
    else:
        c=Product.objects.filter(Category_id=id)

    cat=Category.objects.all()
    return render(request,"cafemenu.html",{"cmenu":c,'cate':cat})

def Reservation(request):
    cat=Category.objects.all()
    return render(request,'reservation.html',{'cate':cat})

def Aboutus(request):
    cat=Category.objects.all()
    return render(request,'about.html',{'cate':cat})

def Gallary(request):
    cat=Category.objects.all()
    return render(request,'gallery.html',{'cate':cat})



def InsertContact(request):
    cat=Category.objects.all()
    if request.method=="POST" :
        ctc=ContactForm(request.POST)
        print("Error in Categoryr",ctc.errors)

        if ctc.is_valid():
            try:
                ctc.save()
                return redirect('/Client/clientindex')
            except:
                print("Error in Contact",sys.exc_info())
    else:
        ctc=ContactForm()
    return render(request,'contact.html',{'insertcontact':ctc,'cate':cat})

def CLogin(request):
    cat=Category.objects.all()
    if request.method =='POST':
        cat=Category.objects.all()
        email=request.POST["Email"]
        password=request.POST["Password"]
        val=Customer.objects.filter(Email=email,Password=password,is_admin=0).count()
        print(val)
        print("---------",email,"----------",password)
        if val == 1:
            data=Customer.objects.filter(Email=email,Password=password,is_admin=0)
            for item in data:
                request.session['customer_id']=item.Customer_id
                request.session['customer_email']=item.Email
                request.session['customer_pass']=item.Password
                if request.POST.get("remember"):
                    response=redirect('/Client/clientindex/')
                    response.set_cookie('client_mail',request.POST['Email'],3600*24*365*2)
                    response.set_cookie('client_pass',request.POST['Password'],3600*24*365*2)
                    return response
            return redirect('/Client/clientindex')
        else:
            messages.error(request,"Invalid Username and Password")
            return redirect('/Client/clientlogin/')
    else:
        if request.COOKIES.get('client_mail'):
            return render(request,"Clientlogin.html",{'c_mail': request.COOKIES['client_mail'],'c_pass':request.COOKIES['client_pass'],'cate':cat})
        return render(request,"Clientlogin.html",{'cate':cat})
    
def ClientLogout(request):
    cid=request.session['customer_id']
    email=request.session['customer_email']
    passw=request.session['customer_pass']
    print("-----------------------",cid,email,passw)
    del request.session['customer_id']
    del request.session['customer_email']
    del request.session['customer_pass']
    print("------------------",cid,email,passw)
    return redirect('/Client/clientlogin/')

def CForgotpass(request):
    cat=Category.objects.all()
    return render(request,'Clientforgotpass.html',{'cate':cat})

def CSendotp(request):
    cat=Category.objects.all()
    otp1=random.randint(100000,999999)
    e=request.POST['Email']

    request.session['temail']=e
    obj=Customer.objects.filter(Email=e).count()

    if obj == 1:
        val=Customer.objects.filter(Email=e).update(otp=otp1,otp_used=0)
        subject='OTP Verification'
        message=str(otp1)
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[e, ]
        send_mail(subject,message,email_from,recipient_list)
    return render(request,'Clientsetpass.html',{'cate':cat})

def CSetpass(request):
    if request.method=="POST":
        T_otp=request.POST['otp']
        T_pass=request.POST['pass']
        T_cpass=request.POST['cpass']

        if T_pass==T_cpass:
            e=request.session['temail']
            val=Customer.objects.filter(Email=e,otp=T_otp,otp_used=0).count()
            if val==1:
                Customer.objects.filter(Email=e).update(otp_used=1,Password=T_pass)
                return redirect('/Client/clientlogin/')
            else:
                messages.error(request,"Invalid OTP")
                return render(request,"Clientforgotpass.html")
        else:
            messages.error(request,"Password does not match")
            return render(request,"Clientsetpass.html")
    else:
        return redirect("/Client/clientforgotpass")
    
def Registration(request):
    cat=Category.objects.all()
    ar=Area.objects.all()
    if request.method=="POST" :
        r=RegistrationForm(request.POST)
        print("Error in Registration",r.errors)

        if r.is_valid():
            try:
                r.save()
                return redirect('/Client/clientlogin/')
            except:
                print("Error in Registartion",sys.exc_info())
    else:
        r=RegistrationForm()
    return render(request,'Clientregistration.html',{'registration':r,'areaa':ar,'cate':cat})

def Reservation(request):
    cat=Category.objects.all()
    print('-------inside function')
    if 'customer_id' in request.session:
        cust=request.session['customer_id']

        if request.method=="POST" :
            print('---------Inside post method')
            re=TablebookingForm(request.POST)
            print("Error in Reservation",re.errors)

            if re.is_valid():
                try:
                    re.save()
                    return redirect('/Client/clientindex')
                except:
                    print("Error in Reservation",sys.exc_info())
        else:
            re=TablebookingForm()
        return render(request,'reservation.html',{'reservation':re,'reser':cust,'cate':cat})
    else:
        return redirect("/Client/clientlogin/")
    
def CFeedback(request):
    da = date.today().strftime("%Y-%m-%d")
    if request.method == "POST":
        try:
            id = request.session['customer_id']
            des = request.POST.get('Description')
            pr = request.POST['Product_id']
            re = Feedback(Description=des,Customer_id_id=id,Product_id_id=pr,Feedback_date=da)
            re.save()
            return redirect("/Client/detail/%s" % pr)
        except:
                print("_", sys.exc_info())
    else:
        re = FeedBackForm()
    return render(request, 'Detailed_product_page.html')

def LoadMenu(request):
    lm=Category.objects.all()
    print('------------------------',lm)
    return render(request,"menu.html",{'cate':lm})
    
def LoadCategory(request):
    ctg=Category.objects.all()
    return render(request,"Client_header_footer.html",{'catg':ctg})


def Blog(request,id):
    cat=Category.objects.all()
    b=Product.objects.get(Product_id=id)
    return render(request,"Detailed_product_page.html",{"blog":b,'cate':cat})

def Myaccount(request):
    cat=Category.objects.all()
    ar=Area.objects.all()
    id = request.session['customer_id']
    ma=Customer.objects.get(Customer_id=id)
    if request.method == 'POST':
        mac=RegistrationForm(request.POST,instance=ma)
        print("Error In Update Registration",mac.errors)
        if mac.is_valid():
            try:
                mac.save()
                return redirect('/Client/myaccount/')
            except:
                print("Error in update registration",sys.exc_info())
    else:
        ma=Customer.objects.get(Customer_id=id)
    return render(request,"Myaccount.html",{'myaccount':ma,'areaa':ar,'cate':cat})



def ItemCart(request):
    cat=Category.objects.all()
    if 'customer_id' in request.session:
        id_c=request.session['customer_id']
        c=CartTable.objects.filter(Customer_id=id_c)
        total=0
        print('==============crt item',c)
        for val in c:
            print('----------------------value',val.Quantity,'val',val.Total)
            total=total+(val.Product_id.Price * val.Quantity)
        print(total)
        shipping=total+50
        return render(request,"Cartitem.html",{'items':c,'total':total,'shipping':shipping,'cate':cat})
    else:
        z=CartTable.objects.all()
        cart=client_Cart(request)
        total=cart.get_total_price()
        print(total)
        shipping=total+50
        return render(request,"Cartitem.html",{'cartitems':z,'total':total,'shipping':shipping ,'cate':cat})



def InsertCart(request):
    if request.method=="POST":
        if 'customer_id' in request.session:
            print('Inside---------------------------------------')         
            qty = request.POST.get("qty")
            pid = request.POST.get("pid")
            id = request.session['customer_id']
            prid = Product.objects.get(Product_id=pid)
            print("---------",prid)
            amt = int(qty) * int(prid.Price)
            ca =CartTable(Product_id_id=pid, Customer_id_id=id, Quantity=qty, Total=amt)
            ca. save()
            return redirect("/Client/cartitem/")
        else:
            print("inside cart function")
            qty=request. POST['qty']
            pid = request.POST.get("pid")
            cart = client_Cart(request)
            product = Product.objects.get(Product_id=pid)
            print(product)
            cart.add(Product=product, quantity=int(qty))
            print(cart)
            return redirect("/Client/cartitem/")
           

def update_quantity(request,id):
    if 'customer_id' in request.session:
        qty = request.GET.get('qty')
        val = CartTable.objects.get(cart_id=id)
        newqty = int(qty)
        total = newqty * int(val.Product_id.Price)
        val = CartTable.objects.filter(cart_id=id).update(Quantity=newqty,Total=total)
        return redirect('/Client/cartitem/')
    else:
        cart = client_Cart(request)
        product = Product.objects.get(Product_id=id)
        qty = request.GET.get('qty')
        if int(qty) > 0:
            cart. add(Product=product, quantity=int(qty), update_quantity=True)
            print(cart)
    return redirect("/Client/cartitem/")


def Checkout(request):
    cat=Category.objects.all()
    if 'customer_id' in request.session:
        id=request.session['customer_id']
        user=Customer.objects.get(Customer_id=id)
        a=CartTable.objects.filter(Customer_id=id)
        total=0
        for data in a:
            total=data.Total+total
        ship=50
        gt=total+ship
        return render(request,"Checkout.html",{'user':user,'cart1':a,'sub':total,'ship':ship,'total':gt,'cate':cat})
    else:
        return redirect('/Client/clientlogin/')  

def destroycart(request):
    if 'id' in request.session:
        product=CartTable.objects.get(Product_id=id)
        product.delete()
        return redirect("/Client/cartitem/")
    else:
        cart=client_Cart(request)
        p=Product.objects.get(Product_id=id)
        cart.remove()
        return redirect("/Client/cartitem/")


@csrf_exempt
def OrderSuccess(request):
    
    return render(request,"OrderSuccessful.html")


@csrf_exempt
def place_order_online(request,id):
    print('---------------------------------inside online')
    if request.session.has_key('customer_id'):
        uid = request.session['customer_id']
        ca = CartTable.objects.filter(Customer_id_id=uid)
        # amt = 0
        for val in ca:
            quen=val.Quantity
            piid=val.Product_id
            z=Product.objects.get(Product_id=piid.Product_id)
            z.Quantity=z.Quantity-quen
            z.save()
        #     amt = amt + (int(val.Product_id.Price) * int(val.Quantity))
        # amt = amt + 100
        # date1 = date.today().strftime("%Y-%m-%d")
        # o = Order(Customer_id_id=uid, Total_Amount=amt, Order_Date=date1, Payment_status='2', Order_status=0)
        # o.save()
        oid = Order.objects.latest('Order_id')
        oid1 = Order.objects.filter(Order_id=oid.Order_id).update(Payment_status="1")
        c = CartTable.objects.filter(Customer_id_id=uid)
        c1 = CartTable.objects.filter(Customer_id_id=uid).count()
        print(c,'----------------------customer',c1)
        if c1 >= 1:
            for data in c:
                pid = data.Product_id_id
                qty = data.Quantity
                pri = data.Product_id.Price
                total = int(qty) * pri
                od = Order_Item(Quantity=int(qty), Product_id_id=pid, Order_id_id=oid.Order_id,
                                   Price=total)
                od.save()
            e = request.session['customer_email']
            obj = Customer.objects.filter(Email=e).count()
            val = Customer.objects.get(Email=e)
            if obj == 1:
                ord1 = Order_Item.objects.filter(Order_id_id=id)
                subject = 'Order Confirmation'
                message = f'Dear {val.First_Name} {val.Last_Name}, \n\n\t ' \
                          f'Your order has been accepted and will arrive soon. ' \
                          f'Order details are as follows:'
                message += f'\n---------------------------------------------------------------------'
                message += f'\n  Product name'
                message += f'\n----------------------------------------------------------------------'
                for data in ord1:
                    print("---------------------------------",data)
                    message += f'\n {data.Product_id.Product_Name}'
                message += f'\n----------------------------------------------------------------------'
                message += f'\n  Total \t\t\t {total}'
                message += f'\n----------------------------------------------------------------------'
                message += f'\n\n Thank uou,\n Regards Venada'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [e, ]
                send_mail(subject, message, email_from, recipient_list)
        else:
            messages.error(request, "You don't have any product in your Cart!")
            return render(request, "Checkout.html")
        c_delete = CartTable.objects.filter(Customer_id_id=uid)
        print('cart delete--------------------',c_delete)
        c_delete.delete()
        return redirect("/Client/ordersuccessfull/")
    return render(request,'Checkout.html')

def DeletecartItem(request,id):
    if 'customer_id' in request.session:
        prod=CartTable.objects.get(cart_id=id)
        print(" Delete Cart Item",prod)
        prod.delete()
        return redirect("/Client/cartitem")
    else:
        cart=client_Cart(request)
        p=Product.objects.get(Product_id=id)
        cart.remove(p)
        return redirect("/Client/cartitem")







def palce_order(request, total):
    print('cash on ------------------------------------------------>>>>',total)
    if request.session.has_key('customer_id'):
        pay = request.POST.get('payment_status')
        amt = total
        uid = request.session['customer_id']
        date1 = date.today().strftime("%Y-%m-%d")
        o = Order(Customer_id_id=uid, Total_Amount=int(amt), Order_Date=date1, Payment_status=pay, Order_status=0)
        o.save()
        id = Order.objects.latest('Order_id')
        c = CartTable.objects.filter(Customer_id_id=uid)
        c1 = CartTable.objects.filter(Customer_id_id=uid).count()
        if c1 >= 1:
            for data in c:
                pid = data.Product_id_id
                qty = data.Quantity
                pri = data.Product_id.Price
                total = int(qty) * int(pri)
                od = Order_Item(Quantity=int(qty), Product_id_id=pid, Order_id_id=id.order_id, Price=int(total))
                od.save()
            e = request.session['customer_email']
            obj = Customer.objects.filter(Email=e).count()
            val = Customer.objects.get(Email=e)
            if obj == 1:
                ord1 = Order_Item.objects.filter(order_id_id=id)
                subject = 'Order Confirmation'
                message = f'Dear, {val.First_Name} {val.Last_Name} \n\n\t Your order is confirm. Order is reach you soon. You ordered'
                message += f'\n---------------------------------------------------------------------'
                message += f'\n  Product name'
                message += f'\n----------------------------------------------------------------------'
                for data in ord1:
                    print("---------------------------------", data)
                    message += f'\n {data.Product_id.Product_Name}'
                message += f'\n----------------------------------------------------------------------'
                message += f'\n  Total \t\t\t {amt}'
                message += f'\n----------------------------------------------------------------------'
                message += f'\n\n Thank uou,\n Regards The Glam House'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [e, ]
                send_mail(subject, message, email_from, recipient_list)
        else:
            messages.error(request, "You don't have any product in your Cart!")
            return render(request, "Checkout.html")
        c_delete = CartTable.objects.filter(Customer_id_id=uid)
        c_delete.delete()
        return redirect("/Client/ordersuccessfull/")
    return render(request, 'Checkout.html')



def OrderHistory(request):
    cat=Category.objects.all()
    if request.session.has_key('customer_id'):

        uid = request.session['customer_id']
        order=Order.objects.filter(Customer_id=uid).order_by('-Order_id')
        return render(request,'Orderhistory.html',{"orders":order,'cate':cat})
    else:
        return redirect('/Client/clientlogin/')
    

def Ordersave(request):
    if request.session.has_key('customer_id'):
        uid = request.session['customer_id']
        order=CartTable.objects.filter(Customer_id=uid)
        if order is None:
            messages.error("Your cart is empty.")

        else:
            amt=0
            for val in order:
                amt=amt+(int(val.Product_id.Price)*int(val.Quantity))
            amt=amt+50
            date2=date.today().strftime("%Y-%m-%d")
            pm=request.POST.get('payment_mode')
            print('modeeeeeeeeeeeeeeeeeeeeeeeeeeee',pm)
            o=Order(Customer_id_id=uid,Total_Amount=amt,Order_Date=date2,Payment_status='0',Order_status='0',Payment_Mode=pm)
            o.save()
            oid=Order.objects.latest('Order_id')
            for data in order:
                pid=data.Product_id_id
                qty=data.Quantity
                pr=data.Product_id.Price
                total=int(qty)*pr
                od=Order_Item(Quantity=int(qty),Product_id_id=pid,Order_id_id=oid.Order_id,Price=total)
                od.save()
        
            return redirect('/Client/orderhistory/')
    else:
        return redirect('/Client/clientlogin/')
