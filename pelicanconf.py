#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Python Portugal Team'
SITENAME = u'Python Portugal'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = u'pt-BR'

# Google Analytics
GOOGLE_ANALYTICS = 'UA-950364-17'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URL's
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

ARTICLE_URL = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

YEAR_ARCHIVE_SAVE_AS = 'arquivo/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'arquivo/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = 'arquivo/{date:%Y}/{date:%m}/{date:%d}/index.html'

AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

LOAD_CONTENT_CACHE = False

THEME = 'theme/python-pt'

# Navbar Links da Home Page
NAVBAR_HOME_LINKS = [
    {
        'title': 'Recursos',
        'href': '#',
        'desc': ('Aprenda ...'),
        'children': [
            {
                'title': 'Documentação Oficial',
                'href': 'https://docs.python.org',
            },
            {
                'title': 'Formação',
                'href': 'formacao',
            },
            {
                'title': 'Livros',
                'href': 'livros',
            },
            {
                'title': 'Vídeos',
                'href': 'videos',
            },
            {
                'title': 'Tutoriais',
                'href': 'tutoriais',
            },
        ]
    },
    {
        'title': 'Eventos',
        'href': 'eventos',
        'desc': 'Eventos...',
    },
]

# Add font-awsome
PLUGINS = [
    # ...
    'pelican_fontawesome',
    # ...
]

# Add static paths
STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico', 'extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}


