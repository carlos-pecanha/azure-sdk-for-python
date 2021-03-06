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

from .proxy_resource_py3 import ProxyResource


class ServerSecurityAlertPolicy(ProxyResource):
    """A server security alert policy.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param state: Required. Specifies the state of the policy, whether it is
     enabled or disabled. Possible values include: 'Enabled', 'Disabled'
    :type state: str or
     ~azure.mgmt.rdbms.mariadb.models.ServerSecurityAlertPolicyState
    :param disabled_alerts: Specifies an array of alerts that are disabled.
     Allowed values are: Sql_Injection, Sql_Injection_Vulnerability,
     Access_Anomaly
    :type disabled_alerts: list[str]
    :param email_addresses: Specifies an array of e-mail addresses to which
     the alert is sent.
    :type email_addresses: list[str]
    :param email_account_admins: Specifies that the alert is sent to the
     account administrators.
    :type email_account_admins: bool
    :param storage_endpoint: Specifies the blob storage endpoint (e.g.
     https://MyAccount.blob.core.windows.net). This blob storage will hold all
     Threat Detection audit logs.
    :type storage_endpoint: str
    :param storage_account_access_key: Specifies the identifier key of the
     Threat Detection audit storage account.
    :type storage_account_access_key: str
    :param retention_days: Specifies the number of days to keep in the Threat
     Detection audit logs.
    :type retention_days: int
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'state': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'ServerSecurityAlertPolicyState'},
        'disabled_alerts': {'key': 'properties.disabledAlerts', 'type': '[str]'},
        'email_addresses': {'key': 'properties.emailAddresses', 'type': '[str]'},
        'email_account_admins': {'key': 'properties.emailAccountAdmins', 'type': 'bool'},
        'storage_endpoint': {'key': 'properties.storageEndpoint', 'type': 'str'},
        'storage_account_access_key': {'key': 'properties.storageAccountAccessKey', 'type': 'str'},
        'retention_days': {'key': 'properties.retentionDays', 'type': 'int'},
    }

    def __init__(self, *, state, disabled_alerts=None, email_addresses=None, email_account_admins: bool=None, storage_endpoint: str=None, storage_account_access_key: str=None, retention_days: int=None, **kwargs) -> None:
        super(ServerSecurityAlertPolicy, self).__init__(**kwargs)
        self.state = state
        self.disabled_alerts = disabled_alerts
        self.email_addresses = email_addresses
        self.email_account_admins = email_account_admins
        self.storage_endpoint = storage_endpoint
        self.storage_account_access_key = storage_account_access_key
        self.retention_days = retention_days
