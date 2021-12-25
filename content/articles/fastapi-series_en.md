Title: FastApi. Learning Path. Introduction
Date: 2021-12-25 11:53
Slug: fast-api-learning-path-introduction
Lang: en
Category: Development
Tags: Python, Development, Techology
og_image: assets/images/fastapi/circuits.jpg

# FastApi. Start the learning Path. Introduction
Series of articles describing the learing path for FastApi

This will be just an introductory post, why the hell I need to learn
how to develop with FastApi, where did I look to get references, why those references
were way out of my current knowledge scope and finally what can I do to fix it.

***

## A bit of Context

I started creating a project with Flask, it took me a bit but I managed to get through that learning 
curve all new langauges, tecnologies, and frameworks require to start being confortable and speed up
development, I was there, really. And then I read about asynchronous development with python, more or 
less in the same way you will do with nodejs and javascript and I got thrilled by it. 
What framework in python could let me to develop in one single threaded asynchronous superfast way?
and there it came FastApi.

Here some comparisons between frameworks:
[Python flask vs fastapi](https://christophergs.com/python/2021/06/16/python-flask-fastapi/)

## My references

Now that I get hooked by it I needed to get some resources to learn how to use it. I like youtube interactive 
way of learning by repeating what other people does in a video and I liked how [PrettyPrinted](https://www.youtube.com/c/PrettyPrintedTutorials/videos)
explains concepts about languages and frameworks. I'm sure I followed some tutorials about flask in this channel too.

Ok this was nice but I wanted something to put me in the path to start developing my projects right away, so 
I looked for some github repository with a full stack ready to start creating my projects with all the initial components
and boilerplate config already set.

An awesome resource came from Tiangolo. The author of FastApi framework itself and he had many flavours depending on the database, Saas platform etc.
Cool, cool, cool.
[Fullstack fastapi postgres](https://github.com/tiangolo/full-stack-fastapi-postgresql) 

This guy knows what he talks about, lets see:

* It uses cookiecutter to create your project based on his template. But I don't know about cookiecutter... let's read about it in the docs
[cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/) 

Now I know the basics of it lets go for it!!!

But wait, what are all this tools, frameworks, engines?

Don't panic, lets start by the backend which is what I really want to know well

* [Poetry](https://python-poetry.org/) -- Darn, not my virtualenv wrapper, nor pyenv, ok will check it out
* [Alembic](https://alembic.sqlalchemy.org/en/latest/) -- To handle database migrations. Nop
* [SqlAlchemy](https://www.sqlalchemy.org/library.html#reference)  -- 1 out of three so far...
* [RabbitMQ](https://www.rabbitmq.com/documentation.html)  -- 2 out of four 50/50 not bad.
* [flower](https://github.com/mher/flower) -- Do I now need to start gardening too?
* [Celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html) -- ~~ 

And all side technologies
* docker-compose. This is my friend
* swarm. This we have common friends
* traefik. What is this? ooh, the new kid on the block for servers

.... 

## So Overwhelmed 

I was so excited about all this new toys I wanted to get started with all of them at once, besides that I like a bit more virutalization and 
clustering with kubernetes rather than docker-compose and developing locally...

I went back and forth trying to start using Tiangolo template or creating a new project from scratch and learn each of the missing puzzle peaces 
little by little.
Just today I decided to start from scratch. I studied a lot how Tiangolo uses authentication with JWT in his template (I also wanted to use mongo instead of Relational databases).

## Here the paths starts

I will start by creating my own backend. Following the path of the Jedy like a good Padawan. No fear!
![Yoda Quote]({attach}/assets/images/fastapi/Yoda-Quote-1.jpg) 

My idea is to start by implementing Authentication with JWT. Having Tiangolo as reference, but maybe switching to MongoDB. We'll see it.

Lets see how high this rocket can fly
![Erlik]({attach}/assets/images/fastapi/erlik_bagman.gif)

