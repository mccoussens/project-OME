from django import forms

class LocationForm(forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=100)
    your_latitude = forms.DecimalField(label='Your Latitude', max_digits=6, decimal_places=4)
    your_longitude = forms.DecimalField(label='Your Longitude', max_digits=6, decimal_places=4)
    their_name = forms.CharField(label='Their Name', max_length=100)
    their_latitude = forms.DecimalField(label='Their Latitude', max_digits=6, decimal_places=4)
    their_longitude = forms.DecimalField(label='Their Longitude', max_digits=6, decimal_places=4)

