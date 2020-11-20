import sys, os, pkg_resources, zipfile
from PIL import Image
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QFileDialog ,QPushButton,QListWidget, QCheckBox, QListWidgetItem, QComboBox


"""This section is needed so relative paths still work dynamically once installed on the target computer"""
this_dir,this_file = os.path.split(__file__)
iconPath = os.path.join(str(this_dir),'res','bigicon.png')
picPath = os.path.join(str(this_dir),'res','default.png')


class pic:
    """This class houses the dynamic info for each picture interacted with"""
    def __init__(self,path,name):
        self.path = path
        self.name = name


class MainWindow(QMainWindow):
    """this class houses the window and its elements"""

    def __init__(self):
        self.list = {}
        #the window itself
        super(MainWindow, self).__init__()
        self.width = 475
        self.height = 375
        self.setFixedSize(self.width,self.height)
        self.title = "Python Image Converter - PIC"
        self.setWindowIcon(QIcon(str(iconPath)))
        self.setWindowTitle(self.title)
        self.setGeometry(50,50,self.width,self.height)
        
        #browse button
        self.browse = QPushButton('Browse',self)
        self.browse.setGeometry(10,10,75,50)
        self.browse.clicked.connect(self.btnstate)

        #remove button
        self.remove = QPushButton('Remove',self)
        self.remove.setGeometry(160,10,75,50)
        self.remove.clicked.connect(self.removeItem)

        #check for directory / single file toggle 
        self.check = QCheckBox("directory",self)
        self.check.move(90,20)
        
        #list of files
        self.fileList = QListWidget(self)
        self.fileList.setGeometry(10,65,250,300)
        self.fileList.clicked.connect(self.clickRow)

        #image preview
        self.label = QLabel(self)
        print(os.getcwd())
        self.setPreview(str(picPath))
        
        #drop down for file type selection
        self.cb = QComboBox(self)
        self.cb.setPlaceholderText("Format")
        self.cb.addItems(["JPEG",
                        "PNG",
                        "EPS",
                        "ICNS",
                        "ICO",
                        "IM",
                        "BPM",
                        "JPEG 2000",
                        "MSP",
                        "PCX",
                        "DIB",
                        "PPM",
                        "SGI",
                        "TGA",
                        "XBM"])
        self.cb.setGeometry(320,215,80,30)

        #convert button
        self.convert = QPushButton('Convert',self)
        self.convert.setGeometry(300,250,120,60)
        self.convert.clicked.connect(self.convertBtn)

    
    def get_dirList(self,path):
        
        """
        Return a sorted list of contents from the directory
        """
        dirList = os.listdir(path)
        dirList.sort()
        return dirList


    def setPreview(self,path):

        """
        Sets the preview image based on the path provided
        """
        pixmap = QPixmap(path).scaled(200,200,QtCore.Qt.IgnoreAspectRatio)
        self.label.resize(pixmap.width(),pixmap.height())
        self.label.setPixmap(pixmap)
        self.label.move(self.width-pixmap.width()-10,10)

    
    def btnstate(self):

        """
        Checks the checkbox element to decide what type of dialog box to display
        Stages the selected objects for use in a list
        """
        if self.check.text() == "directory":
            if self.check.isChecked() == True:
                """
                this section handles directories 
                """
                fileNameD = QFileDialog.getExistingDirectory(self, 'Choose a Folder','C:/')
                if fileNameD != '':            
                    files = self.get_dirList(fileNameD)
                    for i in files:
                        if not os.path.isdir(fileNameD+"/"+i):
                            item = QListWidgetItem(i)
                            self.list[str(item)] = str(fileNameD+"/"+i)
                            self.fileList.addItem(item)
                    return fileNameD

            else:
                """
                this section handles individual pictures and archives
                """
                fileNameF = QFileDialog.getOpenFileNames(self, 'Choose a Picture', 'C:/')
                if fileNameF != ('', ''):
                    for i in fileNameF[0]:
                        if ".zip" in i:
                            path = i.replace('.zip',"/")
                            with zipfile.ZipFile(i) as zf:
                                zf.extractall(path)
                            files = self.get_dirList(path)
                            for j in files:
                                if not os.path.isdir(path+"/"+j):
                                    item = QListWidgetItem(j)
                                    self.list[str(item)] = str(path+"/"+j)
                                    self.fileList.addItem(item)
                            return path
                    
                        else:
                            item = QListWidgetItem(i.split('/')[-1])
                            self.list[str(item)] = str(i)
                            self.fileList.addItem(item)
                            self.setPreview(i)
                    return fileNameF
                        
                 
    def removeItem(self):

        """
        Allows a picture to be removed from the list of staged pictures then sets the preview back to default
        """
        item = self.fileList.currentItem()
        if item:   
            del self.list[str(self.fileList.currentItem())]
            self.fileList.takeItem(self.fileList.row(item))
            self.setPreview(str(picPath))


    def clickRow(self,row):

        """
        Allows the user too select a staged picture to preview it
        """
        item = self.list[str(self.fileList.currentItem())]
        self.setPreview(item)


    def convertBtn(self):

        """
        Takes the list of staged pictures and converts them based on the file type selected in the combo box element
        """
        for i in self.list:
            i = self.list[i]            
            ext = i.split('.')[1]
            newExt = str(self.cb.currentText())
            try:
                im = Image.open(i)
                rgb_im = im.convert('RGB')
                rgb_im.save(i.replace(ext, newExt), quality = 95)
            except Exception as e:

                if hasattr(e,"msg"):
                    print(e.msg)
                else:
                    print(e)

      
def execute():

    """
    Provides a psuedo main to be called from another file without name conflicts
    """
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()

    sys.exit(app.exec_())

if __name__=='__main__':
    execute()