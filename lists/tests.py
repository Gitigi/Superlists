from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import item

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)

    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(),expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text']='A new list item'

        response = home_page(request)

        self.assertIn('A new list item',response.content.decode())

        expected_html = render_to_string('home.html',
                                         {'new_item_text':'A new list item'})
        self.assertEqual(response.content.decode(),expected_html)

class itemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = item()
        first_item.text = 'The first(ever)list item'
        first_item.save()
        
        second_item = item()
        second_item.text = 'Item the second'
        second_item.save()
        
        saved_item = item.objects.all()
        self.assertEqual(saved_item.count(),2)

        first_saved_item = saved_item[0]
        second_saved_item = saved_item[1]
        self.assertEqual(first_saved_item.text,'The first(ever)list item')
        self.assertEqual(second_saved_item.text,'Item the second')
