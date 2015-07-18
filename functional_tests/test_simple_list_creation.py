from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith has heard about a  cool new online to-do app. She goes
        #to check out its homepage
        self.browser.get(self.server_url)
        #she noticess the page title and header metion to-do lists

        self.assertIn('To-Do',self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        #She is invited to enter a to-do item strait away
        inputbox = self.get_item_input_box()
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')
        
        #she types "Buy peackock feathers" into a text box(Edith's hobby is
        #tying fly_fishing lures)
        inputbox.send_keys('Buy peacock feathers')
        
        #when she hits enter ,she is taken to a new
        # URL and now the page lists
        #1:Buy peackock feathers as an itme in a to-do list
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url,'/lists/.+')
        self.check_for_row_in_list_table('1:Buy peacock feathers')
        
        #There is still a text box inviting her to add another item.
        #She enters " Use peackock feathers to make fly" (Edith is very
        #methodical)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        #The page updates again and now shows both itmes on her list
        self.check_for_row_in_list_table("1:Buy peacock feathers")
        self.check_for_row_in_list_table('2:Use peacock feathers to make a fly')

        #Now a new user,Mark comes along to the site

        ##we use a new browser sesssion to make sure the no information
        ##of Edith is comming through from cookies.etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        #Mark visits the home page. There is no sign of Edith's list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertNotIn('make a fly',page_text)

        #Mark starts a new list by entering a new item
        #He is lesss interesting than Edith
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        #Mark gets his own unique URL
        mark_list_url = self.browser.current_url
        self.assertRegex(mark_list_url,'/lists/.+')
        self.assertNotEqual(mark_list_url,edith_list_url)

        #Again there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertNotIn('make a fly',page_text)
        
        #Satisfied they both go back to sleep
