#from compare.models import Category, Mobile
#from django import forms

#categories = Category.objects.all()


#platforms = (
#	('1', 'Andorid'),
#	('2', 'IOS'),
#	('3', 'Window phones'),
#)

#class xyz(forms.Form):
#	name = forms.CharField(max_length=128)
#	choice = forms.ChoiceField(choices=platforms)

#class NameForm(forms.Form):
#    your_name = forms.CharField(label='Your name', max_length=100)
    
#if categoies:
#	for c in categories:
#		choices.append((c.platform, c.platform),)

from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(widget=forms.TextInput())
