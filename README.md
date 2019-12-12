This is the release page of the sisl graphical interface.

The interface is an extension of the [sisl](https://github.com/zerothi/sisl) visualization module.

How to install it
----

You can run the install.sh script (`. install.sh`), or you can follow this guide to install it step by step and understand what are the requirements.

### Package requirements

There are some packages that need to be installed before installing sisl.

`sudo apt-get update`

`sudo apt-get install gcc gfortran python3-dev python3-pip git`

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

How to run it
---

#### To start producing and managing plots, you need to serve the user interface. 

From the sisl-GUI folder: `serve -s build`

Or more generally: `serve -s /path/to/the/build/folder`

#### And then run the API (inside the virtual environment that you created!):

From the sisl-GUI folder: `python api.py`

Or more generally: `python /path/to/api.py`

The API is the one that looks for files in your filesystem, so it is better to run it from the folder where you have your structures and results.

Helpful aliases to do things fast
---

Additionally, here are some useful aliases you can add to your .bash_aliases file (edit for example with `vi ~/.bash_aliases`). If you add this aliases, you will be able to launch the graphical interface from any folder using just one command.

To easily activate your environment:

`alias sislenv="source ~/.venvs/sislGUI/bin/activate"` or `alias sislenv="source /path/to/venv/bin/activate"`

To run only the GUI: 

`alias gui="serve -s /path/to/the/build/folder"`

To run only the API:

`alias api="sislenv; python /path/to/api.py; deactivate"`

To run both (you will usually use this to launch the GUI):

`alias sislGUI="gui > /dev/null & api && fg"`





