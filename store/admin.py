from django.contrib import admin
from . models import ImageAlbum, Image, Product


class ImageInline(admin.StackedInline):
    model = Image


class ProductInline(admin.StackedInline):
    model = Product


@admin.register(ImageAlbum)
class ImageAlbumAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
        ImageInline,
    ]


admin.site.register(Image)
admin.site.register(Product)

# class ImageInline(admin.StackedInline):
#     model = Image


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title', 'author', 'slug', 'price',
#                     'in_stock', 'created', 'updated']
#     list_filter = ['in_stock', 'created', 'updated']
#     list_editable = ['price', 'in_stock']
#     prepopulated_fields = {'slug': ('title',)}
#     inlines = [
#         ImageInline,
#     ]

# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ['id']
