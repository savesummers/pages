from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.

class TestHomePage(SimpleTestCase):

    def test_if_page_exist(self):

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_page_code(self):

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):

        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_content(self):

        response = self.client.get(reverse('home'))
        self.assertContains(response, '<h1>Homepage</h1>')



class TestAboutPage(SimpleTestCase):

    def test_if_page_exist(self):

        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_page_name(self):

        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):

        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about.html')

    def test_content(self):

        response = self.client.get(reverse('about'))
        self.assertContains(response, '<h1>About Page</h1>')

