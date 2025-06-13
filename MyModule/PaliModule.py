# get romanpali, return thai
def romanpali_to_thai(roman_pali):
    dict_thaiunicode = dict_romanpali_to_thaiunicode()

    roman_pali = roman_pali.strip()
    if len(roman_pali) == 0 : return ""

    roman_pali = roman_pali.lower()
    for roman_char in dict_thaiunicode.keys():
      roman_pali = roman_pali.replace( roman_char, dict_thaiunicode[roman_char]  )

    thai_pali = improve_thai_text_sra_o(roman_pali)
    thai_pali = improve_thai_text_sra_a(thai_pali)
    thai_pali = improve_thai_text_sra_aa(thai_pali)

    return thai_pali

# get thai sentence # return thai sentence saparated with spaces
def thai_sentence_to_syllable(thai_sentence):
    if " " in thai_sentence : return []
    if len(thai_sentence) == 0 : return []

    thai_sentence = thai_sentence.strip()
    li_vowel = li_thai_vowel()
    li_vowel.extend(['\u0E31'])  #Mai han agart

    li_vowel_position = []    
    for vowel in li_vowel:
       li_position =  find_all(thai_sentence, vowel) 
       li_position.sort(reverse=True)
       if li_position : 
          #print(vowel,li_position)
          li_vowel_position.extend(li_position)

    li_sentence = []
    for position in li_vowel_position :
        if position == (len(thai_sentence) - 1) :
            sentence = thai_sentence[-2:]
        elif position == (len(thai_sentence) - 2) :
            sentence = thai_sentence[-3:]
        li_sentence.insert(0, sentence)
        thai_sentence = thai_sentence.replace(sentence,"") 

    #return li_sentence

    thai_sentence = ""
    for sentence in li_sentence :
       thai_sentence = thai_sentence + sentence + " "
       
    return thai_sentence.strip()


# get list, and join them using commas as seperator
#


# get line text # return list of sentenced
def break_line_to_sentence(text):
    text = text.strip()
    if len(text) == 0 : return []

    li_sentence = text.split(" ")
    li_new = []
    for sentence in li_sentence :
      if len(sentence) >0  : li_new.append(sentence)

    return li_new

# get raw thai text, return improve thai text
def improve_thai_text_sra_aa(thai_text):
    li_position = find_all(thai_text,'า')
    if li_position == [] : return thai_text

    li_new_position = []
    for position in li_position:
        if position == 0 :
            li_new_position.append(position)
        elif thai_text[position - 1] not in li_thai_consonant():
            li_new_position.append(position)

    if li_new_position :
       thai_text = change_char_in_text(thai_text, li_new_position , 'อา')
   
    thai_text  = thai_text.replace("x", "อา")
    return thai_text

# get raw thai text, returned improve thai text
def improve_thai_text_sra_a(thai_text):
    li_position = find_all(thai_text,'\u0E30')
    if li_position == [] : return thai_text

    li_new_position = []
    for position in li_position:
        if position == 0 :
          thai_text = change_char_in_text(thai_text, [0], "x")
        elif position == (len(thai_text) - 1) :
            pass
            #do nothing
        elif (position == (len(thai_text) - 2)) and  (thai_text[-1] in li_thai_consonant())   :
            li_new_position.append(position)
        elif (thai_text[position - 1] in li_thai_consonant()) and (thai_text[position + 1] in li_thai_consonant() ) and (thai_text[position + 2] in li_thai_consonant() ) :
           li_new_position.append(position)
            
    thai_text = change_char_in_text(thai_text, li_new_position , '\u0E31')
    thai_text  = thai_text.replace("x", "อะ")

    return thai_text

# get raw thai text, returned improve thai text
def improve_thai_text_sra_o(thai_text):
    list_sra_o_position = find_all(thai_text,'\u0E42')
    if list_sra_o_position :
      thai_text = swap_previous_char(thai_text, list_sra_o_position)
    
    return thai_text

# get text ,list of position # return changed text
def change_char_in_text(text, li_position, substring):
   if li_position == [] : return text
   if substring == "" : return text

   li_char = list(text)
   for position in li_position:
      li_char[position] = substring
   
   return "".join(li_char)

# get text ,list of position # return swaped text
def swap_previous_char(text, li_position) :
    if li_position == [] : return text

    text = list(text)

    for position in li_position:
      dummy = text[position-1]
      text[position-1] = text[position]
      text[position] = dummy
      
    return "".join(text)

# get text, substring
# return list_position
def find_all(text, substring) :
    if text == "" : return []

    li_position = []
    start = 0
    while True:
      start = text.find(substring, start)
      if start == -1: 
        break
      else : 
        li_position.append(start)
        start = start + len(substring)

    return li_position

# return dictionary key : pomanpali, value : thai unicode text
def dict_romanpali_to_thaiunicode() :
    list_text = li_consonant_table()
    list_text.extend(li_vowel_table())

    mydict = {}
    for x in list_text :
      mydict[x[0]] = x[2]

    return mydict

#get None # return list of thai vowel
def li_thai_vowel():
    li_vowel = li_vowel_table()
    li_thai_vowel = []
    for vowel in li_vowel:
       li_thai_vowel.append(vowel[2])

    return li_thai_vowel
   
# get None # return list of romanpali_vowel table
def li_vowel_table():
   return [
      ['a', 'อะ', '\u0E30'],  
      ['ā', 'อา', '\u0E32'],
      ['i', 'อิ', '\u0E34'],
      ['ī', 'อี', '\u0E35'],
      ['u', 'อุ', '\u0E38'],
      ['ū', 'อู', '\u0E39'],
      ['e', 'เอ', '\u0E40'],
      ['o', 'โอ', '\u0E42']
    ]
#get None # return list of thai consonant
def li_thai_consonant():
    li_consonant = li_consonant_table()

    li_thai_consonant = []
    for consonant in li_consonant:
       li_thai_consonant.append(consonant[2])

    return li_thai_consonant

# get None # return list of romanpali_consonant table
def li_consonant_table():
    return [
        ['kh', 'ข', '\u0E02'],    
        ['gh', 'ฆ', '\u0E06'],
        ['ch', 'ฉ', '\u0E09'],
        ['jh', 'ฌ', '\u0E0c'],
        ['ṭh', 'ฐ', '\u0E10'],    
        ['ḍh', 'ฒ', '\u0E12'],
        ['th', 'ถ', '\u0E16'],
        ['dh', 'ธ',	'\u0E18'],    
        ['ph', 'ผ', '\u0E1c'],	
        ['bh', 'ภ', '\u0E20'],
        ['k', 'ก', '\u0E01'],
        ['g', 'ค', '\u0E04'],
        ['ṅ', 'ง', '\u0E07'],
        ['c', 'จ', '\u0E08'],
        ['j', 'ช', '\u0E0a'],
        ['ñ', 'ญ', '\u0E0d'],
        ['ṭ', 'ฏ', '\u0E0f'],
        ['ḍ', 'ฑ', '\u0E11'],
        ['ṇ', 'ณ', '\u0E13'],
        ['t', 'ต', '\u0E15'],
        ['d', 'ท', '\u0E17'],
        ['n', 'น', '\u0E19'],
        ['p', 'ป', '\u0E1a'],
        ['b', 'พ', '\u0E1e'],
        ['m', 'ม', '\u0E21'],
        ['y',	'ย', '\u0E22'],
        ['r',	'ร', '\u0E23'],
        ['l',	'ล', '\u0E25'],
        ['v',	'ว', '\u0E27'],
        ['s',	'ส', '\u0E2a'],
        ['h',	'ห', '\u0E2b'],
        ['ḷ',	'ฬ', '\u0E2c'],
        ['ṃ',	'อํ',	'\u0E2d']
    ]
