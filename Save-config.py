from ncclient import manager, xml_ 
from router import router


netconf_filter = '''


  <cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>

'''

with manager.connect(**router, hostkey_verify=False) as m:
    response = m.dispatch(xml_.to_ele(netconf_filter))