from ncclient import manager 
from router import router
import xml.dom.minidom 


with manager.connect(**router, hostkey_verify=False) as m:
    response = m.get_config(source = 'running', filter=('xpath', "/interfaces/interface"))
    xmlDom = xml.dom.minidom.parseString(str(response))
    print(xmlDom.toprettyxml(indent="  "))

#ict_response = xmltodict.parse(response.xml)

#print(dict_response)

