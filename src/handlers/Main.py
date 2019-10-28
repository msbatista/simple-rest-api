from datetime import datetime
from marshmallow import fields, Schema, pprint


class BaseSchema(Schema):
    id = fields.Integer()
    type = fields.Boolean(required=True)
    timestamp = fields.DateTime(required=True)
    call_id = fields.Integer(required=True)


class CallStartRecordSchema(BaseSchema):
    # TODO: Validate lenght of the numbers
    source = fields.Integer(required=True)
    destination = fields.Integer(required=True)


class BaseModel:
    def __init__(self,
                 id: str,
                 type: int,
                 timestamp: datetime.date,
                 call_id: int):
        self.id = id
        self.type = type
        self.timestamp = timestamp
        self.call_id = call_id



class CallStartRecordModel(BaseModel):
    def __init__(self,
                 source: int,
                 destination: int,
                 id: str,
                 type: int,
                 timestamp: datetime.date,
                 call_id: int):
        super(id, type, timestamp, call_id)
        self.source: source
        self.destination: destination


schema = CallStartRecordSchema()
callStartRecordModel = schema.load(
    {
        "id": 1,
        "type": "True",
        "timestamp": "2019-10-25T01:42:06+00:00",
        "call_id": 11,
        "source": 33333333333,
        "destination": 1111111111
    }
)

pprint(callStartRecordModel)


