from django import forms

AVAILABLE_LINKS = [
    ('linkedin', 'LinkedIn'),
    ('indeed', 'Indeed')
]

class URLForm(forms.Form):
    name= forms.CharField(widget = forms.Select(choices = AVAILABLE_LINKS))
    weblink = forms.CharField(max_length = 200)
