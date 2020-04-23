# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class ScopeAssignmentOperations(object):
    """ScopeAssignmentOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~managed_network_management_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get(
        self,
        scope,  # type: str
        scope_assignment_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ScopeAssignment"
        """Get the specified scope assignment.

        :param scope: The base resource of the scope assignment.
        :type scope: str
        :param scope_assignment_name: The name of the scope assignment to get.
        :type scope_assignment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ScopeAssignment or the result of cls(response)
        :rtype: ~managed_network_management_client.models.ScopeAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ScopeAssignment"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-06-01-preview"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'scopeAssignmentName': self._serialize.url("scope_assignment_name", scope_assignment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ScopeAssignment', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/{scope}/providers/Microsoft.ManagedNetwork/scopeAssignments/{scopeAssignmentName}'}

    def create_or_update(
        self,
        scope,  # type: str
        scope_assignment_name,  # type: str
        location=None,  # type: Optional[str]
        assigned_managed_network=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ScopeAssignment"
        """Creates a scope assignment.

        :param scope: The base resource of the scope assignment to create. The scope can be any REST
         resource instance. For example, use 'subscriptions/{subscription-id}' for a subscription,
         'subscriptions/{subscription-id}/resourceGroups/{resource-group-name}' for a resource group,
         and 'subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-
         provider}/{resource-type}/{resource-name}' for a resource.
        :type scope: str
        :param scope_assignment_name: The name of the scope assignment to create.
        :type scope_assignment_name: str
        :param location: The geo-location where the resource lives.
        :type location: str
        :param assigned_managed_network: The managed network ID with scope will be assigned to.
        :type assigned_managed_network: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ScopeAssignment or the result of cls(response)
        :rtype: ~managed_network_management_client.models.ScopeAssignment or ~managed_network_management_client.models.ScopeAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ScopeAssignment"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _parameters = models.ScopeAssignment(location=location, assigned_managed_network=assigned_managed_network)
        api_version = "2019-06-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'scopeAssignmentName': self._serialize.url("scope_assignment_name", scope_assignment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_parameters, 'ScopeAssignment')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ScopeAssignment', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('ScopeAssignment', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/{scope}/providers/Microsoft.ManagedNetwork/scopeAssignments/{scopeAssignmentName}'}

    def delete(
        self,
        scope,  # type: str
        scope_assignment_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes a scope assignment.

        :param scope: The scope of the scope assignment to delete.
        :type scope: str
        :param scope_assignment_name: The name of the scope assignment to delete.
        :type scope_assignment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-06-01-preview"

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'scopeAssignmentName': self._serialize.url("scope_assignment_name", scope_assignment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/{scope}/providers/Microsoft.ManagedNetwork/scopeAssignments/{scopeAssignmentName}'}

    def list(
        self,
        scope,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ScopeAssignmentListResult"
        """Get the specified scope assignment.

        :param scope: The base resource of the scope assignment.
        :type scope: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ScopeAssignmentListResult or the result of cls(response)
        :rtype: ~managed_network_management_client.models.ScopeAssignmentListResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ScopeAssignmentListResult"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-06-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ScopeAssignmentListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/{scope}/providers/Microsoft.ManagedNetwork/scopeAssignments'}