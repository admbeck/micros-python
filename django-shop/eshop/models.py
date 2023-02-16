from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# from colorama.ansi import clear_screen

class Category(models.Model):
    """Creates table with categories for shop inventory"""
    title = models.CharField(max_length=150, verbose_name='Category name')
    image = models.ImageField(upload_to='categories/', null=True, blank=True, verbose_name='Images')
    slug = models.SlugField(unique=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Sub-category', related_name='subcategories')

    def get_absolute_url(self):
        """Link to category page"""
        return reverse('category_detail', kwargs={'slug': self.slug})

    def get_parent_category_photo(self):
        """Get images for parent categories"""
        if self.image:
            return self.image
        else:
            return 'https://http.cat/404.jpg'

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Category: pk={self.pk}, title={self.title}'

    class Meta:
        """Used for translation"""
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    """Creates table of product items"""
    title = models.CharField(max_length=255, verbose_name='Product name')
    price = models.FloatField(verbose_name='Price')
    watched = models.IntegerField(default=0, verbose_name='Views')
    quantity = models.IntegerField(default=0, verbose_name='Quantity of items')
    description = models.TextField(default='Product description', verbose_name='Product description')
    info = models.TextField(default='Information on the product', verbose_name='Product info')
    created_at = models.DateField(auto_now_add=True, verbose_name='Date of creation')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categories', related_name='products')
    slug = models.SlugField(unique=True, null=True)
    size = models.IntegerField(default=30,verbose_name='Size in mm')
    color = models.CharField(max_length=30, default='Template color', verbose_name='Color/Material')

    def get_absolute_url(self):
        pass

    def get_first_photo(self):
        """Get first image of the product"""
        if self.images:
            return self.images.first().image.url
        else:
            return 'https://http.cat/404.jpg'

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Product: pk={self.pk}, title={self.title}, price={self.price}'

    class Meta:
        """Used for translation"""
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Gallery(models.Model):
    """Creates table for images"""
    image = models.ImageField(upload_to='products/', verbose_name='Image')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    class Meta:
        """Used for translation"""
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
