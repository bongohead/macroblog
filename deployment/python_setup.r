#' Install Python, Create Virtual Environment, and Install Modules
#' 
#' Deployment:
#' (1) Install and update R
#' (2) Install package reticulate
#' (3) Run python_setup.r, update BLOG_DIR to the directory containing the build source

BLOG_DIR = 'D:/OneDrive/__Projects/macroblog'

if (!dir.exists(file.path(BLOG_DIR, '.virtualenvs'))) {
	dir.create(file.path(BLOG_DIR, '.virtualenvs'), mode = '0755')
}

library(reticulate)
install_python(version = '3.9:latest')
use_python_version('3.9:latest')
virtualenv_create(file.path(BLOG_DIR, '.virtualenvs', 'bongohead'))
# jinja2: HTML templating 
# pyyaml: YAML parse
lapply(c('jinja2', 'pyyaml'), function(x)
	virtualenv_install(file.path(BLOG_DIR, '.virtualenvs', 'bongohead'), x)
)


# Reset
library(reticulate)
use_python_version('3.9:latest')
virtualenv_remove(file.path(BLOG_DIR, '.virtualenvs', 'bongohead'))