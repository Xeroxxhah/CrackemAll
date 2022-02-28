from core.zip import Zip
from core.pdf import Pdf
from threading import Thread
import sys

VERSION = '0.1.0'

__banner__ = f'''
 _____                _    _____           ___  _ _ 
/  __ \              | |  |  ___|         / _ \| | |
| /  \/_ __ __ _  ___| | _| |__ _ __ ___ / /_\ \ | |
| |   | '__/ _` |/ __| |/ /  __| '_ ` _ \|  _  | | |
| \__/\ | | (_| | (__|   <| |__| | | | | | | | | | |
 \____/_|  \__,_|\___|_|\_\____/_| |_| |_\_| |_/_|_|
v{VERSION}
'''

print(__banner__)

threads = []

try:
    mode = sys.argv[1]

    file = sys.argv[2]

    wordlist = sys.argv[3]

except IndexError:
    print(f'{sys.argv[0]} <mode> <file> <worldlist>')
    print(f'Example: {sys.argv[0]} zip secret.zip /usr/share/wordlists/rockyou.txt')
    sys.exit()



if mode == 'zip':
    print('Cracking Zip')
    zipFile = Zip(file)
    print(f'File: {zipFile.filename}')
    print('\nArchive Content\n')
    zipFile.listzip()
elif mode == 'pdf':
    print('Cracking pdf')
    Pdf.unlock(file, wordlist)
else:
    print('Wrong Mode...')
