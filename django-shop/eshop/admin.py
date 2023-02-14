from django.contrib import admin
from .models import Product, Category, Gallery
from django.utils.safestring import mark_safe


class GalleryInline(admin.TabularInline):
    """Creates inline image upload in admin panel"""
    fk_name = 'product'
    model = Gallery
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Creates automatic slugs"""
    list_display = ('title', 'parent', 'get_products_count')
    prepopulated_fields = {'slug': ('title',)}

    def get_products_count(self, obj):
        """Gets sum total of available produtcs for admin page"""
        if obj.products:
            return len(obj.products.all())
        else:
            return 0

    get_products_count.short_description = 'Product quantity'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Display products in admin panel"""
    list_display = ('pk', 'title', 'category', 'quantity', 'price', 'created_at', 'size', 'color', 'get_thumbnail')
    list_editable = ('price', 'quantity', 'size', 'color')
    list_display_links = ('pk', 'title')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'price')
    inlines = (GalleryInline,)

    def get_thumbnail(self,obj):
        """Creates thumbnail for admin page"""
        if obj.images:
            return mark_safe(f'<img src="{obj.images.all()[0].image.url}" width="75">')
        else:
            return '-'

    get_thumbnail.short_description = 'Thumbnail'

admin.site.register(Gallery)
