# Socket-MyChat
## 第一步，实现通信
### UDP/TCP通信
TCP（传输控制协议）和UDP（用户数据报协议是网络体系结构TCP/IP模型中传输层一层中的两个不同的通信协议。

TCP：传输控制协议，一种面向连接的协议，给用户进程提供可靠的全双工的字节流，TCP套接口是字节流套接口(stream socket)的一种。

UDP：用户数据报协议。UDP是一种无连接协议。UDP套接口是数据报套接口(datagram socket)的一种。如视频、通话等丢几帧没有关系，连接快就好了。

### Description
server_tcp.py和client_tcp.py是TCP协议的服务端和客户端文件

server_tcp_test.py和client_tcp_test.py是用来测试传输时间的文件，其中client_tcp_test.py每次发送100个“0”，server_tcp_test.py重复接收100次，记录每次接收的时间，我感觉可以直接用wireshark捕获结果看丢帧和传输速率，这里test文件写得还不一定对，原理目前还不是很清楚。

server_udp.py和client_udp.py是UDP协议的服务端和客户端文件

先运行server文件，默认ip地址为“0.0.0.0”，可以设置为可用的ip，可以设置端口号，建议输入四位数端口号以免端口以被占用，当端口号大于可用端口号时有错误提示，则重新运行文件输入可用端口号。

运行server文件后，运行client文件，输入要连接服务端的ip地址，输入server文件中输入的端口号，等待输出提示后即可以相互通信

先关闭client文件再关闭server文件

### 同一局域网下两台电脑通信
两台电脑均连接同一手机热点

使用ipconfig获得服务端电脑的ip地址

客户端电脑ping这个ip地址看能不能ping通

实验中发现无法ping通，但是使用arp -a指令可以发现对方的ip地址，于是检查防火墙设置，更改防火墙设置后可以ping通

注意需要将server的ip地址设置为“0.0.0.0”

分别运行server.py和client.py，client.py中输入刚才使用ipconfig查询到的服务端电脑的ip地址，连接成功，可以通信：

