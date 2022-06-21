from django.db import models
from django.urls import reverse
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=20, db_index=True, unique=True)
    image = models.ImageField(upload_to='products/%y/%m/%d')
    info = models.CharField(max_length=58, db_index=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_category', args=[self.slug])



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='Category', on_delete = models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    info = models.TextField(default='Ürün Aaçıklama')
    price = models.DecimalField(max_digits=10, decimal_places=0)
    normal_price = models.CharField(max_length=4,db_index=True,default='SOME STRING')
    discount = models.CharField(max_length=4,db_index=True,default='SOME STRING')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    descrip = models.CharField(max_length=160, db_index=True, default='Description')
    keyword = models.CharField(max_length=60, db_index=True, default='Keyword')
    page_title = models.CharField(max_length=60, db_index=True, default='Sayfa Title')
    alt = models.CharField(max_length=100, db_index=True, default='Ürün İmage Alt Açıklaması')
    title = models.CharField(max_length=100, db_index=True, default='Ürün İmage Title Açıklaması')
    canocinal = models.CharField(max_length=100, db_index=True, default='www.centralwebagency.com')

    def __str__(self):
        return self.name




    def get_absolute_url(self):
        return reverse('show_category', args=[self.slug, self.id])





class Restaurant(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    link = models.CharField(max_length=200, db_index=True)
    facebook = models.CharField(max_length=200, db_index=True)
    instagram = models.CharField(max_length=200, db_index=True)
    twitter = models.CharField(max_length=200, db_index=True)
    location = models.CharField(max_length=200, db_index=True)
    map = models.CharField(max_length=200, db_index=True)
    day = models.CharField(max_length=200, db_index=True)
    dayend = models.CharField(max_length=200, db_index=True)
    phone = models.CharField(max_length=200, db_index=True)



    def __str__(self):
        return self.name



