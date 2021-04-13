# shellcheck disable=SC2162
# shellcheck disable=SC2229
# shellcheck disable=SC2154
echo 'Write yor app name'
read $app
python manage.py makemigrations $app
python manage.py migrate
python manage.py runserver

