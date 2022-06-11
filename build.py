BLOG_DIR = 'D:/OneDrive/__Projects/macroblog'

import jinja2
import yaml

with open(BLOG_DIR + '/conf.yaml', 'r') as stream:
    try:
        print(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)
        
env = jinja2.Environment(loader = jinja2.FileSystemLoader(searchpath = BLOG_DIR + '/posts'))

TEMPLATE_FILE = "content.html"
template = env.get_template(TEMPLATE_FILE)
output_text = template.render()  # this is where to put args to the template renderer

print(output_text)
