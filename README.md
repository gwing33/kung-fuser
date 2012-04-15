# Kung Fuser

## Initial Setup with RVM

- Install RVM (http://beginrescueend.com/)
- Install VirtualBox (https://www.virtualbox.org/)

Clone the repo and cd into it.

<code>cd /path/to/cloned_repo</code>

It should prompt you to use rvmrc file, say "yes", then bundle install

<code>bundle install</code>

Build VM Server (see below)


## Initial Setup without RVM

Install VirtualBox and Vagrant:

- https://www.virtualbox.org/
- http://vagrantup.com/

Clone the repo and cd into it.

<code>cd /path/to/cloned repo</code>

Build VM Server (see below)


## Build your VM Server and Run the project
<code>vagrant up</code>

SSH into it...

<code>vagrant ssh</code>

Go into the python folder...

<code>cd /vagrant/src/python/</code>

Run the server on port 8000

<code>python manage.py runserver 0.0.0.0:8000</code>

In a browser you'll be able to access the site at http://33.33.0.10:8000/

## Working with styles

Don't modify the css files, instead from this location, run compass and modify the files in the src/assets/sass/ folder...

<code>cd /path/to/cloned_repo</code>

<code>compass watch</code>