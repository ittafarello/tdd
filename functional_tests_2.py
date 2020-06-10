from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome('/home/itamart/Documents/chromedriver') 
		
	def tearDown(self):
		self.browser.quit()
		
	def test_can_start(self):
		self.browser.get("http://localhost:8000/")
		self.assertIn('Django', self.browser.title)
        
        # The command below will raise an error even if the condition above is True
		#self.fail('Finish the test!')


if __name__ == '__main__':
	unittest.main(warnings='ignore')