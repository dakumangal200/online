"""
URL configuration for Cafe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include, re_path as url
from Cafe_admin import views

from Cafe_admin.views import HomeView, ChartData


urlpatterns = [
    path('admin/', admin.site.urls),
    path('icontact/',views.ShowContact),
    path('index/',views.Index),
    path('customertable/',views.ShowCustomer),
    path('areatable/',views.ShowArea),
    path('categorytable/',views.ShowCategory),
    path('product/',views.ShowProduct),
    path('order/',views.ShowOrder),
    path('orderitem/<int:id>',views.ShowOrder_Item),
    path('feedback/',views.ShowFeedback),
    path('cafetable/',views.ShowCafe_Table),
    path('tablebooking/',views.ShowTable_Booking),
    path('basicelement/',views.basicelemet),
    path('dashboard/',views.Showindex),
    path('insertarea/',views.InsertArea),
    path('insertcategory/',views.InsertCategory),
    path('insertproduct/',views.InsertProduct),
    path('insertcafetable/',views.InsertCafeTable),
    path('deletecafetable/<int:id>',views.DeleteCafeTable),
    path('deletearea/<int:id>',views.DeleteArea),
    path('deletecategory/<int:id>',views.DeleteCategory),
    path('deleteproduct/<int:id>',views.DeleteProduct),
    path('updatearea/<int:id>',views.updateArea),
    path('updatecafetable/<int:id>',views.updateCafeTable),
    path('updatecategory/<int:id>',views.updateCategory),
    path('updateproduct/<int:id>',views.updateProduct),
    path('login/',views.Login),
    path('sendotp/',views.Sendotp),
    path('forgotpass/',views.Forgotpass),
    path('setpassword/',views.Setpass),
    path('Client/',include('Venada.Clienturls')),
    path('cart/',views.ShowCart),
    path('logout/',views.Logout),
    path('accept/<int:id>',views.Accept_order),
    path('reject/<int:id>',views.Reject_order),
    path('report/',views.ReportProduct),
    path('orderreport/',views.ReportOrder),
    url(r'home', HomeView.as_view(), name='home'),
    url(r'^api/chart/data/$', ChartData.as_view(),name="api-data"),
    path('Myaccount/',views.AdminMyaccount),
    path('assigntable/<int:id>',views.AssignTable),
    path('changestatus/<int:id>',views.ChangeStatus),
    
    

]
