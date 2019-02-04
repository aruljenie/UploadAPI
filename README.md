# UploadAPI
This is an application in Flask to upload an image and convert text in image to string.

In Windows
Pre-requisite
Install Tesseract from https://github.com/UB-Mannheim/tesseract/wiki and 
add to path (Default :C:\Program Files (x86)\Tesseract-OCR) in Environment variables.

In Ubuntu
Pre-requisite
Install Tesseract by executing the following command in terminal.
sudo apt install tesseract-ocr

The steps are explained considering windows as the environment. However execting the same steps for Ubuntu can make the project running.

1. Download the python file to any directory[let's call it as working directory].
2. Open command prompt and change directory to working directory.
3. If you are using Visual studio code, type code . to open the editor.
4. Create virtual environment by executing virtualenv venv in command prompt. To create virtual environment in ubuntu please refer to the link https://www.linode.com/docs/development/python/create-a-python-virtualenv-on-ubuntu-1610/
5. Activate the virtual environment by executing venv\Scripts\Activate.
6. Execute requirements.txt file to install the packages.
7. Using Command Palette, choose Python Select:Interpreter and select .\venv\Scripts\python.exe
8. Press F5 to debug.
9 Use any REST Client(such as Postman) to execute the Post operation.

