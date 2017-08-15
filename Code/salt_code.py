import salt.client
import web
import os
class salt_manage:
    def GET(self):
        client = salt.client.LocalClient()
        x = client.cmd('*' , 'test.ping')
        #x = {'nginx-136': False, 'WEBnginx-119': True, 'nginx-162': True, 'mysql-master-79': True, 'centos6-114': True, 'mysql-slave-186': True, 'mysql-master-165': True, 'centos6-100': True, 'mysql-slave-174': True, 'centos6-176': True}
        list = []
        for key in x.keys():
            if x[key] == True:
                list.append(key)
        return list

class dealRequest:
    def GET(self):
        i = web.input()
        rs = dealRequest().dealreques(i['redis'] , i['server'] , i['type'])
        return rs

    def dealreques(self,filename , server , type):
        from top import redis_path
        client = salt.client.LocalClient()
        listserver=[]
        for i in server.replace(' ,' , ',').split(','):
            if i != '':
                listserver.append(i)

        rootpath = redis_path.replace('/srv/salt/' , '')

        if type == '1':
            try:
                rootpath = redis_path.replace('/srv/salt/' , '')
                ret = ''
                # client.cmd(listserver,'cp.get_file' , ('salt://'+rootpath+'/'+filename,'/root/'+filename) , 2 , 'list')
                ret=client.cmd(listserver,'cp.get_file' , ('salt://'+rootpath+'/'+filename,'/root/'+filename) , 2 , 'list')

                x=client.cmd(listserver,'cmd.run' , ('rpm -qa|grep ^gcc',) , 2 , 'list')
                list=[]
                for key in x.keys():
                    if x[key]=='':
                        list.append(key)
                if len(list)!=0:
                    z=client.cmd(list,'cmd.run' , ('yum install -y gcc',) , 2 , 'list')

                cmd = 'tar xvf /root/' + filename + ' &>/dev/null && cd /root/'+ filename.replace('.tar' , '').replace('.gz' , '') +' &&  make'
                ret=client.cmd(listserver,'cmd.run' , (cmd,) , 2 , 'list')
            except:
                return 1
            return 0
        elif type == '2':
            client.cmd(listserver,'cmd.run' , ('mkdir /root/redisconfig ; mkdir /root/log ; mkdir /root/dump' ,) , 2 , 'list')
            client.cmd(listserver,'cp.get_file' , ('salt://'+rootpath+'/'+filename,'/root/redisconfig/'+filename) , 2 , 'list')
            os.system('rm -rf '+rootpath+'/'+filename)
	    return 0
	elif type == '3':
            client.cmd(listserver,'cmd.run' , ('mkdir /root/redisconfig ; mkdir /root/log ; mkdir /root/dump') , 2 , 'list')
            client.cmd(listserver,'cp.get_file' , ('salt://'+rootpath+'/'+filename,'/root/redisconfig/'+filename) , 2 , 'list')
            os.system('rm -rf '+rootpath+'/'+filename)
            return 0
	return 0
