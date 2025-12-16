#XML is great at structuring data 
#XML runs in every language and os
# We can use both the SAX and DOM modules
#SAX usefull for very large xml files or very limited memory
import xml.sax
from xml.sax.xmlreader import AttributesImpl

#we need a content handler for the xml file and a parser that translates the file to python
class GroupHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs):
        self.current = name
        if self.current == "person":
            print("------PERSON------")
            print(f"ID: {attrs['id']}")
    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = content
    
    def endElement(self, name) :
        if self.current == "name":
            print(f"Name: {self.name}")
        elif self.current == "age":
            print(f"Age: {self.age}")
        elif self.current == "weight":
            print(f"Weight: {self.weight}")
        elif self.current == "height":
            print(f"Height: {self.height}")
        self.current = 

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
from xml.sax import InputSource

source = InputSource()
source.setByteStream(open(r"C:/Users/eryba\Desktop/Python/Python-All Topics/Intermediate topics/data.xml", "rb"))
parser.parse(source)

