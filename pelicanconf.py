#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Tory Law'
SITENAME = u'torypages'
SITEURL = 'http://torypages.com/me/'

THEME = os.path.join(os.path.expanduser('~'), 'Code/Flex')
SITETITLE = "Tory Law"
SITESUBTITLE = "Backend Software Developer in Toronto, Canada"
SITELOGO = os.path.join(SITEURL, 'images/me.jpg')
ROBOTS = 'index, follow'
MAIN_MENU = False
PAGE_EXCLUDES = ['index.html']
DISPLAY_PAGES_ON_MENU = False



PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = set()
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('envelope-o', 'mailto:t.law@torypages.com'),
          ('github', 'https://github.com/torypages'),
          ('linkedin', 'https://ca.linkedin.com/in/tory-law-444b681b'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
