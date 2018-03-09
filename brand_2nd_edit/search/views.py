from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django import forms
from .models import Rating, CompanyToBrand, Assessment, TransIndex, LabourRating, Evaluation
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
                'placeholder': '    Enter a brand name here',
                'size':90,
                'style': 'height:45px;'
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
    template_name = 'search/search.html'
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
    company_result= set()
    brand_result = set()
    context = {}
    company_id_set = set()
    for key_word in key_word_list: 
        result = Rating.objects.filter(company_name__icontains = key_word)
        company_result = company_result | set(result)
    for key_word in key_word_list:
        result = CompanyToBrand.objects.filter(brand_name__icontains = key_word)
        brand_result = brand_result | set(result)
    context["company_result"] = company_result 
    context["brand_result"] = brand_result
    for company in company_result:
        company_id_set.add(company.company_id)
    for brand in brand_result:
        company_id_set.add(brand.company_id)
    if len(company_id_set) == 1:
        company_id = company_id_set.pop()
        return redirect('detail', company_id)
    else:
        return render(request, 'search/result.html', context)


def detail(request, comp_id):
    template_name = 'search/detail.html'
    context = {}
    try:
        rating = Rating.objects.get(company_id = comp_id)

    except Rating.DoesNotExist:
        raise Http404("Question does not exist")

    context["rating"] = rating
    brands = CompanyToBrand.objects.filter(company_id = comp_id)
    brand_all = {}
    company_evaluation = []
    for brand in brands:
        brand_info = {} 
        brand_id = brand.brand_id
        trans_index = TransIndex.objects.filter(brand_id = brand_id + ".0")
        if len(trans_index) != 0:
            brand_info["trans_index"] =  trans_index[0]
        labour_rating = LabourRating.objects.filter(brand_id = brand_id + ".0")
        if len(labour_rating) != 0:
            brand_info["labour_rating"] = labour_rating[0]
        evaluation = Evaluation.objects.filter(brand_id = brand_id)
        if len(evaluation)  != 0:
            company_evaluation.append(evaluation[0])
        brand_all[brand] = brand_info
    
    if len(company_evaluation) == 0:
        context["evaluation"] = []
    else:
        context["evaluation"] = [company_evaluation[0]]



    context["brands"] = brand_all
    context["environment"] = Assessment.objects.filter(company_id = comp_id, aspect = "Environment")
    context["business"] = Assessment.objects.filter(company_id = comp_id, aspect = "Business Ethics")
    context["social"] = Assessment.objects.filter(company_id = comp_id, aspect = "Social")
    context["animal"] = Assessment.objects.filter(company_id = comp_id, aspect = "Animals")
    context["information"] = Assessment.objects.filter(company_id = comp_id, aspect = "Information")



    return render(request, template_name, context)


def brand_info(request, brand_id):
    template_name = 'search/brand_info.html'
    context = {}
    try: 
        brand = CompanyToBrand.objects.get(brand_id = brand_id)
    except CompanyToBrand.DoesNotExist:
        raise Http404("Brand does not exist")



    return render(request, template_name, context)



