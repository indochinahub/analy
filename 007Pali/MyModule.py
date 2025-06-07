# get romanpali, return thai
def romanpali_to_thai(roman_pali):
  dict_thaiunicode = dict_romanpali_to_thaiunicode()

  if len(roman_pali) == 0 : return ""

  roman_pali = roman_pali.lower()
  for roman_char in dict_thaiunicode.keys():
    roman_pali = roman_pali.replace( roman_char, dict_thaiunicode[roman_char]  )

  return roman_pali

# get raw thai text, returned improve thai text
def improve_thai_text(thai_text):
  return False

# get  ,list of position
# return swaped text
def swap_previous_char(text, li_position) :
  if li_position == [] : return text

  text = list(text)

  for position in li_position:
    dummy = text[position-1]
    text[position-1] = text[position]
    text[position] = dummy
    
  return "".join(text)

  

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
  list_text = [
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
    ['ṃ',	'อํ',	'\u0E2d'],
    ['a', 'อะ', '\u0E30'],
    ['ā', 'อา', '\u0E32'],
    ['i', 'อิ', '\u0E34'],
    ['ī', 'อี', '\u0E35'],
    ['u', 'อุ', '\u0E38'],
    ['ū', 'อู', '\u0E39'],
    ['e', 'เอ', '\u0E40'],
    ['o', 'โอ', '\u0E42']
  ]

  mydict = {}
  for x in list_text :
    mydict[x[0]] = x[2]

  return mydict