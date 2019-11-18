#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#
# About the site
#
AUTHOR = u'Marianne Maertens & Guillermo Aguilar'
SITENAME = u'Computational Psychology at TU Berlin'
SITETITLE = u'Computational<br/>Psychology'
SITESUBTITLE = u'at TU Berlin'
SITEURL = 'www.psyco.tu-berlin.de'

FAVICON = SITEURL + '/img/favicon.ico'

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = u'en'
LOCALE = u'en_US.UTF-8'

MAIN_MENU = True

#
# Configure Pelican a bit
#
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [ 'sitemap', 'just_table']
SITEMAP = { 'format': 'xml' }

DIRECT_TEMPLATES = ['404'] # unset all templates; add 404
THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#
# Configure the site
#
STATIC_PATHS = ['img', 'files']
MENUITEMS = (('Home', 'index.html'),
             ('People', 'people.html'),
             ('Research', 'research.html'),
             ('Publications', 'publications.html'),
             ('Teaching', 'teaching.html'),
             ('Contact', 'contact.html')
)

DEFAULT_PAGINATION = False

# We prefer document-relative URLs
RELATIVE_URLS = True

CACHE_CONTENT = False
