#In this file, I will cover xml with a dom module
import xml.dom.minidom
#DOM sees a xml file as branches of a tree. Lets create a dom tree:
domtree = xml.dom.minidom.parse("C:/Users/eryba/Desktop/Python/Python-All Topics/Intermediate topics/data.xml")
#The main part(group) in our xml file is the document element. We can think of this like the root of the dom tree
group = domtree.documentElement

persons = group.getElementsByTagName('person') 

for person in persons: 
    print("------PERSON------")
    if person.hasAttribute('id'):
        print(f"ID: {person.getAttribute('id')}")
    #printing all the subnodes(age, name, etc)
    print(f"Name: {person.getElementsByTagName('name')[0].childNodes[0].data}") #picks all the elements with the tag name 'name' however, it gives it to us as a collection so we need to use [0] and we then pick the  child nodes(the subnode or main node value we want) and we also need [0] and finaly .data to access its data
    print(f"Age: {person.getElementsByTagName('age')[0].childNodes[0].data}")
    print(f"Weight: {person.getElementsByTagName('weight')[0].childNodes[0].data}")
    print(f"Height: {person.getElementsByTagName('height')[0].childNodes[0].data}")

#Lets use the fact that we are using the DOM module and that we can change the data we have. 
#First, lets make the change in our ram and then send it to the file
"""persons[2].getElementsByTagName('name')[0].childNodes[0].nodeValue = "New Name"
persons[0].setAttribute('id', '100')
persons[3].getElementsByTagName('age')[0].childNodes[0].nodeValue = "-10"
domtree.writexml(open('C:/Users/eryba/Desktop/Python/Python-All Topics/Intermediate topics/data.xml', 'w')) """

#Adding new elements to the xml file:
newperson = domtree.createElement('person')
newperson.setAttribute('id', '6')

name = domtree.createElement('name')
name.appendChild(domtree.createTextNode('Paul Green'))

age = domtree.createElement('age')
age.appendChild(domtree.createTextNode('19'))

weight = domtree.createElement('weight')
weight.appendChild(domtree.createTextNode('80'))

height = domtree.createElement('height')
height.appendChild(domtree.createTextNode('179'))

newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

group.appendChild(newperson)

domtree.writexml(open('C:/Users/eryba/Desktop/Python/Python-All Topics/Intermediate topics/data.xml', 'w'))