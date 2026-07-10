import unittest
import mymodule

class TestMyModule(unittest.TestCase):
    """Test cases for mymodule.py."""

    def test_greeting(self):
        """Test the greeting function."""
        self.assertEqual(mymodule.greeting("Jonathan"), "Hello, Jonathan")
        self.assertEqual(mymodule.greeting("World"), "Hello, World")
    
    def test_get_group_of_line(self):
        """Get text and devide it into group_of_lines"""
        
        # Get blank, return blank
        result = mymodule.get_group_of_line('')
        self.assertEqual(result, '')

        # Get text, strip text
        result = mymodule.get_group_of_line('\nline\n')
        self.assertEqual(result, 'line')

        # Relplace
        result = mymodule.get_group_of_line('\nline1\r\nline2\r\nline3\r\n')
        self.assertEqual(result, 'line1\nline2\nline3')

        

        





if __name__ == '__main__':
    unittest.main()