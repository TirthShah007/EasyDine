from django import forms

# # from .models import Booking

# # #form for book table
# class BookingForm(forms.Form):
#     names = forms.CharField(max_length=100)
#     datetime = forms.DateTimeField()
#     people = forms.IntegerField()

# class PaymentForm(forms.Form):
#     invoice_number = forms.CharField(max_length=20)
#     total_payment = forms.DecimalField(max_digits=10, decimal_places=2)


#signup form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Login

class SignUpForm(UserCreationForm):
    phone = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2', 'phone')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.save()
        profile = Login.objects.create(user=user, phone=self.cleaned_data['phone'])
        return user







    
        
  