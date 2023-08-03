# create python3.9 virtual env
py -3.9 -m venv venv
# activate the powershell venv
venv\Scripts\activate.ps1
# if requirements.txt file exists then pip install it other wise install and freeze
if (Test-Path requirements.txt) {
    pip install -r requirements.txt
} else {
    # install gradio package
    pip install gradio
    pip install opencv-python
    # eventually we'll intsall some other stuff too
    # install other stuff!!
    # done installing everything!
    # pip freeze environment
    pip freeze > requirements.txt
}



