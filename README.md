# atc_myproject Deployment guidelines

1. Launch instances
2. select ubuntu os
3. select t2.micro
4. create existing key pair
5. under security groups add ssh,http,https
6. under security tab in instance click on security group and edit inbound rule and add your port 8000 for tcp and allow 0.0.0.0/0
7. go to elastic ip service > allocate elastic ip address > create > go to created ip > click on associate elastic ip> select which instance you want to allocate
8. connect to instance
9. connect to server either through filezilla or winscp using public ip address
10. go to file in filezilla > sitemanager > add new site > set protocol to sftp > host is public ip > logon type is key file > user is ubuntu > select pem file of keypair
11. change ip address in api url under static > js > main.js file > search for apiurl and paste public address of server and copy myproject folder to ubuntu (check the main file should be on myproject.py and wsgi file should call from myproject)

sudo apt update
sudo apt install nginx -y
sudo ufw app list
sudo ufw allow 'Nginx Full'
sudo ufw allow ssh
sudo ufw enable 
systemctl status nginx 
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
sudo apt install python3-venv
cd ~/myproject
python3 -m venv myprojectenv
source myprojectenv/bin/activate
pip install wheel
pip install -r requirements.txt
sudo ufw allow 8000
gunicorn --bind 0.0.0.0:8000 wsgi:app

> check whether theapp is running or not by typing <public ipaddress>:8000
> if working stop the gunicorn server

deactivate

sudo nano /etc/systemd/system/myproject.service
> copy below text (ctrl+x to exit it will ask to save click on y and click enter)
[Unit]
Description=Gunicorn instance to serve myproject
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/myproject
Environment="PATH=/home/ubuntu/myproject/myprojectenv/bin"
ExecStart=/home/ubuntu/myproject/myprojectenv/bin/gunicorn --workers 1 --bind unix:myproject.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target

sudo systemctl start myproject
sudo systemctl enable myproject
sudo systemctl status myproject

sudo nano /etc/nginx/sites-available/myproject
> copy below text (ctrl+x to exit it will ask to save click on y and click enter)
server {
    listen 80;
	server_name <ipaddress>;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/myproject/myproject.sock;
    }
}

sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled (if this steps throws error > sudo rm /etc/nginx/sites-enabled/myproject and try same step again)
sudo nginx -t
sudo ufw delete allow 8000
sudo chmod 755 /home/ubuntu
sudo systemctl restart nginx
> type your public ip in chrome and check whether the server is up or not
