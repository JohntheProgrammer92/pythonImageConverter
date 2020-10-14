import sys, os
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QFileDialog ,QPushButton,QListWidget, QCheckBox, QListWidgetItem, QComboBox

class pic:
    def __init__(self,path,name):
        self.path = path
        self.name = name

class MainWindow(QMainWindow):

    def __init__(self):
        self.list = {}
        #the window itself
        super(MainWindow, self).__init__()
        self.width = 475
        self.height = 375
        self.title = "Python Image Converter - PIC"
        self.setWindowIcon(QIcon("res/bigicon.png"))
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

        #check for directory single file toggle 
        self.check = QCheckBox("directory",self)
        self.check.move(90,20)
        
        #list of files
        self.fileList = QListWidget(self)
        self.fileList.setGeometry(10,65,250,300)
        self.fileList.clicked.connect(self.clickRow)

        #image preview
        self.label = QLabel(self)
        self.setPreview('res/default.png')
        
        #drop down for file type selection
        self.cb = QComboBox(self)
        self.cb.setPlaceholderText("Format")
        self.cb.addItems(["BMP",
                        "DIB",
                        "EPS",
                        "ICNS",
                        "ICO",
                        "IM",
                        "JPEG",
                        "JPEG 2000",
                        "MSP",
                        "PCX",
                        "PNG",
                        "PPM",
                        "SGI",
                        "TGA",
                        "XBM"])
        self.cb.setGeometry(265,215,80,30)

        #convert button
        self.convert = QPushButton('Convert',self)
        self.convert.setGeometry(10,10,75,50)
        self.convert.clicked.connect(self.)




    
    def get_dirList(self,path):
        
        """
        Return a sorted list of contents from the directory
        """
        dirList = os.listdir(path)
        dirList.sort()
        return dirList
        
    def setPreview(self,path):
        pixmap = QPixmap(path).scaled(200,200,QtCore.Qt.IgnoreAspectRatio)
        self.label.resize(pixmap.width(),pixmap.height())
        self.label.setPixmap(pixmap)
        self.label.move(self.width-pixmap.width()-10,10)

    
    def btnstate(self):
        if self.check.text() == "directory":
            if self.check.isChecked() == True:
                fileNameD = QFileDialog.getExistingDirectory(self, 'Choose a Folder','C:/')
                files = self.get_dirList(fileNameD)
                for i in files:
                    if not os.path.isdir(fileNameD+"/"+i):
                        item = QListWidgetItem(i)
                        self.list[str(item)] = str(fileNameD+"/"+i)
                        self.fileList.addItem(item)
                return fileNameD
                
            else:
                fileNameF = QFileDialog.getOpenFileName(self, 'Choose a Picture', 'C:/')
                item = QListWidgetItem(fileNameF[0].split('/')[-1])
                self.list[str(item)] = str(fileNameF[0])
                self.fileList.addItem(item)
                self.setPreview(fileNameF[0])
                return fileNameF
                
    def removeItem(self):
        item = self.fileList.currentItem()
        if item:   
            del self.list[str(self.fileList.currentItem())]
            self.fileList.takeItem(self.fileList.row(item))
            self.setPreview('res/default.png')

    def clickRow(self,row):
        item = self.list[str(self.fileList.currentItem())]
        self.setPreview(item)

      
        


app = QApplication(sys.argv)
w = MainWindow()
w.show()

sys.exit(app.exec_())