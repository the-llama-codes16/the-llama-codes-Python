import socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
while True:
    url=input('Enter URL:')
    try:
        words=url.split('/')
        webpage=words[2]
        mysock.connect((webpage,80))
        cmd='GET '+url+' HTTP/1.0\r\n\r\n'
        cmd=cmd.encode()
        mysock.send(cmd)
        break
    except:
        print('Invalid URL')
        continue

while True:
    data=mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
mysock.close()


