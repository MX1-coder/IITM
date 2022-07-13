# IITM

Project technical stuff-
Dashboard-
Step 1) 
 install python globally-With this link python officially site
https://www.python.org/
python version    -   3.10.4
django version Django==4.0.4
install django using command line-
$pip install django==4.0.4

Open the project folder and create the virtual environment

Step -2 
create virtual enviroment by command line
first start the Powershell
python -m venv virtual_envorment_name
$python –m venv venv
Start the virtual envorment by using this command
$venv\Scripts\activate

After start the virtual envorment install the all required libraries using by command line
(venv) PS C:\Users\Admin\Desktop\dashboard1>pip3 install -r requirements.txt
Start the mysql localserver 
create the database name of ----‘dashboard’
after that follow the command
$python manage.py makemigrations
$python manage.py migrate
Start the server-
$python manage.py runserver

System check identified 0 issue (0 silenced).
May 31, 2022 - 16:37:38
Django version 4.0.4, using settings 'dashboard.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
Run this server in your browser
http://127.0.0.1:8000/ 
