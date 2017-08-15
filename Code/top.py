#-*- coding: utf-8 -*-
'''
python api.py 8090 指定端口运行方式
'''

import web,logging,os
from salt_code import salt_manage , dealRequest
from writeConfig import createconfig
from sentinelCreate import createsentinel

redis_path='/srv/salt/redis'

urls = (
    '/redis','Index',
    '/redis/getfile' , 'getFile',
    '/redis/getserver', 'salt_manage',
    '/redis/deal', 'dealRequest',
    '/redis/createconfig' , 'createconfig',
    '/redis/createsentinel' , 'createsentinel'
)


class Index:

    def GET(self):
        raise web.seeother('/INSPINIA/graph_peity.html')

    def POST(self):
        return 'POST hello'


class getFile:

    def GET(self):
        files = []
        for root,file,filename in os.walk(redis_path):
            for i in filename:
                if not i.startswith('.'):
                    files.append(i)
        return files


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    web.application(urls,globals()).run()
