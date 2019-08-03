from http import HTTPStatus

#https://github.com/noirbizarre/flask-restplus/issues/438
from apispec.ext.marshmallow.openapi import OpenAPIConverter
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask
from flask_restplus import Api, Resource
from marshmallow import Schema, fields

app = Flask(__name__)
api = Api(app)


class MySchema(Schema):
    myStr = fields.String()

def resolver(schema):
    return None

spec = APISpec(
    title=api.title,
    version=api.version,
    openapi_version="2.0",
    plugins=[MarshmallowPlugin(schema_name_resolver=resolver)],
    info=dict(description=api.description)
)

schema2jsonschema = spec.plugins.pop().openapi.schema2jsonschema

json_schema = schema2jsonschema(schema=MySchema)
schema_model = api.schema_model(MySchema.__name__, json_schema)


@api.route("/myResource")
class Models(Resource):
    @api.response(200, "OK", schema_model)
    def get(self):
        response = {"myStr": "something"}
        return MySchema().dump(response), HTTPStatus.OK


app.run()