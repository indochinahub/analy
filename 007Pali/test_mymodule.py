import unittest
import MyModule

class TestMyModule(unittest.TestCase):

    # get romanpali, return thai
    def test_romanpali_to_thai(self):

        result = MyModule.romanpali_to_thai("manussa")
        expected_result = "มะนุสสะ"
        self.assertEqual(result, expected_result)

        result = MyModule.romanpali_to_thai(" Buddho Buddho ")
        expected_result = 'พุทโธ พุทโธ'
        self.assertEqual(result, expected_result)

        result = MyModule.romanpali_to_thai("")
        expected_result = ""
        #self.assertEqual(result, expected_result)        

    # get raw thai text, returned improve thai text
    def test_improve_thai_text(self):
        result = MyModule.improve_thai_text('\u0E25'+ '\u0E42'+" " + '\u0E25' + '\u0E42' )
        expected_result = "โล โล"
        self.assertEqual(result, expected_result)


    # get raw thai text ,list of position
    # returned improve thai text
    def test_swap_previous_char(self) :
        result = MyModule.swap_previous_char(text = "abcdefghijk", li_position = [])
        expected_result = "abcdefghijk"
        self.assertEqual(result, expected_result)

        result = MyModule.swap_previous_char(text = "", li_position = [])
        expected_result = ""
        self.assertEqual(result, expected_result)

        result = MyModule.swap_previous_char(text = "abcdefghijk", li_position = [1])
        expected_result = "bacdefghijk"
        self.assertEqual(result, expected_result)

        result = MyModule.swap_previous_char(text = "abcdefghijk", li_position = [1,3])
        expected_result = "badcefghijk"
        self.assertEqual(result, expected_result)

    # get text, substring # return list_position
    def test_find_all(self) :
        result = MyModule.find_all("aaaaabccbbcccbdddd", "b")
        expected_result = [5, 8, 9, 13]
        self.assertEqual(result, expected_result)

        result = MyModule.find_all("โล โย โล", '\u0E42')
        expected_result = [0, 3, 6]   
        self.assertEqual(result, expected_result)

        result = MyModule.find_all("", "b")
        expected_result = []
        self.assertEqual(result, expected_result)        

    def test_separate_text_to_words(self):
        result = MyModule.separate_text_to_words("  Hello   world  this is a test  ")
        expected_result = ["Hello", "world", "this", "is", "a", "test"]
        self.assertEqual(result, expected_result)

        result = MyModule.separate_text_to_words("  ")
        expected_result = []
        self.assertEqual(result, expected_result)

        result = MyModule.separate_text_to_words("")
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_strip_list(self):
        result = MyModule.strip_list(["  hello  ", "world", "  ", "  test  "])
        expected_result = ["hello", "world", "test"]
        self.assertEqual(result, expected_result)

        result = MyModule.strip_list(["   ", "   "])
        expected_result = []
        self.assertEqual(result, expected_result)

        result = MyModule.strip_list([])
        expected_result = []
        self.assertEqual(result, expected_result)

        result = MyModule.strip_list(['single'])
        expected_result = ['single']
        self.assertEqual(result, expected_result)

    # return dictionary key : pomanpali, value : thai unicode text
    def test_dict_romanpali_to_thaiunicode(self) :
        result = len(MyModule.dict_romanpali_to_thaiunicode())
        expected_result = 41
        self.assertEqual(result, expected_result)

    # get None # return list of romanpali_vowel table
    def test_li_vowel_table(self):
        result = len(MyModule.li_vowel_table())
        expected_result = 8     
        self.assertEqual(result, expected_result)

        result = MyModule.li_vowel_table()[0]
        expected_result = ['a', 'อะ', '\u0E30']     
        self.assertEqual(result, expected_result)

    #get None # return list of thai consonant
    #def li_thai_consonant():
    def test_li_thai_consonant(self):
        result = len(MyModule.li_thai_consonant())
        expected_result = 33
        self.assertEqual(result, expected_result)

    # get None # return list of romanpali_consonant table
    def test_li_consonant_table(self):        
        result = len(MyModule.li_consonant_table())
        expected_result = 33
        self.assertEqual(result, expected_result)

        result = MyModule.li_consonant_table()[0]
        expected_result = ['k', 'ก', '\u0E01']
        self.assertEqual(result, expected_result)        


if __name__ == '__main__':
    unittest.main()