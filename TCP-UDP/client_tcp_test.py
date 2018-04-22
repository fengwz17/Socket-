#
## 测试传输速度
#
# fengweizhi
# 采用TCP通信的客户端
# 可靠的TCP连接，创建连接时，客户端向服务端发起连接
# 由于服务器被动无限等待连接，需要先运行服务端，再运行客户端
# 发送"DISCONNECT"断开连接
import socket
import sys
# 创建一个socket，指定使用ipv4协议，指定使用面向流的TCP协议
tcp_cli_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
# 输入要连接服务端的IP地址
# 设置端口
#HOST = socket.gethostbyname(socket.gethostname())
#HOST = '192.168.38.1'
HOST = input("Please input the host: ")
print("the host is " + HOST)
PORT = int((input("Please input the port: ")))
print("Waiting for connection ....")
tcp_cli_s.connect((HOST, PORT))


# 接收主机消息
# 发送连接成功消息
recv_msg = tcp_cli_s.recv(1024)
print(str(recv_msg,encoding="utf-8"))
send_msg = "Successfully connected.  Hi,I am the Client!"
tcp_cli_s.sendall(bytes(send_msg,encoding="utf-8"))
#print("Please input your message")
print("input the test data: ")
#print("Send the next one after receiving the Server's message")
# 输入并发送消息
while (True):
    try:
        # 测试发送速度，每次发送100个0
        # 发送消息
        test_data = ""
        for i in range(100):
            test_data = test_data + "0"
        print(test_data)
        # my_message = input("the Client: ")
        tcp_cli_s.sendall(bytes(test_data, encoding="utf-8"))
        #t = t + 1
        # # 断开连接
        # if my_message == "DISCONNECT":
        #     break

        # # 接受消息
        # accpt_msg = str(tcp_cli_s.recv(1024), encoding="utf-8")
        # print("".join(("the Server: ", accpt_msg)))

    except Exception as err:
        print("Error: ", err)

# 关闭连接
tcp_cli_s.close()