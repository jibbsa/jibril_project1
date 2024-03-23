from django import forms
from Jibril_Painting_Item.models import Painting

class OrderForm(forms.Form):
    player_name = forms.CharField(label='Name', max_length=100)
    full_name = forms.CharField(label='Full Name', max_length=100)
    email = forms.EmailField(label='Email Address')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    address = forms.CharField(widget=forms.Textarea, label='Address')
    city = forms.CharField(label='City', max_length=100)
    province = forms.CharField(label='Province', max_length=100)
    postal_code = forms.CharField(label='Postal Code', max_length=10)
    painting = forms.ModelChoiceField(queryset=Painting.objects.all(), label='Select a Painting')
