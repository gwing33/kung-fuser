include_recipe "python::pip"

python_pip "http://www.djangoproject.com/download/1.4-alpha-1/tarball/" do
  action :install
end