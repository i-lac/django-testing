# Running the server
## Set up your virtual environment
The instructions for doing so are available [here](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/development_environment#using_django_inside_a_python_virtual_environment). The Ubuntu instructions are wrong(? I think) if you are on Ubuntu 24.04.4 LTS. because.

Follow the instructions under the "Using Django inside a Python virtual environment" and "Creating a virtual environment" headers.

Do so to ensure a consistent dev environment between python projects (I'm pretty sure).

## Install packages

Run the following in your terminal to install the required packages for this project:
```bash
pip install -r requirements.txt
```
I think this works cross-platform... LMK if it does not work for you. You may need to append `python3 -m` on Mac or `py -3 -m` on Windows to the command.

If you ever install something else load-bearing on this or another python project, you can run the following to extract the packages required for the project into a `requirements.txt` file:

```bash
pip freeze > requirements.txt
```
