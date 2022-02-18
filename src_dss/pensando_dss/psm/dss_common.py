from pensando_dss.psm.models.network import *
from pprint import pprint
from typing import NamedTuple
import json


class Key_Struct(NamedTuple):
    name: dict
    next: list

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
    padding = 10
    res_list = []
    for out in api_out:
        e = set_api_keys(key_list, out)
        res = get_result_dict(e)
        res_list.append(res)
    width_list = []
    for key in key_list:
        w = 0
        for res in res_list:
            if key in res[0]:
                if len(str(res[0][key]))+padding > w:
                    w = len(str(res[0][key]))+padding
        width_list.append(w)
    return width_list