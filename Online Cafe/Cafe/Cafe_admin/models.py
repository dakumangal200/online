from django.db import models

# Create your models here.
class Area(models.Model):
    Area_id=models.AutoField(primary_key=True)
    Area_name = models.CharField(max_length=100)

    class Meta:
        db_table="Area"

class Customer(models.Model):
    Customer_id=models.AutoField(primary_key=True)
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=50)
    Phone=models.CharField(max_length=20,null=False)
    Address=models.CharField(max_length=300)
    Area_id=models.ForeignKey(Area,on_delete=models.CASCADE)
    is_admin=models.CharField(max_length=50)
    otp=models.CharField(max_length=10,null=True)
    otp_used=models.IntegerField()

    class Meta:
        db_table="Customer"

class Category(models.Model):
    Category_id=models.AutoField(primary_key=True)
    Category_Name=models.CharField(max_length=100)
    Description=models.CharField(max_length=400)

    class Meta:
        db_table="Category"


class Product(models.Model):
    Product_id=models.AutoField(primary_key=True)
    Product_Name=models.CharField(max_length=100)
    Price=models.IntegerField()
    Description=models.CharField(max_length=400)
    Product_image=models.CharField(max_length=2000)
    Category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    Quantity=models.IntegerField(null=False)

    class Meta:
        db_table="Product"



class Order(models.Model):
    Order_id=models.AutoField(primary_key=True)
    Customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Order_Date=models.DateField(null=False)
    Total_Amount=models.IntegerField()
    Order_status=models.CharField(max_length=100)
    Payment_status=models.CharField(max_length=100)
    Payment_Mode=models.CharField(max_length=100)

    class Meta:
        db_table="Order"

class Order_Item(models.Model):
    Order_Item_id = models.AutoField(primary_key=True)
    Order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    Product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField(null=False)
    Price=models.IntegerField()

    class Meta:
        db_table="Order_Item"

class Feedback(models.Model):
    Feedback_id=models.AutoField(primary_key=True)
    Description=models.CharField(max_length=400)
    Customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    Feedback_date=models.DateField(null=False)

    class Meta:
        db_table="Feedback"

class Cafe_Table(models.Model):
    Table_id=models.AutoField(primary_key=True)
    Layout_Image=models.CharField(max_length=2000)
    No_of_seats=models.IntegerField()
    Avaibility_status=models.CharField(max_length=100)
    Description=models.CharField(max_length=400)

    class Meta:
        db_table="Cafe_Table"

class Table_booking(models.Model):
    Booking_id=models.AutoField(primary_key=True)
    Customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Phonenumber=models.IntegerField()
    Table_id=models.ForeignKey(Cafe_Table,on_delete=models.CASCADE)
    Booking_Date=models.DateField(null=False)
    Booking_status=models.CharField(max_length=100)
    Booking_Time=models.TimeField(null=False)
    NumberofPeople=models.IntegerField()
    class Meta:
        db_table="Table_booking"


class Contactus(models.Model):
    contact_id=models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Message=models.CharField(max_length=300)

    class Meta:
        db_table='ContactUs'

class CartTable(models.Model):
    cart_id=models.AutoField(primary_key=True)
    Customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    Quantity=models.PositiveIntegerField()
    Total=models.IntegerField()

    class Meta:
        db_table='Cart'