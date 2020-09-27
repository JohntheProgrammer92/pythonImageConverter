# PIC - pythonImageConverter
This project is a part of my Capstone for my associate's degree. It is designed to provide a fast means to convert image file types. This repo is for the CLI portion of the project.

## Installation

```powershell
pip install pythonImageConverter
```

## Usage

* ##### For single pictures:

```powershell
pic [input file name] [output file name]
```

* ##### For entire directories:

```powershell
pic [directory name] [output file type]
```

### Examples

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
