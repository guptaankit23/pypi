from pensando_dss.psm.models.network import *
from pprint import pprint
from typing import NamedTuple
import json


class Key_Struct(NamedTuple):
    name: dict
    next: list

required_fields = {
    'Network': ['virtual_router', 'vlan', 'name', 'type']
}

def set_api_keys(key_list, api_output):
    e = Key_Struct(name={}, next=[])
    for val in api_output.values():
        if type(val) == dict:
            for k,v in val.items():
                if k in key_list:
                    if k == 'alg':
                        e.name[k] = "Yes"
                        e.name['type'] = v['type']
                    if type(v) == list:
                        e.name[k] = (",").join(v)
                    elif type(v) is not dict:
                        e.name[k] = v
                    continue
                find_next_key(e,v,key_list)
    return e

def find_next_key(entry, d, key_list):
    if type(d) == dict:
        e = Key_Struct(name={}, next=[])
        for k,v in d.items():
            if k in key_list:
                e.name[k] = v
            if type(v) == list or type(v) == dict:
                find_next_key(e, v, key_list)
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
    if 'ingress_security_policy' in input_dict and 'egress_security_policy' in input_dict:
        spec = NetworkNetworkSpec(
                    egress_security_policy=[
                        input_dict['egress_security_policy']
                    ],
                    ingress_security_policy=[
                        input_dict['ingress_security_policy']
                    ],
                    type=input_dict['type'],
                    virtual_router=input_dict['virtual_router'],
                    vlan_id=input_dict['vlan'],
                )
    elif 'ingress_security_policy' in input_dict:
        spec = NetworkNetworkSpec(
                    ingress_security_policy=[
                        input_dict['ingress_security_policy']
                    ],
                    type=input_dict['type'],
                    virtual_router=input_dict['virtual_router'],
                    vlan_id=input_dict['vlan'],
                )
    elif 'egress_security_policy' in input_dict:
        spec = NetworkNetworkSpec(
                    egress_security_policy=[
                        input_dict['egress_security_policy']
                    ],
                    type=input_dict['type'],
                    virtual_router=input_dict['virtual_router'],
                    vlan_id=input_dict['vlan'],
                )
    else:
        print('\n**Both Ingress & Egress Policy are empty. No updates required**\n')
        exit()
    return NetworkNetwork(
            kind="Network",
            spec=spec
        )

def validate_input_file(input_dict, type):
    if type in input_dict:
        input = input_dict[type]
    else:
        print(f'\n**{type} not found in input file**\n')
        exit()
    for field in required_fields[type]:
        if field not in input:
            print(f'\n**Required field: {field}, is missing, update the input file correctly with required fields**\n')
            exit()
