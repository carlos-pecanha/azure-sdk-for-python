# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import map_error

from ... import models


class MessagesOperations:
    """MessagesOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar peekonly: . Constant value: "true".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self._config = config
        self.peekonly = "true"

    async def dequeue(self, number_of_messages=None, visibilitytimeout=None, timeout=None, request_id=None, *, cls=None, **kwargs):
        """The Dequeue operation retrieves one or more messages from the front of
        the queue.

        :param number_of_messages: Optional. A nonzero integer value that
         specifies the number of messages to retrieve from the queue, up to a
         maximum of 32. If fewer are visible, the visible messages are
         returned. By default, a single message is retrieved from the queue
         with this operation.
        :type number_of_messages: int
        :param visibilitytimeout: Optional. Specifies the new visibility
         timeout value, in seconds, relative to server time. The default value
         is 30 seconds. A specified value must be larger than or equal to 1
         second, and cannot be larger than 7 days, or larger than 2 hours on
         REST protocol versions prior to version 2011-08-18. The visibility
         timeout of a message can be set to a value later than the expiry time.
        :type visibilitytimeout: int
        :param timeout: The The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>
        :type timeout: int
        :param request_id: Provides a client-generated, opaque value with a 1
         KB character limit that is recorded in the analytics logs when storage
         analytics logging is enabled.
        :type request_id: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: list or the result of cls(response)
        :rtype: list[~azure.storage.queue.models.DequeuedMessageItem]
        :raises:
         :class:`StorageErrorException<azure.storage.queue.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.dequeue.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if number_of_messages is not None:
            query_parameters['numofmessages'] = self._serialize.query("number_of_messages", number_of_messages, 'int', minimum=1)
        if visibilitytimeout is not None:
            query_parameters['visibilitytimeout'] = self._serialize.query("visibilitytimeout", visibilitytimeout, 'int', maximum=604800, minimum=0)
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id", request_id, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        header_dict = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('[DequeuedMessageItem]', response)
            header_dict = {
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }

        if cls:
            return cls(response, deserialized, header_dict)

        return deserialized
    dequeue.metadata = {'url': '/{queueName}/messages'}

    async def clear(self, timeout=None, request_id=None, *, cls=None, **kwargs):
        """The Clear operation deletes all messages from the specified queue.

        :param timeout: The The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>
        :type timeout: int
        :param request_id: Provides a client-generated, opaque value with a 1
         KB character limit that is recorded in the analytics logs when storage
         analytics logging is enabled.
        :type request_id: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`StorageErrorException<azure.storage.queue.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.clear.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id", request_id, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        if cls:
            response_headers = {
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }
            return cls(response, None, response_headers)
    clear.metadata = {'url': '/{queueName}/messages'}

    async def enqueue(self, queue_message=None, visibilitytimeout=None, message_time_to_live=None, timeout=None, request_id=None, *, cls=None, **kwargs):
        """The Enqueue operation adds a new message to the back of the message
        queue. A visibility timeout can also be specified to make the message
        invisible until the visibility timeout expires. A message must be in a
        format that can be included in an XML request with UTF-8 encoding. The
        encoded message can be up to 64 KB in size for versions 2011-08-18 and
        newer, or 8 KB in size for previous versions.

        :param queue_message: A Message object which can be stored in a Queue
        :type queue_message: ~azure.storage.queue.models.QueueMessage
        :param visibilitytimeout: Optional. Specifies the new visibility
         timeout value, in seconds, relative to server time. The default value
         is 30 seconds. A specified value must be larger than or equal to 1
         second, and cannot be larger than 7 days, or larger than 2 hours on
         REST protocol versions prior to version 2011-08-18. The visibility
         timeout of a message can be set to a value later than the expiry time.
        :type visibilitytimeout: int
        :param message_time_to_live: Optional. Specifies the time-to-live
         interval for the message, in seconds. Prior to version 2017-07-29, the
         maximum time-to-live allowed is 7 days. For version 2017-07-29 or
         later, the maximum time-to-live can be any positive number, as well as
         -1 indicating that the message does not expire. If this parameter is
         omitted, the default time-to-live is 7 days.
        :type message_time_to_live: int
        :param timeout: The The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>
        :type timeout: int
        :param request_id: Provides a client-generated, opaque value with a 1
         KB character limit that is recorded in the analytics logs when storage
         analytics logging is enabled.
        :type request_id: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: list or the result of cls(response)
        :rtype: list[~azure.storage.queue.models.EnqueuedMessage]
        :raises:
         :class:`StorageErrorException<azure.storage.queue.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.enqueue.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if visibilitytimeout is not None:
            query_parameters['visibilitytimeout'] = self._serialize.query("visibilitytimeout", visibilitytimeout, 'int', maximum=604800, minimum=0)
        if message_time_to_live is not None:
            query_parameters['messagettl'] = self._serialize.query("message_time_to_live", message_time_to_live, 'int', minimum=-1)
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        header_parameters['Content-Type'] = 'application/xml; charset=utf-8'
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id", request_id, 'str')

        # Construct body
        if queue_message is not None:
            body_content = self._serialize.body(queue_message, 'QueueMessage')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        header_dict = {}
        deserialized = None
        if response.status_code == 201:
            deserialized = self._deserialize('[EnqueuedMessage]', response)
            header_dict = {
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }

        if cls:
            return cls(response, deserialized, header_dict)

        return deserialized
    enqueue.metadata = {'url': '/{queueName}/messages'}

    async def peek(self, number_of_messages=None, timeout=None, request_id=None, *, cls=None, **kwargs):
        """The Peek operation retrieves one or more messages from the front of the
        queue, but does not alter the visibility of the message.

        :param number_of_messages: Optional. A nonzero integer value that
         specifies the number of messages to retrieve from the queue, up to a
         maximum of 32. If fewer are visible, the visible messages are
         returned. By default, a single message is retrieved from the queue
         with this operation.
        :type number_of_messages: int
        :param timeout: The The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>
        :type timeout: int
        :param request_id: Provides a client-generated, opaque value with a 1
         KB character limit that is recorded in the analytics logs when storage
         analytics logging is enabled.
        :type request_id: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: list or the result of cls(response)
        :rtype: list[~azure.storage.queue.models.PeekedMessageItem]
        :raises:
         :class:`StorageErrorException<azure.storage.queue.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.peek.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if number_of_messages is not None:
            query_parameters['numofmessages'] = self._serialize.query("number_of_messages", number_of_messages, 'int', minimum=1)
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        query_parameters['peekonly'] = self._serialize.query("self.peekonly", self.peekonly, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id", request_id, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        header_dict = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('[PeekedMessageItem]', response)
            header_dict = {
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }

        if cls:
            return cls(response, deserialized, header_dict)

        return deserialized
    peek.metadata = {'url': '/{queueName}/messages'}
