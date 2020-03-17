This is the release page of the sisl graphical interface.

The interface is an extension of the [sisl](https://github.com/zerothi/sisl) visualization module.

How to install it
----

### If you don't have sisl installed

Install sisl in a virtual environment by following this instructions:

#### Building a virtual environment

The best way to install all the python packages needed is to create a virtual environment.
In this way, it won't affect any of the other python installations in your computer.
Furthermore, you will be able to remove the virtual environment by just removing the folder and your system won't be affected.

`sudo apt-get install python3-venv && python3 -m venv ~/.venvs/sislGUI`

Then, to enter your virtual environment:

`source ~/.venvs/sislGUI/bin/activate`

#### Installing sisl

At the current moment, the sisl GUI implementation is still under developement. To keep up with changes, we recommend that you clone the repository and then install sisl from that folder in developement mode, like so:

```
git clone -b GUI https://github.com/pfebrer96/sisl.git
cd sisl
pip install -e .
```

### After installing sisl

#### Install GUI dependencies

Inside the environment, install the additional dependencies that the interface has:

`pip install flask flask-restplus flask-cors`

#### Download the GUI

Since the GUI itself is also under developement, we recommend you to clone the repository too, instead of downloading:

`git clone https://github.com/pfebrer96/sisl-GUI.git`

And with this, you are all set up!

How to run it
----

Easy, just run the `sislGUI` file that you will find in the folder. You can run it from wherever you want, no need to be inside the directory.

`
path/to/sislGUI/executable
`

*Disclaimer*:You might need to make the file executable first:

`
chmod +x path/to/sislGUI/executable
`

**Enjoy!**





