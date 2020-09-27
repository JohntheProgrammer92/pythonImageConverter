# PIC - pythonImageConverter
A lightweight and easy to use image type converter built in Python as a deliverable for my Capstone project.

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

## Examples

#### Single Files

```powershell
pic test.png test.jpg
```

#### Directories

```powershell
pic ./ png
```

## Todo

* add support for inner folders
* add support for ignoring certain file types
* finish GUI 
