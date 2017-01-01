from xml.etree import ElementTree as et
import requests

# get xml from a website
xml = requests.get("http://www.w3schools.com/xml/cd_catalog.xml")

# write into a local xml file
with open("test.xml", "wb") as code:
    code.write(xml.content)

# parse xml
doc = et.parse("test.xml")

# output
for element in doc.findall("CD"):
    print("Album: ", element.find("TITLE").text)
    print("Artist: ", element.find("ARTIST").text)
    print("year: ", element.find("YEAR").text, "\n")