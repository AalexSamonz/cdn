import socket
import time

def get_ip():
    """获取访问者的 IP 地址"""

    # 获取客户端的 IP 地址
    client_ip = socket.gethostbyname(socket.gethostname())
    print(client_ip)

#    return client_ip


def handle_request(client_socket):
    """处理客户端请求"""

    # 获取客户端的 IP 地址
    client_ip = get_ip()

    # 向客户端发送响应
    client_socket.sendall(f"访问者的 IP 地址：{client_ip}\n".encode("utf-8"))


if __name__ == "__main__":
    # 创建一个 TCP 套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定套接字到端口 80
    server_socket.bind(("127.0.0.1", 81))

    # 监听端口
    server_socket.listen(5)

    # 循环处理客户端请求
    while True:
        # 接受客户端连接
        client_socket, client_address = server_socket.accept()

        # 处理客户端请求
        handle_request(client_socket)

        # 关闭客户端套接字
        client_socket.close()


        nginx定义head，然后访问控制台的ip获取页面，有自定义的header，表示是node