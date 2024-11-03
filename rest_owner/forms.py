from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'post', 'city', 'about', 'phone', 'image']


#signup & login
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Login_owner

class ownerSignUpForm(UserCreationForm):
    phone = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'phone')

    def save(self, commit=True):
        user = super(ownerSignUpForm, self).save(commit=False)
        user.save()
        profile = Login_owner.objects.create(user=user, phone=self.cleaned_data['phone'])
        return user
