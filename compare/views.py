from django.shortcuts import render
from compare.models import Category, Mobile

def index(request):
    category_list = Category.objects.all()
    context_dict = {'categories': category_list}
    return render(request, 'compare/index.htm', context_dict)
    
def category(request):
    category = Category.objects.all()
    context_dict['categories'] = category
    
    mobile = Mobile.objects.filter(category=category)
    context_dict['mobiles'] = mobile
    
    return render(request, 'rango/category.html', context_dict)
