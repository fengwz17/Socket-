# fengweizhi
# 当传输的是视频音频等数据时，丢几个包也无所谓，可以采用UDP协议
# UDP服务器不是面向连接的，所以不需要设置什么东西，
# 直接等待连接就好。
# 同时由于数据报套接字是无连接的，所以无法把客户端连接交给另外的套接字进行后续的通讯，
# 服务端只是接受消息，返回收到的结果给客户端。
import socket
import time
import sys
import os

# 创建一个socket，指定使用ipv4协议，指定UDP
udp_ser_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 本地主机ip
# 设置端口
#HOST = socket.gethostbyname(socket.gethostname())
#HOST = input("Please input the host: ")
HOST = '0.0.0.0'
print("the host is " + HOST)
PORT = int(input("please input the port: "))

# 绑定地址到套接字
udp_ser_s.bind((HOST,PORT))

# 一直循环等待连接到来
while True:
    try:
        print("Waiting for message ....")

        # 接受客户端消息，消息以数据报方式传输，使用函数recvfrom
        #accept_time, addr = udp_ser_s.recvfrom(1024)
        accept_msg, addr = udp_ser_s.recvfrom(1024)
        #print("".join(("Time of receiving the Client's message: ", str(time.time()))))
        print("".join(("Get the Client's message: ", str(accept_msg, encoding="utf-8"))))

        # 向客户端发送消息
        udp_ser_s.sendto(accept_msg, addr)
        print("Received: ", str(accept_msg, encoding="utf-8"), " FROM ", addr)
        #udp_ser_s.sendto(bytes(str(time.time()),encoding="utf-8"), addr)
        #print("Send the confirm AT ", time.time())

    except Exception as err:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("Error: ", err)
        print(exc_type, fname, exc_tb.tb_lineno)

#udp_ser_s.close()
