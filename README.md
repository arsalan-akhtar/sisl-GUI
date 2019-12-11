This is the release page of the sisl graphical interface.

The interface is an extension of the [sisl](https://github.com/zerothi/sisl) visualization module.

How to install it
----

You can run the install.sh script (`sh install.sh`), or you can follow this guide to install it step by step and understand what are the requirements.
 
### Package requirements

There are some packages that need to be installed before installing sisl.

`sudo apt-get update`

`sudo apt-get install gcc gfortran python3-dev python3-pip git`

`sudo apt-get install git`

### Virtual environment

The best way to install all the python packages needed is to create a virtual environment.
In this way, it won't affect any of the other python installations in your computer.
Furthermore, you will be able to remove the virtual environment by just removing the folder and your system won't be affected.

`sudo apt-get install python3-venv && python3 -m venv ~/.venvs/sislGUI`

Then, to enter your virtual environment:

`source ~/.venvs/sislGUI/bin/activate`

### Python packages

Once inside your environment, install all the python packages required

`pip install wheel`

Installing sisl:

`pip install git+https://github.com/pfebrer96/sisl.git`
`pip install tqdm plotly pandas pathos`

Installing flask, for the python api that the GUI uses:

`pip install flask flask-restplus flask-cors`

###  Install the graphical interface

Install nodejs and the node package manager (required for the GUI backend):

`sudo apt-get install nodejs npm`

Install the serve package to serve the GUI:

`sudo npm install -g serve`

