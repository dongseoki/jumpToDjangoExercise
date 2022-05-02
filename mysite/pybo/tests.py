from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve
# from ..views import home_page
import pybo.mycalc as mycalc
# Create your tests here.

class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1+1,2)

# https://ugaemi.com/tdd/Django-unit-test/
# class HomePageTest(TestCase):
#     def test_root_url_resolves_to_home_page_view(self):
#         found = resolve('/pybo/homepagetest')
#         self.assertEqual(found.func, home_page)
#
#     def test_home_page_returns_to_home_page_view(self):
#         request = HttpRequest()
#         response = home_page(request)
#         self.assertTrue(response.content.startswith(b'<html>'))
#         self.assertIn(b'<title>To-Do lists</title>', response.content)
#         self.assertTrue(response.content.endswith(b'</html>'))


class MyCalcTest(TestCase):

    def test_add(self):
        c = mycalc.add(20, 10)
        self.assertEqual(c, 30)

    def test_substract(self):
        c = mycalc.substract(20, 10)
        self.assertEqual(c, 10)

class MyCalcTest2(TestCase):
    def setUp(self):
        print("1. Executing the setUp method")
        self.fixture = { 'a' : 1 }

    def tearDown(self):
        print("3. Executing the tearDown method")
        self.fixture = None

    def test_fixture(self):
        print("2. Executing the test_fixture method")
        self.assertEqual(self.fixture['a'], 1)