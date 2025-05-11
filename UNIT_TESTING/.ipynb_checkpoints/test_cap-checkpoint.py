import unittest
import cap

class TestCap(unittest.TestCase): # This allows it to inherit from the parent class (unittest.TestCase)

	def test_one_word(self):
		text = 'python'
		result = cap.cap_text(text)
		# Note that this assertEqual is from the imported "unittest" class
		self.assertEqual(result, 'Python');

	def test_multiple_words(self):
		text = 'monty python'
		result = cap.cap_text(text)
		self.assertEqual(result, 'Monty Python')


# This is to call the main() function of the unit test class only when this file is running
if __name__ == '__main__':
	unittest.main()

# Then we go to the folder in the terminal and then run the test file
# Python test_cap.py

