from ncclient import manager 
from router import router
import logging 

logging.basicConfig(level=logging.DEBUG)

netconf_filter = '''
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
        <name>GigabitEthernet2</name>
        <description>from netconf</description>
      </interface>
    </interfaces>
</config>  
      '''

with manager.connect(**router, hostkey_verify=False) as m:
    response = m.edit_config(netconf_filter, target='running') 

