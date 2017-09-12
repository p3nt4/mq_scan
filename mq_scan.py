import pymqi
import socket
import sys

def getQueueName(ip, port):
	hex_string ="545348200000010c0101310000000000000000000000011104b80000494420200d2600000000000000007ff6064000000000000053595354454d2e4445462e535652434f4e4e2020510004b841414141414141413320202020202020202020202020202020202020202020202020202020202020202020202020202000000001008a000000ff00ffffffffffffffffffffffffffffff0000000000000000000a080000000000000000000000000000444d514a42303830303030303343414e4e45445f444154412020202020202020202020202020202020202020202020202020202020202020202020202000010000ffffffffffffffffffffffffffffffff349b6485f3dc0a7361d1509b"
	hex_data = hex_string.decode("hex")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = (ip,port)
	s.settimeout(8.0)
	s.connect(server_address)
	s.send(hex_data)
	data = s.recv(268)
	i = 76
	str =''
	c='w'
	while c!='\x20':
		c = data[i]
		str=str+c
		i+=1
	s.close()
	return str;
  
if len(sys.argv)<3:
	print "Usage: mq_scan.py <IP> <PORT>"
	quit()
host = sys.argv[1]
port = sys.argv[2]
conn_info = '%s(%s)' % (host, port)
for channel in 'SYSTEM.ADMIN.SVRCONN', 'SYSTEM.DEF.SVRCONN', 'SYSTEM.AUTO.SVRCONN':
	queue_manager = getQueueName(host,int(port))
	try:
		print "[*] " + host +':'+ port +  " " + channel + " "  + queue_manager
		qmgr = pymqi.connect(queue_manager, channel, conn_info)
		print "[+] SUCCESS " + host +':'+ port +  " " + channel + " "  + queue_manager
		qmgr.disconnect()
	except:
		pass


