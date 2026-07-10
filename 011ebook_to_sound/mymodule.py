def greeting(name):
  return ("Hello, " + name)



def get_group_of_line(text):
  if text == "": return ""

  text = prepare_text(text)
  li_text = text.split('\n\n')
  return li_text


  return text

def prepare_text(text):
  if text == "": return ""

  text = text.strip()
  text = text.replace('\r\n', '\n')

  while '\n\n\n' in text:
    text = text.replace('\n\n\n', '\n\n')

  return text  
