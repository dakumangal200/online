from django import forms
from Cafe_admin.models import Contactus,Customer,Table_booking,Feedback



class ContactForm(forms.ModelForm):
    class Meta:
        model=Contactus
        fields=["Name","Email","Message"]

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=["First_Name","Last_Name","Email","Password","Phone","Address","Area_id","otp","otp_used","is_admin"]

class TablebookingForm(forms.ModelForm):
    class Meta:
        model=Table_booking
        fields=["Customer_id","Phonenumber","Booking_Date","Booking_status","Booking_Time","NumberofPeople"]

class FeedBackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=["Description","Customer_id","Product_id","Feedback_date"]
