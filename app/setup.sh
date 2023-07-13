sudo apt update -y 
sudo apt upgrade -y
sudo apt install python
sudo apt install pip

#sudo /usr/local/bin/python -m pip install --upgrade pip
sudo pip install --no-cache-dir --upgrade -r requirements.txt --target=/app/appRequirements
#export PYTHONPATH=/app/appRequirements

git config --global user.name "mario-69-mario"
git config --global user.email mario-69-mario@nel.id.au