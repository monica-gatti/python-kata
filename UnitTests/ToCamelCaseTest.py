import unittest
from statementToCamelCase import to_camel_case

class testCamelCaseMethods(unittest.TestCase):
    
    def testEmptyString(self):
        self.assertEqual(to_camel_case(""), "")
    
    def testEmptyString(self):
        self.assertEqual(to_camel_case("A-B-C"), "")

