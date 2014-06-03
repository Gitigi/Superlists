from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith has heard about a  cool new online to-do app. She goes
        #to check out its homepage
        self.browser.get('http://localhost:8000')
        #she noticess the page title and header metion to-do lists

        self.assertIn('To-Do',self.browser.title)
        self.fail("Finish the test!")
        #She is invited to enter a to-do item strait away

#she types "Buy peackock feathers" into a text box(Edith's hobby is
#tying fly_fishing lures)

#when she hits enter , the page updates and now the page lists
#1:Buy peackock feathers as an itme in a to-do list

#There is still a text box inviting her to add another item.
#She enters " Use peackock feathers to make fly" (Edith is very
#methodical)

#The page updates again and now shows both itmes on her list

#Edith wonders whether the site will remember her list. Then she sees
#that the site has generated a unique URL for her --there is some
#explanatory text to that effect

#She visits that URL -her to-do list is still there.

#Satisfied, she goes back to sleep

if __name__=='__main__':
    unittest.main(warnings = 'ignore')
