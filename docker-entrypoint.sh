echo "Run database makemigrations"
python manage.py makemigrations

echo "Run database migrations"
python manage.py migrate


echo "Creating admin..."
echo "from api.models import CustomUser; CustomUser.objects.create_superuser('admin', 'admin@deepcase.com.tr', '123123123', first_name='Admin')" | python manage.py shell

echo "Starting application server"
python manage.py runserver 0.0.0.0:8000
# gunicorn duzeyligi_backend.wsgi:application --bind 0.0.0.0:8000 --workers 3

