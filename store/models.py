from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField(max_length=200,blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/products',blank=True)
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
       return reverse('product_detail',args=[self.category.slug, self.slug])

    def __str__(self):
      return self.product_name