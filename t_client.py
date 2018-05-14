import socks
s = socks.socksocket() # Same API as socket.socket in the standard lib
s.setproxy(socks.SOCKS5, "localhost", 8888)

s.connect(("www.qq.com", 80))
s.sendall("GET / HTTP/1.1 /r/n/r/n")
print(s.recv(4096))