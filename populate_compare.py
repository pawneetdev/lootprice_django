import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lootprice.settings')

import django
django.setup()

from compare.models import Category, Mobile


def populate():
    android_cat = add_cat('Android')

    add_mobile(cat=android_cat, company="Xiaomi", name="Mi3", price="14999")

    add_mobile(cat=android_cat, company="Samsung", name="S6", price="52235")
    
    add_mobile(cat=android_cat, company="Asus", name="Zenfone 2", price="19999")
    
    ios_cat = add_cat('IOS')
    
    add_mobile(cat=ios_cat, company="Apple", name="Iphone 5S", price="39999")
    
    add_mobile(cat=ios_cat, company="Apple", name="Iphone 6", price="69999")

    android_cat = add_cat('Window phones')

    add_mobile(cat=android_cat, company="Microsoft", name="Lumia", price="14999")

    
    
    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Mobile.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_mobile(cat, company, name, price):
    p = Mobile.objects.get_or_create(category=cat, company=company, name=name, price=price)[0]
    #p.url=url
    #p.views=views
    #p.save()
    return p

def add_cat(platform):
    c = Category.objects.get_or_create(platform=platform)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Compare population script..."
    populate()
