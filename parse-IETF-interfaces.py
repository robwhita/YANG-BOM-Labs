from ncclient import manager 
from router import router
import xmltodict 

netconf_filter = '''
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  </interfaces>
  ''' 

with manager.connect(**router, hostkey_verify=False) as m:
    response = m.get(filter=('subtree', netconf_filter))

    
dict_resp = xmltodict.parse(response.xml)
#print(dict_resp)

int_name = dict_resp['rpc-reply']['data']['interfaces']['interface'][0]['name']
print(f' The name of the interfaces is: {int_name}')


