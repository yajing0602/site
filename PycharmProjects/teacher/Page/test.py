import os

if __name__ == '__main__':
    path = os.getcwd()
    print(path)
    fupath = os.path.abspath(os.path.dirname(os.getcwd()))
    zipath = r"\Data\screenshot"
    print(fupath)
    pinjie = fupath+zipath
    print(pinjie)