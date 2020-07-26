import numpy as np
import pandas as pd
import requests
import json

#url = "http://10.209.239.13:7180/api/v19/clusters/cluster1/services/hdfs/roles/roleName/process"
url = "http://10.209.239.13:7180/api/v1/clusters/Cluster%201/services/yarn/config?view=FULL"
JSONContent = requests.get(url).json()
content = json.dumps(JSONContent, indent = 4, sort_keys=True)
print(content)
