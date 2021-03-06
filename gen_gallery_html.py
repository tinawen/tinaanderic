# Hacky script for generating gallery page html.
# The input is assumed the be copy-pasted directly from picasaweb source code,
# that contains image srcs. i.e.:
#
# <div><a href=""><img src=""></a></p></div><div><a href=""><img src=""></a></p></div>
# <div><a href=""><img src=""></a></p></div><div><a href=""><img src=""></a></p></div>
#
# The output html for the gallery page is written to standard out.

import sys
from bs4 import BeautifulSoup

THUMBNAIL_SIZE = 150

def add_size_param(base_url, param):
  parts = base_url.split('/')
  return '/'.join(parts[:-1] + [param] + [parts[-1]])

def gen_html(big_url, thumb_url, caption):
  return ''.join(
    ['<a href="',
     big_url,
     '" title="',
     caption,
     '" data-gallery="">\n',
     '  <img src="',
     thumb_url,
     '">\n',
     '</a>'])
     

if __name__ == "__main__":
  input_file = sys.argv[1]
  soup = BeautifulSoup(open(input_file).read())
  urls = [img['src'] for img in soup.find_all('img')]
  for url in urls:
    base_url = ''.join(url.split('s128/'))
    # Base url, use original size of the image, i.e. 's0'
    big_url = add_size_param(base_url, 's0')
    # Thumbnail url, square smart crop to THUMBNAIL_SIZE.
    thumb_url = add_size_param(base_url, 's'+str(THUMBNAIL_SIZE)+'-p')
    print gen_html(big_url, thumb_url, '')
