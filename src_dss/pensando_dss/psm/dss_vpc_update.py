import click
import os
import requests
import urllib3
import yaml
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pprint import pprint
from dss_common import *


# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json",
    interactive_mode = True
)
configuration.verify_ssl = False

urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

@click.command()
@click.option('--input_file', help='yaml_file for input fields to update vpc/vrf object', prompt=True)

 
# update_vrf_policy() reads the yaml input file.
# validate if it is for kind 'Vrf' and other required fields are provided.
# Update Vrf/Virtual-Router object
def update_vrf_policy(input_file):
    if not input_file:
        print("\n**input yaml file is missing**\n")
        os.system("python3 dss_vpc_update.py --help")
        exit()
    with open(input_file, 'r') as fp:
        input = yaml.safe_load(fp)
        validate_input_file(input, 'Vrf')
    for item in input['Vrf']:
        with pensando_dss.psm.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = network_v1_api.NetworkV1Api(api_client)
            body = get_vrf_body(item)
            # example passing only required values which don't have defaults set

            try:
                # Update VirtualRouter object
                api_response = api_instance.update_virtual_router1(item['name'], body)
                pprint(api_response)
            except pensando_dss.psm.ApiException as e:
                print("Exception when calling NetworkV1Api->update_virtual_router1: %s\n" % e)


if __name__ == '__main__':
    update_vrf_policy()