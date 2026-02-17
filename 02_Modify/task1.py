import re

reg = re.compile(r'(https?://)?(www\.)?([a-zA-Z0-9-]+)(\.[a-z]{2,})+/?.*')

m = reg.match("www.google.com")
print(m)

m = reg.match("https://www.youtube.com")
print(m)

m = reg.match("http://www.uni-wuerzburg.de")
print(m)

m = reg.match("www.wiwi.uni-wuerzburg.de/wiba/startseite/")
print(m)