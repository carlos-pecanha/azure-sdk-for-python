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


class HierarchicalModel(Model):
    """HierarchicalModel.

    :param name:
    :type name: str
    :param children:
    :type children: list[str]
    :param inherits:
    :type inherits:
     ~azure.cognitiveservices.language.luis.authoring.models.PrebuiltDomainObject
    :param roles:
    :type roles: list[str]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'children': {'key': 'children', 'type': '[str]'},
        'inherits': {'key': 'inherits', 'type': 'PrebuiltDomainObject'},
        'roles': {'key': 'roles', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(HierarchicalModel, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.children = kwargs.get('children', None)
        self.inherits = kwargs.get('inherits', None)
        self.roles = kwargs.get('roles', None)