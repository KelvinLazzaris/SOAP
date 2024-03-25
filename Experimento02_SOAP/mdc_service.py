from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class MDCService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def CalculateMDC(ctx, x, y):
        while y != 0:
            x, y = y, x % y
        return x

application = Application([MDCService],
                          tns='http://localhost:3000/mdc',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    import logging
    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    server = make_server('localhost', 3000, wsgi_application)
    server.serve_forever()
