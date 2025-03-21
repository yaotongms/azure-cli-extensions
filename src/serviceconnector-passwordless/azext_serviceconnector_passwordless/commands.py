# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType

from azure.cli.command_modules.serviceconnector._resource_config import (
    RESOURCE,
    SOURCE_RESOURCES,
    TARGET_RESOURCES_DEPRECATED
)
from azure.cli.command_modules.serviceconnector._transformers import (
    transform_linker_properties,
)
from azure.cli.command_modules.serviceconnector._utils import should_load_source

from ._resource_config import PASSWORDLESS_TARGET_RESOURCES
from ._client_factory import (
    cf_linker,
    cf_connector
)


def load_command_table(self, _):
    connection_type = CliCommandType(
        operations_tmpl='azure.mgmt.servicelinker.operations._linker_operations#LinkerOperations.{}',
        client_factory=cf_linker)
    local_connection_type = CliCommandType(
        operations_tmpl='azure.mgmt.servicelinker.operations._connector_operations#ConnectorOperations.{}',
        client_factory=cf_connector)

    for target in PASSWORDLESS_TARGET_RESOURCES:
        # FabricSql is not supported for Local Connector
        if target == RESOURCE.FabricSql:
            continue
        with self.command_group('connection create',
                                local_connection_type, client_factory=cf_connector) as ig:
            if target in TARGET_RESOURCES_DEPRECATED:
                ig.custom_command(target.value, 'local_connection_create_ext', deprecate_info=self.deprecate(hide=False),
                                  supports_no_wait=True, transform=transform_linker_properties)
            else:
                ig.custom_command(target.value, 'local_connection_create_ext',
                                  supports_no_wait=True, transform=transform_linker_properties)

    for source in SOURCE_RESOURCES:
        # if source resource is released as an extension, load our command groups
        # only when the extension is installed
        if should_load_source(source):
            for target in PASSWORDLESS_TARGET_RESOURCES:
                if source == RESOURCE.KubernetesCluster and target == RESOURCE.FabricSql:
                    continue
                with self.command_group(f'{source.value} connection create',
                                        connection_type, client_factory=cf_linker) as ig:
                    if target in TARGET_RESOURCES_DEPRECATED:
                        ig.custom_command(target.value, 'connection_create_ext', deprecate_info=self.deprecate(hide=False),
                                          supports_no_wait=True, transform=transform_linker_properties)
                    else:
                        ig.custom_command(target.value, 'connection_create_ext',
                                          supports_no_wait=True, transform=transform_linker_properties)
