# ajax-django-CRUD
Simple django book library showcasing CRUD operations with ajax

App Demo : https://ajax-library.herokuapp.com/

CRUD operations form basics for database operations at backend. Conventional django apps results in page reload after http methods such as 'POST' and 'GET'. To overcome this and for providing more immersive User experience we can use ajax along with jquery for posting data to server. 

# Configuration

run pip install -r requirements.txt  ----  For installing dependencies

To avoid sensitive info such as SECRET_KEY,DB details etc being public, project uses a third party module called python-decouple, python-decouple imports data from env variables. 
For using python decouple define a '.env' file in project root and populate them with these values

ALLOWED_HOSTS=127.0.0.1
DEBUG = True
SECRET_KEY = //generated secret key//

if you are using prod DB define below values as well

DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_HOST=''

On deployment you can define the environment variables directly in dashbord of platform, in my case , heroku dashboard

# Execution

Run 'python manage.py runserver' 

