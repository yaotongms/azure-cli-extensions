# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "devcenter admin devcenter create",
)
class Create(AAZCommand):
    """Create a dev center.

    :example: Create
        az devcenter admin devcenter create --location "eastus" --tags CostCode="12345" --name "Contoso" --resource-group "rg1"
        az devcenter admin devcenter create --identity-type "UserAssigned" --user-assigned-identities "{\\\\"/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/identityGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/testidentity1\\\\":{}}" --location "eastus" --tags CostCode="12345" --name "Contoso" --resource-group "rg1"
    """

    _aaz_info = {
        "version": "2025-04-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.devcenter/devcenters/{}", "2025-04-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the dev center.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9-]{2,25}$",
                max_length=26,
                min_length=3,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Body",
            help="The geo-location where the resource lives. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Body",
            help="Resource tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "DevBoxProvisioningSettings"

        _args_schema = cls._args_schema
        _args_schema.install_azure_monitor_agent_enable_status = AAZStrArg(
            options=["-i", "--install-azure-monitor-agent-enable-status"],
            arg_group="DevBoxProvisioningSettings",
            help="Whether project catalogs associated with projects in this dev center can be configured to sync catalog items.",
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )

        # define Arg Group "Identity"

        _args_schema = cls._args_schema
        _args_schema.identity_type = AAZStrArg(
            options=["--identity-type"],
            arg_group="Identity",
            help="Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).",
            enum={"None": "None", "SystemAssigned": "SystemAssigned", "SystemAssigned, UserAssigned": "SystemAssigned, UserAssigned", "UserAssigned": "UserAssigned"},
        )
        _args_schema.user_assigned_identities = AAZDictArg(
            options=["-u", "--user-assigned-identities"],
            arg_group="Identity",
            help="The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.",
        )

        user_assigned_identities = cls._args_schema.user_assigned_identities
        user_assigned_identities.Element = AAZObjectArg(
            blank={},
        )

        # define Arg Group "NetworkSettings"

        _args_schema = cls._args_schema
        _args_schema.microsoft_hosted_network_enable_status = AAZStrArg(
            options=["-m", "--microsoft-hosted-network-enable-status"],
            arg_group="NetworkSettings",
            help="Indicates whether pools in this Dev Center can use Microsoft Hosted Networks. Defaults to Enabled if not set.",
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )

        # define Arg Group "ProjectCatalogSettings"

        _args_schema = cls._args_schema
        _args_schema.project_catalog_item_sync_enable_status = AAZStrArg(
            options=["-p", "--project-catalog-item-sync-enable-status"],
            arg_group="ProjectCatalogSettings",
            help="Whether project catalogs associated with projects in this dev center can be configured to sync catalog items.",
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.display_name = AAZStrArg(
            options=["--display-name"],
            arg_group="Properties",
            help="The display name of the devcenter.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.DevCentersCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class DevCentersCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevCenter/devcenters/{devCenterName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "devCenterName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2025-04-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("identity", AAZIdentityObjectType)
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            identity = _builder.get(".identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".identity_type", typ_kwargs={"flags": {"required": True}})
                identity.set_prop("userAssignedIdentities", AAZDictType, ".user_assigned_identities")

            user_assigned_identities = _builder.get(".identity.userAssignedIdentities")
            if user_assigned_identities is not None:
                user_assigned_identities.set_elements(AAZObjectType, ".")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("devBoxProvisioningSettings", AAZObjectType)
                properties.set_prop("displayName", AAZStrType, ".display_name")
                properties.set_prop("networkSettings", AAZObjectType)
                properties.set_prop("projectCatalogSettings", AAZObjectType)

            dev_box_provisioning_settings = _builder.get(".properties.devBoxProvisioningSettings")
            if dev_box_provisioning_settings is not None:
                dev_box_provisioning_settings.set_prop("installAzureMonitorAgentEnableStatus", AAZStrType, ".install_azure_monitor_agent_enable_status")

            network_settings = _builder.get(".properties.networkSettings")
            if network_settings is not None:
                network_settings.set_prop("microsoftHostedNetworkEnableStatus", AAZStrType, ".microsoft_hosted_network_enable_status")

            project_catalog_settings = _builder.get(".properties.projectCatalogSettings")
            if project_catalog_settings is not None:
                project_catalog_settings.set_prop("catalogItemSyncEnableStatus", AAZStrType, ".project_catalog_item_sync_enable_status")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.identity = AAZIdentityObjectType()
            _schema_on_200_201.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200_201.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200_201.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200_201.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.dev_box_provisioning_settings = AAZObjectType(
                serialized_name="devBoxProvisioningSettings",
            )
            properties.dev_center_uri = AAZStrType(
                serialized_name="devCenterUri",
                flags={"read_only": True},
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.encryption = AAZObjectType()
            properties.network_settings = AAZObjectType(
                serialized_name="networkSettings",
            )
            properties.project_catalog_settings = AAZObjectType(
                serialized_name="projectCatalogSettings",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            dev_box_provisioning_settings = cls._schema_on_200_201.properties.dev_box_provisioning_settings
            dev_box_provisioning_settings.install_azure_monitor_agent_enable_status = AAZStrType(
                serialized_name="installAzureMonitorAgentEnableStatus",
            )

            encryption = cls._schema_on_200_201.properties.encryption
            encryption.customer_managed_key_encryption = AAZObjectType(
                serialized_name="customerManagedKeyEncryption",
            )

            customer_managed_key_encryption = cls._schema_on_200_201.properties.encryption.customer_managed_key_encryption
            customer_managed_key_encryption.key_encryption_key_identity = AAZObjectType(
                serialized_name="keyEncryptionKeyIdentity",
            )
            customer_managed_key_encryption.key_encryption_key_url = AAZStrType(
                serialized_name="keyEncryptionKeyUrl",
            )

            key_encryption_key_identity = cls._schema_on_200_201.properties.encryption.customer_managed_key_encryption.key_encryption_key_identity
            key_encryption_key_identity.delegated_identity_client_id = AAZStrType(
                serialized_name="delegatedIdentityClientId",
            )
            key_encryption_key_identity.identity_type = AAZStrType(
                serialized_name="identityType",
            )
            key_encryption_key_identity.user_assigned_identity_resource_id = AAZStrType(
                serialized_name="userAssignedIdentityResourceId",
            )

            network_settings = cls._schema_on_200_201.properties.network_settings
            network_settings.microsoft_hosted_network_enable_status = AAZStrType(
                serialized_name="microsoftHostedNetworkEnableStatus",
            )

            project_catalog_settings = cls._schema_on_200_201.properties.project_catalog_settings
            project_catalog_settings.catalog_item_sync_enable_status = AAZStrType(
                serialized_name="catalogItemSyncEnableStatus",
            )

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
