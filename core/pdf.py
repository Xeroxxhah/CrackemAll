import pikepdf


class Pdf():

    def unlock(pdffile,wordlist):
        try:
            with open(wordlist, 'r') as wordlist:
                content = wordlist.read().splitlines()

                for password in content:
                    try:
                        with pikepdf.open(pdffile, password=password) as pdfFile:
                            print(f'Password Found: {password}')
                            break
                    except pikepdf._qpdf.PasswordError:
                        continue
                    except FileNotFoundError:
                        print('File not Found')
                        quit()
                    except pikepdf._qpdf.PdfError:
                        print(f'{pdffile} is not a valid pdf file or it is damaged..')
                        quit()
        except FileNotFoundError:
            print('Wordlist not Found')
            quit()