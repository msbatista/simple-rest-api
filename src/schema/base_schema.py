from marshmallow import fields, Schema


class BaseSchema(Schema):
    id = fields.Integer(required=True)
    type = fields.Boolean(required=True)
    timestamp = fields.DateTime(required=True)
    call_id = fields.Integer(required=True)