# fengweizhi
# UDP客户端与TCP客户端区别是不用与UDP服务器建立连接，
# 而是直接把消息发送出去，然后等待服务器回复即可。
import socket
from time import ctime
import time
# 服务端ip
# 设置端口
HOST = socket.gethostbyname(socket.gethostname())
#HOST = input("Please input the host: ")
#HOST = '127.0.0.1'
print("the host is " + HOST)
PORT = int(input("please input the port: "))
ADDR = (HOST,PORT)

# 创建一个socket，指定使用ipv4协议，指定UDP
udp_cli_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    try:
        # 发送消息,因为是面向无连接，使用sendto函数要指定发送地址
        print("Please input your message: ")
        my_message = input("the Client: ")
        if not my_message:
            break

        #print("Send message at ",time.time())
        udp_cli_s.sendto(bytes(my_message,encoding="utf-8"), ADDR)

        # 接收数据
        print("Waiting for the Server ...")
        # udp_cli_s.settimeout(5)    # 5秒后未收到确认回信则重传
        accpt_msg, addr = udp_cli_s.recvfrom(1024)
        if not accpt_msg:
            break
        print("".join(("the Server received your message: ", str(accpt_msg, encoding="utf-8"))))

        #accpt_time, addr = udp_cli_s.recvfrom(1024)
        #if not accpt_time:
        #    break
        #print("".join(("the Server received your message at : ", str(accpt_time, encoding="utf-8"))))
        #print("Received the confirm at ",time.time())
    except Exception as err:
        print("Error: ", err)

# 关闭客户端
udp_cli_s.close()