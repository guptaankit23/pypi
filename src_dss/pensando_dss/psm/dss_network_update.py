import click
import os
import requests
import urllib3
import yaml
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
from pensando_dss.psm.model.network_network import NetworkNetwork
from pensando_dss.psm.model.network_network_spec import NetworkNetworkSpec
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dss_common import *
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False

urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

@click.command()
@click.option('--input_file', help='yaml_file for input fields to update')

 
# update_network_policy() reads the yaml input file.
# validate if it is for kind 'Network' and other required fields are provided.
# network update example assumes modifying either ingress or egress security policy.
def update_network_policy(input_file):
    if not input_file:
        print("\n**input yaml file is missing**\n")
        os.system("python3 dss_network_update.py --help")
        exit()
    with open(input_file, 'r') as fp:
        input = yaml.safe_load(fp)
        validate_input_file(input, 'Network')
        
    with pensando_dss.psm.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = network_v1_api.NetworkV1Api(api_client)
        body = get_network_body(input['Network'])
        # example passing only required values which don't have defaults set
        try:
            api_response = api_instance.update_network1(input['Network']['name'], body)
            display_fields = ['name', 'virtual_router', 'vlan_id', 'ingress_security_policy', 'egress_security_policy', 'status']
            # Update Network object
            api_response_dict = api_response.to_dict()
            # print(api_response_dict)
            max_column_width_list = get_max_width([api_response_dict], display_fields)
            print("NETWORK NAME".ljust(max_column_width_list[0])+ "VRF".ljust(max_column_width_list[1])+ "VLAN".ljust(max_column_width_list[2])+ "INGRESS POLICY".ljust(max_column_width_list[3])+ "EGRESS POLICY".ljust(max_column_width_list[4])+ "PRPOGATION STATUS".ljust(max_column_width_list[5]))
            print("------------".ljust(max_column_width_list[0])+ "---".ljust(max_column_width_list[1])+ "----".ljust(max_column_width_list[2])+ "--------------".ljust(max_column_width_list[3])+ "-------------".ljust(max_column_width_list[4])+ "-----------------".ljust(max_column_width_list[5]))
            
            print_list = pretty_print(display_fields, api_response_dict)
            for v in print_list:
                name, vrf, vlan, ing_pol, egr_pol, prop_status = v
                print(name.ljust(max_column_width_list[0])+ vrf.ljust(max_column_width_list[1]) + str(vlan).ljust(max_column_width_list[2]) + ing_pol.ljust(max_column_width_list[3]) + egr_pol.ljust(max_column_width_list[4]) + prop_status.ljust(max_column_width_list[5]))
        
            pprint(api_response)
        except pensando_dss.psm.ApiException as e:
            print("Exception when calling NetworkV1Api->update_network1: %s\n" % e)

if __name__ == '__main__':
    update_network_policy()