# Noteshub
__Noteshub__ is a simple college project started by a group of freshers to have a convenient way to manage and share notes.
As can be seen, the project has just been started and we're adding stuff to it as we learn.

# Installation
<sub><sup>__Note__: This project uses the Django framework written in Python. So you need a python interpreter on your system.</sup></sub>
### For Linux/MacOS:
+ Clone the repo:
    ` git clone https://github.com/pratik-devkota/noteshub.git`
+ Make a virtual environment. Eg:
    `python -m venv venv`
+ Activate the virtual environment. Eg:
    `source ./venv/bin/activate`
+ Install the dependencies from the repo's requirements.txt file.
    `pip install -r requirements.txt`
+ Run the following code:
    `python manage.py makemigrations && python manage.py migrate`
+ Run the server.
    `python manage.py runserver`
+ Go to the url `localhost:8000` on your browser.

# Objectives
+ The current objective of the project is:
    - to have a system where user can login, register and also upload their own content.
    - to have a page where users can view recent uploads (similar to a blog application) and download the files if provided on that post.

We are planning to group the notes based on the subjects and maybe, <i>in the future</i>, also based on semester.
