from django.test import TestCase
from store.models import Category, Product, ImageAlbum, Image
from django.urls import reverse


class TestCategories(TestCase):

    def setUp(self):
        ImageAlbum.objects.create()
        Image.objects.create(name='django-image',
                             image='django-image1/', album_id='1')
        self.cat = Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners',
                               slug='django-beginners', price='20.00', album_id='1')

    def test_category_model_entry(self):
        d = self.cat
        self.assertTrue(isinstance(d, Category))
        self.assertEqual(str(d), 'django')

    def test_category_url(self):
        d = self.cat
        response = self.client.post(reverse('store:category_list', args=[d.slug]))
        self.assertEqual(response.status_code, 200)


class TestProducts(TestCase):

    def setUp(self):
        ImageAlbum.objects.create()
        Image.objects.create(name='django-image',
                             image='django-image1/', album_id='1')
        Category.objects.create(name='django', slug='django')
        self.prod = Product.objects.create(category_id=1, title='django beginners',
                                           slug='django-beginners', price='20.00', album_id='1')

    def test_products_model_entry(self):
        d = self.prod
        self.assertTrue(isinstance(d, Product))
        self.assertEqual(str(d), 'django beginners')

    def test_products_url(self):
        d = self.prod
        url = reverse('store:product_detail', args=[d.slug])
        self.assertEqual(url, '/item/django-beginners/')
        response = self.client.post(reverse('store:product_detail', args=[d.slug]))
        self.assertEqual(response.status_code, 200)
