#! /bin/sh
while true; do
    flask db upgrade
    if [ $? -eq 0 ]; then
        break
    fi
    printf  "%s\n"  "Deloy command failed, retrying in 5 secs..."
done

. ./.env
exec flask run --host 0.0.0.0 
