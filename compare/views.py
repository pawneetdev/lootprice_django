from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from compare.models import Category, Mobile
from compare.forms import xyz, search_mobiles, compare_form
from django.db.models import Q
import itertools

#def index(request):
#    category_list = Category.objects.all()
#    context_dict = {'categories': category_list}
#    return render(request, 'compare/index.htm', context_dict)

#def category(request, category_platform_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
#    context_dict = {}

#    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
#        category = Category.objects.get(slug=category_platform_slug)
#        context_dict['category_platform'] = category.platform

        # Retrieve all of the associated mobiles.
        # Note that filter returns >= 1 model instance.
#        mobiles = mobile.objects.filter(category=category)

        # Adds our results list to the template context under name mobiles.
#        context_dict['mobiles'] = mobiles
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
#        context_dict['category'] = category
#    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
#        pass

    # Go render the response and return it to the client.
#    return render(request, 'compare/category.htm', context_dict)

#def mobile(request):
#	return HttpResponse("working")

#	if request.method == "POST":
	
#		form = NameForm(request.POST)
	
#		if form.is_valid():
			#plat = form.cleaned_data['choice']
#			return HttpResponseRedirect('/thanks/')
		
		#return HttpResponseRedirect('compare/mobile/')
	
 #   	else:
    	
 #   		form = NameForm()
    	
#	return render(request, 'compare/index.htm', {'form': form})
	
	
#	context_dict = {'plat': plat}
	
#	return render(request, '/compare/mobile.htm', contex_dict)

#def get_name(request):

#    if request.method == 'POST':
        
#        form = NameForm(request.POST or None)
        
#        if form.is_valid():
            
#            return HttpResponseRedirect('/thanks/')


#    else:
#        form = NameForm()

#    return render(request, 'compare/index.htm', {'form': form})

#def get_name(request):
#   if request.method == 'POST':
#      form = NameForm(request.POST)
#      if form.is_valid():
#          return HttpResponseRedirect('/thanks/')

#   else:
#      form = NameForm()

#   return render(request, 'compare/index.htm', {'form': form})

def homepage(request):
	return render(request, 'compare/homepage.htm')


def get_name(request):
   
   	#####################################
	# Find mobile by selecting platform #
	#####################################
   
   if request.method == 'POST':
      form = xyz(request.POST)

      if form.is_valid():

          plat = form.cleaned_data['Mobiles']
          return display(request, plat)

   else:
      form = xyz()

   return render(request, 'compare/index.htm', {'form': form})
   

def display(request, plat):
	
	#################################
	# view to get data from get_name#
	################################# 
	
	mobiles = []
	prices = []
	context_dict = {}
	
	context_dict['plat'] = plat
	for c in Category.objects.filter(platform = plat):
	        for p in Mobile.objects.filter(category=c):
	            mobiles.append(p)
	#print mobiles
	
	if plat == 'All':
			for p in Mobile.objects.all():
				mobiles.append(p)
				
	context_dict['mobile_post'] = mobiles
	
	return render(request, 'compare/mobile.htm', context_dict);

def search(request):
	
	########################
	# find mobiles by name #
	########################
	
	if request.method == 'POST':
		form = search_mobiles(request.POST)
	
		if form.is_valid():
			search_text = form.cleaned_data['Search']
			return result(request, search_text)
			
	else:
		form = search_mobiles()
			
	return render(request, 'compare/search.htm', {'form': form})



def result(request, search_text):
	
	################################
	# view to get data from search #
	################################
	
	context_dict = {}
	a = []
	search_mobile = []
	
	a = search_text.split() #To split the searched text using space as delimiter
	
	for x in a:
		search_mobile.append(Mobile.objects.filter(Q(company__icontains = x) | Q(name__icontains = x))) 
		#Q allows complex computations like OR is used here
		#Company_icontains: checks whether company contains x or not
		
	chain = itertools.chain(*search_mobile) #To convert non-linear or multidimensional list to linear or 1-D
	
	chain = list(set(chain)) #To remove duplicates from the list
	
	context_dict['search_post'] = chain
	
	return render(request, 'compare/results.htm', context_dict);

def specs(request, mobile_id):
	
	################################
	#  show mobile features/specs  #
	################################	
		
	mobile = Mobile.objects.filter(id = mobile_id)
	
	return render(request, 'compare/specs.htm', {'mobile': mobile})

def compare(request):
	
	if request.method == 'POST':
		form = compare_form(request.POST)
		
		if form.is_valid():
			search_text = form.cleaned_data['m1']
			return compare_result(request, search_text)
	else:
		form = compare_form()
	
	return render(request, 'compare/compare.htm', {'form': form})
			
def compare_result(request, search_text):
	
	################################
	# 							   #
	################################
	
	context_dict = {}
	a = []
	search_mobile = []
	
	a = search_text.split() #To split the searched text using space as delimiter
	
	for x in a:
		search_mobile.append(Mobile.objects.filter(Q(company__icontains = x) | Q(name__icontains = x))) 
		#Q allows complex computations like OR is used here
		#Company_icontains: checks whether company contains x or not
		
	chain = itertools.chain(*search_mobile) #To convert non-linear or multidimensional list to linear or 1-D
	
	chain = list(set(chain)) #To remove duplicates from the list
	
	context_dict['search_post'] = chain
	
	return render(request, 'compare/compare1.htm', context_dict);

def add(request, mobile_id):
	
	################################
	#                              #
	################################	
	
	if request.method == 'POST':
		form = compare_form(request.POST)
		
		if form.is_valid():
			search_text = form.cleaned_data['m1']
			return compare_result(request, search_text)
	else:
		form = compare_form()
	
	try:
		if len(request.session['m'])<4 :
			try:
				ids = [request.session['m'],]
				chain = itertools.chain(*ids)
				ids = list(set(chain))
				ids.append(mobile_id)
					
				
			except:
				ids = []
				ids = [mobile_id,]
				
			request.session['m'] = ids
			print request.session['m']
								
				
			for x in request.session['m']:
				try:
					mobile = mobile + [Mobile.objects.filter(id = x)]
			
				except UnboundLocalError:
					mobile = [Mobile.objects.filter(id = x)]
				
			chain = itertools.chain(*mobile)
			mobile = list(set(chain))
			
		else:
			mobile = []

			for x in request.session['m']:
				try:
					mobile = mobile + [Mobile.objects.filter(id = x)]
			
				except UnboundLocalError:
					mobile = [Mobile.objects.filter(id = x)]
				
			chain = itertools.chain(*mobile)
			mobile = list(set(chain))
			
			message = "*Cannot select more than 4 phones"
			
			return render(request, 'compare/compare.htm', {'message': message, 'mobile': mobile, 'form':form})
			
	except Exception:
		
		try:
				ids = [request.session['m'],]
				chain = itertools.chain(*ids)
				ids = list(set(chain))
				ids.append(mobile_id)
					
				
		except:
			ids = []
			ids = [mobile_id,]
				
		request.session['m'] = ids
		print request.session['m']
								
				
		for x in request.session['m']:
			try:
				mobile = mobile + [Mobile.objects.filter(id = x)]
			
			except UnboundLocalError:
				mobile = [Mobile.objects.filter(id = x)]
				
		chain = itertools.chain(*mobile)
		mobile = list(set(chain))
	
				
	return render(request, 'compare/compare.htm', {'mobile': mobile, 'form':form})

def remove(request, mobile_id):

	################################
	#                              #
	################################
		
	try:
		if mobile_id == '0':
			print "here"
			del request.session['m']
		else:
			print request.session['m']
			request.session['m'].remove(mobile_id)
			print request.session['m']
	except:
		pass
	
	
	return add(request, 0)
