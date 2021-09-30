"""
    Browser API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pensando_cloud.psm.api_client import ApiClient, Endpoint as _Endpoint
from pensando_cloud.psm.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
import pensando_cloud.psm as psm
from pensando_cloud.psm.model.browser_browse_request_list import BrowserBrowseRequestList
from pensando_cloud.psm.model.browser_browse_response import BrowserBrowseResponse
from pensando_cloud.psm.model.browser_browse_response_list import BrowserBrowseResponseList


class BrowserV1Api(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_query1(
            self,
            **kwargs
        ):
            """get_query1  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_query1(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                t_kind (str): Kind represents the type of the API object.. [optional]
                t_api_version (str): APIVersion defines the version of the API object. This can only be set by the server.. [optional]
                meta_name (str): Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64.. [optional]
                meta_tenant (str): Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48.. [optional]
                meta_namespace (str): Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64.. [optional]
                meta_generation_id (str): GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user.. [optional]
                meta_resource_version (str): Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user.. [optional]
                meta_uuid (str): UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user.. [optional]
                meta_creation_time (datetime): CreationTime is the creation time of the object. System generated and updated, not updatable by user.. [optional]
                meta_mod_time (datetime): ModTime is the Last Modification time of the object. System generated and updated, not updatable by user.. [optional]
                meta_self_link (str): SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                BrowserBrowseResponseList
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.get_query1 = _Endpoint(
            settings={
                'response_type': (BrowserBrowseResponseList,),
                'auth': [],
                'endpoint_path': '/configs/browser/v1/query',
                'operation_id': 'get_query1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    't_kind',
                    't_api_version',
                    'meta_name',
                    'meta_tenant',
                    'meta_namespace',
                    'meta_generation_id',
                    'meta_resource_version',
                    'meta_uuid',
                    'meta_creation_time',
                    'meta_mod_time',
                    'meta_self_link',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    't_kind':
                        (str,),
                    't_api_version':
                        (str,),
                    'meta_name':
                        (str,),
                    'meta_tenant':
                        (str,),
                    'meta_namespace':
                        (str,),
                    'meta_generation_id':
                        (str,),
                    'meta_resource_version':
                        (str,),
                    'meta_uuid':
                        (str,),
                    'meta_creation_time':
                        (datetime,),
                    'meta_mod_time':
                        (datetime,),
                    'meta_self_link':
                        (str,),
                },
                'attribute_map': {
                    't_kind': 'T.kind',
                    't_api_version': 'T.api-version',
                    'meta_name': 'meta.name',
                    'meta_tenant': 'meta.tenant',
                    'meta_namespace': 'meta.namespace',
                    'meta_generation_id': 'meta.generation-id',
                    'meta_resource_version': 'meta.resource-version',
                    'meta_uuid': 'meta.uuid',
                    'meta_creation_time': 'meta.creation-time',
                    'meta_mod_time': 'meta.mod-time',
                    'meta_self_link': 'meta.self-link',
                },
                'location_map': {
                    't_kind': 'query',
                    't_api_version': 'query',
                    'meta_name': 'query',
                    'meta_tenant': 'query',
                    'meta_namespace': 'query',
                    'meta_generation_id': 'query',
                    'meta_resource_version': 'query',
                    'meta_uuid': 'query',
                    'meta_creation_time': 'query',
                    'meta_mod_time': 'query',
                    'meta_self_link': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_query1
        )

        def __get_references(
            self,
            **kwargs
        ):
            """get_references  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_references(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                t_kind (str): Kind represents the type of the API object.. [optional]
                t_api_version (str): APIVersion defines the version of the API object. This can only be set by the server.. [optional]
                meta_name (str): Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64.. [optional]
                meta_tenant (str): Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48.. [optional]
                meta_namespace (str): Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64.. [optional]
                meta_generation_id (str): GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user.. [optional]
                meta_resource_version (str): Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user.. [optional]
                meta_uuid (str): UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user.. [optional]
                meta_creation_time (datetime): CreationTime is the creation time of the object. System generated and updated, not updatable by user.. [optional]
                meta_mod_time (datetime): ModTime is the Last Modification time of the object. System generated and updated, not updatable by user.. [optional]
                meta_self_link (str): SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user.. [optional]
                b_uri (str): URI is the root node from where to query. Length of string should be between 2 and 512.. [optional]
                b_query_type (str): QueryType is the direction of the query.. [optional]
                b_max_depth (int): Max-Depth specifies how deep the query should explore. By default depth is set to 1 which means immediate relations 0 means to maximum depth.. [optional]
                b_count_only (bool): When CountOnly is set the response only contains counts and not the actual objects.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                BrowserBrowseResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.get_references = _Endpoint(
            settings={
                'response_type': (BrowserBrowseResponse,),
                'auth': [],
                'endpoint_path': '/configs/browser/v1/dependencies/**',
                'operation_id': 'get_references',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    't_kind',
                    't_api_version',
                    'meta_name',
                    'meta_tenant',
                    'meta_namespace',
                    'meta_generation_id',
                    'meta_resource_version',
                    'meta_uuid',
                    'meta_creation_time',
                    'meta_mod_time',
                    'meta_self_link',
                    'b_uri',
                    'b_query_type',
                    'b_max_depth',
                    'b_count_only',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    't_kind':
                        (str,),
                    't_api_version':
                        (str,),
                    'meta_name':
                        (str,),
                    'meta_tenant':
                        (str,),
                    'meta_namespace':
                        (str,),
                    'meta_generation_id':
                        (str,),
                    'meta_resource_version':
                        (str,),
                    'meta_uuid':
                        (str,),
                    'meta_creation_time':
                        (datetime,),
                    'meta_mod_time':
                        (datetime,),
                    'meta_self_link':
                        (str,),
                    'b_uri':
                        (str,),
                    'b_query_type':
                        (str,),
                    'b_max_depth':
                        (int,),
                    'b_count_only':
                        (bool,),
                },
                'attribute_map': {
                    't_kind': 'T.kind',
                    't_api_version': 'T.api-version',
                    'meta_name': 'meta.name',
                    'meta_tenant': 'meta.tenant',
                    'meta_namespace': 'meta.namespace',
                    'meta_generation_id': 'meta.generation-id',
                    'meta_resource_version': 'meta.resource-version',
                    'meta_uuid': 'meta.uuid',
                    'meta_creation_time': 'meta.creation-time',
                    'meta_mod_time': 'meta.mod-time',
                    'meta_self_link': 'meta.self-link',
                    'b_uri': 'B.uri',
                    'b_query_type': 'B.query-type',
                    'b_max_depth': 'B.max-depth',
                    'b_count_only': 'B.count-only',
                },
                'location_map': {
                    't_kind': 'query',
                    't_api_version': 'query',
                    'meta_name': 'query',
                    'meta_tenant': 'query',
                    'meta_namespace': 'query',
                    'meta_generation_id': 'query',
                    'meta_resource_version': 'query',
                    'meta_uuid': 'query',
                    'meta_creation_time': 'query',
                    'meta_mod_time': 'query',
                    'meta_self_link': 'query',
                    'b_uri': 'query',
                    'b_query_type': 'query',
                    'b_max_depth': 'query',
                    'b_count_only': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_references
        )

        def __get_referrers(
            self,
            **kwargs
        ):
            """get_referrers  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_referrers(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                t_kind (str): Kind represents the type of the API object.. [optional]
                t_api_version (str): APIVersion defines the version of the API object. This can only be set by the server.. [optional]
                meta_name (str): Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64.. [optional]
                meta_tenant (str): Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48.. [optional]
                meta_namespace (str): Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64.. [optional]
                meta_generation_id (str): GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user.. [optional]
                meta_resource_version (str): Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user.. [optional]
                meta_uuid (str): UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user.. [optional]
                meta_creation_time (datetime): CreationTime is the creation time of the object. System generated and updated, not updatable by user.. [optional]
                meta_mod_time (datetime): ModTime is the Last Modification time of the object. System generated and updated, not updatable by user.. [optional]
                meta_self_link (str): SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user.. [optional]
                b_uri (str): URI is the root node from where to query. Length of string should be between 2 and 512.. [optional]
                b_query_type (str): QueryType is the direction of the query.. [optional]
                b_max_depth (int): Max-Depth specifies how deep the query should explore. By default depth is set to 1 which means immediate relations 0 means to maximum depth.. [optional]
                b_count_only (bool): When CountOnly is set the response only contains counts and not the actual objects.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                BrowserBrowseResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.get_referrers = _Endpoint(
            settings={
                'response_type': (BrowserBrowseResponse,),
                'auth': [],
                'endpoint_path': '/configs/browser/v1/dependedby/**',
                'operation_id': 'get_referrers',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    't_kind',
                    't_api_version',
                    'meta_name',
                    'meta_tenant',
                    'meta_namespace',
                    'meta_generation_id',
                    'meta_resource_version',
                    'meta_uuid',
                    'meta_creation_time',
                    'meta_mod_time',
                    'meta_self_link',
                    'b_uri',
                    'b_query_type',
                    'b_max_depth',
                    'b_count_only',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    't_kind':
                        (str,),
                    't_api_version':
                        (str,),
                    'meta_name':
                        (str,),
                    'meta_tenant':
                        (str,),
                    'meta_namespace':
                        (str,),
                    'meta_generation_id':
                        (str,),
                    'meta_resource_version':
                        (str,),
                    'meta_uuid':
                        (str,),
                    'meta_creation_time':
                        (datetime,),
                    'meta_mod_time':
                        (datetime,),
                    'meta_self_link':
                        (str,),
                    'b_uri':
                        (str,),
                    'b_query_type':
                        (str,),
                    'b_max_depth':
                        (int,),
                    'b_count_only':
                        (bool,),
                },
                'attribute_map': {
                    't_kind': 'T.kind',
                    't_api_version': 'T.api-version',
                    'meta_name': 'meta.name',
                    'meta_tenant': 'meta.tenant',
                    'meta_namespace': 'meta.namespace',
                    'meta_generation_id': 'meta.generation-id',
                    'meta_resource_version': 'meta.resource-version',
                    'meta_uuid': 'meta.uuid',
                    'meta_creation_time': 'meta.creation-time',
                    'meta_mod_time': 'meta.mod-time',
                    'meta_self_link': 'meta.self-link',
                    'b_uri': 'B.uri',
                    'b_query_type': 'B.query-type',
                    'b_max_depth': 'B.max-depth',
                    'b_count_only': 'B.count-only',
                },
                'location_map': {
                    't_kind': 'query',
                    't_api_version': 'query',
                    'meta_name': 'query',
                    'meta_tenant': 'query',
                    'meta_namespace': 'query',
                    'meta_generation_id': 'query',
                    'meta_resource_version': 'query',
                    'meta_uuid': 'query',
                    'meta_creation_time': 'query',
                    'meta_mod_time': 'query',
                    'meta_self_link': 'query',
                    'b_uri': 'query',
                    'b_query_type': 'query',
                    'b_max_depth': 'query',
                    'b_count_only': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_referrers
        )

        def __post_query(
            self,
            body,
            **kwargs
        ):
            """post_query  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.post_query(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (BrowserBrowseRequestList):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                BrowserBrowseResponseList
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.post_query = _Endpoint(
            settings={
                'response_type': (BrowserBrowseResponseList,),
                'auth': [],
                'endpoint_path': '/configs/browser/v1/query',
                'operation_id': 'post_query',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'body',
                ],
                'required': [
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'body':
                        (BrowserBrowseRequestList,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__post_query
        )