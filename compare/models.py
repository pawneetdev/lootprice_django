from django.template.defaultfilters import slugify
from django.db import models

class Category(models.Model):
    platform = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.platform)
        super(Category, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.platform
      
class Mobile(models.Model):
    category = models.ForeignKey(Category)
    company = models.CharField(max_length=128)
    name = models.CharField(max_length=128, unique=True)
    price = models.IntegerField(default=0)
    
    def __unicode__(self):
        return "%s %s" %(self.company, self.name)
