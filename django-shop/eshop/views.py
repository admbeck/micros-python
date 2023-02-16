from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Category, Product

class MainPage(ListView):
    """Index page"""
    model = Product
    context_object_name = 'categories'
    extra_context = {'title': 'Main Page'}
    template_name = 'index.html'

    def get_queryset(self):
        """Show parent categories"""
        return Category.objects.filter(parent=None)

class SubCategoryPage(ListView):
    """Show subcategories on separate page"""
    model = Product
    context_object_name = 'products'
    template_name = 'category_page.html'

    def get_queryset(self):
        """Get all products of subcategory"""
        parent_category = Category.objects.get(slug=self.kwargs['slug'])
        subcategories = parent_category.subcategories.all()
        products = Product.objects.filter(category__in=subcategories).order_by('?')
        return products
