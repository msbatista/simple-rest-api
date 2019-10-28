from tornado.web import Application
from tornado.ioloop import IOLoop
from .urls import handlers


def make_app():
    return Application(handlers)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()
