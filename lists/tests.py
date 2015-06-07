from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item

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
        request.POST['item_text']='A new list Item'

        response = home_page(request)

        self.assertEqual(Item.objects.count(),1)
        new_Item = Item.objects.first()
        self.assertEqual(new_Item.text,'A new list Item')

    def test_home_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertEqual(response.status_code,302)
        self.assertEqual(response['location'],'/lists/the-only-list-in-the-world/')

    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(),0)

        


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_Items(self):
        first_Item = Item()
        first_Item.text = 'The first(ever)list Item'
        first_Item.save()
        
        second_Item = Item()
        second_Item.text = 'Item the second'
        second_Item.save()
        
        saved_Item = Item.objects.all()
        self.assertEqual(saved_Item.count(),2)

        first_saved_Item = saved_Item[0]
        second_saved_Item = saved_Item[1]
        self.assertEqual(first_saved_Item.text,'The first(ever)list Item')
        self.assertEqual(second_saved_Item.text,'Item the second')

class ListViewTest(TestCase):

    def test_display_all_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response,'itemey 1')
        self.assertContains(response,'itemey 2')

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response,'list.html')
