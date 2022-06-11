DIR = 'D:/OneDrive/__Projects/macroblog'

rmarkdown::yaml_front_matter(file.path(DIR, 'test_yaml.html'))
rmarkdown::html_fragment(file.path(DIR, 'test_yaml.html'))


