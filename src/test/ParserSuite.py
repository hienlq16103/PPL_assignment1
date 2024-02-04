import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func main() return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    def test_wrong_declaration(self):
        input = """var aPI <- 3.14"""
        expect = "Error on line 1 col 15: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 202))