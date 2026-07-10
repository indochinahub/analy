def greeting(name):
  return ("Hello, " + name)



def get_group_of_line(text):
  if text == "": return ""

  text = text.strip()
  text = text.replace('\r\n', '\n')
  #text = text.split('\n')

  return text
