# Women in Computer Science Website
Team 13 - It Can't Hurt

The project (Project 7) is a website focusing on women in the School of Computer Science at the University of Auckland. Featuring eight different pages - news, events, staff, PhD students, projects, image gallery, resources and contact - this website provides resources, inspiration and opportunities to connect for women pursuing Computer Science. 

This project also features an administration panel where admins can add, edit or delete any item on the page. The website will display these changes automatically for a smooth connection between the administrators' and website visitors' experience.

---
<!-- TOC -->
* [Women in Computer Science Website](#women-in-computer-science-website)
  * [Project Information](#project-information)
  * [Technologies Used](#technologies-used)
  * [Development](#development)
  * [Configuration](#configuration)
    * [Environment variables](#environment-variables)
  * [Deployment](#deployment)
    * [Docker](#docker)
  * [Future Plans](#future-plans)
  * [Acknowledgements](#acknowledgements)
<!-- TOC -->

## Project Information

Project Management board: [Team 13 It-Can-t-Hurt Jira](https://itcanthurt-team13.atlassian.net/jira/software/projects/ICH/boards/1/roadmap?shared=&atlOrigin=eyJpIjoiMGJhZGM2YTBiMWVlNGFlMmJjZjFjOTA1ZGM3NjBjZDMiLCJwIjoiaiJ9)

Demo Deployment (will be unavailable after the semester): [http://ec2-13-211-149-16.ap-southeast-2.compute.amazonaws.com/](http://ec2-13-211-149-16.ap-southeast-2.compute.amazonaws.com/)
- Admin interface is accessible at [/admin](http://ec2-13-211-149-16.ap-southeast-2.compute.amazonaws.com/admin)
    - credentials have been privately shared

## Technologies Used

The backend for this application is written in Python, using version 3.10. 
It is built using the [Django Web Framework](https://www.djangoproject.com/) (version 4.1.1+).
Both sqlite and postgresql database backends are supported. This can easily be extended to support other database backends due to Django's support.
The frontend consists of a mix of HTML, CSS and Javascript, making use of the [Bootstrap](https://getbootstrap.com/) (version 5.1.3) and [FontAwesome](https://fontawesome.com/) frameworks.

A simple CI/CD pipeline is implemented using GitHub Actions. 
This runs the Django tests and linter on every commit, and automatically deploys the application to the production server when a commit is pushed to the `main` branch.

Docker and Docker Compose is used for deployment, however any other method is also supported.

Python dependencies are listed in the [requirements.txt](requirements.txt) file.

## Development

This is a standard Django application, following Django conventions. 

Pre-requisite: Python, pip and a basic understanding of Django. See the [Django Tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial01/) for a quick introduction.

See the [Django documentation](https://docs.djangoproject.com/en/dev/) for more information.

1. Clone and create a new branch
2. Set up virtual environment
   
   Unix:
   ```shell
       python -m venv venv
       source venv/bin/activate
   ```
   
   Windows:
   ```shell
       py -3 -m venv venv
       venv\Scripts\activate
   ```

   Refer to the [Python docs](https://docs.python.org/3/library/venv.html) for more information.
   
3. Install dependencies:
   ```shell
       pip install -r requirements-dev.txt
   ```
4. Database migration
   ```shell
       python manage.py makemigrations
       python manage.py migrate
   ```
5. Create superuser
   ```shell
       python manage.py createsuperuser
   ```
6. Run the application
   ```shell
       DEBUG=1 python manage.py runserver
   ```
   Note: `DEBUG=1` environment variable is required for development.
7. Run tests with `python manage.py test`
8. Run black with `black .` (auto-formatter)
9. Run flake8 with `flake8 .` and correct any issues (code style/PEP8 checker)

## Configuration

Environment variables are used to configure the application.

### Environment variables

| Variable            | Value                                                         | Description                                                                                                                                                  |
|---------------------|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DEBUG               | 1 or 0. Default 0                                             | Enable Django debug mode  <br/>See: https://docs.djangoproject.com/en/4.1/ref/settings/#debug                                                                |
| SECRET_KEY          | Required                                                      | Django secret key. **Keep safe in production**<br/>See: https://docs.djangoproject.com/en/4.1/ref/settings/#secret-key                                       |
| ALLOWED_HOSTS       | comma seperated list of hosts e.g. `localhost,127.0.0.1`      | See https://docs.djangoproject.com/en/4.1/ref/settings/#allowed-hosts                                                                                        |
| DB_TYPE             | `sqlite` (default) or `postgres`                              | database backend to use                                                                                                                                      |
| DB_NAME             | Required                                                      | database name                                                                                                                                                |
| DB_USER             | Required for postgres                                         | database user for postgres                                                                                                                                   |
| DB_PASSWORD         | Required for postgres                                         | database password for postgres                                                                                                                               |
| DB_HOST             | Requied for postgres - default `localhost`                    | host of database                                                                                                                                             |
| DB_PORT             | Required for postgres - default `5432`                        | database port                                                                                                                                                |
| DJANGO_STATIC_ROOT  | Path string, required                                         | Where to collect staticfiles for deployment.<br/>See: https://docs.djangoproject.com/en/4.1/ref/settings/#static-root                                        |
| DJANGO_MEDIA_ROOT   | Path string, required. Default is `media` within project base | Where to save uploaded images. See: <br/> https://docs.djangoproject.com/en/4.1/ref/settings/#media-root                                                     |
| EMAIL_HOST          | Required for contact form SMTP email.                         | Email server hostname. E.g. smtp.gmail.com. See: <br/>https://docs.djangoproject.com/en/4.1/ref/settings/#email-host                                         |
| EMAIL_PORT          | Required for contact form SMTP email.                         | Email server port e.g. 587. See: <br/>https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-EMAIL_PORT                                             |
| EMAIL_HOST_USER     | Required for contact form SMTP email.                         | Email server user. See:  <br/>https://docs.djangoproject.com/en/4.1/ref/settings/#email-host-user                                                            |
| EMAIL_HOST_PASSWORD | Required for contact form SMTP email.                         | Email server password. See: <br/>https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-EMAIL_HOST_PASSWORD                                         |
| EMAIL_USE_TLS       | 1 or 0. default `1` (enable)                                  | Enable TLS for emails. Required for some mail servers such as gmail. See: <br/>https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-EMAIL_USE_SSL |
| EMAIL_SEND_TO       | Required for contact form SMTP email.                         | Email to send contact us inquiries to                                                                                                                        |

Note: DJANGO_STATIC_ROOT and DJANGO_MEDIA_ROOT are already set by default for Docker deployment.


## Deployment

Django is very versatile and can be deployed in many ways depending on how your infrastructure is set up. 
We have provided a simple Docker deployment setup using NGINX Reverse Proxy as one example.

See the [Django deployment documentation](https://docs.djangoproject.com/en/dev/howto/deployment/) for more information.


### Docker 

Pre-requisite: [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/), and an understanding of how to use them.

Note: These instructions are for a basic HTTP deployment using NGINX as a reverse proxy. 

1. Modify the example [docker-compose.yml](docker-compose.yml) to your needs, setting above environment variables appropriately.
2. Run `docker compose up -d --build` to build and run. (note: might be `docker-compose` instead of `docker compose` depending on your Compose install)
3. Create a superuser account
   `docker compose exec -it app python manage.py createsuperuser`
4. The website should be available at `http://localhost:8080`
5. Admin panel is available at `http://localhost:8080/admin`

For reference, the Dockerfile sets the following environment variables:
```
DJANGO_STATIC_ROOT="/data/www/static"
DJANGO_MEDIA_ROOT="/data/www/media"
```

## Future Plans

- Image Carousel for news/events/projects pages
- Separate page for past events
- Related news/events sidebar
- Individual project pages
- Basic image cropping and preview tools in admin
- Search engine optimisations


## Acknowledgements

- [Deploying Django with Docker Compose -  London App Developer](https://www.youtube.com/watch?v=mScd-Pc_pX0)
