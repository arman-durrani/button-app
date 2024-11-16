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


 