sudo apt-get update
sudo apt-get install gcc gfortran python3-dev python3-pip
sudo apt-get install git

#-------------------------------------------
#       Create a virtual environment
#-------------------------------------------
sudo apt-get install python3-venv && python3 -m venv ~/.venvs/sislGUI
source ~/.venvs/sislGUI/bin/activate

#-------------------------------------------
#     Install all the python packages
#-------------------------------------------
pip install wheel

#Sisl
pip install git+https://github.com/pfebrer96/sisl.git
pip install tqdm plotly pandas pathos

#Flask (for the api)
pip install flask flask-restplus flask-cors


#-------------------------------------------
#    Install the graphical interface
#-------------------------------------------

#Install nodejs
sudo apt-get install nodejs npm

#Install the serve package to serve the GUI
sudo npm install -g serve
