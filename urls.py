from src.handlers.call_start_record_handler import CallStartRecordHandler
from src.handlers.call_end_record_handler import CallEndRecordHandler

handlers = [
    (r"/v1/startCall", CallStartRecordHandler),
    (r"/v1/endCall", CallEndRecordHandler)
]
