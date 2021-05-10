from django import forms
from django_countries.fields import CountryField
from . import models

class SearchForm(forms.Form):

    city = forms.CharField(initial="Anywhere",)
    country = CountryField(default="KR").formfield()
    price = forms.IntegerField(required=True)
    room_type = forms.ModelChoiceField(empty_label = "Any kind", queryset=models.RoomType.objects.all(),required=False)
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    baths  = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
    amentities = forms.ModelMultipleChoiceField(required=False, queryset=models.Amentity.objects.all(), widget=forms.CheckboxSelectMultiple)
    facilities = forms.ModelMultipleChoiceField(required=False, queryset=models.Facilitiy.objects.all(), widget=forms.CheckboxSelectMultiple)