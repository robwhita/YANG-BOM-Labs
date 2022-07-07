from ncclient import manager 
from router import router
import sys

search = sys.argv[1]

with manager.connect(**router, hostkey_verify=False) as m: 
  for capability in m.server_capabilities: 
    if search in capability:
      print('*' * 100)
      print(capability) 
    






