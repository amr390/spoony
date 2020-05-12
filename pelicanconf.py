#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Spoony'
SITENAME = 'Full Stack Troubles'
SITESUBTITLE = 'Notes and descriptions in my day by day job issues'
SITEURL = ''

PATH = 'content'

DEFAULT_DATE = 'fs'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 3

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

STATIC_PATHS = ['assets']

EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
    'assets/CNAME': {'path': 'CNAME'}
}

# Post and Pages path
ARTICLE_PATHS = ['articles']
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_LANG_URL = 'articles/{slug}-{lang}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
ARTICLE_LANG_SAVE_AS = 'articles/{slug}-{lang}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'catgegories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'

# Plugins
PLUGIN_PATHS = [
    'pelican-plugins'
]

PLUGINS = [
    'i18n_subsites',
    'sitemap',
    'neighbors',
    'assets'
]

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

I18N_SUBSITES = {
    'es': {
        'SITENAME': 'Tormentos Full Stack',
        'LOCALE': 'es_ES'
    },
}

LANGUAGES_LOOKUP = {
    'en': 'English',
    'es': 'Español',
}


def lookup_lang_name(lang_code):
    """ Lookup for language code function """
    return LANGUAGES_LOOKUP[lang_code]


def my_ordered_items(item_d):
    """ Sorting items function """
    items = list(item_d.items())
    # swap first and last using tuple unpacking
    items[0], items[-1] = items[-1], items[0]
    return items


JINJA_FILTERS = {
    'lookup_lang_name': lookup_lang_name,
    'my_ordered_items': my_ordered_items,
}

JINJA_ENVIRONMENT = {
    'extensions' : ['jinja2.ext.i18n']
}

THEME = 'attila'
# Theme specific settings

# This is deprecated. Will be removed in future releases.
# Work around will be use HOME_COVER and use cover in individual articles.
# HEADER_COVER = 'https://casper.ghost.org/v1.0.0/images/welcome.jpg'

# This is deprecated. Will be removed in future releases.
# Work around will be use HOME_COLOR and use color in individual articles.
# HEADER_COLOR = 'black'

# To set background image for the home page.
# Theme specific settings

# This is deprecated. Will be removed in future releases.
# Work around will be use HOME_COVER and use cover in individual articles.
# HEADER_COVER = 'https://casper.ghost.org/v1.0.0/images/welcome.jpg'

# This is deprecated. Will be removed in future releases.
# Work around will be use HOME_COLOR and use color in individual articles.
# HEADER_COLOR = 'black'

# To set background image for the home page.

HEADER_COVER = 'assets/images/bombilla.jpg'
HEADER_COVERS_BY_TAG = {
    'cupcake': 'assets/images/rainbow_cupcake_cover.png',
    'general': 'https://casper.ghost.org/v1.0.0/images/writing.jpg'
}

HOME_COVER = 'https://casper.ghost.org/v1.0.0/images/welcome.jpg'
# SITE_LOGO = 'assets/images/skull.png'
AUTHORS_BIO = {
    "spoony": {
        "name": "Toni Mas",
        "cover": "assets/images/writing_machine.jpg",
        "image": "assets/images/skull.png",
        "website": "http://blog.spoonsdevs.com",
        "linkedin": "antonio-mas-6953a821",
        "github": "amr390",
        "location": "Spain",
        "bio": "Software Engineer since 2004, tech addict, proud father and curious in general"
    }
}


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
