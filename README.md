# Kung Fuser

## Initial Setup

Install VirtualBox and Vagrant:

- https://www.virtualbox.org/
- http://vagrantup.com/

Clone the repo and cd into it.

<code>cd /path/to/cloned repo</code>

Build your VM server...

<code>vagrant up</code>

SSH into it...

<code>vagrant ssh</code>

Go into the python folder...

<code>cd /vagrant/src/python/</code>

Run the server on port 8000

<code>python manage.py runserver 0.0.0.0:8000</code>