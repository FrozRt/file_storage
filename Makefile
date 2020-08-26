# Set the default goal if no targets were specified on the command line
.DEFAULT_GOAL = run

PROJECT_NAME = online_store

run:  ## Runs dev server
		@python manage.py runserver

migrations:  ## Migrate database to the latest version
		@python manage.py makemigrations
		@python manage.py migrate

.PHONY: \
  run \
  migrations\

