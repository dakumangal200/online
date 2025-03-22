from django import forms
from Cafe_admin.models import Area,Category,Product,Cafe_Table,Customer

class AreaForm(forms.ModelForm):
    class Meta:
        model=Area
        fields=["Area_name"]

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=["Category_Name","Description"]  

class ProductForm(forms.ModelForm):
    Product_image = forms.FileField()
    class Meta:
        model= Product
        fields=["Product_Name","Price","Description","Product_image","Category_id","Quantity"]

class CafeTableForm(forms.ModelForm):
    Layout_Image= forms.FileField()
    class Meta:
        model=Cafe_Table
        fields=["Layout_Image","No_of_seats","Avaibility_status","Description"]

class AdminMyaccountForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=["First_Name","Last_Name","Email","Password","Phone","Address","Area_id","is_admin","otp","otp_used"]

    
    