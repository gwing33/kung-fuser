# Kung Fuser

## Initial Setup

- Clone the Repo into your directory then in a terminal cd into the location

<code>cd /your/location/to/kung_fuser/</code>

- Copy local_settings.py.template

<code>cp local_settings.py.template local_settings.py</code>
 
- Configure local_settings.py to your local DB settings
- Run the syncdb command (Will probably be asked to create a super user...)

<code>python manage.py syncdb</code>

- Start Server

<code>python manage.py runserver</code>

- Should be started at http://127.0.0.1:8000/
- To see the admin section just append 'admin' on to that