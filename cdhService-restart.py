import cm_client
from cm_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
cm_client.configuration.username = 'admin'
cm_client.configuration.password = 'admin'

# Create an instance of the API class
api_host = 'http://10.209.239.13'
port = '7180'
api_version = 'v17'
# Construct base URL for API
# http://cmhost:7180/api/v30
api_url = api_host + ':' + port + '/api/' + api_version
api_client = cm_client.ApiClient(api_url)
cluster_api_instance = cm_client.ClustersResourceApi(api_client)

# Lists all known clusters.
api_response = cluster_api_instance.read_clusters(view='SUMMARY')
for cluster in api_response.items:
    print cluster.name,"-", cluster.full_version


if cluster.full_version.startswith("5."):
    services_api_instance = cm_client.ServicesResourceApi(api_client)
    services = services_api_instance.read_services(cluster.name, view='FULL')
    for service in services.items:
        print service.display_name, "-", service.type
        if service.type == 'HDFS':
            hdfs = service

#Below shows how to restart any service
cmd = services_api_instance.restart_command(cluster.name, service.name)
print cmd.active
