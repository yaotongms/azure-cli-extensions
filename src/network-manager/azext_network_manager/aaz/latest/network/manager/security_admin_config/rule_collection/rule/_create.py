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
    "network manager security-admin-config rule-collection rule create",
)
class Create(AAZCommand):
    """Create an admin rule.

    :example: Create security admin rules
        az network manager security-admin-config rule-collection rule create --configuration-name "myTestSecurityConfig" --network-manager-name "TestNetworkManager" --resource-group "rg1" --rule-collection-name "myTestCollection" --rule-name "SampleAdminRule" --kind "Custom" --protocol "Tcp" --access "Allow" --priority 32 --direction "Inbound" --destinations address-prefix="*" address-prefix-type="IPPrefix"  --dest-port-ranges 22
    """

    _aaz_info = {
        "version": "2024-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networkmanagers/{}/securityadminconfigurations/{}/rulecollections/{}/rules/{}", "2024-05-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.configuration_name = AAZStrArg(
            options=["--config", "--config-name", "--configuration-name"],
            help="Name of the network manager security configuration.",
            required=True,
        )
        _args_schema.network_manager_name = AAZStrArg(
            options=["-n", "--name", "--network-manager-name"],
            help="The name of the network manager.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[0-9a-zA-Z]([0-9a-zA-Z_.-]{0,62}[0-9a-zA-Z_])?$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.rule_collection_name = AAZStrArg(
            options=["--rc", "--rule-collection-name"],
            help="The name of the network manager security Configuration rule collection.",
            required=True,
        )
        _args_schema.rule_name = AAZStrArg(
            options=["--rule-name"],
            help="The name of the rule.",
            required=True,
        )

        # define Arg Group "AdminRule"

        _args_schema = cls._args_schema
        _args_schema.custom = AAZObjectArg(
            options=["--custom"],
            arg_group="AdminRule",
        )
        _args_schema.default = AAZObjectArg(
            options=["--default"],
            arg_group="AdminRule",
        )

        custom = cls._args_schema.custom
        custom.access = AAZStrArg(
            options=["access"],
            help="Indicates the access allowed for this particular rule",
            enum={"Allow": "Allow", "AlwaysAllow": "AlwaysAllow", "Deny": "Deny"},
        )
        custom.description = AAZStrArg(
            options=["description"],
            help="A description for this rule. Restricted to 140 chars.",
        )
        custom.destination_port_ranges = AAZListArg(
            options=["destination-port-ranges"],
            help="The destination port ranges.",
        )
        custom.destinations = AAZListArg(
            options=["destinations"],
            help="The destination address prefixes. CIDR or destination IP ranges.",
        )
        custom.direction = AAZStrArg(
            options=["direction"],
            help="Indicates if the traffic matched against the rule in inbound or outbound.",
            enum={"Inbound": "Inbound", "Outbound": "Outbound"},
        )
        custom.priority = AAZIntArg(
            options=["priority"],
            help="The priority of the rule. The value can be between 1 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.",
            fmt=AAZIntArgFormat(
                maximum=4096,
                minimum=1,
            ),
        )
        custom.protocol = AAZStrArg(
            options=["protocol"],
            help="Network protocol this rule applies to.",
            enum={"Ah": "Ah", "Any": "Any", "Esp": "Esp", "Icmp": "Icmp", "Tcp": "Tcp", "Udp": "Udp"},
        )
        custom.source_port_ranges = AAZListArg(
            options=["source-port-ranges"],
            help="The source port ranges.",
        )
        custom.sources = AAZListArg(
            options=["sources"],
            help="The CIDR or source IP ranges.",
        )

        destination_port_ranges = cls._args_schema.custom.destination_port_ranges
        destination_port_ranges.Element = AAZStrArg()

        destinations = cls._args_schema.custom.destinations
        destinations.Element = AAZObjectArg()
        cls._build_args_address_prefix_item_create(destinations.Element)

        source_port_ranges = cls._args_schema.custom.source_port_ranges
        source_port_ranges.Element = AAZStrArg()

        sources = cls._args_schema.custom.sources
        sources.Element = AAZObjectArg()
        cls._build_args_address_prefix_item_create(sources.Element)

        default = cls._args_schema.default
        default.flag = AAZStrArg(
            options=["flag"],
            help="Default rule flag.",
        )
        return cls._args_schema

    _args_address_prefix_item_create = None

    @classmethod
    def _build_args_address_prefix_item_create(cls, _schema):
        if cls._args_address_prefix_item_create is not None:
            _schema.address_prefix = cls._args_address_prefix_item_create.address_prefix
            _schema.address_prefix_type = cls._args_address_prefix_item_create.address_prefix_type
            return

        cls._args_address_prefix_item_create = AAZObjectArg()

        address_prefix_item_create = cls._args_address_prefix_item_create
        address_prefix_item_create.address_prefix = AAZStrArg(
            options=["address-prefix"],
            help="Address prefix.",
        )
        address_prefix_item_create.address_prefix_type = AAZStrArg(
            options=["address-prefix-type"],
            help="Address prefix type.",
            enum={"IPPrefix": "IPPrefix", "NetworkGroup": "NetworkGroup", "ServiceTag": "ServiceTag"},
        )

        _schema.address_prefix = cls._args_address_prefix_item_create.address_prefix
        _schema.address_prefix_type = cls._args_address_prefix_item_create.address_prefix_type

    def _execute_operations(self):
        self.pre_operations()
        self.AdminRulesCreateOrUpdate(ctx=self.ctx)()
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

    class AdminRulesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkManagers/{networkManagerName}/securityAdminConfigurations/{configurationName}/ruleCollections/{ruleCollectionName}/rules/{ruleName}",
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
                    "configurationName", self.ctx.args.configuration_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "networkManagerName", self.ctx.args.network_manager_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "ruleCollectionName", self.ctx.args.rule_collection_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "ruleName", self.ctx.args.rule_name,
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
                    "api-version", "2024-05-01",
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
            _builder.set_const("kind", "Custom", AAZStrType, ".custom", typ_kwargs={"flags": {"required": True}})
            _builder.set_const("kind", "Default", AAZStrType, ".default", typ_kwargs={"flags": {"required": True}})
            _builder.discriminate_by("kind", "Custom")
            _builder.discriminate_by("kind", "Default")

            disc_custom = _builder.get("{kind:Custom}")
            if disc_custom is not None:
                disc_custom.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get("{kind:Custom}.properties")
            if properties is not None:
                properties.set_prop("access", AAZStrType, ".custom.access", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("description", AAZStrType, ".custom.description")
                properties.set_prop("destinationPortRanges", AAZListType, ".custom.destination_port_ranges")
                properties.set_prop("destinations", AAZListType, ".custom.destinations")
                properties.set_prop("direction", AAZStrType, ".custom.direction", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("priority", AAZIntType, ".custom.priority", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("protocol", AAZStrType, ".custom.protocol", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("sourcePortRanges", AAZListType, ".custom.source_port_ranges")
                properties.set_prop("sources", AAZListType, ".custom.sources")

            destination_port_ranges = _builder.get("{kind:Custom}.properties.destinationPortRanges")
            if destination_port_ranges is not None:
                destination_port_ranges.set_elements(AAZStrType, ".")

            destinations = _builder.get("{kind:Custom}.properties.destinations")
            if destinations is not None:
                _CreateHelper._build_schema_address_prefix_item_create(destinations.set_elements(AAZObjectType, "."))

            source_port_ranges = _builder.get("{kind:Custom}.properties.sourcePortRanges")
            if source_port_ranges is not None:
                source_port_ranges.set_elements(AAZStrType, ".")

            sources = _builder.get("{kind:Custom}.properties.sources")
            if sources is not None:
                _CreateHelper._build_schema_address_prefix_item_create(sources.set_elements(AAZObjectType, "."))

            disc_default = _builder.get("{kind:Default}")
            if disc_default is not None:
                disc_default.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get("{kind:Default}.properties")
            if properties is not None:
                properties.set_prop("flag", AAZStrType, ".default.flag")

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
            _schema_on_200_201.kind = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
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

            disc_custom = cls._schema_on_200_201.discriminate_by("kind", "Custom")
            disc_custom.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200_201.discriminate_by("kind", "Custom").properties
            properties.access = AAZStrType(
                flags={"required": True},
            )
            properties.description = AAZStrType()
            properties.destination_port_ranges = AAZListType(
                serialized_name="destinationPortRanges",
            )
            properties.destinations = AAZListType()
            properties.direction = AAZStrType(
                flags={"required": True},
            )
            properties.priority = AAZIntType(
                flags={"required": True},
            )
            properties.protocol = AAZStrType(
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.resource_guid = AAZStrType(
                serialized_name="resourceGuid",
                flags={"read_only": True},
            )
            properties.source_port_ranges = AAZListType(
                serialized_name="sourcePortRanges",
            )
            properties.sources = AAZListType()

            destination_port_ranges = cls._schema_on_200_201.discriminate_by("kind", "Custom").properties.destination_port_ranges
            destination_port_ranges.Element = AAZStrType()

            destinations = cls._schema_on_200_201.discriminate_by("kind", "Custom").properties.destinations
            destinations.Element = AAZObjectType()
            _CreateHelper._build_schema_address_prefix_item_read(destinations.Element)

            source_port_ranges = cls._schema_on_200_201.discriminate_by("kind", "Custom").properties.source_port_ranges
            source_port_ranges.Element = AAZStrType()

            sources = cls._schema_on_200_201.discriminate_by("kind", "Custom").properties.sources
            sources.Element = AAZObjectType()
            _CreateHelper._build_schema_address_prefix_item_read(sources.Element)

            disc_default = cls._schema_on_200_201.discriminate_by("kind", "Default")
            disc_default.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200_201.discriminate_by("kind", "Default").properties
            properties.access = AAZStrType(
                flags={"read_only": True},
            )
            properties.description = AAZStrType(
                flags={"read_only": True},
            )
            properties.destination_port_ranges = AAZListType(
                serialized_name="destinationPortRanges",
                flags={"read_only": True},
            )
            properties.destinations = AAZListType(
                flags={"read_only": True},
            )
            properties.direction = AAZStrType(
                flags={"read_only": True},
            )
            properties.flag = AAZStrType()
            properties.priority = AAZIntType(
                flags={"read_only": True},
            )
            properties.protocol = AAZStrType(
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.resource_guid = AAZStrType(
                serialized_name="resourceGuid",
                flags={"read_only": True},
            )
            properties.source_port_ranges = AAZListType(
                serialized_name="sourcePortRanges",
                flags={"read_only": True},
            )
            properties.sources = AAZListType(
                flags={"read_only": True},
            )

            destination_port_ranges = cls._schema_on_200_201.discriminate_by("kind", "Default").properties.destination_port_ranges
            destination_port_ranges.Element = AAZStrType()

            destinations = cls._schema_on_200_201.discriminate_by("kind", "Default").properties.destinations
            destinations.Element = AAZObjectType()
            _CreateHelper._build_schema_address_prefix_item_read(destinations.Element)

            source_port_ranges = cls._schema_on_200_201.discriminate_by("kind", "Default").properties.source_port_ranges
            source_port_ranges.Element = AAZStrType()

            sources = cls._schema_on_200_201.discriminate_by("kind", "Default").properties.sources
            sources.Element = AAZObjectType()
            _CreateHelper._build_schema_address_prefix_item_read(sources.Element)

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""

    @classmethod
    def _build_schema_address_prefix_item_create(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("addressPrefix", AAZStrType, ".address_prefix")
        _builder.set_prop("addressPrefixType", AAZStrType, ".address_prefix_type")

    _schema_address_prefix_item_read = None

    @classmethod
    def _build_schema_address_prefix_item_read(cls, _schema):
        if cls._schema_address_prefix_item_read is not None:
            _schema.address_prefix = cls._schema_address_prefix_item_read.address_prefix
            _schema.address_prefix_type = cls._schema_address_prefix_item_read.address_prefix_type
            return

        cls._schema_address_prefix_item_read = _schema_address_prefix_item_read = AAZObjectType()

        address_prefix_item_read = _schema_address_prefix_item_read
        address_prefix_item_read.address_prefix = AAZStrType(
            serialized_name="addressPrefix",
        )
        address_prefix_item_read.address_prefix_type = AAZStrType(
            serialized_name="addressPrefixType",
        )

        _schema.address_prefix = cls._schema_address_prefix_item_read.address_prefix
        _schema.address_prefix_type = cls._schema_address_prefix_item_read.address_prefix_type


__all__ = ["Create"]
