from django.shortcuts import render,redirect
import sys,random
from Cafe_admin.models import Customer,Area,Category,Product,Order,Order_Item,Feedback,Cafe_Table,Table_booking,Contactus,CartTable
from Cafe_admin.form import AreaForm,CategoryForm,ProductForm,CafeTableForm,AdminMyaccountForm
from Cafe_admin.function import handle_uploaded_file
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from datetime import date
from django.db import connection
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response



class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {"customers": 10})


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        #qs = Company.objects.all()
        cursor=connection.cursor()
        print('-------------------')
        cursor.execute('''select * from Product''')
        qs=cursor.fetchall()
        print("------------+++++++++++++++++++-----------------qs",qs)
        labels = []
        
        
        default_items = []
       
        for item in qs:
            print('item',item[0])
            labels.append(item[1])
            default_items.append(item[2])
        print('labels',labels)
        data = {
            "labels": labels,
            "default": default_items,
        }
        print(data)
        return Response(data)

# Create your views here.
def Index(request):
    user=Customer.objects.all().count()
    order=Order.objects.all().count()
    feed=Feedback.objects.all().count()
    od=Order.objects.filter(Order_status=0).order_by('-Order_id')[:10]
    return render(request,"index.html",{'customer':user,'order':order,'feedback':feed,'pending':od})

def ShowCustomer(request):
    if 'admin_id' in request.session:
        customer=Customer.objects.all()
        return render(request,'Customer_table.html',{'customer':customer})
    
    else:
        return redirect('/login/')

def ShowArea(request):
    if 'admin_id' in request.session:
        a=Area.objects.all()
        return render(request,'Area_table.html',{'area':a})
    else:
        return redirect('/login/')

def ShowContact(request):
    if 'admin_id' in request.session:
        cu=Contactus.objects.all()
        return render(request,"Contactus.html",{'icontact':cu})
    else:
        return redirect('/login/')
    
def ShowCategory(request):
    if 'admin_id' in request.session:
        c=Category.objects.all()
        return render(request,"Category_table.html",{"category":c})
    else:
        return redirect('/login/')

def ShowProduct(request):
    if 'admin_id' in request.session:
        p=Product.objects.all()
        return render(request,"Product_table.html",{"product":p})
    else:
        return redirect('/login/')

def ShowCart(request):
    if 'admin_id' in request.session:
        cr=CartTable.objects.all()
        return render(request,"Cart_table.html",{'cart':cr})
    else:
        return redirect('/login/')

def ShowOrder(request):
    if 'admin_id' in request.session:
        da = date.today().strftime("%Y-%m-%d")
        o=Order.objects.all()
        return render(request,"Order_table.html",{"order":o})
    else:
        return redirect('/login/')

def ShowOrder_Item(request,id):
    if 'admin_id' in request.session:
        oi=Order_Item.objects.filter(Order_id=id)
        print('-----------------------------',oi)
        return render(request,"Order_itemtable.html",{"orderitem":oi})
    else:
        return redirect('/login/')

def ShowFeedback(request):
    if 'admin_id' in request.session:
        f=Feedback.objects.all()
        return render(request,"Feedback_table.html",{"feedback":f})
    else:
        return redirect('/login/')

def ShowCafe_Table(request):
    if 'admin_id' in request.session:
        cf=Cafe_Table.objects.all()
        return render(request,"Cafe_Table.html",{"cafetable":cf})
    else:
        return redirect('/login/')

def ShowTable_Booking(request):
    if 'admin_id' in request.session:
        tb=Table_booking.objects.all()
        return render(request,"Table_Booking.html",{"tablebooking":tb})
    else:
        return redirect('/login/')

def basicelemet(request):
    return render(request,"basic_elements.html")

def Showindex(request):
    user=Customer.objects.all().count()
    order=Order.objects.all().count()
    feed=Feedback.objects.all().count()
    od=Order.objects.filter(Order_status=0).order_by('-Order_id')[:10]
    return render(request,"index.html",{'customer':user,'order':order,'feedback':feed,'pending':od})


def InsertArea(request):
    if request.method=="POST" :
        area=AreaForm(request.POST)
        print("Error in Area",area.errors)

        if area.is_valid():
            try:
                area.save()
                return redirect('/areatable')
            except:
                print("Error in Area",sys.exc_info())
    else:
        area=AreaForm()
    return render(request,'InsertArea.html',{'insertarea':area})

def InsertCategory(request):
    if request.method=="POST" :
        cat=CategoryForm(request.POST)
        print("Error in Categoryr",cat.errors)

        if cat.is_valid():
            try:
                cat.save()
                return redirect('/categorytable')
            except:
                print("Error in Category",sys.exc_info())
    else:
        cat=CategoryForm()
    return render(request,'InsertCategory.html',{'insertcategory':cat})   

def InsertProduct(request):
    cat = Category.objects.all()
    if request.method=="POST" :
        pro=ProductForm(request.POST, request.FILES)
        print("------------------------------",pro.errors)

        if pro.is_valid():
            try:
                handle_uploaded_file(request.FILES['Product_image'])
                pro.save()
                return redirect('/product')
            except:
                print("Error in Product",sys.exc_info())
    else:
        pro=ProductForm()
    return render(request,'InsertProduct.html',{'insertproduct':pro, 'cate':cat}) 


def InsertCafeTable(request):
    if request.method=="POST" :
        cafet=CafeTableForm(request.POST,request.FILES)
        print("Error in Cafetable",cafet.errors)

        if cafet.is_valid():
            try:
                handle_uploaded_file(request.FILES['Layout_Image'])
                cafet.save()
                return redirect('/cafetable')
            except:
                print("Error in Cafe Table",sys.exc_info())
    else:
        cafet=CafeTableForm()
    return render(request,'InsertCafeTable.html',{'insertcafetable':cafet})

def DeleteCafeTable(request,id):
    cafetable=Cafe_Table.objects.get(Table_id=id)
    cafetable.delete()
    return redirect('/cafetable/')

def DeleteArea(request,id):
    area=Area.objects.get(Area_id=id)
    area.delete()
    return redirect('/areatable/')

def DeleteCategory(request,id):
    cat=Category.objects.get(Category_id=id)
    cat.delete()
    return redirect('/categorytable/')

def DeleteProduct(request,id):
    pro=Product.objects.get(Product_id=id)
    pro.delete()
    return redirect('/product/')

def updateArea(request,id):
    a=Area.objects.get(Area_id=id)
    if request.method == 'POST':
        area=AreaForm(request.POST,instance=a)
        print("Error In Update Area",area.errors)
        if area.is_valid():
            try:
                area.save()
                return redirect('/areatable/')
            except:
                print("Error in update area",sys.exc_info())
    else:
        a=Area.objects.get(Area_id=id)
    return render(request,'UpdateArea.html',{'Area':a})

def updateCafeTable(request,id):
    ct=Cafe_Table.objects.get(Table_id=id)
    if request.method == 'POST':
        cafet=CafeTableForm(request.POST,request.FILES,instance=ct)
        print("Error In Update Cafe table",cafet.errors)
        if cafet.is_valid():
            try:
                handle_uploaded_file(request.FILES['Layout_Image'])
                cafet.save()
                return redirect('/cafetable/')
            except:
                print("Error in update cafe table",sys.exc_info())
    else:
        ct=Cafe_Table.objects.get(Table_id=id)
    return render(request,'UpdateCafeTable.html',{'Cafe':ct})

def updateCategory(request,id):
    c=Category.objects.get(Category_id=id)
    if request.method == 'POST':
        cate=CategoryForm(request.POST,instance=c)
        print("Error In Update Category table",cate.errors)
        if cate.is_valid():
            try:
                cate.save()
                return redirect('/categorytable/')
            except:
                print("Error in update category table",sys.exc_info())
    else:
        c=Category.objects.get(Category_id=id)
    return render(request,'UpdateCategory.html',{'Cate':c})

def updateProduct(request,id):
    cat = Category.objects.all()
    pro=Product.objects.get(Product_id=id)
    if request.method == 'POST':
        prod=ProductForm(request.POST,request.FILES,instance=pro)
        print("Error In Update product table",prod.errors)
        if prod.is_valid():
            try:
                handle_uploaded_file(request.FILES['Product_image'])
                prod.save()
                return redirect('/product/')
            except:
                print("Error in update product table",sys.exc_info())
    else:
        pro=Product.objects.get(Product_id=id)
    return render(request,'UpdateProduct.html',{'Pro':pro,'cate':cat})

def Login(request):
    if request.method =='POST':
        email=request.POST["Email"]
        password=request.POST["Password"]
        val=Customer.objects.filter(Email=email,Password=password,is_admin=1).count()
        print(val)
        print("---------",email,"----------",password)
        if val == 1:
            data=Customer.objects.filter(Email=email,Password=password,is_admin=1)
            for item in data:
                request.session['admin_id']=item.Customer_id
                request.session['admin_email']=item.Email
                request.session['admin_pass']=item.Password
                if request.POST.get("remember"):
                    response=redirect('/dashboard/')
                    response.set_cookie('admin_email',request.POST['Email'],3600*24*365*2)
                    response.set_cookie('admin_pass',request.POST['Password'],3600*24*365*2)
                    return response
            return redirect('/dashboard/')
        else:
            messages.error(request,"Invalid Username and Password")
            return redirect('/login/')
    else:
        if request.COOKIES.get('admin_email'):
            return render(request,"login.html",{'a_mail': request.COOKIES['admin_email'],'a_pass':request.COOKIES['admin_pass']})
        return render(request,"login.html")
    
def Logout(request):
    aid=request.session['admin_id']
    aemail=request.session['admin_email']
    apassw=request.session['admin_pass']
    print("-----------------------",aid,aemail,apassw)
    del request.session['admin_id']
    del request.session['admin_email']
    del request.session['admin_pass']
    # messages.success(request,"Logged out Successfully")
    print("----------------",aid,aemail,apassw)
    return redirect("/login/")


    
def Forgotpass(request):
    return render(request,'Forgotpass.html')

def Sendotp(request):
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
    return render(request,'Setpass.html')

def Setpass(request):
    if request.method=="POST":
        T_otp=request.POST['otp']
        T_pass=request.POST['pass']
        T_cpass=request.POST['cpass']

        if T_pass==T_cpass:
            e=request.session['temail']
            val=Customer.objects.filter(Email=e,otp=T_otp,otp_used=0).count()
            if val==1:
                Customer.objects.filter(Email=e).update(otp_used=1,Password=T_pass)
                return redirect('/login/')
            else:
                messages.error(request,"Invalid OTP")
                return render(request,"Forgotpass.html")
        else:
            messages.error(request,"Password does not match")
            return render(request,"Setpass.html")
    else:
        return redirect("forgotpass")

def Accept_order(request,id):
    ac=Order.objects.get(Order_id=id)
    ac.Order_status="1"
    ac.save()
    return redirect("/order/")

def Reject_order(request,id):
    rj=Order.objects.get(Order_id=id)
    rj.Order_status="2"
    rj.save()
    return redirect("/order/")

def ReportProduct(request):
    cat=Category.objects.all()
    print(cat)
    if request.method == "POST":
        sd=request.POST.get('scat')
        order_dt=Product.objects.filter(Category_id=sd)
    else:
        order_dt = Product.objects.all()
    return render(request,"Report.html",{'order':order_dt,'product':cat})

def ReportOrder(request):
    # da = date.today().strftime("%Y-%m-%d")
    rt=Order.objects.all()
    print(rt)
    if request.method =="POST":
        st=request.POST.get('sdate')
        ed=request.POST.get('edate')
        # st1 = st.strftime("%Y-%m")
        ro=Order.objects.filter(Order_Date__range=[st,ed])
        
    else:
        ro=Order.objects.all()
    return render(request,"Order_report.html",{'orderreport':ro,'orderr':rt})


def AdminMyaccount(request):
    
    ar=Area.objects.all()
    id = request.session['admin_id']
    ma=Customer.objects.get(Customer_id=id)
    if request.method == 'POST':
        mac=AdminMyaccountForm(request.POST,instance=ma)
        print("Error In Update Registration",mac.errors)
        if mac.is_valid():
            try:
                mac.save()
                return redirect('/Myaccount/')
            except:
                print("Error in update registration",sys.exc_info())
    else:
        ma=Customer.objects.get(Customer_id=id)
    return render(request,"Adminaccount.html",{'amyaccount':ma,'areaa':ar})

def AssignTable(request,id):

    if request.method=="POST":
        asd = request.POST.get('Table_id')
        print('inside assign =================')
        ct=Cafe_Table.objects.filter(Avaibility_status=0)
        # tb=Table_booking.objects.filter(Booking_id=id).update(Table_id_id=asd,Booking_status=1)
        dg=Table_booking.objects.get(Booking_id=id)
        ct = Cafe_Table.objects.get(Table_id=asd)
        ct.Avaibility_status='1'
        print('=========================')
        ct.save()
        dg.Booking_status ="1"
        dg.Table_id_id=asd
        dg.save()
        return redirect('/tablebooking')
    else:
        ct=Cafe_Table.objects.filter(Avaibility_status=0)
        # tb=Table_booking.objects.filter(Booking_id=id).update(Table_id_id=asd,Booking_status=1)
        dg=Table_booking.objects.get(Booking_id=id)
    return  render(request,"Assigntable.html",{"ct":ct,"dg":dg})


def ChangeStatus(request,id):
    if request.method=="POST":
        asr=request.POST.get('Avaibility_status')
        ct = Cafe_Table.objects.get(Table_id=id)
        ct.Avaibility_status=asr
        ct.save()
        return redirect('/cafetable')
    else:
        asr=request.POST.get('Avaibility_status')
        ct = Cafe_Table.objects.get(Table_id=id)
    return render(request,"ChangeStatus.html",{"cs":ct,"asd":asr})
