from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith has heard about a  cool new online to-do app. She goes
        #to check out its homepage
        self.browser.get('http://localhost:8000')
        #she noticess the page title and header metion to-do lists

        self.assertIn('To-Do',self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        #She is invited to enter a to-do item strait away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')
        
        #she types "Buy peackock feathers" into a text box(Edith's hobby is
        #tying fly_fishing lures)
        inputbox.send_keys('Buy peacock feathers')
        
        #when she hits enter , the page updates and now the page lists
        #1:Buy peackock feathers as an itme in a to-do list
        inputbox.send_keys(Keys.ENTER)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1:Buy peacock feathers',[row.text for row in rows])
        
        #There is still a text box inviting her to add another item.
        #She enters " Use peackock feathers to make fly" (Edith is very
        #methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        #The page updates again and now shows both itmes on her list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1:Buy peacock feathers',[row.text for row in rows])
        self.assertIn('2:Use peacock feathers to make a fly',[row.text for row in rows])

#Edith wonders whether the site will remember her list. Then she sees
#that the site has generated a unique URL for her --there is some
#explanatory text to that effect
        self.fail('Finish the test')

#She visits that URL -her to-do list is still there.

#Satisfied, she goes back to sleep

if __name__=='__main__':
    unittest.main(warnings = 'ignore')
