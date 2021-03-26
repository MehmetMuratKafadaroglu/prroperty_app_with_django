from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from PIL import Image
class PublishedManager(models.Manager):
    def get_queryset(self):
           return super(PublishedManager,
                        self).get_queryset()\
                             .filter(status='published')

       

class Post(models.Model) :
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    PROPERTY_CHOICES = (
        ('house','House'),
        ('flat', 'Flat'),
        ('boat','Boat'),
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,null = False, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    objects = models.Manager()
    published = PublishedManager()
    address = models.CharField(max_length=250, default = 'Unit 3 Victoria Way, Rawtenstall')
    city = models.CharField(max_length=50, default = 'London') 
    postcode = models.CharField(max_length=50, default = 'BB4 7NY')
    price = models.IntegerField(default = 200000.00)
    property_type = models.CharField(max_length=10, choices=PROPERTY_CHOICES, default='house')
    number_of_beds = models.IntegerField(default = 2)
    number_of_baths = models.IntegerField(default = 1)
    property_pic = models.ImageField( upload_to = 'property_photos')

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk' : self.id, 'slug': self.slug})
    
    def save(self, *args, **kwargs,):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
         
class Meta:
    ordering = ('-publish',)

def __str__(self):
           return self.title

