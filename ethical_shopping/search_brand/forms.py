from django import forms

class SearchForm(forms.Form):
	brand_name = forms.CharField(label = 'Brand name', max_length = 300)
	company_anme = forms.CharField(label = 'Company name', max_length = 300)