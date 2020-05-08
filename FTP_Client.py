from socket import *
import sys
import time

# 具体功能

#　发起请求

#　网络链接
def main():
    #　服务器地址
    ADDR = ('127.0.0.1',8080)
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print("链接服务器失败")
        return
    else:
        print("""
            ************************
             Data   File    Image
            ************************
        """)
        cls = input("请选择文件种类：")
        if cls not in ['Data','File','Image']:
            print("Sorry input Error!!")
            return
        else:
            sockfd.send(cls.encode())
            request(sockfd)  #　发送具体请求

if __name__ == "__main__":
    main()





