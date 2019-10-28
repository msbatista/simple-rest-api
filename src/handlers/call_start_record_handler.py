import json
from tornado.web import RequestHandler
from ..schema.call_start_record_schema import CallStartRecordSchema
from marshmallow import ValidationError


class CallStartRecordHandler(RequestHandler):
    async def post(self):
        self.set_header("Content-Type", "application/json")
        try:
            call_start_record_model = CallStartRecordSchema().load(json.loads(self.request.body))
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
