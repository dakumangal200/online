from django.urls import path
from Venada import Clientviews

urlpatterns = [
    path('clientindex/',Clientviews.ClientIndex),
    path('menu/<int:id>',Clientviews.ClientMenu),
    path('clientlogin/',Clientviews.CLogin),
    path('insertcontact/',Clientviews.InsertContact),
    path('clientforgotpass/',Clientviews.CForgotpass),
    path('csendotp/',Clientviews.CSendotp),
    path('csetpass/',Clientviews.CSetpass),
    path('registration/',Clientviews.Registration),
    path('reservation/',Clientviews.Reservation),
    path('aboutus/',Clientviews.Aboutus),
    path('clogout/',Clientviews.ClientLogout),
    path('gallery/',Clientviews.Gallary),
    path('loadmenu/',Clientviews.LoadMenu),
    path('loadcategory/',Clientviews.LoadCategory),
    path('detail/<int:id>',Clientviews.Blog),
    path('myaccount/',Clientviews.Myaccount),
    path('insfeedback/',Clientviews.CFeedback),
    path('cartitem/',Clientviews.ItemCart),
    path('insertitem/',Clientviews.InsertCart),
    path('updatecart/<int:id>',Clientviews.update_quantity),
    path('checkout/',Clientviews.Checkout),
    path('removecart/<int:id>',Clientviews.destroycart),
    path('ordersuccessfull/',Clientviews.OrderSuccess),
    path('placeorder/<int:id>', Clientviews.place_order_online),
    path('deletecart/<int:id>',Clientviews.DeletecartItem),
    path('orderhistory/',Clientviews.OrderHistory),
    path('placeorder/<int:total>',Clientviews.palce_order),
    path('Ordersave/',Clientviews.Ordersave),

    
    
]