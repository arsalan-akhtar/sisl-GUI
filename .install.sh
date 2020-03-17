# DON'T USEEEEE PLEASE
# IT DOESN'T WORK RN

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

