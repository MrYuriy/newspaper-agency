# NEWSPAPER AGENCY 

is a project aimed at assisting a team of editors in their efforts to produce content for various newspapers. 
The platform allows editors to register and create personal profile pages that can only be accessed by authenticated users. 
These pages serve as a space for editors to highlight their work and share background information about themselves. 
This helps to streamline the editorial process and ensure that content is consistent and of high quality.

Redactors have exclusive access to create, update, and delete their own newspaper.
However, all users of the site, including non-registered users, are able to read the newspaper.

The website includes a variety of topics for newspaper, which are listed on a separate page for easy navigation. 
By clicking on a single topic, all relevant newspaper associated with that topic will be displayed.

### Running project locally

To run this projects locally, use the following steps:

1. Clone repo from GIT:

`git clone https://github.com/MrYuriy/newspaper-agency.git`

2. If you are using PyCharm - it may propose you to automatically create venv for your project 
and install requirements in it, but if not: 

```python
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

3. Run the migrations:

`python manage.py migrate`

4. Use the following command to load prepared data from fixture:
  
`python manage.py loaddata newspaper_db.json`

Upon loading data from fixture you can use following superuser (or create another one by yourself):
  - Login: `yurii.admin`
  - Password: `1qazcde3`

### Environment variables
   
The secret key to this project is saved within .env file, which is hidden.
You can create your own `.env` file to store your `SECRET_KEY`, `DB_NAME` and other environment 
variables like it is shown in `.env_sample` file. 


Feel free to add more data using admin panel, if needed.
![Website Interface](demo.png)
