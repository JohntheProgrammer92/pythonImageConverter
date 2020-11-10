# PIC - pythonImageConverter
A lightweight and easy to use image type converter. Built in Python as a deliverable for my Capstone project.

## Installation

```powershell
pip install pythonImageConverter
```

## Usage

#### For single pictures:

```powershell
pic [input file name] [output file name]
```

#### For entire directories:

```powershell
pic [directory name] [output file type]
```

#### To launch the GUI:

```powershell
pic GUI
```

## Examples

### CLI

#### Single Files

```powershell
pic test.png test.jpg
```

#### Directories

```powershell
pic ./ png
```

### GUI

![GUI PIC](https://raw.githubusercontent.com/JohntheProgrammer92/pythonImageConverter/master/pythonImageConverter/pyImgConvertGUI/res/ReadmePic.PNG)

#### choosing ZIP archives as a source

Because zip archives are treated like single objects do not select directory:

![ZIP1 PIC](https://raw.githubusercontent.com/JohntheProgrammer92/pythonImageConverter/master/pythonImageConverter/pyImgConvertGUI/res/zip1.PNG)

Press browse and then select the archive just as you would an individual file:

![ZIP2 PIC](https://raw.githubusercontent.com/JohntheProgrammer92/pythonImageConverter/master/pythonImageConverter/pyImgConvertGUI/res/zip2.PNG)

![ZIP3 PIC](https://raw.githubusercontent.com/JohntheProgrammer92/pythonImageConverter/master/pythonImageConverter/pyImgConvertGUI/res/zip3.PNG)


## Supported Image types

  * BMP
  * DIB
  * EPS
  * ICNS
  * ICO
  * IM
  * JPEG
  * JPEG 2000
  * MSP
  * PCX
  * PNG
  * PPM
  * SVG
  * SGI
  * TGA
  * XBM
