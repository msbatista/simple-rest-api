from src.schema.base_schema import BaseSchema
from marshmallow import fields, validate


class CallStartRecordSchema(BaseSchema):
    source = fields.Str(required=True, validate=validate.Length(min=8, max=9))
    destination = fields.Str(required=True, validate=validate.Length(min=8, max=9))
