import sys
import os
from PIL import Image
from pyImgConvertGUI.gui import execute
"""

USAGE: 
pic [input filename] [output filename]
example: pic test.png test.jpg

pic [input directory] [output file type]
example: pic ./res/ jpg

"""
def get_dirList(path):
    """
    Return a sorted list of contents from the directory
    """
    dirList = os.listdir(path)
    dirList.sort()
    return dirList

def main(args=None):
    if args is None:
        args = sys.argv
    if args[1] != "GUI":
        if len(args) != 3:
            print(""" 
    USAGE: 
    pic [input filename] [output filename]
    example: pic test.png test.jpg

    pic [input directory] [output file type]
    example: pic ./res/ jpg
    """)

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
    else: 
        execute()

              
if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv[0:]))
    except KeyboardInterrupt:
        pass
