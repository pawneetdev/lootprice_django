from compare.models import Category, Mobile
from django import forms

categories = Category.objects.all()

choices=[]

if categories:
	for c in categories:
		choices.append([c.platform, c.platform],)
		#a = ((c.platform, c.platform),)
	
choices1 = [('All','All')] + choices


class xyz(forms.Form):
    
	Mobiles = forms.ChoiceField(choices=choices1, required=False, label = "Mobiles")


class search_mobiles(forms.Form):
	
	Search = forms.CharField(max_length = 128, required = False, label = "")

class compare_form(forms.Form):
	
	m1 = forms.CharField(max_length = 128, required = True, label = "")
	#m2 = forms.CharField(max_length = 128, required = True, label = "")
	
#platforms = [
#	['1', 'Andorid'],
#	['2', 'IOS'],
#	['3', 'Window phones'],
#]


#class xyz(forms.Form):
#	name = forms.CharField(max_length=128)
#	choice = forms.ChoiceField(choices=platforms)

