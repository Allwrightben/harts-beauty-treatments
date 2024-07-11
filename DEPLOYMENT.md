# Deployment

- The app was deployed to [Heroku](https://www.heroku.com/).
- The app user [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/) to store all the data.

- The app can be reached by the [link](https://beauty-treatments-2d7074a7a100.herokuapp.com).

## Heroku Deployment

### Prerequisites

Before deploying, ensure you have the following installed:

- Git
- Python
- Pip
- Heroku CLI (Download from [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli))

## Local Setup

1. **Navigate to your project directory**:
    ```bash
    cd path/to/your/project
    ```

2. **Create a `requirements.txt` file** to list all dependencies:
    ```bash
    pip freeze > requirements.txt
    ```

3. **Create a `Procfile`** to specify the commands that are executed by the app on startup:
    ```bash
    echo "web: gunicorn <your_project_name>.wsgi:application" > Procfile
    ```
    Replace `<your_project_name>` with the name of your Django project.

4. **Initialize a Git repository** if you haven't already:
    ```bash
    git init
    ```

5. **Add and commit your changes**:
    ```bash
    git add .
    git commit -m "Initial commit"
    ```

6. **Push your code to GitHub**:
    ```bash
    git remote add origin <your_github_repo_url>
    git push -u origin master
    ```

## Heroku Setup

1. **Log in to Heroku**:
    ```bash
    heroku login
    ```

2. **Create a new Heroku app**:
    ```bash
    heroku create <your_app_name>
    ```
    Replace `<your_app_name>` with a unique name for your Heroku app.

3. **Add a PostgreSQL add-on**:
    ```bash
    heroku addons:create heroku-postgresql:hobby-dev
    ```

4. **Set configuration variables**:
    - Go to your app's dashboard on Heroku.
    - Navigate to the "Settings" tab.
    - Click on "Reveal Config Vars".
    - Add `DISABLE_COLLECTSTATIC` with the value `1`.
    - Ensure `DATABASE_URL` is set automatically by Heroku when you add the PostgreSQL add-on.

## env.py file before you deply
- Before you deploy you must make sure that you have a env.py file that store your DATABASE_URL and SECRET_KEY variables. 
- You must also make sure that your env.py file is listed in your .gitignore file otherwise you will be making your private information available to the public potentially leaving yourself open to attack.

## Deploying the App

1. **Connect your Heroku app to your GitHub repository**:
    - Go to the "Deploy" tab in your app's dashboard on Heroku.
    - In the "Deployment method" section, select "GitHub".
    - Search for your repository and connect it.

2. **Enable automatic deploys (optional)**:
    - This will deploy your app every time you push to the specified branch (e.g., `master` or `main`).

3. **Manually deploy your app**:
    - In the "Manual deploy" section, select the branch you want to deploy and click "Deploy Branch".

4. **Monitor the deployment process**:
    - Heroku will display the build and deployment logs.

5. **View your deployed app**:
    - Once the deployment is complete, click the "View" button to open your app.

### Static and Media Files

If your app uses static files, consider using a storage service like AWS S3. Install `django-storages` and configure your settings accordingly.

### Environment Variables

Securely manage sensitive information like secret keys and API keys using Heroku's Config Vars.