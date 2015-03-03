from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser = implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Grace has heard about this new great online to-do app. She opens
		# her browser to check it out
		self.browser.get('http://localhost:8000')

		# She notices that the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# She is invited to enter a to-do item as soon as the page opens

		# She types "Buy peacock feathers" into the text box (Grace
		# just really loves peacocks).

		# When she hits enter, the page updates, and now the page lists
		# "1: Buy peacock feathers" as an item in a to-do list

		# There is still a text box inviting her to add another item. She
		# enters "Use peacock feathers to make a cool craft"

		# The page again updates, and now shows both items on her list

		# Grace wonders whether the site will remember her list. Then she
		# sees that the site has generated a unique URL just for her -- there
		# is an explanation that this is the case.

		# She visits that URL - her to-do list is still there.

		# Satisfied, she goes back to studying - ready to start her project
		# once she finishes this paper!

if __name__ == '__main__':
	unittest.main()#warnings='ignore')