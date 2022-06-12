BLOG_DIR = 'D:/OneDrive/__Projects/macroblog'

import sys
import os
import jinja2
import yaml
import sass
from slugify import slugify

# Initialize template loader & conf file
env = jinja2.Environment(
	loader = jinja2.FileSystemLoader(searchpath = [x[0] for x in os.walk(os.path.join(BLOG_DIR, 'posts'))])
)
with open(os.path.join(BLOG_DIR, 'conf.yaml'), 'r') as x:
	conf = yaml.safe_load(x)

# Build pages
def build_page(template, date):
	page_template = env.get_template(template)
	page_html = page_template.render(
		date = date
	)
	return(page_html)

# Save pages
def save_page(page_html, title):
	title_slug = slugify(title)
	# print(title_slug)
	with open(os.path.join(BLOG_DIR, 'public', title_slug + '.html'), 'w') as x:
		x.write(page_html)

# Build SCSS
def build_css():
	compiled_css = sass.compile(
		filename = os.path.join(BLOG_DIR, 'assets', 'style', 'main.scss'),
		output_style = 'compressed'
	)
	css_dir = os.path.join(BLOG_DIR, 'public', 'static')
	if not os.path.isdir(css_dir):
		os.makedirs(css_dir)
	with open(os.path.join(css_dir, 'style.css'), 'w') as fileobj:
		fileobj.write(compiled_css)

# Run
def main():

	print(conf)

	built_pages = list(map(
		lambda x: build_page(x['template'], x['date']),
		conf['posts']
	))
	
	conf_appended = list(map(
		lambda x: {'page_html': x[0]} | x[1],
		list(zip(built_pages, conf['posts']))
	))

	print(conf_appended)

	res = list(map(
		lambda x: save_page(x['page_html'], x['title']),
		conf_appended
	))
	
	#build_css()
	print(res)


main()