project:
	django-admin startproject
app:
	python manage.py startapp
rs:
	python src/manage.py runserver
mag:
	python src/manage.py makemigrations
mig:
	python src/manage.py migrate
col:
	python src/manage.py collectstatic
sup:
	python src/manage.py createsuperuser
hel:
	python src/manage.py help
test:
	python src/manage.py test
shell:
	pipenv shell
lock:
	pipenv lock
sync:
	pipenv sync --dev
update:
	pipenv update
build:
	docker build .
up:
	docker-compose up -d
psa:
	docker-compose ps -a
upb:
	docker-compose up -d --build
docbuild:
	docker-compose build
down:
	docker-compose down
doccol:
	docker-compose exec app python src/manage.py collectstatic
docmag:
	docker-compose exec app python src/manage.py makemigrations
docmig:
	docker-compose exec app python src/manage.py migrate
docsup:
	docker-compose exec app python src/manage.py createsuperuser
docapp:
	docker-compose exec app python src/manage.py startapp
doctest:
	docker-compose exec app python src/manage.py test
reload:
	uvicorn main:app --reload
gun:
	gunicorn src.config.wsgi:application --bind

celery:
	celery -A config worker -l INFO

# cq == Code Quality
cq:
	flake8 ./ && black ./ && isort ./ && mypy ./
	
# import ipdb; ipdb.set_trace()
