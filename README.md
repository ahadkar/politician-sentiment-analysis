# politician-sentiment-analysis

## Summary

This is a project for UIUC CS410 Text Retrieval and Analysis class.

In this project we extract meaningful topics from a corpus of tweets for US politicians to create topic model. Futher we analyze the topic coverage for each politician's corpus of tweets. The tweets are then analyzed for positive/ negative/ neutral sentiment.

**This project requires Python3 to run.**

## Required Python Frameworks

* [Django](https://www.djangoproject.com/)
```bash
pip install django
```

VirtualEnv is also required to run the virtual environment. You can install this by using:
```bash
pip install virtualenv
```

## Running the app

1. Clone or download the repository files.
2. [Download the database](https://drive.google.com/file/d/1SjLypL6uYzSoWR9cRzZLVypzbfGrnJiX/view?usp=sharing) required to run the app.
3. Navigate to the project directory **politician-sentiment-analysis** and run the following command to activate the virtual environment.

```bash
source env/bin/activate
```

4. You will see the command prompt with the environment name **env**.

```bash
env
```

5. Use ```cd psa_app``` to navigate to the psa_app sub directory.

6. Next, enter the following command to start the runserver for the environment.

```bash
python manage.py runserver
```

7. On a successful build the command prompt will print:

```bash
System check identified no issues (0 silenced).
November 21, 2018 - 22:03:33
Django version 2.1.3, using settings 'psa_app.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

8. Finally, start the development server by going to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
