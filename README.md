# Python_BI_2022

OS version: Ubuntu 22.04.1 LTS

Python version: python 3.11. 

Make sure, that `python3.11-dev` and `pipenv` are installed. Otherwise, run the commands:
```
sudo apt-get install python3.11-dev
pip install --user pipenv
PATH=$PATH:/home/user_name/.local/bin
```
Instruction:

1. Download file `ultraviolence.py`

```
wget https://github.com/krglkvrmn/Virtual_environment_research/blob/master/ultraviolence.py?raw=true
```

2. Rename file:

```
mv 'ultraviolence.py?raw=true' ultraviolence.py
```

3. install required libraries:

```
pipenv install pandas==1.4.4
pipenv install numpy
pipenv install requests
pipenv install google-cloud
pipenv install google-cloud-vision
pipenv install Bio
pipenv install aiohttp
pipenv install opencv-python
pipenv install lxml
```

4. Run the script:
```
pipenv run python3 ultraviolence.py
```
