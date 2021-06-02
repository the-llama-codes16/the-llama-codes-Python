import xml.etree.ElementTree as ET
data='''
<person>
    <name>Chuck</name>
    <phone type="intgl">+1 734 303 4456</phone>
    <email hide="yes"/>
</person>'''

tree=ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))
print('Phone Number:',tree.find('phone').text)
print('Phone Type:',tree.find('phone').get('type'))
