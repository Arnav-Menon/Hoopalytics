# Hoopalytics

# Application Setup
Please follow the instructions below, from top to bottom sequentially, to ensure that you are set up to run the app. The app is run on an Angular frontend, Django backend, and a PostgreSQL database.

## Set up database
1. Download and install PostgreSQL from https://www.postgresql.org/download/
2. Ensure PostgreSQL is running, and in a terminal run
    ```
    createuser hooper --createdb;
    createdb hoops;
    ```
3. connect to the hoops database to grant permissions `psql hoops`
    ```
    create schema app;
    alter user hooper with password 'basketball';
    grant all on schema app to hooper;
    ```


## Backend

### 1. Install pyenv and virtualenv

Read about pyenv here https://github.com/pyenv/pyenv as well as info on how to install it.
You may also need to install virtualenv in order to complete step 2.

### 2. Installing Prerequisites
The steps below attempt to install Python version 3.10.1 within your pyenv environment. If you computer is unable to install this particular version, you can feel free to use a version that works for you, but note that you may also be required to update existing parts of the codebase to make it compatible with your installed version.
```
cd root/of/project
pyenv install 3.10.1
pyenv virtualenv 3.10.1 venv
pyenv local venv
eval "$(pyenv init -)" (may or may not be necessary)
pip install -r backend/requirements.txt
```

### 3. Starting the Backend
Start the backend by running the following commands
```
cd /path/to/project/backend
python manage.py runserver
```
The backend should run on http://localhost:8000/.


## Frontend

### 1. Installing Prerequisites
Install Node.js (16.x.x), then run the following commands
```
cd /path/to/project/frontend
# Install Angular-Cli
npm install -g @angular/cli@12.1.0 typescript@4.6.4 --force
# Install dependencies
npm install --force
```

### 2. Starting the Frontend
Start the frontend by running the following commands
```
cd /path/to/project/frontend
npm start
```
The frontend should run on http://localhost:4200/. Visit this address to see the app in your browser.
