import click
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False

@click.command()
@click.option('--name', help='name of the Security-Policy to be deleted')

def delete_security_policy(name):

    # Enter a context with an instance of the API client
    with pensando_dss.psm.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = security_v1_api.SecurityV1Api(api_client)
        o_name = name # str | 

        # example passing only required values which don't have defaults set
        try:
            # Delete NetworkSecurityPolicy object
            api_response = api_instance.delete_network_security_policy1(o_name)
            pprint(api_response)
        except pensando_dss.psm.ApiException as e:
            print("Exception when calling SecurityV1Api->delete_network_security_policy1: %s\n" % e)


if __name__ == '__main__':
    delete_security_policy()