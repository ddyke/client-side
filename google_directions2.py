"""
Pull driving directions from Annecy to Brunico in XML.
Then extract the step-by-step directions.
"""

import requests
from xml.etree import ElementTree as et

start_point = "Annecy"
destination_point = "Brunico"
travel_mode = {1: 'driving', 2: 'walking', 3: 'bicycling', 4: 'transit'}
url ='https://maps.googleapis.com/maps/api/directions/xml?origin={}&destination={}&sensor=false&mode={}'.format(
    start_point, destination_point, travel_mode[1]
)

data = requests.get(url)
with open('test.xml', 'wb') as output:
    output.write(data.content)

doc = et.parse('test.xml')
for rt in doc.findall('route'):
    for lg in rt.findall('leg'):
        for stp in lg.findall('step'):
            print(stp.find('html_instructions').text)

    print([sub.tag for sub in rt])  # print list of tags



