import os
import pensando_dss
import pensando_dss.psm
import argparse
import urllib3
import requests
from pensando_dss.psm.api import network_v1_api
from pensando_dss.psm.models.network import *
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

# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = network_v1_api.NetworkV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    try:
        #Uncomment this to suppress "InsecureRequestWarning: Unverified HTTPS request" message
        #urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        description = "List all configured VRF objects on the Pensando PSM"
        parser = argparse.ArgumentParser(description=description)
        parser.add_argument("-v", "--verbose", help = "Verbose output for all configured VRFs", action="store_true")
        parser.add_argument("-n", "---name", help = "Show verbose information for specified VRF")
        args = parser.parse_args()
        display_fields = ['name', 'uuid', 'status']
        if not args.verbose and not args.name:
            api_response = api_instance.list_virtual_router1()
            print(f"\nThere are {len(api_response.to_dict()['items'])} configured VRFs\n")
            api_response_dict = api_response.to_dict()
            max_column_width_list = get_max_width(api_response_dict['items'], display_fields)
            print("VRF NAME".ljust(max_column_width_list[0])+ "UUID".ljust(max_column_width_list[1])+ "STATUS".ljust(max_column_width_list[2]))
            print("--------".ljust(max_column_width_list[0])+ "----".ljust(max_column_width_list[1])+ "------".ljust(max_column_width_list[2]))
            for out in api_response_dict['items']:
                print_list = pretty_print(display_fields, out)
                for v in print_list:
                    name, por, pro = v
                    print(name.ljust(max_column_width_list[0])+ por.ljust(max_column_width_list[1]) + pro.ljust(max_column_width_list[2]))
        if args.verbose:
            api_response = api_instance.list_virtual_router1()
            pprint(api_response.to_dict())
        if args.name:
            api_response = api_instance.list_virtual_router1(o_name=args.name)
            pprint(api_response.to_dict())
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling NetworkV1Api->list_virtual_router1: %s\n" % e)