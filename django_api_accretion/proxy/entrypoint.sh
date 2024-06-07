#!/bin/sh

echo "make directory and grant permission for /var/log/nginx..."

# Create log directory and set permissions
mkdir -p /var/log/nginx
chown -R www-data:www-data /var/log/nginx

echo "start nginx service entrypoint.sh..."

nginx -g 'daemon off;' 

echo "end nginx service entrypoint.sh..."