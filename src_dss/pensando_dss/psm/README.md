# Example Flow

## List existing Objects:
* `python3 dss_vpc_list`
* `python3 dss_app_list`
* `python3 dss_security_policy_list`
* `python3 dss_network_list`

## Adding Objects
### Adding PSM Objects in sequence:
* Add VRFs or Apps
    * `python3 dss_vpc_add --input_file dss_add_config.yml`
    * `python3 dss_app_add.py --input_file dss_add_config.yml`
* Add Security Policies:
    * `python3 dss_security_policy_add.py --input_file dss_add_config.yml`
* Add Network
    * `python3 dss_network_add.py --input_file dss_add_config.yml`

## Updating Objects:
### Updating PSM Objects: (Objects can be modified in any Sequence) 
* `python3 dss_vpc_update.py --input_file dss_update_config.yml`
* `python3 dss_app_update.py --input_file dss_update_config.yml`
* `python3 dss_security_policy_update.py --input_file dss_update_config.yml`
* `python3 dss_network_update.py --input_file dss_update_config.yml`

## Deleting Objects in sequence:
### Deleting PSM Objects in Sequence:
* Delete Network:
    * `python3 dss_network_delete.py --name <network name>`
* Delete Security Policy:
    * `python3 dss_security_policy_delete.py --name <security policy name>`
* Delete App or VRF:
    * `python3 dss_vpc_delete.py --name <vpc/vrf name>`
    * `python3 dss_app_delete.py --name <app name>`

