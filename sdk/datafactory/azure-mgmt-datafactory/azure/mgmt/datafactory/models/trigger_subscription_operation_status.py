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

from msrest.serialization import Model


class TriggerSubscriptionOperationStatus(Model):
    """Defines the response of a trigger subscription operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar trigger_name: Trigger name.
    :vartype trigger_name: str
    :ivar status: Event Subscription Status. Possible values include:
     'Enabled', 'Provisioning', 'Deprovisioning', 'Disabled', 'Unknown'
    :vartype status: str or
     ~azure.mgmt.datafactory.models.EventSubscriptionStatus
    """

    _validation = {
        'trigger_name': {'readonly': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'trigger_name': {'key': 'triggerName', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TriggerSubscriptionOperationStatus, self).__init__(**kwargs)
        self.trigger_name = None
        self.status = None
