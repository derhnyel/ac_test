

### STARTING UP PROJECT
- Get python installed from [https://www.python.org/downloads/](https://www.python.org/downloads/).

- Check python version `python --version`

- Set up Postgresql Server on your Computer and Get the service Running. 

- On Windows You can Download the PgAdmin Application [https://www.pgadmin.org/download/](https://www.pgadmin.org/download/)
 
- Create a database with the name hackernewsdb. 

- You could use any other name as your database name but remember to update the "DATABASE" variable in the django projects 'settings.py' file.

- Connect to the Postgres database.

- A Virtual Machine was shipped with this project Activate on Windows with ,

- Navigate into the project directory via your terminal (newsaggregator directory should be your root directory).

- Install the requirements by typing the command  `pip install -r requirements.txt` in yout terminal

- Run make Migrations on hackernews_engine app using command `python manage.py makemigations` . 

- Run Migrations with command `python manage.py migrate` .This will migrate all created models to the postgres db

- Start server and run application with command `python manage.py runserver`

- The app is built using Django so this command Runs the app in Development mode. Open [http://localhost:8000](http://localhost:8000) to view it in the browser. The page will reload if you make edit to the scripts. To turn this feature off use the "--noreload" `python manage.py runserver --noreload`

#### NOTE
    At first, running the page takes a while(around 2minutes) to load since the database is empty and has to be populated.
    After the initialization all these do not happen, the page loads normally with all resources available on it. 
    I would advice aganst using the django default sql database because it has lock that makes it process one request at a time thereby preventing concurrent requests.   

### API Call

#### Response Type
- You get a Json Response From the Api.

#### Request Format

- Interact with the restapi from your browser using this url format [http://localhost:8000/api](http://localhost:8000/api) 

- **story**   
You can query the Api using this format [http://localhost:8000/api?story=your_story_query](http://localhost:8000/api/?story=your_story_query) (`restricted your_story_query can only be integers`) with story your query based on the number of top stories to be returned. This returns the result of word occurences in the titles from those top stories.
- **day**   
You can query the Api using this format [http://localhost:8000/api?day=your_day_query](http://localhost:8000/api/?day=your_day_query) (`your_day_query can only be integers`) with your day query based on the number of days ago of which the item was created. This returns the result of word occurences from the top stories titles of that particular day.
- **word**   
You can query the Api using this format [http://localhost:8000/api?word=your_word_query](http://localhost:8000/api/?word=your_word_query) (`your_word_query can only be integers`) with your word query. It return the number of words specified sorted by thier frequent occurence in the title in top stories.
- **score**   
You can query the Api using this format [http://localhost:8000/api?score=your_score_query](http://localhost:8000/api/?score=your_score_query) (`your_score_query can only be integers`) with a query based on the items karma. It returns the words with the highet word occurence in the title of top stories with the karma/score/rating specified.

#### NOTE
    - The Query's can be combined with each other using `&` in any manner to get desired result. 
    - For Example : To get the words with the highest frequency of occurence from top 10 words from top 25 stories you could use the url format http://localhost:8000/api/?story=25&word=10 .
    - If you want to get words with the highest frequency of occurence from just the stories with greater than or equal 10 karmas you could modify the url to something like http://localhost:8000/api?story=25&word=10&score=10 .
    - You could further extend the query to get words with the highest frequency of occurence from the stories from 2 days ago. The url format will be http://localhost:8000/api?story=25&word=10&score=10&day=2.



