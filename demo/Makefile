PYTHON=../ve/bin/python


run:
	$(PYTHON) manage.py runserver

create-user:
	- $(PYTHON) manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('demo', 'demo@example.com', 'demo')"
