import unittest

from functions import read_localfile,get_prev_last_name,sort_name,get_sorted_name,write_localfile

class TestReadLocalfile(unittest.TestCase):
    def setUp(self):
        self.localfile = 'unsorted-names-list.txt'
        self.content = read_localfile(self.localfile)

    def test_not_empty(self):
        self.assertFalse(self.content == '')

    def test_first_lines(self):
        self.assertTrue(self.content[0] == 'Orson Milka Iddins')
		
class Testget_prev_last_name(unittest.TestCase):

	def setUp(self):
		self.array = list('syerif elfaz')
		
	def test_get_prev_last_name(self):
	    self.assertTrue(get_prev_last_name(['syerif elfaz'])== [['syerif elfaz','syerif','elfaz']])

class Testsort_name(unittest.TestCase):

	def setUp(self):
		self.array = ['syerif elfaz','ahmad alber']
		
	def test_sort_name(self):
	  self.assertTrue(sort_name(self.array,1) == ['ahmad alber','syerif elfaz'])

class Testget_sorted_name(unittest.TestCase):
	
	def setUp(self):
		self.array = [['syerif elfaz','syerif','elfaz']]
		
	def test_get_sorted_name(self):
		self.assertTrue(get_sorted_name(self.array) == ['syerif elfaz'] )

class Testwrite_localfile(unittest.TestCase):
	
	def setUp(self):
		self.array = ['syerif elfaz']
		
	def test_write_localfile(self):
		self.assertTrue(write_localfile(self.array,'myfile.txt'))
	   
if __name__ == '__main__':
    unittest.main()		
