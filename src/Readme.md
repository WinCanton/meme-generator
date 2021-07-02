# MEME GENERATOR

This application dynamically generates meme based on quote. The meme generated can either be based on manually supplied image and quote or randomly generated from a collection of images and quotes located in the file system.

# INSTALLATION
Plese use Python's `pip` package manager to install required libraries as provided in the `requirements.txt` file. Also, the use of a virtual environment is recommended.

```
python3 -m venv venv
source venv/bin/activate
pip install requirements.txt
```


### PDFTOTEXT
One of the sub-modules utilises an open source `pdftotext` utility which can be downloaded from the following location[https://www.xpdfreader.com/download.html]. Please follow provided instruction on the website on how to install on your working OS platform.

# INTERFACE
There are 2 possible interface routes to the application: Command Line based and Web based.

### 1. Command Line (CLI)
A set of CLI commands are available and are listed in the help section available from the `--help` option.

To run application, please type `$ python3 meme.py` on the command line.

By default, the application will choose, randomly, an image to use from the file system and a quote to use, also from files of various types, on the file system.
Files containing quotes can be of the following types: `.csv`, `.docx`, `.pdf`, `.txt`

Alternatively, Image and Quote can be manually provided as arguments to the command above by using the following arguments;

- `--path` - image to the path
- `--body` - the body of the quote
- `--author` - the author of the quote

### 2. Web Interface

Meme can also be generated and viewed using a web interface. An image is randomly chosen from a directory location in the file system. And a quote also is selected randomly from a collection of files of different types stored in the file system.


The web interface can be accessed by the following:

1. Start Flask server, for example:
	`$ export FLASK_APP=app.py`
	`$ flask run --host 0.0.0.0 --port 5000`
2. Access the web application on the URL address as provided by the Flask server.


# SUB-MODULES
There are 2 main modules used to realise 2 main functionalities: (i) ingestion of quotes from different types of files, and (ii) the actual creation of meme.

## INGESTION
The ingestion functionality concrete implementation is realised by the following modules:
	- `CSVIngestor.py`
	- `DocxIngestor.py`
	- `TxtIngestor.py`
	- `PDFIngestor.py`
The `Ingestor.py` is a strategy object that wraps the above implementation into a simple, single interface.

## MEME CREATION
The creation of meme is realised by `MemeEngine.py` module.
This module is implemented by using PILLOW library.

# SAMPLE MEME
The following is an example of meme generated.

![Meme](./static/output.jpg)