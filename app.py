# -*- coding:utf-8 -*-

__author__ = 'huochai'
import time
from wsgiref.simple_server import make_server, demo_app
from jinja2 import Template


def index():
    data = open('html/index.html').read()

    template = Template(data)
    result = template.render(
        name='luotianshuai',
        age='18',
        time=str(time.time()),
        user_list=['tianshuai', 'tim', 'shuaige'],
        num=1
    )

    # 同样是替换为什么用jinja,因为他不仅仅是文本的他还支持if判断 & for循环 操作

    # 这里需要注意因为默认是的unicode的编码所以设置为utf-8
    return result.encode('utf-8')


def login():
    # 读取html并返回
    data = open('html/login.html').read()
    return data


# 1 定义一个列表,上面定义函数
url_list = [
    # 这里吧URL和函数做一个对应
    ('/index/', index),
    ('/login/', login),
]


def simple_app(environ, start_response):
    # 在环境变量里面获得url信息
    # print(environ )
    request_url = environ['PATH_INFO']
    query_param = environ['QUERY_STRING']
    print(request_url)
    print(query_param)

    # 循环这个列表
    for url in url_list:
        # 如果用户请求的url和咱们定义的rul匹配
        if request_url == url[0]:
            print(url)
            return url[1]()
            # 执行里面的方法
    else:
        # url_list列表里都没有返回404
        return [b'404']

    response_headers = [('Content-type', 'text/html')]
    start_response("200  OK", response_headers)
    return [b'Hello world!\n']


if __name__ == "__main__":
    httpd = make_server('localhost', 8000, simple_app)
    sa = httpd.socket.getsockname()
    print('http://{0}:{1}/'.format(*sa))
    httpd.serve_forever()
