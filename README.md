

### STARTING UP PROJECT
- Get python installed.

- Check python version
###### In the project directory, you can run:
###### `python --version` 
###### "check python version"

- Set up Postgresql Server on your Computer and Get the service Running.
 
- Create a database with the name hackernewsdb. 
###### "You could use any other name but remember to update the DATABASE in the projects settings.py file to that name."

- Connect to the Postgres database.

- A Virtual Machine was shipped with this project Activate on Windows with ,
###### `path_to_project_directory/hackernews/news/Scripts/activate.bat` 
###### "Start virtual machine on windows"

- Or create a virtual environment 
###### `pip install venv` 
"Install virtualmachine package"
Navigate to your desired virtual environment path and run command
###### `venv nameofvirtualenv`
###### "Create new virtual machine"

- Navigate into the project directory via terminal (newsaggregator directory should be your root directory).

- If you created a new virtual machine run command 
###### `pip install -r requirements.txt`
###### "Required libaries installed"
###### This will install the the neccesarry libaries needed to run the application on your machine. 

- Run make Migrations on hackernews_engine app using command 
###### `python manage.py makemigations`

- Run Migrations with command 
###### `python manage.py migrate`

- Start server 
###### `python manage.py runserver" : "python-scripts start"`,
###### The app is built using `Django` so this command Runs the app in Development mode. Open [http://localhost:8000](http://localhost:8000) to view it in the browser. The page will reload if you make edits. 
###### To turn this feature off use the --noreload 
###### `python manage.py runserver --noreload`
###### "Python-script starts with noreload"
###### You will also see any lint errors in the console.

- You can hover over items on the webpage to view thier text.

- The default home page is the New stories page.
#### NOTE
    At first, running the page takes a while(around 2minutes) to load since the database is empty and has to be populated.
    After the initialization all these do not happen, the page loads normally with all resources available on it. 
    I would advice aganst using the django default sql database because it has lock that makes it process one request at a time thereby preventing concurrent requests.   

### MAKING API REQUESTS
containing JSON data.

#### API Calls Locally

- Interact with the rest_api from browser using [http://localhost:8000/api](http://localhost:8000/api)
- **GET** 
Query the Api  [http://localhost:8000/api](http://localhost:8000/api) with a `GET` request why which ever query parameter
- **GET?story**   
You can also query the Api [http://localhost:8000/api?story=story&](http://localhost:8000/api/?story=story) <restricted to integers> with a `GET` request and a query based on the number of top stories to return the result of word occurences from those stories.
- **GET?day**   
You can also query the Api [http://localhost:8000/api?day=day&](http://localhost:8000/api/?day=day) <restricted to integers> with a `GET` request and a query based on the number of days of which the item was created to return the result of word occurences from the stories of that day.
- **GET?word**   
You can also query the Api [http://localhost:8000/api?word=word&](http://localhost:8000/api/?word=word) <restricted to integers> with a `GET` request and a query based on the number of top word with the highest frequency. to be returned.
- **GET?=score**   
You can also query the Api [http://localhost:8000/api?score=score&](http://localhost:8000/api/?score=score) <restricted to integers> with a `GET` request and a query based on the items karma it return the highest word occurence in the title of the karma specified.


