import unittest
import PaliModule

class TestPaliModule(unittest.TestCase):

    # get romanpali, return thai
    def test_romanpali_to_thai(self):
        result = PaliModule.romanpali_to_thai("")
        expected_result = ""
        self.assertEqual(result, expected_result)        

        result = PaliModule.romanpali_to_thai("manussa")
        expected_result = "มะ นุส สะ"
        self.assertEqual(result, expected_result)        
    
        result = PaliModule.romanpali_to_thai(" Buddho Buddho ")
        expected_result = 'พุท โธ, พุท โธ'
        self.assertEqual(result, expected_result)

        result = PaliModule.romanpali_to_thai(" āgacchati āgacchati ")
        expected_result = "อา คัจ ฉะ ติ, อา คัจ ฉะ ติ"
        self.assertEqual(result, expected_result)  

    # get roman text, clean it #return cleaned text
    def test_clean_roman_text (self):
        result = PaliModule.clean_roman_text("")
        expected_result = ""
        self.assertEqual(result, expected_result) 

        '''
        result = PaliModule.clean_roman_text(" Buddho Buddho ")
        expected_result = False
        self.assertEqual(result, expected_result) 

        result = PaliModule.clean_roman_text(" 1.Buddho Buddho ")
        expected_result = "xxxx"
        self.assertEqual(result, expected_result) 
        '''

    # get thai text # return thai sentence sapated with commas
    def test_thai_sentence_to_syllable(self):
        result = PaliModule.thai_sentence_to_syllable("")
        expected_result = []
        self.assertEqual(result, expected_result)
    
        result = PaliModule.thai_sentence_to_syllable(" ")
        expected_result = []
        self.assertEqual(result, expected_result) 

        result = PaliModule.thai_sentence_to_syllable("กา กา")
        expected_result = []
        self.assertEqual(result, expected_result)    

        result = PaliModule.thai_sentence_to_syllable(" กัก ")
        expected_result = []
        self.assertEqual(result, expected_result)            

        result = PaliModule.thai_sentence_to_syllable("กา")
        expected_result = "กา"
        self.assertEqual(result, expected_result)    

        result = PaliModule.thai_sentence_to_syllable("คากา")
        expected_result = "คา กา"
        self.assertEqual(result, expected_result)    

        result = PaliModule.thai_sentence_to_syllable("มะนุสสะ")
        expected_result = "มะ นุส สะ"
        self.assertEqual(result, expected_result)                    

        result = PaliModule.thai_sentence_to_syllable("พุทโธ")
        expected_result = "พุท โธ"
        self.assertEqual(result, expected_result) 

        '''
        result = PaliModule.thai_sentence_to_syllable("เมเมนเม")
        expected_result = "เม เมน เม"
        self.assertEqual(result, expected_result)                                    
        '''

    # get line text # return list of sentenced
    def test_break_line_to_sentence(self):
        result = PaliModule.break_line_to_sentence("  ")
        expected_result = []
        self.assertEqual(result, expected_result)
              
        result = PaliModule.break_line_to_sentence(" กา กากา  กักกา ")
        expected_result = ['กา', 'กากา', 'กักกา']
        self.assertEqual(result, expected_result)      

    # get raw thai text, returned improve thai text
    def test_improve_thai_text_sra_aa(self):
        result = PaliModule.improve_thai_text_sra_aa("าอาอาดมา าอามา")
        expected_result = "อาอาอาดมา อาอามา"
        self.assertEqual(result, expected_result)

    # get raw thai text, returned improve thai text
    def test_improve_thai_text_sra_a(self):
        result = PaliModule.improve_thai_text_sra_a( "\u0E30" + "กะกะกกะ")
        expected_result = "อะกะกักกะ"
        self.assertEqual(result, expected_result)

        result = PaliModule.improve_thai_text_sra_a( "กะกกะกะกะก")
        expected_result = "กักกะกะกัก"
        self.assertEqual(result, expected_result)        

        result = PaliModule.improve_thai_text_sra_a("กะ")
        expected_result = "กะ"
        self.assertEqual(result, expected_result)        

    # get raw thai text, returned improve thai text
    def test_improve_thai_text_sra_o(self):
        result = PaliModule.improve_thai_text_sra_o('\u0E25'+ '\u0E42'+" " + '\u0E25' + '\u0E42' ) # โอ + ลอ 
        expected_result = "โล โล"
        self.assertEqual(result, expected_result)

    # get text ,list of position # return changed text
    def test_change_char_in_text(self):
        result = PaliModule.change_char_in_text("aaabbbcccddd",[],"x")
        expected_result = "aaabbbcccddd"
        self.assertEqual(result, expected_result)

        result = PaliModule.change_char_in_text("aaabbbcccddd",[1, 3, 5],"")
        expected_result = "aaabbbcccddd"
        self.assertEqual(result, expected_result)

        result = PaliModule.change_char_in_text("aaabbbcccddd",[1, 3, 5],"x")
        expected_result = 'axaxbxcccddd'
        self.assertEqual(result, expected_result)

    # get raw thai text ,list of position # returned improve thai text
    def test_swap_previous_char(self) :
        result = PaliModule.swap_previous_char(text = "abcdefghijk", li_position = [])
        expected_result = "abcdefghijk"
        self.assertEqual(result, expected_result)

        result = PaliModule.swap_previous_char(text = "", li_position = [])
        expected_result = ""
        self.assertEqual(result, expected_result)

        result = PaliModule.swap_previous_char(text = "abcdefghijk", li_position = [1])
        expected_result = "bacdefghijk"
        self.assertEqual(result, expected_result)

        result = PaliModule.swap_previous_char(text = "abcdefghijk", li_position = [1,3])
        expected_result = "badcefghijk"
        self.assertEqual(result, expected_result)

    # get text, substring # return list_position
    def test_find_all(self) :
        result = PaliModule.find_all("aaaaabccbbcccbdddd", "b")
        expected_result = [5, 8, 9, 13]
        self.assertEqual(result, expected_result)

        result = PaliModule.find_all("โล โย โล", '\u0E42')
        expected_result = [0, 3, 6]   
        self.assertEqual(result, expected_result)

        result = PaliModule.find_all("", "b")
        expected_result = []
        self.assertEqual(result, expected_result)        

    # return dictionary key : pomanpali, value : thai unicode text
    def test_dict_romanpali_to_thaiunicode(self) :
        result = len(PaliModule.dict_romanpali_to_thaiunicode())
        expected_result = 41
        self.assertEqual(result, expected_result)

    #get None # return list of thai vowel
    def test_li_thai_vowel(self):
        result = len(PaliModule.li_thai_vowel())
        expected_result = 8
        self.assertEqual(result, expected_result)

        result = PaliModule.li_thai_vowel()[0]
        expected_result = '\u0E30' #sra a
        self.assertEqual(result, expected_result)

    #get None # return list of roman vowel
    def test_li_roman_vowel(self):
        result = len(PaliModule.li_roman_vowel())
        expected_result = 8
        self.assertEqual(result, expected_result)

        result = PaliModule.li_roman_vowel()[0]
        expected_result = 'a'
        self.assertEqual(result, expected_result)

    # get None # return list of romanpali_vowel table
    def test_li_vowel_table(self):
        result = len(PaliModule.li_vowel_table())
        expected_result = 8     
        self.assertEqual(result, expected_result)

        result = PaliModule.li_vowel_table()[0]
        expected_result = ['a', 'อะ', '\u0E30']     
        self.assertEqual(result, expected_result)

    #get None # return list of thai consonant
    def test_li_thai_consonant(self):
        result = len(PaliModule.li_thai_consonant())
        expected_result = 33
        self.assertEqual(result, expected_result)

        result = PaliModule.li_thai_consonant()[0]
        expected_result =  '\u0E02' #'ข'
        self.assertEqual(result, expected_result)        

    #get None # return list of roman consonant
    def test_li_roman_consonant(self):
        result = len(PaliModule.li_roman_consonant())
        expected_result = 33
        self.assertEqual(result, expected_result)
        
        result1 = PaliModule.li_roman_consonant()
        result = result1[0]
        expected_result = "kh"
        self.assertEqual(result, expected_result)

    # get None # return list of romanpali_consonant table
    def test_li_consonant_table(self):        
        result = len(PaliModule.li_consonant_table())
        expected_result = 33
        self.assertEqual(result, expected_result)

        result = PaliModule.li_consonant_table()[0]
        expected_result = ['kh', 'ข', '\u0E02']
        self.assertEqual(result, expected_result)        

if __name__ == '__main__':
    unittest.main()