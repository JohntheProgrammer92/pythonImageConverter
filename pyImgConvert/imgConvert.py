import sys
import os
from PIL import Image
"""
USAGE: 
$ python pyConverter [input filename] [output filename]
example: pyConverter test.png test.jpg

$ python pyConverter [input directory] [output file type]
example: pyConverter ./res/ jpg

"""
def get_dirList(path):
    """
    Return a sorted list of contents from the directory
    """
    dirList = os.listdir(path)
    dirList.sort()
    return dirList

def main(args):
    if len(args) != 3 :
        print("CLI requires two arguments")

    else:
        if os.path.isdir(args[1]) == False:
                
            try:
                im = Image.open(args[1])
                rgb_im = im.convert('RGB')
                rgb_im.save(args[2], quality = 95)

            except Exception as e:

                if hasattr(e,"msg"):
                    print(e.msg)
                else:
                    print(e)

        else: 
            files = get_dirList(args[1])
            try:     
                for i in files:
                    i = args[1] + i
                    im = Image.open(i)
                    rgb_im = im.convert('RGB')
                    name = i.split('.')
                    name[2] = args[2]
                    newName = '.'.join(name)
                    rgb_im.save(newName, quality = 95)
              
            except Exception as e:

                if hasattr(e,"msg"):
                    print(e.msg)
                else:
                    print(e)

              
if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv))
    except KeyboardInterrupt:
        pass
