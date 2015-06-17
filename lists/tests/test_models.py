from django.test import TestCase
from lists.models import Item,List

# Create your tests here.


class ListAndItemModelsTest(TestCase):
    def test_saving_and_retrieving_Items(self):
        list_ = List()
        list_.save()
        
        first_Item = Item()
        first_Item.text = 'The first(ever)list Item'
        first_Item.list = list_
        first_Item.save()
        
        second_Item = Item()
        second_Item.text = 'Item the second'
        second_Item.list = list_
        second_Item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list,list_)
        
        saved_Item = Item.objects.all()
        self.assertEqual(saved_Item.count(),2)

        first_saved_Item = saved_Item[0]
        second_saved_Item = saved_Item[1]
        self.assertEqual(first_saved_Item.text,'The first(ever)list Item')
        self.assertEqual(first_saved_Item.list,list_)
        self.assertEqual(second_saved_Item.text,'Item the second')
        self.assertEqual(second_saved_Item.list,list_)
