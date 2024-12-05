import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.python.org')
except urllib.error.URLError:
    print('O site não está acessível no momento!')
else:
    print('Consegui acessar o site!')