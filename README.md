
## Index

- [Descripción del proyecto en Español.](#django-portfolio-website-blog-español)
- [Project description in English.](#django-portfolio-website-blog-english)
- [Instalación.](#instalacion)
- [Installation.](#installation)
- [Hoja de Ruta.](#hoja-de-ruta)
- [Author](#author)
- [Tech used for this Project](#tech-used-for-this-project)


# Django Portfolio Website / Blog [Español]

Este es mi Portafolio web personal con una función de Blog que permite a los usuarios revisar, comentar y gustar mis proyectos mostrados con el fin de ayudarme a seguir creciendo y mejorando como desarrollador.

El proyecto cuenta con 3 apps:
- Post: contiene los models 'Post', 'Review', 'Comment'y 'Like'.
- UserProfile: contiene los models 'UserProfile' -es una extensión del modelo default User de Django para incorporarle atributos-, y 'AnonymousUser' -es un model que se creó para que usuarios que no están registrados puedan dejar comentarios y reviews-.
- Extra: contiene los models 'Study', 'Technology' y 'Validation'

# Django Portfolio Website / Blog [English]

This is my personal web Portfolio with a Blog feature that allows users to review, comment and like my displayed projects in order to help me keep growing and improving as a developer.

The project has 3 apps:
- Post: contains the models 'Post', 'Review', 'Comment'and 'Like'.
- UserProfile: contains the models 'UserProfile' -it is an extension of Django's default User model to incorporate attributes-, and 'AnonymousUser' -it is a model created so that users who are not registered can leave comments and reviews-.
- Extra: contains the models 'Study', 'Technology' and 'Validation'.
## Instalacion

Primero active el entorno virtual una vez que se encuentre en el directorio 'django_portfolio_blog':

```bash
  ./venv/scripts/activate
```
Instale las dependencias necesarias del archivo requirements.txt:

```bash
  pip install -r requirements.txt
```


## Installation

First activate the virtual environment once in the directory 'django_portfolio_blog':

```bash
  ./venv/scripts/activate
```
Install the required dependencies from the requirements.txt file:

```bash
  pip install -r requirements.txt
```
    
## Hoja de Ruta

- Primero active el entorno virtual una vez que se encuentre en el directorio 'django_portfolio_blog':
```bash
  ./venv/scripts/activate
```

- Luego, para iniciar el servidor, asegúrese de estar en la carpeta del proyecto 'portfolio_blog':
```bash
  cd portfolio_blog
```
- Inicie el servidor de Django:
```bash
  python manage.py runserver
```

**Nota: puede crear su propio super usuario para testear funcionalidades desde el admin panel:**
```bash
  python manage.py createsuperuser
```

- Paths del proyecto:
```bash
  /                         - [home page]
  /admin                    - [admin panel page]
  /contact                  - [contact page]
  /about                    - [about page]

  /users                    - [muestra todos los usuarios]
  /users/register/          - [form para registrar nuevo usuario]
  /users/<int:id>/          - [muestra un usuario por el id pasado en la url]
  /users/search/            - [form de búsqueda de un usuario]
  /users/search/result/     - [muestra el resultado de la busqueda de un usuario] 

  /posts                    - [muestra todos los posts]
  /posts/<int:pk>/          - [muestra un post por el id pasado en la url]
  /posts/create/            - [form para crear un nuevo post] 

  /extras                   - [no muestra nada, sirve solo para acceder a /studies y /technologies]
  /extras/studies/          - [muestra todos los estudios cargados en el modelo 'Study']
  /extras/studies/add       - [form para agregar un 'Study']
  /extras/technologies/     - [muestra todas las tecnologías cargadas en el modelo 'Technology']
  /extras/technologies/add  - [form para agregar una 'Technology'] 
```

- Posts:
Al encontrarse en la url /posts se puede ver un display de los posts cargados en formato de link (puede cargarse uno nuevo desde /posts/create).

Si se clickea sobre un post, se redirigirá a la vista detallada del post, ya con su función de blog incorporada, donde se puede dejar Reviews y comentarios.

Un Post puede recibir Reviews.

Una Review puede recibir Comments.

Un Comment puede recibir Comments.

- Studies & Technologies:
La idea de estos es poder hacer un display de los mismos y que los usuarios puedan validar las aptitudes -model Validation- (_funcionalidad todavía no desarrollada en HTML pero todo puede realizarse desde el admin panel_)
- Likes:
Los usuarios pueden likear Posts, Reviews y Comments. (_funcionalidad todavía no desarrollada en HTML pero todo puede realizarse desde el admin panel_)

## Roadmap




## Author

- [@andresdeinnocentiis](https://github.com/andresdeinnocentiis)


## 🛠 Skills
Python, Django, HTML, CSS.

