from django import forms

class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(
        label='Your QR Name',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter QR name'
            })
        )
    url = forms.URLField(
        label='Your URL',
        max_length=200,
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your URL'
            })
        )