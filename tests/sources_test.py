import unittest

class Sources:
    '''
    Sources class to determine sources objects
    '''

    def __init__(self,id,name,category,description,language):
        self.id = id
        self.name = name
        self.category = category
        self.description = description
        self.language = language

class TestSources(unittest.TestCase):
    '''
    Test class that defines test cases for the Sources class behaviours.

    Args:
        unittest.TestCase: TestCase class that aims in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_source = Sources('al-jazeera-english','Al Jazeera English','general','','en')

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_source.id,"al-jazeera-english")
        self.assertEqual(self.new_source.name,"Al Jazeera English")
        self.assertEqual(self.new_source.category,"general")
        self.assertEqual(self.new_source.description,"")
        self.assertEqual(self.new_source.language,"en")

if __name__ == '__main__':
    unittest.main()
