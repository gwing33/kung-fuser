# TODO: When get to deploy server, probably should get something like this set up - via Ted Kaemming
require 'rubygems'
require 'bundler/setup'
 
require 'susy'
# require 'starterkit'
 
project_path = 'src/assets'
 
# environment is a method, not a symbol by default
environment = environment().nil? ? :development : environment()
 
http_path = (environment.equal? :development) ? '/static/' : '/'
# build_dir = "#{project_path}/#{environment}"
build_dir = "#{project_path}"
 
css_dir = "css"
css_path = "#{build_dir}/#{css_dir}"
sass_dir = "sass"
images_dir = "images"
javascripts_dir = "javascripts"
fonts_dir = "fonts"