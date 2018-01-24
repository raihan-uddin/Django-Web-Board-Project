# Django Web Board Project

[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-1.11-brightgreen.svg)](https://djangoproject.com)


![Class Diagram Screenshots](class_diagrams/use-case-diagram.png)


Figure 1: Use case diagram of the core functionalities offered by the Web Board

![Class Diagram Screenshots](class_diagrams/basic-class-diagram.png)


Figure 2: Draft of the class diagram of the Web Board

![Class Diagram Screenshots](class_diagrams/class-diagram.png)


Figure 3: Class diagram emphasizing the relationship between the classes (models)


##  Relationship between the models:

![Class Diagram Screenshots](class_diagrams/class-diagram-board-topic.png)
![Class Diagram Screenshots](class_diagrams/class-diagram-topic-post.png)
![Class Diagram Screenshots](class_diagrams/class-diagram-topic-user.png)
![Class Diagram Screenshots](class_diagrams/class-diagram-post-user.png)

## Another way to draw this class diagram is emphasizing the fields rather than in the relationship between the models:

![Class Diagram Screenshots](class_diagrams/class-diagram-attributes.png)


##  Wireframes


![HomePage](class_diagrams/wireframe-boards.png)

Figure 5: Boards project wireframe homepage listing all the available boards.

![Topics](class_diagrams/wireframe-topics.png)

Figure 6: Boards project wireframe listing all topics in the Django board.

![New Topic](class_diagrams/wireframe-new-topic.png)

Figure 7: New topic screen

![Posts](class_diagrams/wireframe-posts.png)

Figure 8: Topic posts listing screen

![Reply](class_diagrams/wireframe-reply.png)

Figure 9: Reply topic screen


## Comparison between the class diagram and the source code to generate the models with Django

![Class diagram django models](class_diagrams/class-diagram-django-models.png)

## Running the Project Locally

First, clone the repository to your local machine:

```bash
https://github.com/theprogrammingthinker/Django-Web-Board-Project.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Setup the local configurations:

```bash
cp .env.example .env
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.
