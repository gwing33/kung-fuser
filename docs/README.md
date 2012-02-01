# Environemnt & Repository Structure

This is designed to closely follow the [Filesystem Hierarchy Standard][FHS] when
possible for consistency and clarity with Linux-based environments.

I have Ted Kaemming to thank for this.

* /*virtualenv*: a python virtual environment
    * /repository: source code repository
        * /bin: shell scripts
            * svd: wrapper for supervisord
            * svctl: wrapper for supervisorctl
        * /config: configuration files
            * /fabric: fabfiles
            * /requirements: pip requirements files
                * requirements.pip: requirements used on all environments
                * requirements.development.pip: requirements used only in development (debugging tools and the like)
            * /supervisord: supervisord requirements
                * supervisord.conf: environment-agnostic supervisord configuration
                * /includes: files for inclusion by environments (similar to ubuntu's 'sites-available' pattern. you can think of this as 'includes-enabled')
                * /environments:
                    * /development: development environment configuration
                        * supervisord.conf: environment-aware supervisord configuration
                        * includes/: included configuration files (similar to ubuntu's 'sites-enabled'). these should be a symbolic link to ../../includes/*filename*
                    * /production: production environment configuration, see development environment
            * other application configuration directories can be in here, /postgres, /nginx, /solr, etc.
            * compass.rb: compass configuration file
        * /doc: project documentation
        * /fixtures:
            * initial_data.json: should only contain sites.Site fixtures
            * /development
                * initial_data.json: all fixtures tht should be loaded by default in development environments
        * /src: source files
            * /assets: static assets
                * /.build: temporary build directory. these files are not versioned, and only used for serving in development. (they will be copied to /var later, or deployed to a CDN)
                * /images
                    * /sprites: images/icons that will be combined into sprite files
                    * /vendor: vendor (third-party) images from plugins, etc.
                * /fonts
                * /javascripts
                    * /vendor: vendor (third-party) libraries and dependencies
                * /sass
                    * /vendor: vendor (third-party) libraries and dependencies
            * /javascript: server-side (node.js) javascript
            * /python: python source files
                * /*project*: a django project
                    * /settings
                        * defaults.py: settings inherited by all environments
                        * development.py: development settings
                        * production.py: production settings
                    * /templates: project-specific templates
                        * base.html: the base template for the project, should be inherited by all others
                    * /utils: module for all non-app related bits (pagination helpers, context processors, templatetags)
                    * wsgi.py: wsgi file
        * /var
            * /media
                * /fixtures: fixture data for user-uploaded media (use sparingly)
    * /tmp: temporary files, not persisted in any fashion, may be deleted on reboot
    * /var: variable data, not versioned but reasonably consistent (in production this is outside of the virtualenv and symlinked to, shared by all deployments)
        * /lock: lockfiles: see `lockfile(1)`
        * /log: log files
        * /mail: output for mail files in development
        * /media: media (asset files, but not required or provided by application code)
            * /fixtures: symlink to `$VIRTUAL_ENV/repository/var/media/fixtures` for fixture data
            * /uploads: user uploaded data
        * /postgres: database cluster, created with `initdb`
        * /run: pid files, sockets, and other runtime data
        * /spool: application spool (buffer) data
            * /nginx: nginx temporary files (request body, etc.)
        * /static: collection point for static files (may not be served from this directory, instead a CDN)
    * /vendor: other dependencies (solr, etc) (in production this is outside of the virtualenv and symlinked to, shared by all deployments)

# Service-Style Layout

used for deployment, usually located in `/srv`

* /*name* (something like "reviewgallery.com")
    * /deployments
        * /current: currently active version, symlink to ../versions/*hash*
        * /previous: symlink to previous deployed version for quick rollbacks
    * /versions
        * /*hash*: virtualenv containing the repository clone with head named by *HASH*
            * /var: symlink to $SERVICE_DIR/var
            * /vendor: symlink to #SER_VICE_DOR/vendor
    * /var: see above (deployments symlink to this directory rather than use their own)
    * /vendor: see above (deployments symlink to this directory rather than use their own)

[FHS]: http://www.pathname.com/fhs/pub/fhs-2.3.html