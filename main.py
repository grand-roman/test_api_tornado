from tornado.ioloop import IOLoop
from tornado.web import Application

from api import ItemCRUD, LookItems, TotalDuplicate


def make_app():
    urls = [
        ("/", LookItems),
        (r"/api/([^/]+)?", ItemCRUD),
        (r"/api/duplicate", TotalDuplicate)
    ]
    return Application(urls, debug=True)


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    IOLoop.instance().start()
