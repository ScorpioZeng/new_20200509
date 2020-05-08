
from socket import *
from threading import Thread
import os
from time import sleep

# 　全局变量
HOST = '0.0.0.0'
PORT = 8081
ADDR = (HOST, PORT)
FTP = "/home/tarena/FTP/"  # 文件库路径


# 将客户端请求功能封装为类

# 客户端请求处理函数
def handle(connfd):
    # 　选择文件夹
    cls = connfd.recv(1024).decode()
    FTP_PATH = FTP + cls + '/'
    ftp = FtpServer(connfd, FTP_PATH)
    while True:
        # 接受客户端请求
        data = connfd.recv(1024).decode()
        #　如果客户端断开返回ｄａｔａ为空
        if not data or data[0] == 'Q':
            return


# 网络搭建
def main():
    # 　创建套接字
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    print("Listen the port 8080...")
    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            print("退出服务程序")
            return
        except Exception as e:
            print(e)
            continue
        print("链接的客户端：", addr)
        # 　创建线程处理请求
        client = Thread(target=handle, args=(connfd,))
        client.setDaemon(True)
        client.start()


if __name__ == "__main__":
    main()
