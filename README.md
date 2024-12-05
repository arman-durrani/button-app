# button-app


__BASIC INSTRUCTIONS :__

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

__CURL USAGE :__
What if I want to access the button application purely from curl (perhaps I don't have port-forwarding set up).
We can use CURL to make POST and GET requests from our application. In order to do so in a singular session, start by running :

    curl -X POST http://localhost:8000/button-click/ -H "Content-Type: application/json" -c cookies.txt -d "{}"

This command creates a file cookies.txt which essentially contains session metadata that you can use in subsequent requests like the following :

    curl -X POST http://localhost:8000/button-click/     -H "Content-Type: application/json"     -b cookies.txt     -d "{}" -i
    #This will increment the button-click counter again

    curl -X GET http://localhost:8000/button-click/ -b cookies.txt
    #This will return the current number of clicks in your session.

NOTE : You must have launched the site with a python manage.py runserver command for curl commands to work.


__DOCKER INSTRUCTIONS :__

Use the dockerfile to create an image of this application with the following build command :

    docker build . -t {image-name}

You now built an image with a desired name. In order to create and run a container, you must use the following command :

    docker run -p {host-port}:{container-port} {image-name}

The -p flag orchestrates port-mapping between a container and your virtual machine. In our case, the dockerfile has indicated that the container port is 8000. You can set the host port to any arbitrary port number and use 'curl localhost:{host-port}' to access the web app on your virtual machine. If you are on VS code you can also port map the vm's host port to your local machine to access it on an external browser.


