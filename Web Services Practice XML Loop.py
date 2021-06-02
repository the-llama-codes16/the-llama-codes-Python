import xml.etree.ElementTree as ET
input='''
<stuff>
    <users>
        <user x='2'>
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x='7'>
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''
stuff=ET.fromstring(input)
lst=stuff.findall('users/user')
print('Number of Users:',len(lst))

for item in lst:
    print('\nName:',item.find('name').text)
    print('Attribute:',item.get('x'))
    print('ID Number:',item.find('id').text)
    
