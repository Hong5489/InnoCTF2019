import re
text = open("flag",'r').read()
print re.findall("InnoCTF{[a-z0-9]+_[a-zA-Z0-9]+}",text)