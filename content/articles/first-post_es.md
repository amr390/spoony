Title: My First Post
Date: 2020-05-09 09:33
Slug: my-first-post
Lang: es
Category: General
Tags: Pelican, Blog, Blogging, Python, Vim, Nginx
og_image: /assets/images/2.png

# Blogueando mis notas con Pelican
En este POST explico como he decidido usar *pelican* un generador de contenido 
estático hecho con python para crear un blog sencillo donde documentar y recordar
las complicaciones en el día a día de mi trabajo.

Además así tendré la oportunidad de practicar un poco mi forma de escribir en 
inglés y además la forma de expresarme, tendré que invertir algo de tiempo en este 
blog pero creo que a la larga será beneficioso para mi.

***

## Lo que quería y lo que he conseguido
Quería tener algo rápido para empezar a crear notas personales, he estado usando 
vim wiki para mis tareas diarias, y está muy bien pero tiene algunos problemas que 
me gustaría solucionar.  Con vim wiki todos los ficheros se guardan en el mismo 
directorio, necesito poder guardar las notas en la nube para poder acceder a ellas
desde casa y la oficina.  
Una utilizada útil de vim wiki es poder generar ficheros PDF de las notas así que
creo que mantendré también esta aplicación.

He elegido *pelican*, pero no era tan sencillo como esperaba, he tenido que refrescar
mis conocimientos con `make`, mirar diferentes tutoriales, 
[documentación](https://docs.getpelican.com/en/stable/quickstart.html), 
buenas prácticas para crear posts, páginas, archivos, assets, complementos, temas etc.

Me arrepiento de elegir pelican para el Blog? No creo, pero este es mi primer post.
Espero escribir un nuevo post después -puede que un año- un tiempo para dar una 
opinión con algún conocimiento.

Hay otros generadores de contenido como:

* [Jekill (2008, v4 at time of writing)](https://jekyllrb.com/) desarrollado con ruby.

* [Hugo](http://gohugo.io) desarrollado con Go.

Y otras alternativas con Python también:

* [mkDocs](https://www.mkdocs.org/)

* [makesite.py](https://github.com/sunainapai/makesite)

Por ahora intentaré usar pelican, me gustaría saber gestionar las plantillas y 
colocar imágenes (conseguido :) ), aplicar estilos, archivar artículos, añadir comentarios 
y un montón de cosas

## Setting up the work environment
Installing and setting the work environment is quite simple the steps I follow:
* Having virtualenv and virtualenvwrapper installed...
* Create a python virtual environment to get all pelican dependencies isolated
    <blockquote> 
        mkvirtualenv pelican --python=`which python3`
    </blockquote>
* Install pelican
    <blockquote> 
        pip install pelican
    </blockquote>

*That's all you need to have an initial environment to create your own blog*
Just that? and I could even save a step if I don't mind having pelican in my host 
python environment!

## Now to create the initial blog

* Create the initial blog
    <blockquote> 
        <p>mkdir path_to_my_blog</p>
        <p>cd path_to_my_blog</p>
        <p>pelican-quickstart</p>
    </blockquote>

* Now you have to follow the steps in the wizard

![initial setup]({attach}/assets/images/my_first_post/initial_project.png)


* In the brand new folder tree inside of content folder create a markdown file

* Free your mind and your ideas in that post

* `pelican content`

* `pelican --listen`

* Open your browser in the path [http://localhost:8000](http://localhost:8000)


**BooM!!! you have your blog up and running**

## Publishing

You can have your blog published in a huge variety of options,
**github**, **dropbox**, **s3**, **ftp** or **ssh** to your server.

I choose to push it to a little droplet I have in DigitalOcean, giving the 
ssh details to rsync my output blog to that path and having an nginx server to 
serve my blog (too much for a little blog?)


## Next tasks in my TODO list

I eyed a nice clean theme for my blog [attila](https://github.com/arulrajnet/attila) 
and now I'll try to make it look pretty having that theme as base.

I need to explore how to adjust templates to have a post structure nice and appealing to read.

I like using vim for whatever I can, this is a good excuse to use it, there are some 
things I can do to develop posts and see the output interactively and I can speed 
things up a bit with it, for example I'd like to create snippets to create new posts 
with more or less a good structure.

*OOooOOh I'm all excited to get this thing on going!!!*

Now I hope this is not my last post after the 'new thing excitement' rush 


## Referencias

[Pelican Documentation](https://docs.getpelican.com/en/stable/quickstart.html)

[Blogging with Vim and Pelican](http://www.deepython.com/blogging-with-vim-and-pelican.html)


