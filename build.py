BLOG_DIR = 'D:/OneDrive/__Projects/macroblog'

import sys
import jinja2
import yaml

# Initialize template loader & conf file
env = jinja2.Environment(loader = jinja2.FileSystemLoader(searchpath = BLOG_DIR + '/posts'))
with open(BLOG_DIR + '/conf.yaml', 'r') as x:
	conf = yaml.safe_load(x)


# Build pages
def build_page(date, template):
	page_template = env.get_template(template)
	page_output = page_template.render(
		date = date
	)
	return(page_output)
	
# Run
def main():
	print(conf)
	built_pages = list(map(lambda x: build_page(x['date'], x['template']), conf['posts']))
	
print(main())
