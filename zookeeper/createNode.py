from kazoo.client import KazooClient

zk = KazooClient(hosts='192.168.30.135:2181')
zk.start()

zk.create('/GuangDong/ShenZhen/OPPO/shuzhi',b'this is my company',makepath=True)
nodes = zk.get_children('/')

print("nodes: ",nodes)

zk.stop()