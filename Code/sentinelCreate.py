#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import web

sentinel_fixed_text = """daemonize yes
protected-mode no
"""

port = "2101"

# master_instance = [["192.168.168.59", ["16380", ], ], ["192.168.168.223", ["16379", ], ], ["192.168.168.225", ["16381", ], ], ]

class createsentinel:
    def GET(self):
        print 11234123412
        i = web.input()
        master_ip = i['master_ip']
        master_pt = i['master_pt']
        sentinel_pt = i['sentinel_pt']
        master_instance=[]
        master_instance.append(master_ip)
        listport=[]
        for i in master_pt.replace(' ,' , ',').split(','):
            if i != '':
                listport.append(i)
        master_instance.append(listport)
        name = write_sentinel_conf(sentinel_fixed_text, sentinel_pt, master_instance)
        print name
        return name

def write_sentinel_conf(sentinel_fixed_text, port, master_instance):
    print 23412412342
    from top import redis_path
    print master_instance
    file_name = "sentinel-%s.conf" % (port)
    with open(redis_path + '/' + file_name, 'w+') as conf_file:
        conf_file.write(sentinel_fixed_text)
        conf_file.write("port %s\n" % (port))
        conf_file.write('logfile "./log/sentinel-%s.log"\n' % (port))
        for i in master_instance:
            for j in i[1]:
                conf_file.write("sentinel monitor mymaster%s %s %s 3\n" % (j, i[0], j))
                conf_file.write("sentinel down-after-milliseconds mymaster%s 3100\n" % (j))
                conf_file.write("sentinel failover-timeout mymaster%s 15000\n" % (j))
            break;
    return file_name

