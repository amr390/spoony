Title: Sigo trasteando con Pelican
Date: 2020-05-13 12:35
Slug: dealing-with-pelican
Lang: es
Status: draft
Category: Blogging
Tags: Pelican, Blog, Blogging, Python, Vim, Nginx
og_image: assets/images/2.png


# A vueltas con Pelican
Todavía sigo dándole vueltas a la configuración del blog con *PELICAN*, este post explica 
una forma de lidiar con internacionalización y los temas en Pelican.

# Aplicando plugins
Existe un plugin para pelican que permite añadir posts en varios idiomas, se llama
 **i18_subsites** para poder añadir este este plugin a *Pelican* solo es necesario 
 bajarlo del [repositorio de plugins de Pelican](https://github.com/getPelican/pelican-plugins) 

 Un par de snippets con la configuración necesaria: 

 ```python
# Plugins
PLUGIN_PATHS = [
    'plugins'
]

PLUGINS = [
    'i18n_subsites',
    ...,
]
```




