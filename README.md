log into server ssh -i ~/.ssh/linuxCourse.pem ubuntu@your_ip_address_here
1 update server
$ sudo apt-get update

1.5 install finger
$ sudo apt install finger

2 create new user
$ sudo adduser grader
  check if user was created
  $ finger grader

3 give grader sudo access
$ sudo cp /etc/sudoers.d/90-cloud-init-users /etc/sudoers.d/student
 now vim into file and replace the user (ubuntu) with (student)
 $ sudo vim /etc/sudoers.d/student

4 generate keypair for grader user
  go to local terminal
  $ ssh-keygen
  add folder directory
  $ /Users/col/.ssh/linuxCourse
 modify key file
 $ chmod 600 /Users/col/.ssh/linuxCourse.pem

5 add public key to server
  Sign in to linux server as grader user and enter password
  $ su - grader
  create folder
  $ mkdir .ssh
  create a file within .ssh directory
  $ touch .ssh/authorized_keys
  add /Users/col/.ssh/linuxCourse.pub file/key from local terminal to linux server
  $ vim .ssh/authorized_keys

6 add file permissions to key file
 $ chmod 700 .ssh
 $ chmod 644 .ssh/authorized_keys

7 now you can log in as grader with the linuxCourse pub file/key
$ ssh -i ~/.ssh/linuxCourse grader@your_ip_address_here

8 forcing key based authentication on linux server
search for the line that says PasswordAuthentication and change the value to (no) and         remove the (#)
$ vim /etc/ssh/sshd_config
   
  restart service
  $ sudo service ssh restart

9 add custom port 2200 to https://lightsail.aws.amazon.com/ls/webapp/us-east-2/instances/Ubuntu-512MB-Ohio-1/networking
  search for port 22 and remove (#) and add new line for port 2200
  $ vim /etc/ssh/sshd_config
  open another terminal
  $ ssh -i ~/.ssh/linuxCourse -p 2200 grader@your_ip_address here

10 configure ufw 
$ sudo ufw allow 2200/tcp
$ sudo ufw allow 80/tcp
$ sudo ufw allow 123/udp
$ sudo ufw enable

11 log in to linux terminal in another window
  $ ssh -i ~/.ssh/linuxCourse -p 2200 grader@Your-ip-address-here

12 configure time zone to chicago
$ sudo dpkg-reconfigure tzdata

13 configure sync to other servers
$ sudo apt-get update 
$ sudo apt-get install ntp

14 install apache and mod wsgi and psycopg2
$ sudo apt-get install apache2
$ sudo apt-get install libapache2-mod-wsgi python-dev
$ sudo apt-get install postgresql python-psycopg2

15 enable wsgi
$ sudo a2enmod wsgi

16 start up apache
$ sudo service apache2 start

17 setup git
$ sudo apt-get install git
    setup username
    $ git config --global user.name “username here”

    check username

    $ git config --global user.name

    setup email

    $ git config --global user.email “user email here”
    check email

    $ git config --global user.email



18 installs

$ sudo apt-get install python-pip 
$ sudo pip -H install Flask 
$ sudo -H pip install sqlalchemy
$ sudo apt-get install postgresql postgresql-contrib
19 check if no remote connections allowed and make sure it says local
$ sudo vim /etc/postgresql/9.5/main/pg_hba.conf
  log in to postgres
  $ sudo su - postgres

  log in to shell
  $ psql
  
  create database
  $ CREATE DATABASE catalog;
 
  create user catalog
  $ CREATE USER catalog;

  create password for user catalog
  $ ALTER ROLE catalog WITH PASSWORD ‘insert your password address here’;
  
  giver user catalog access to catalog database
  $ GRANT ALL PRIVILEGES ON DATABASE catalog TO catalog;

  log out of postgres
  $ \q
  $ exit
  
20 project setup
$ cd /var/www

make flask app directory
$ sudo mkdir FlaskApp

change directory to FlaskApp
$ sudo cd /FlaskApp

clone github repo with project
$ sudo git clone https://github.com/zach-col/itemCatalog.git

change github repo project name to FlaskApp
$ sudo mv itemCatalog FlaskApp

change directorys to flask app
$ cd FlaskApp

install freeze for package management
$ sudo pip freeze

instal all needed python packages in packages.txt file
$ sudo pip install -r packages.txt
change application.py file to __init__.py
$ sudo cp application.py __init__.py
$ sudo rm -rf application.py

update sql path create engine for  __init__.py and database_setup.py and lotsOfCatalogs.py to 
$ engine = create_engine('postgresql://catalog:catalog123@localhost/catalog')

update client_secret path in __init__.py file on line 26 to 
CLIENT_ID = json.loads(

    open('/var/www/FlaskApp/FlaskApp/client_secrets.json', 'r').read())['web']['client_id’]

$ sudo vim __init__.py

edit clientsecret.json fil and add client secret api from google make sure it has 
add this to origins
http://localhost:8000
http://[your_ip_address_here].xip.io

add this to redirects
http://localhost:8000/disconnect
http://localhost:8000/catalogs
http://localhost:8000/gconnect
http://your_ip_address_here.xip.io
http://your_ip_address_here.xip.io/disconnect
http://[your_ip_address_here].xip.io/catalogs
http://[your_ip_address_here].xip.io/gconnect
$ vim clientsecret.json

add client id to templates/googleSignIn.html on line 13
$ vim templates/googleSignIn.html

create file for virtual host and add this code
<VirtualHost *:80>
		ServerName your_ip_address_xip.io
		ServerAdmin youremail@example.com
		WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
		<Directory /var/www/FlaskApp/FlaskApp/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/FlaskApp/FlaskApp/static
		<Directory /var/www/FlaskApp/FlaskApp/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
$ sudo vim /etc/apache2/sites-available/FlaskApp.conf

reload apache
$ sudo service apache2 reload

enable virtual host
$ sudo a2ensite FlaskApp

create .wsgi file used to server Application
$ cd /var/www/FlaskApp

$ vim flaskapp.wsgi
add this code to flaskapp.wsgi
#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")
from FlaskApp import app as application
application.secret_key = ‘INSERT_YOUR_SUPER_SECRET_From__init__.py’

restart apache
$ sudo service apache2 restart

change directory to inner flask app

setup database
 $ python database_setup.py this will setup the database
add data to the database
$ sudo python lotsOfCatalogs.py
run the application
$ python __init__.py
Setup Google OAuth

download json file and replace current json file at client_secret.json

vim FlasApp.conf and change servername to [your_ip_address_here.xip.io]


restart apache
$ sudo service apache2 restart
