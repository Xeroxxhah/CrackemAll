import os
import zipfile


class Zip():

    def __init__(self,file):
        try:
            self.filepath = file
            self.zfile = zipfile.ZipFile(self.filepath)
            self.filename = os.path.basename(file)
        except FileNotFoundError:
            print('File Not Found')
            quit()
        except zipfile.BadZipFile:
            print(f'{file} is not a valid zip archive.')
            quit()
        except Exception as e:
            print(f'An error ocurred: {e}')
            quit()

    def unlock(self,wordlist):
        try:
            self.zfile.extractall()
        except Exception as e:
            if 'password required for extraction' in str(e):
                try:
                    with open(wordlist, 'rb') as wl:
                        data = wl.read().splitlines()
                        for word in data:
                            try:
                                self.zfile.extractall(pwd=word.strip())
                            except:
                                continue
                            else:
                                print(f'Password Found: {word.decode()}')
                except FileNotFoundError:
                    print('Wordlist not found')
            else:
                print(f'Following error ocurred: {e}')
    
    def listzip(self):
        try:
            self.zfile.printdir()
        except Exception as e:
            print(f'Following error ocurred: {e}')
    
    def extract(self):
        try:
            self.zfile.extractall()
        except Exception as e:
            if 'password required for extraction' in str(e):
                print('Passowrd Required')
            else:
                print(f'Following error ocurred: {e}')



