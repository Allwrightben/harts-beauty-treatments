# Deployment

- The app was deployed to [Heroku](https://www.heroku.com/).
- The app user [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/) to store all the data.

- The app can be reached by the [link](https://beauty-treatments-2d7074a7a100.herokuapp.com).

## Heroku Deployment

* Set up a local workspace on your computer for Heroku:
    - Create a list of requirements that the project needs to run:
      - type this in the terminal: `pip3 freeze > requirements.txt`
    - Commit and push the changes to GitHub
    
* Go to [www.heroku.com](www.heroku.com) 
* Log in or create a Heroku account.
* Create a new app with any unique name.

* Create a Procfile in your local workplace:    
    This file will will contain the following:
    ```python
        web: gunicorn <name app>.wsgi:application
    ```
* Commit and push the changes to GitHub.

* Go to resources in Heroku and be sure you are using an eco-dyno.

* Go to the settings app in Heroku and go to Config Vars. be sure you have DISABLE_COLLECTSTATIC set to '1'
* Go to the settings app in Heroku and go to Config Vars. be sure you have your DATABASE_URL with your database URL.
* go to the Heroku Deply tab and for the deployment method select githun and connect to your repo.
* Finally, scroll down to "deploy branch" and click. You will get feedback regarding the deployment as Heroku goes through your files. Once complete, click "View" to view your deployed app. 