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

        result = mymodule.get_group_of_line('line1')
        self.assertEqual(result, ['line1'])        

        result = mymodule.get_group_of_line('line1\nline2')
        self.assertEqual(result, ['line1\nline2'])        

        result = mymodule.get_group_of_line('line1\nline2\n\nline3\nline4')
        self.assertEqual(result, ['line1\nline2', 'line3\nline4'])

    def test_prepare_text(self):
        result = mymodule.prepare_text('')
        self.assertEqual(result, '')

        # Get text, strip text
        result = mymodule.prepare_text('\nline\n')
        self.assertEqual(result, 'line')        

        # Relplace
        result = mymodule.prepare_text('\nline1\r\nline2\r\nline3\r\n')
        self.assertEqual(result, 'line1\nline2\nline3')

        result = mymodule.prepare_text('line1\n\nline2\n\n\n\n\nline3\nline4')
        self.assertEqual(result, 'line1\n\nline2\n\nline3\nline4')

        

        





if __name__ == '__main__':
    unittest.main()