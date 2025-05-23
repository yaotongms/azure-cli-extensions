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
    "redisenterprise database force-link-to-replication-group",
)
class ForceLinkToReplicationGroup(AAZCommand):
    """Forcibly recreates an existing database on the specified cluster, and rejoins it to an existing replication group. **IMPORTANT NOTE:** All data in this database will be discarded, and the database will temporarily be unavailable while rejoining the replication group.

    :example: How to relink a database after a regional outage
        az redisenterprise database force-link-to-replication-group --resource-group rg1 --cluster-name cache1 --database-name default --group-nickname groupName --linked-databases '[{id:"/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.Cache/redisEnterprise/cache1/databases/default"},{id:"/subscriptions/11111111-1111-1111-1111-111111111111/resourceGroups/rg2/providers/Microsoft.Cache/redisEnterprise/cache2/databases/default"}]'
    """

    _aaz_info = {
        "version": "2025-05-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.cache/redisenterprise/{}/databases/{}/forcelinktoreplicationgroup", "2025-05-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, None)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.cluster_name = AAZStrArg(
            options=["--cluster-name"],
            help="The name of the Redis Enterprise cluster. Name must be 1-60 characters long. Allowed characters(A-Z, a-z, 0-9) and hyphen(-). There can be no leading nor trailing nor consecutive hyphens",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^(?=.{1,60}$)[A-Za-z0-9]+(-[A-Za-z0-9]+)*$",
            ),
        )
        _args_schema.database_name = AAZStrArg(
            options=["--database-name"],
            help="The name of the Redis Enterprise database.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^(?=.{1,60}$)[A-Za-z0-9]+(-[A-Za-z0-9]+)*$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "GeoReplication"

        _args_schema = cls._args_schema
        _args_schema.group_nickname = AAZStrArg(
            options=["--group-nickname"],
            arg_group="GeoReplication",
            help="The name of the group of linked database resources. This should match the existing replication group name.",
        )
        _args_schema.linked_databases = AAZListArg(
            options=["--linked-databases"],
            arg_group="GeoReplication",
            help="The resource IDs of the databases that are expected to be linked and included in the replication group. This parameter is used to validate that the linking is to the expected (unlinked) part of the replication group, if it is splintered.",
        )

        linked_databases = cls._args_schema.linked_databases
        linked_databases.Element = AAZObjectArg()

        _element = cls._args_schema.linked_databases.Element
        _element.id = AAZResourceIdArg(
            options=["id"],
            help="Resource ID of a database resource to link with this database.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.DatabasesForceLinkToReplicationGroup(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    class DatabasesForceLinkToReplicationGroup(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    None,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/redisEnterprise/{clusterName}/databases/{databaseName}/forceLinkToReplicationGroup",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "clusterName", self.ctx.args.cluster_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "databaseName", self.ctx.args.database_name,
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
                    "api-version", "2025-05-01-preview",
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
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("geoReplication", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})

            geo_replication = _builder.get(".geoReplication")
            if geo_replication is not None:
                geo_replication.set_prop("groupNickname", AAZStrType, ".group_nickname")
                geo_replication.set_prop("linkedDatabases", AAZListType, ".linked_databases")

            linked_databases = _builder.get(".geoReplication.linkedDatabases")
            if linked_databases is not None:
                linked_databases.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".geoReplication.linkedDatabases[]")
            if _elements is not None:
                _elements.set_prop("id", AAZStrType, ".id")

            return self.serialize_content(_content_value)


class _ForceLinkToReplicationGroupHelper:
    """Helper class for ForceLinkToReplicationGroup"""


__all__ = ["ForceLinkToReplicationGroup"]
