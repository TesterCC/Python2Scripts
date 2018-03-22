import time
import grpc
import django
import os
from concurrent import futures

from admin import admin_pb2 
from base.base import DecoMeta

from tornado.options import define, options
define(type=int, default=50054, name="port")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metatron.settings')
django.setup()

from admin.imp_admin import EventAdmin

class AdminHandler(admin_pb2.AdminHandlerServicer):
    __metaclass__ = DecoMeta

    def insert_event(self, request, context):
        self.handler = EventAdmin()
        return self.handler.insert_event(request.json_request, request.user_id)

    def display_event(self, request, context):
        self.handler = EventAdmin()
        return self.handler.display_event(request.id)

    def get_all_province(self, request, context):
        self.handler = EventAdmin()
        return self.handler.get_all_province()

    def get_all_tag(self, request, context):
        self.handler = EventAdmin()
        return self.handler.get_all_tag()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    admin_pb2.add_AdminHandlerServicer_to_server(AdminHandler(), server)

    options.parse_command_line()
    server.add_insecure_port('[::]:{}'.format(options.port))
    server.start()
    try:
      while True:
        time.sleep(186400)
    except KeyboardInterrupt:
      server.stop(0)

serve()
