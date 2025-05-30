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
    "monitor pipeline-group show",
)
class Show(AAZCommand):
    """Get the specific pipeline group instance.
    """

    _aaz_info = {
        "version": "2024-10-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.monitor/pipelinegroups/{}", "2024-10-01-preview"],
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
        _args_schema.pipeline_group_name = AAZStrArg(
            options=["-n", "--name", "--pipeline-group-name"],
            help="The name of pipeline group. The name is case insensitive.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^(?!-)[a-zA-Z0-9-]{3,32}[^-]$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.PipelineGroupsGet(ctx=self.ctx)()
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

    class PipelineGroupsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Monitor/pipelineGroups/{pipelineGroupName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "pipelineGroupName", self.ctx.args.pipeline_group_name,
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
                    "api-version", "2024-10-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.extended_location = AAZObjectType(
                serialized_name="extendedLocation",
            )
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            extended_location = cls._schema_on_200.extended_location
            extended_location.name = AAZStrType(
                flags={"required": True},
            )
            extended_location.type = AAZStrType(
                flags={"required": True},
            )

            properties = cls._schema_on_200.properties
            properties.exporters = AAZListType(
                flags={"required": True},
            )
            properties.networking_configurations = AAZListType(
                serialized_name="networkingConfigurations",
            )
            properties.processors = AAZListType(
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.receivers = AAZListType(
                flags={"required": True},
            )
            properties.replicas = AAZIntType()
            properties.service = AAZObjectType(
                flags={"required": True},
            )

            exporters = cls._schema_on_200.properties.exporters
            exporters.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.exporters.Element
            _element.azure_monitor_workspace_logs = AAZObjectType(
                serialized_name="azureMonitorWorkspaceLogs",
            )
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.tcp = AAZObjectType()
            _element.type = AAZStrType(
                flags={"required": True},
            )

            azure_monitor_workspace_logs = cls._schema_on_200.properties.exporters.Element.azure_monitor_workspace_logs
            azure_monitor_workspace_logs.api = AAZObjectType(
                flags={"required": True},
            )
            azure_monitor_workspace_logs.cache = AAZObjectType()
            azure_monitor_workspace_logs.concurrency = AAZObjectType()

            api = cls._schema_on_200.properties.exporters.Element.azure_monitor_workspace_logs.api
            api.data_collection_endpoint_url = AAZStrType(
                serialized_name="dataCollectionEndpointUrl",
                flags={"required": True},
            )
            api.data_collection_rule = AAZStrType(
                serialized_name="dataCollectionRule",
                flags={"required": True},
            )
            api.schema = AAZObjectType(
                flags={"required": True},
            )
            api.stream = AAZStrType(
                flags={"required": True},
            )

            schema = cls._schema_on_200.properties.exporters.Element.azure_monitor_workspace_logs.api.schema
            schema.record_map = AAZListType(
                serialized_name="recordMap",
                flags={"required": True},
            )
            schema.resource_map = AAZListType(
                serialized_name="resourceMap",
            )
            schema.scope_map = AAZListType(
                serialized_name="scopeMap",
            )

            record_map = cls._schema_on_200.properties.exporters.Element.azure_monitor_workspace_logs.api.schema.record_map
            record_map.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.exporters.Element.azure_monitor_workspace_logs.api.schema.record_map.Element
            _element["from"] = AAZStrType(
                flags={"required": True},
            )
            _element.to = AAZStrType(
                flags={"required": True},
            )

            resource_map = cls._schema_on_200.properties.exporters.Element.azure_monitor_workspace_logs.api.schema.resource_map
            resource_map.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.exporters.Element.azure_monitor_workspace_logs.api.schema.resource_map.Element
            _element["from"] = AAZStrType(
                flags={"required": True},
            )
            _element.to = AAZStrType(
                flags={"required": True},
            )

            scope_map = cls._schema_on_200.properties.exporters.Element.azure_monitor_workspace_logs.api.schema.scope_map
            scope_map.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.exporters.Element.azure_monitor_workspace_logs.api.schema.scope_map.Element
            _element["from"] = AAZStrType(
                flags={"required": True},
            )
            _element.to = AAZStrType(
                flags={"required": True},
            )

            cache = cls._schema_on_200.properties.exporters.Element.azure_monitor_workspace_logs.cache
            cache.max_storage_usage = AAZIntType(
                serialized_name="maxStorageUsage",
            )
            cache.retention_period = AAZIntType(
                serialized_name="retentionPeriod",
            )

            concurrency = cls._schema_on_200.properties.exporters.Element.azure_monitor_workspace_logs.concurrency
            concurrency.batch_queue_size = AAZIntType(
                serialized_name="batchQueueSize",
            )
            concurrency.worker_count = AAZIntType(
                serialized_name="workerCount",
            )

            tcp = cls._schema_on_200.properties.exporters.Element.tcp
            tcp.url = AAZStrType(
                flags={"required": True},
            )

            networking_configurations = cls._schema_on_200.properties.networking_configurations
            networking_configurations.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.networking_configurations.Element
            _element.external_networking_mode = AAZStrType(
                serialized_name="externalNetworkingMode",
                flags={"required": True},
            )
            _element.host = AAZStrType()
            _element.routes = AAZListType(
                flags={"required": True},
            )

            routes = cls._schema_on_200.properties.networking_configurations.Element.routes
            routes.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.networking_configurations.Element.routes.Element
            _element.path = AAZStrType()
            _element.port = AAZIntType()
            _element.receiver = AAZStrType(
                flags={"required": True},
            )
            _element.subdomain = AAZStrType()

            processors = cls._schema_on_200.properties.processors
            processors.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.processors.Element
            _element.batch = AAZObjectType()
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.type = AAZStrType(
                flags={"required": True},
            )

            batch = cls._schema_on_200.properties.processors.Element.batch
            batch.batch_size = AAZIntType(
                serialized_name="batchSize",
            )
            batch.timeout = AAZIntType()

            receivers = cls._schema_on_200.properties.receivers
            receivers.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.receivers.Element
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.otlp = AAZObjectType()
            _element.syslog = AAZObjectType()
            _element.type = AAZStrType(
                flags={"required": True},
            )
            _element.udp = AAZObjectType()

            otlp = cls._schema_on_200.properties.receivers.Element.otlp
            otlp.endpoint = AAZStrType(
                flags={"required": True},
            )

            syslog = cls._schema_on_200.properties.receivers.Element.syslog
            syslog.endpoint = AAZStrType(
                flags={"required": True},
            )
            syslog.protocol = AAZStrType()

            udp = cls._schema_on_200.properties.receivers.Element.udp
            udp.encoding = AAZStrType()
            udp.endpoint = AAZStrType(
                flags={"required": True},
            )
            udp.json_array_mapper = AAZObjectType(
                serialized_name="jsonArrayMapper",
            )
            udp.read_queue_length = AAZIntType(
                serialized_name="readQueueLength",
            )

            json_array_mapper = cls._schema_on_200.properties.receivers.Element.udp.json_array_mapper
            json_array_mapper.destination_field = AAZObjectType(
                serialized_name="destinationField",
            )
            json_array_mapper.keys = AAZListType(
                flags={"required": True},
            )
            json_array_mapper.source_field = AAZObjectType(
                serialized_name="sourceField",
            )

            destination_field = cls._schema_on_200.properties.receivers.Element.udp.json_array_mapper.destination_field
            destination_field.destination = AAZStrType()
            destination_field.field_name = AAZStrType(
                serialized_name="fieldName",
            )

            keys = cls._schema_on_200.properties.receivers.Element.udp.json_array_mapper.keys
            keys.Element = AAZStrType()

            source_field = cls._schema_on_200.properties.receivers.Element.udp.json_array_mapper.source_field
            source_field.field_name = AAZStrType(
                serialized_name="fieldName",
            )

            service = cls._schema_on_200.properties.service
            service.persistence = AAZObjectType()
            service.pipelines = AAZListType(
                flags={"required": True},
            )

            persistence = cls._schema_on_200.properties.service.persistence
            persistence.persistent_volume_name = AAZStrType(
                serialized_name="persistentVolumeName",
                flags={"required": True},
            )

            pipelines = cls._schema_on_200.properties.service.pipelines
            pipelines.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.service.pipelines.Element
            _element.exporters = AAZListType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.processors = AAZListType()
            _element.receivers = AAZListType(
                flags={"required": True},
            )
            _element.type = AAZStrType(
                flags={"required": True},
            )

            exporters = cls._schema_on_200.properties.service.pipelines.Element.exporters
            exporters.Element = AAZStrType()

            processors = cls._schema_on_200.properties.service.pipelines.Element.processors
            processors.Element = AAZStrType()

            receivers = cls._schema_on_200.properties.service.pipelines.Element.receivers
            receivers.Element = AAZStrType()

            system_data = cls._schema_on_200.system_data
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

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""


__all__ = ["Show"]
