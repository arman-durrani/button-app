# button-app

Practice Docker Containerization & Kube Hosting

Start by setting up django on your Laptop. I recommend creating a miniconda environment.

    mkdir -p ~/miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
    rm ~/miniconda3/miniconda.sh

    source ~/miniconda3/bin/activate

Create a django miniconda environment

    conda create -n django python=3.8

Activate the virtual environment

    conda activate django

Install the right dependencies

    pip install django

Use the following command to run the server

    python manage.py runserver

It should give you an output like : 

    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    November 16, 2024 - 01:54:08
    Django version 4.2.16, using settings 'button_count.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

Command Click or Copy the http url and it should provide you an instance of the button app.

Use Ctl-C to exit this instance.