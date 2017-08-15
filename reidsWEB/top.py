#-*- coding: utf-8 -*-
'''
python api.py 8090 指定端口运行方式
'''
import web,logging

urls = (
    '/redis','Index',
)


class Index:
    def GET(request):
        raise web.seeother('/INSPINIA/graph_peity.html')

    def POST(request):
        return 'POST hello'

if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    web.application(urls,globals()).run()
