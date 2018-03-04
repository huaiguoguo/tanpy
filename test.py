# -*- coding:utf-8 -*-
__author__ = 'huochai'

import socket


def handle_request(client):
    #接收请求
    buf = client.recv(1024)
    #返回信息
    client.send(b"HTTP/1.1 200 OK\r\n\r\n")
    client.send(b"Hello, Tim")


def main():
    #创建sock对象
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #监听80端口
    sock.bind(('localhost',8000))
    #最大允许排队的客户端
    sock.listen(5)

    #循环
    while True:
        #等待用户的连接,默认accept阻塞当有请求的时候往下执行
        connection, address = sock.accept()
        #把连接交给handle_request函数
        handle_request(connection)
        #关闭连接
        connection.close()

if __name__ == '__main__':
    main()