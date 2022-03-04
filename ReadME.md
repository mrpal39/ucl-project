##
##pip install django
##pip install git+https://github.com/django-nonrel/django@nonrel-1.5
##pip install git+https://github.com/django-nonrel/djangotoolbox
##pip install git+https://github.com/django-nonrel/mongodb-engine

#pip install pymongo==3.12.3.
#pip install mongoengine
#
#The actual problem is with pymongo==4.0.1. 
#when installing the mongoengine by pip install
#mongoengine it installs the pymongo==3.12.3 So,
#it is not necessary to again install mongoengine 
#just install pymongo==3.12.3 by 
# #pip install pymongo==3.12.3.


# curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -

# apt-key list

# echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

# sudo apt update

# sudo apt install mongodb-org
# sudo systemctl start mongod.service

# sudo systemctl status mongod

# sudo systemctl enable mongod

# mongo --eval 'db.runCommand({ connectionStatus: 1 })'

# sudo systemctl status mongod


# sudo systemctl stop mongod

# sudo systemctl start mongod

# sudo systemctl restart mongod

# sudo systemctl disable mongod

# sudo systemctl enable mongod

