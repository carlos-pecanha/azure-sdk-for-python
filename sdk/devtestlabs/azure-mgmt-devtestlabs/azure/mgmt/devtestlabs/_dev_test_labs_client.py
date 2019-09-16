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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import DevTestLabsClientConfiguration
from .operations import ProviderOperations
from .operations import LabsOperations
from .operations import Operations
from .operations import GlobalSchedulesOperations
from .operations import ArtifactSourcesOperations
from .operations import ArmTemplatesOperations
from .operations import ArtifactsOperations
from .operations import CostsOperations
from .operations import CustomImagesOperations
from .operations import FormulasOperations
from .operations import GalleryImagesOperations
from .operations import NotificationChannelsOperations
from .operations import PolicySetsOperations
from .operations import PoliciesOperations
from .operations import SchedulesOperations
from .operations import ServiceRunnersOperations
from .operations import UsersOperations
from .operations import DisksOperations
from .operations import EnvironmentsOperations
from .operations import SecretsOperations
from .operations import ServiceFabricsOperations
from .operations import ServiceFabricSchedulesOperations
from .operations import VirtualMachinesOperations
from .operations import VirtualMachineSchedulesOperations
from .operations import VirtualNetworksOperations
from . import models


class DevTestLabsClient(SDKClient):
    """The DevTest Labs Client.

    :ivar config: Configuration for client.
    :vartype config: DevTestLabsClientConfiguration

    :ivar provider_operations: ProviderOperations operations
    :vartype provider_operations: azure.mgmt.devtestlabs.operations.ProviderOperations
    :ivar labs: Labs operations
    :vartype labs: azure.mgmt.devtestlabs.operations.LabsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.devtestlabs.operations.Operations
    :ivar global_schedules: GlobalSchedules operations
    :vartype global_schedules: azure.mgmt.devtestlabs.operations.GlobalSchedulesOperations
    :ivar artifact_sources: ArtifactSources operations
    :vartype artifact_sources: azure.mgmt.devtestlabs.operations.ArtifactSourcesOperations
    :ivar arm_templates: ArmTemplates operations
    :vartype arm_templates: azure.mgmt.devtestlabs.operations.ArmTemplatesOperations
    :ivar artifacts: Artifacts operations
    :vartype artifacts: azure.mgmt.devtestlabs.operations.ArtifactsOperations
    :ivar costs: Costs operations
    :vartype costs: azure.mgmt.devtestlabs.operations.CostsOperations
    :ivar custom_images: CustomImages operations
    :vartype custom_images: azure.mgmt.devtestlabs.operations.CustomImagesOperations
    :ivar formulas: Formulas operations
    :vartype formulas: azure.mgmt.devtestlabs.operations.FormulasOperations
    :ivar gallery_images: GalleryImages operations
    :vartype gallery_images: azure.mgmt.devtestlabs.operations.GalleryImagesOperations
    :ivar notification_channels: NotificationChannels operations
    :vartype notification_channels: azure.mgmt.devtestlabs.operations.NotificationChannelsOperations
    :ivar policy_sets: PolicySets operations
    :vartype policy_sets: azure.mgmt.devtestlabs.operations.PolicySetsOperations
    :ivar policies: Policies operations
    :vartype policies: azure.mgmt.devtestlabs.operations.PoliciesOperations
    :ivar schedules: Schedules operations
    :vartype schedules: azure.mgmt.devtestlabs.operations.SchedulesOperations
    :ivar service_runners: ServiceRunners operations
    :vartype service_runners: azure.mgmt.devtestlabs.operations.ServiceRunnersOperations
    :ivar users: Users operations
    :vartype users: azure.mgmt.devtestlabs.operations.UsersOperations
    :ivar disks: Disks operations
    :vartype disks: azure.mgmt.devtestlabs.operations.DisksOperations
    :ivar environments: Environments operations
    :vartype environments: azure.mgmt.devtestlabs.operations.EnvironmentsOperations
    :ivar secrets: Secrets operations
    :vartype secrets: azure.mgmt.devtestlabs.operations.SecretsOperations
    :ivar service_fabrics: ServiceFabrics operations
    :vartype service_fabrics: azure.mgmt.devtestlabs.operations.ServiceFabricsOperations
    :ivar service_fabric_schedules: ServiceFabricSchedules operations
    :vartype service_fabric_schedules: azure.mgmt.devtestlabs.operations.ServiceFabricSchedulesOperations
    :ivar virtual_machines: VirtualMachines operations
    :vartype virtual_machines: azure.mgmt.devtestlabs.operations.VirtualMachinesOperations
    :ivar virtual_machine_schedules: VirtualMachineSchedules operations
    :vartype virtual_machine_schedules: azure.mgmt.devtestlabs.operations.VirtualMachineSchedulesOperations
    :ivar virtual_networks: VirtualNetworks operations
    :vartype virtual_networks: azure.mgmt.devtestlabs.operations.VirtualNetworksOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = DevTestLabsClientConfiguration(credentials, subscription_id, base_url)
        super(DevTestLabsClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-09-15'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.provider_operations = ProviderOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.labs = LabsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.global_schedules = GlobalSchedulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.artifact_sources = ArtifactSourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.arm_templates = ArmTemplatesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.artifacts = ArtifactsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.costs = CostsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.custom_images = CustomImagesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.formulas = FormulasOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.gallery_images = GalleryImagesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.notification_channels = NotificationChannelsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.policy_sets = PolicySetsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.policies = PoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.schedules = SchedulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.service_runners = ServiceRunnersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.users = UsersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.disks = DisksOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.environments = EnvironmentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.secrets = SecretsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.service_fabrics = ServiceFabricsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.service_fabric_schedules = ServiceFabricSchedulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_machines = VirtualMachinesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_machine_schedules = VirtualMachineSchedulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_networks = VirtualNetworksOperations(
            self._client, self.config, self._serialize, self._deserialize)
