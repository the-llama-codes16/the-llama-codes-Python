import urllib.request
url=input('Enter URL:')
content=urllib.request.urlopen(url).read()
content=content.decode()
print(content[:3000])
print(len(content))
