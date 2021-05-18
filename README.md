# my arduino Data display and alarm

This is an IoT platform developped using flask where people can veiw the temperature, humidity and gaz state

## Overview

Some photos about this project:

![login](/images/login.png)

![regsiter](/images/register.png)

![cards_edit](/images/cards_edit.png)

![card_data](/images/card_data.png)
![DHT11](/images/DHT11.png)
![Humidity](/images/Humidity.png)
![Gaz](/images/Gaz.png)

## Running this app


## As a standalone app
### install python (Optional:Create virtual environment)
1. install [python](https://www.python.org/)
2. `git clone` the project then `cd` into the directory
3. run `virtualenv -p /usr/bin/python3 venv`or `python -m venv venv` to create a virtual environment
4. activate it using `source venv/bin/activate`
5. `pip install -r requirements/base.txt` to install the app libaries and it dependencies
6. you must install mosquitto as mqtt server accept arduino data`apt install mosquitto`

### setting up the databse 

1. you need to have [mysql server](https://www.mysql.com/) installed in your machine, if you are working in linux just typr ` sudo apt-get update && apt-get install mysql-server`
2. type `sudo mysql` to enter to the database
3. app sql config in `.env` `.env-mysql` `app/config/py` `migtatnois/alembic.ini` files
4. example:
5. `sqlalchemy.url = mysql+pymysql://iot_platform:secret@localhost:3306/iot_platform_db`
6. `mysql+pymysql://db_user:db_user_passwd@lP:port/db_name`
7. .....

### run the app

After installing, run the server using `./start.sh`
Access the running app in a browser at the URL written to the console (most likely http://localhost:5000)

### set mail address
You can set the recipient and sender of the alert mailbox in the file `policy/bot.py`

### set nginx web proxy server 
``` bash
# example file
# /etc/nginx/sites-available/arduino-web 
server{
  listen 80;
  server_name 127.0.0.1;  #you ip address or name address
  location / {
    proxy_pass  http://127.0.0.1:5000;
    proxy_set_header Host $proxy_host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  }
}
```

set nginx enable
``` bash
ln -s /etc/nginx/sites-available/arduino-web  /etc/nginx/sites-enabled/
sudo systemctl enable nginx --now
```
