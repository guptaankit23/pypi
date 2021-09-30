"""
    Workload API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""



import os
import time
import requests
import json
from dateutil.parser import parse as dateutil_parser
import psm
from psm.models import *
from pprint import pprint
from psm.api import *
from api import workload_v1_api
from pensando_ent.psm.model.api_label import ApiLabel
from pensando_ent.psm.model.api_status import ApiStatus
from pensando_ent.psm.model.workload_auto_msg_endpoint_watch_helper import WorkloadAutoMsgEndpointWatchHelper
from pensando_ent.psm.model.workload_auto_msg_workload_watch_helper import WorkloadAutoMsgWorkloadWatchHelper
from pensando_ent.psm.model.workload_endpoint import WorkloadEndpoint
from pensando_ent.psm.model.workload_endpoint_list import WorkloadEndpointList
from pensando_ent.psm.model.workload_workload import WorkloadWorkload
from pensando_ent.psm.model.workload_workload_list import WorkloadWorkloadList

HOME = os.environ["HOME"]
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False



# Enter a context with an instance of the API client
with psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workload_v1_api.WorkloadV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
o_name = "O.Name_example" # str | 
body = WorkloadWorkload(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=WorkloadWorkloadSpec(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfSpec(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    external_vlan=0,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    micro_seg_vlan=0,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_timeout="60s",
        ),
        status=WorkloadWorkloadStatus(
            host_name="host_name_example",
            interfaces=[
                WorkloadWorkloadIntfStatus(
                    dsc_interfaces=[
                        "dsc_interfaces_example",
                    ],
                    endpoint="endpoint_example",
                    external_vlan=1,
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_address="mac_address_example",
                    micro_seg_vlan=1,
                    network="network_example",
                    vni=1,
                ),
            ],
            migration_status=WorkloadWorkloadMigrationStatus(
                completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stage="migration-none",
                started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="none",
            ),
            mirror_sessions=[
                "mirror_sessions_example",
            ],
            propagation_status=SecurityPropagationStatus(
                dsc_status=[
                    SecurityDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
        ),
    ) # WorkloadWorkload | 

    try:
        # Abort Workload Migration operation
        api_response = api_instance.abort_migration(o_tenant, o_name, body)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling WorkloadV1Api->abort_migration: %s\n" % e)
