import socket

def createserver():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(('localhost', 9000))
        s.listen(5)
        while(1):
            (clientsocket, address) = s.accept()

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if ( len(pieces) > 0 ) : print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello, World!</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        print("shutting down...\n")
    except Exception as exc:
        print("error:\n")
        print(exc)

    s.close()

print("access http://localhost:9000")
createserver()
