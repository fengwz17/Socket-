# fengweizhi
# 采用TCP通信的服务端
# 可靠的TCP连接，创建连接时，服务端开启，等待客户端发起连接
# 由于服务器被动无限等待连接，需要先运行服务器，再运行客户端
# 接收的客户端的消息"DISCONNECT"表示其断开连接
import socket
from time import ctime

# 创建一个socket，指定使用ipv4协议，指定使用面向流的TCP协议
tcp_ser_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
# 获取本地主机ip
# 设置端口
#HOST = socket.gethostbyname(socket.gethostname())
#HOST = input("Please input the host: ")
HOST = '0.0.0.0'
print("the host is " + HOST)
PORT = int(input("please input the port: "))
#PORT=999
# 绑定地址到套接字
tcp_ser_s.bind((HOST,PORT))
# 监听 最多同时5个连接进来
tcp_ser_s.listen(5)

# 无限循环等待连接到来
while True:
    try:
        print("Waiting for connection ....")
        # 接受客户端连接
        tcp_cli_s, addr = tcp_ser_s.accept()
        print("Connected client from : ", addr)

        # 向客户端发送连接成功信息
        msg = "the Server: Successfully connected.  Hello, I am the Server!"
        tcp_cli_s.sendall(bytes(msg, encoding="utf-8"))

        # 接受连接成功信息
        recv_msg = tcp_cli_s.recv(1024)
        print(str(recv_msg, encoding="utf-8"))

        while True:
            # 接受客户端消息
            accept_msg = str(tcp_cli_s.recv(1024), encoding="utf-8")
            print("".join(["the Client: ", accept_msg, "    the port: ", str(addr[1])]))

            # 断开连接
            if accept_msg == "DISCONNECT":
                break

            # 向客户端发送消息
            send_msg = input("the Server: ")
            tcp_cli_s.sendall(bytes(send_msg, encoding="utf-8"))

        # 关闭连接
        tcp_cli_s.close()

    except Exception as err:
        print("Error: ", err)

#tcp_ser_s.close()