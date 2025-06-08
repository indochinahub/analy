# get romanpali, return thai
def romanpali_to_thai(roman_pali):
    dict_thaiunicode = dict_romanpali_to_thaiunicode()

    roman_pali = roman_pali.strip()
    if len(roman_pali) == 0 : return ""

    roman_pali = roman_pali.lower()
    for roman_char in dict_thaiunicode.keys():
      roman_pali = roman_pali.replace( roman_char, dict_thaiunicode[roman_char]  )

    roman_pali = improve_thai_text(roman_pali) 
    return roman_pali

# get raw thai text, returned improve thai text
def improve_thai_text(thai_text):
    # sra o
    list_sra_o_position = find_all(thai_text,'\u0E42')
    if list_sra_o_position :
      thai_text = swap_previous_char(thai_text, list_sra_o_position)
    
    return thai_text

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

# get text, return list
def separate_text_to_words(text):
    text = text.strip()
    if len(text) == 0:
      return []
    
    return strip_list(text.split())

# get list, return list
def strip_list(lst):
    """Trim whitespace from each item in a list and remove empty items."""
    return [item.strip() for item in lst if item.strip()]


# return dictionary key : pomanpali, value : thai unicode text
def dict_romanpali_to_thaiunicode() :
    list_text = li_consonant_table()
    list_text.extend(li_vowel_table())

    mydict = {}
    for x in list_text :
      mydict[x[0]] = x[2]

    return mydict

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
        ['k', 'ก', '\u0E01'],
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
