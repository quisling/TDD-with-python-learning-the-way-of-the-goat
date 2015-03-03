from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Grace has heard about this new great online to-do app. She opens
		# her browser to check it out
		self.browser.get('http://localhost:8000')

		# She notices that the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# She is invited to enter a to-do item as soon as the page opens
		input_box = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
				input_box.get_attribute('placeholder'),
				'Enter a to-do item'
		)

		# She types "Buy peacock feathers" into the text box (Grace
		# just really loves peacocks).
		input_box.send_keys('Buy peacock feathers')

		# When she hits enter, the page updates, and now the page lists
		# "1: Buy peacock feathers" as an item in a to-do list
		input_box.send_keys(Keys.ENTER)
		
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows),
			"New to-do item did not appear in table"
		)

		# There is still a text box inviting her to add another item. She
		# enters "Use peacock feathers to make a cool craft"
		self.fail('Finish the test!')

		# The page again updates, and now shows both items on her list

		# Grace wonders whether the site will remember her list. Then she
		# sees that the site has generated a unique URL just for her -- there
		# is an explanation that this is the case.

		# She visits that URL - her to-do list is still there.

		# Satisfied, she goes back to studying - ready to start her project
		# once she finishes this paper!

if __name__ == '__main__':
	unittest.main()#warnings='ignore')