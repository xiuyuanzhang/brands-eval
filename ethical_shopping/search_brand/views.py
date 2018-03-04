from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django import forms
from .models import Rating 
from django.db.models import Q 


'''
class brand1(forms.CharField):
	def __init__(self, , *args, **kwargs):
		field = forms.CharField()
        super(brand1, self).__init__(fields=field,
                                           *args, **kwargs)
'''



class SearchForm(forms.Form):
    brand_name = forms.CharField(label = 'Brand name', 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter a brand name'
            }
        ), max_length = 300, required = True)



    def clean(self):
   
        #cleaned_data = super(SearchForm, self).clean()
        #brand_name = cleaned_data
        brand_name = self.cleaned_data
        if not brand_name:
            raise forms.ValidationError('You have to enter a brand or company name')
        return brand_name


def search(request):
    template_name = 'search_brand/search.html'
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            brand_name = form.cleaned_data["brand_name"]
            return redirect('result', brand_name)

           
            #HttpResponseRedirect(reverse('result'))
            #render(request, 'search_brand/result.html', {"result_set": result_set})


    else:
        form = SearchForm()



    return render(request, template_name, {'form':form})
# Create your views here.


def result(request, brand_name):
    key_word_list = brand_name.split()
            #brand_name = form.cleaned_data['brand_name']
    result_set = set()
    for key_word in key_word_list: 
        result = Rating.objects.filter(company_name__icontains = key_word)
        result_set = result_set | set(result)

    return render(request, 'search_brand/result.html', {"result_set": result_set})


def detail(request, comp_id):
    template_name = 'search_brand/detail.html'
    context = {}
    entry = Rating.objects.get(company_id = comp_id)
    context["company_name"] = entry.company_name
    context["company_rating"] = entry.rating


    return render(request, template_name, context)


