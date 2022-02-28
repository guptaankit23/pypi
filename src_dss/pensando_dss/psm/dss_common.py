from pensando_dss.psm.models.network import *
from pprint import pprint
from typing import NamedTuple
import copy
from pensando_dss.psm.model.security_app import SecurityApp
from pensando_dss.psm.model.security_app_spec import SecurityAppSpec
from pensando_dss.psm.model.security_alg import SecurityALG
from pensando_dss.psm.model.security_icmp import SecurityIcmp
from pensando_dss.psm.model.security_proto_port import SecurityProtoPort
from pensando_dss.psm.model.network_network import NetworkNetwork
from pensando_dss.psm.model.network_virtual_router import NetworkVirtualRouter
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_network_security_policy import SecurityNetworkSecurityPolicy


class Key_Struct(NamedTuple):
    name: dict
    next: list

required_fields = {
    'Network': ['vrf', 'vlan', 'name'],
    'Vrf': [],
    'Security_policy': [],
    'App': []
}

def set_api_keys(key_list, api_output):
    key_list_copy = copy.deepcopy(key_list)
    e = Key_Struct(name={}, next=[])
    for val in api_output.values():
        if type(val) == dict:
            for k,v in val.items():
                if k in key_list:
                    update_key_list(key_list_copy,k)
                    if k == 'alg':
                        e.name[k] = "Yes"
                        e.name['type'] = v['type']
                    if type(v) == list:
                        e.name[k] = (",").join(v)
                    elif type(v) is not dict:
                        e.name[k] = v
                    continue
                find_next_key(e,v,key_list_copy)
    return e

def update_key_list(key_list,k):
    key_list.remove(k)

def find_next_key(entry, d, key_list):
    key_list_copy = copy.deepcopy(key_list)
    if type(d) == dict:
        e = Key_Struct(name={}, next=[])
        for k,v in d.items():
            if k in key_list:
                e.name[k] = v
                update_key_list(key_list_copy,k)
            if type(v) == list or type(v) == dict:
                find_next_key(e, v, key_list_copy)
        if len(e.name.keys()) > 0:
            entry.next.append(e)
    elif type(d) == list:
        for item in d:
            if type(item) != dict:
                continue
            e = Key_Struct(name={}, next=[])
            for k,v in item.items():
                if k in key_list:
                    e.name[k] = v
                if type(v) == list or type(v) == dict:
                    find_next_key(e, v, key_list)
            if len(e.name.keys()) > 0:
                entry.next.append(e)

def get_result_dict(e):
    res_list = []
    if len(e.next) == 0:
        res_list.append(e.name)
        return res_list
    for i in range(len(e.next)):
        ent = e.next[i]
        temp_list = get_result_dict(ent)
        for ele in temp_list:
            for k,v in e.name.items():
                if i == 0:
                    ele[k] = v
                else:
                    ele[k] = ""
            res_list.append(ele)
    return res_list

def update_result_list(print_list, temp_list):
    if len(print_list) == 0:
        for ele in temp_list:
            print_list.append([ele])
        return
    
    for i in range(len(temp_list)):
        print_list[i].append(temp_list[i])


def pretty_print(key_list, api_out):
    e = set_api_keys(key_list, api_out)
    res = get_result_dict(e)
    print_list = []
    for key in key_list:
        temp_list = []
        for ele in res:
            if key in ele:
                temp_list.append(ele[key])
            else:
                temp_list.append("-")
        update_result_list(print_list, temp_list)
    return print_list

def get_max_width(api_out, key_list):
    min_width = get_key_max_width(key_list)
    padding = 10
    res_list = []
    for out in api_out:
        e = set_api_keys(key_list, out)
        res = get_result_dict(e)
        # print(e,'\n',res)
        res_list.append(res)
    width_list = []
    for key in key_list:
        for res in res_list:
            if key in res[0]:
                if len(str(res[0][key]))+padding > min_width:
                    min_width = len(str(res[0][key]))+padding
        width_list.append(min_width)
    return width_list

def get_key_max_width(key_list):
    w = 0
    for key in key_list:
        if len(key) > w:
            w = len(key)
    return w

def get_network_body(input_dict):
    netspec_dict = {           
                "firewall_profile" : NetworkNetworkFirewallProfile(
                    enable_fw_logging = True,
                ),
                "virtual_router" : input_dict["vrf"],
                "vlan_id" : input_dict["vlan"]
                }
    #Check if ig/eg policies are absent or empty and add only if present.
    if 'ingress_security_policy' in input_dict and input_dict["ingress_security_policy"] != "":
        netspec_dict["ingress_security_policy"] = [input_dict["ingress_security_policy"]]
    if 'egress_security_policy' in input_dict and input_dict["egress_security_policy"] != "":
        netspec_dict["egress_security_policy"] = [input_dict["egress_security_policy"]]
    spec = NetworkNetworkSpec(**netspec_dict)
    return NetworkNetwork(
            kind="Network",
            meta=ApiObjectMeta(name=input_dict["name"]),
            spec=spec
        )

def get_vrf_body(input_dict):
    body = NetworkVirtualRouter(
        meta=ApiObjectMeta(
            name=input_dict["name"],
        ),
    )
    if 'labels' in input_dict:
        body.meta.labels = input_dict['labels']
    return body

def get_security_policy_body(input_dict):
    rules_list = []
    #Default required params for rule_dict
    rule_dict =     {
                        "action": "",
                        "description" : "",
                        "from_ip_addresses": [],
                        "name": "",
                        "to_ip_addresses":[]
                }
    #Creating rules list
    for rule_item in input_dict["rules"]:
        rule_dict_item = rule_dict.copy()
        rule_dict_item["action"]= rule_item["action"]
        rule_dict_item["description"]= rule_item["description"]
        rule_dict_item["from_ip_addresses"]= rule_item["from-ip-addresses"]
        rule_dict_item["name"]= rule_item["name"]
        rule_dict_item["to_ip_addresses"] = rule_item["to-ip-addresses"]

        #Checking if "proto-ports" is used or "apps" is used and add the param accordingly
        if "proto-ports" in rule_item.keys():
            rule_dict_item["proto_ports"] = [SecurityProtoPort(
                                ports=rule_item["proto-ports"][0]["ports"],
                                protocol=rule_item["proto-ports"][0]["protocol"],
                            )
            ]
        elif "apps" in rule_item.keys():
            rule_dict_item["apps"] = [rule_item["apps"]]
        
        rules_list.append(SecuritySGRule(**rule_dict_item))

    body = SecurityNetworkSecurityPolicy(
        meta=ApiObjectMeta(
            name=input_dict["name"],
        ),
        spec=SecurityNetworkSecurityPolicySpec(
            attach_tenant=True,
            rules=rules_list,
        ),

    )

    return body

def get_app_body(input_dict):
    spec = SecurityAppSpec()
    alg_spec = {}
    if 'proto_ports' in input_dict:
        pp = []
        for entry in input_dict['proto_ports']:
            pp.append(SecurityProtoPort(**entry))
        spec.proto_ports = pp
    if 'alg' in input_dict and 'icmp' in input_dict['alg']:
        spec = SecurityAppSpec(
            alg = SecurityALG(
            type = 'icmp',
            icmp = SecurityIcmp(**input_dict['alg']['icmp'])
            ),
        )

    body = SecurityApp(
        kind = 'App',
        meta = ApiObjectMeta(
            name=input_dict["name"],
        ),
        spec = spec,
    )
    print(body)
    return body


def validate_input_file(input_dict, type):
    if type in input_dict:
        input = input_dict[type]
    else:
        print(f'\n**{type} not found in input file**\n')
        exit()
    for item in input:
        for field in required_fields[type]:
            if field not in item:
                print(f'\n**Required field: {field}, is missing, update the input file correctly with required fields**\n')
                exit()

def get_rule_length(out):
    if 'rules' not in out['spec']:
        return str(0)
    return str(len(out['spec']['rules']))