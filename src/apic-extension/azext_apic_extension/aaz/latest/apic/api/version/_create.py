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
    "apic api version create",
)
class Create(AAZCommand):
    """Create a new API version or update an existing API version.

    :example: Create API version
        az apic api version create -g api-center-test -n contosoeuap --api-id echo-api --version-id 2023-01-01 --title "2023-01-01" --lifecycle-stage production
    """

    _aaz_info = {
        "version": "2024-03-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.apicenter/services/{}/workspaces/{}/apis/{}/versions/{}", "2024-03-01"],
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
        _args_schema.api_id = AAZStrArg(
            options=["--api-id"],
            help="The id of the API.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]{3,90}$",
                max_length=90,
                min_length=1,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.service_name = AAZStrArg(
            options=["-n", "--service-name"],
            help="The name of Azure API Center service.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]{3,90}$",
                max_length=90,
                min_length=1,
            ),
        )
        _args_schema.version_id = AAZStrArg(
            options=["--version-id"],
            help="The id of the API version.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]{3,90}$",
                max_length=90,
                min_length=1,
            ),
        )
        _args_schema.workspace_name = AAZStrArg(
            options=["-w", "--workspace", "--workspace-name"],
            help="The name of the workspace.",
            required=True,
            default="default",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]{3,90}$",
                max_length=90,
                min_length=1,
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.lifecycle_stage = AAZStrArg(
            options=["--lifecycle-stage"],
            arg_group="Properties",
            help="Current lifecycle stage of the API.",
            required=True,
            enum={"deprecated": "deprecated", "design": "design", "development": "development", "preview": "preview", "production": "production", "retired": "retired", "testing": "testing"},
        )
        _args_schema.title = AAZStrArg(
            options=["--title"],
            arg_group="Properties",
            help="API version.",
            required=True,
            fmt=AAZStrArgFormat(
                max_length=50,
                min_length=1,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ApiVersionsCreateOrUpdate(ctx=self.ctx)()
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

    class ApiVersionsCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiCenter/services/{serviceName}/workspaces/{workspaceName}/apis/{apiName}/versions/{versionName}",
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
                    "apiName", self.ctx.args.api_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "serviceName", self.ctx.args.service_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "versionName", self.ctx.args.version_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-03-01",
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
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("lifecycleStage", AAZStrType, ".lifecycle_stage", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("title", AAZStrType, ".title", typ_kwargs={"flags": {"required": True}})

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
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.lifecycle_stage = AAZStrType(
                serialized_name="lifecycleStage",
                flags={"required": True},
            )
            properties.title = AAZStrType(
                flags={"required": True},
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

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
