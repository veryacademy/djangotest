from django.test import RequestFactory, TestCase, Client
from django.http import HttpRequest
from django.urls import reverse
from store.models import Category, Product, ImageAlbum, Image
from store.views import all_products


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        ImageAlbum.objects.create()
        Image.objects.create(name='django-image',
                             image='django-image1/', album_id='1')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners',
                               slug='django-beginners', price='20.00', album_id='1')

    def test_url_allowed_hosts(self):
        response = self.c.get(
            '/item/django-beginners', HTTP_HOST='nodomain.com')
        self.assertEqual(response.status_code, 400)

    def test_homepage_url(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_list_url(self):
        response = self.c.get(
            reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        response = self.c.get(
            reverse('store:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    # Example - Code Validation
    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    # Example - Request Factory
    def test_view_function(self):
        request = self.factory.get('/item/django-beginners')
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
