# Django Installation
## How to install Django?
> pip install django

## Virtual environments
What if I need a different version of Django for each Django project. And inside of those projects we need some particular packages ~And not in our computer~. We use **Virtual environments**.

A virtual environment it's like a little box where everything your project is stored in. "mini-environment".

### How to create Virtual environments?
1. Install a virtual environment. In this project we are using **Virtual env wrapper**:  
    `pip install virtualenvwrapper-win`
    > Note from the author: Im going to leave **my steps** because, unfortunately, the tutorial is for windows ~zzz...~. So yeah, I'm using venv. What could possibly go wrong?.  
    > So yeah, you alredy have virtual environments. It's called `venv`. Here it's the (https://docs.python.org/3/library/venv.html)[documentation]

2. Create a virtual environment and give it a name:  
    `mkvirtualenv [NAME_OF_VIRTUAL_ENVIRONMENT]`
    > `python3 -m venv /path/to/new/virtual/environment]` I reccomend you using sudo... ¿Is that okay? 🤔.

3. Activate the virtual environment: We already did it with the last step. You should see (myapp) in the console
    > I didn't: `source <venv>/bin/activate`. You should see (myapp) in the console.
    > Btw, the last command is for linux. And I use Arch btw.

4. Now, everithing you write in that command line (`(myapp)`) is going to be in the virtual environment. We are installing Django again.
    > The same that the man said. I support it 👍.

### Deactivating virtual environment
Type `deactivate`
> He's right.

### Opening virtual environment in Visual Studio Code
Type `workon [NAME_OF_VIRTUAL_ENVIRONMENT]`
> This is how you have to do it `source <venv>/bin/activate`

------------------------------------------------------------------
## Creating a project
Insert the next command line with the name `myproject`:  
`django-admin startproject [NAME_HERE]`
And now you have a folder called `myproject`!

## Files inside a Django project
- **manage.py:** Settings file for Django. *Don't touch it*.
- **__init__.py:** ---
- **asgi.py:** ---
- **settings.py:** Bedrock of our whole project. 
- **urls.py:** Where we specify all the URLs we want in our project.
- **wsgi.py:** ---

## Running a project
Insert the next command line for running our project in our localhost:  
`python manage.py runserver`  

Where it says `Starting development server at [PORT]`, that's where our project is running.

