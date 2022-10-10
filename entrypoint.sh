#/bin/sh

if [ "$1" = "import" ]; then
    python /var/web/xlsx_to_mongodb.py /var/data/data.xlsx "$2"
elif [ "$1" = "runserver" ]; then
        python /var/web/manage.py  migrate \
        &&  python /var/web/manage.py runserver 0.0.0.0:8000
fi