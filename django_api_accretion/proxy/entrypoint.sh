#!/bin/sh

echo "create error.log and grant permission for /var/log/nginx/error.log..."

# Create error.log file
touch /var/log/nginx/error.log

# Change ownership of the log file
chown www-data:www-data /var/log/nginx/error.log

echo "start nginx service entrypoint.sh..."

nginx -g 'daemon off;' 

echo "end nginx service entrypoint.sh..."