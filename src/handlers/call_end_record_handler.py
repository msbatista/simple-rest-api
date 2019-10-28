import json
from tornado.web import RequestHandler
from src.schema.call_end_record_schema import CallEndRecordSchema
from marshmallow import ValidationError


class CallEndRecordHandler(RequestHandler):
    async def post(self):
        self.set_header("Content-Type", "application/json")
        try:
            call_end_record = CallEndRecordSchema().load(json.loads(self.request.body))
            self.set_status(202)
            self.write({'code': 202, 'status': 'Acepted'})
        except ValidationError as e:
            self.set_status(400, reason=str(e.messages))
            self.write(e.messages)
        except Exception as e:
            self.set_status(400, reason=str(e))
            self.write({'code': 400, 'message': str(e)})

    async def get(self):
        raise NotImplementedError("You must implement this method")