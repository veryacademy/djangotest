from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()

    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)

    def __str__(self):
        return self.id


class Image(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    primary_image = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(
        ImageAlbum, related_name='images', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='product', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='unknown')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    album = models.OneToOneField(
        ImageAlbum, related_name='model', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title
