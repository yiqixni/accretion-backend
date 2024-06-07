#!/bin/sh

# Check if we have existing certificates
if [ ! -f /etc/letsencrypt/live/$DOMAIN/fullchain.pem ]; then
  echo "Certificates not found, creating new ones..."
#   certbot certonly --webroot -w /data/letsencrypt -d $DOMAIN --email $CERTBOT_EMAIL --agree-tos --no-eff-email
  certbot certonly --nginx -d $DOMAIN --email $CERTBOT_EMAIL --agree-tos --no-eff-email
else
  echo "Certificates found, skipping generation."
fi

# Check if placeholder files exist and copy them if necessary
if [ ! -f /etc/letsencrypt/options-ssl-nginx.conf ]; then
  echo "Copying options-ssl-nginx.conf.placeholder to /etc/letsencrypt/options-ssl-nginx.conf"
  cp /etc/letsencrypt/options-ssl-nginx.conf.placeholder /etc/letsencrypt/options-ssl-nginx.conf
fi

if [ ! -f /etc/letsencrypt/ssl-dhparams.pem ]; then
  echo "Copying ssl-dhparams.pem.placeholder to /etc/letsencrypt/ssl-dhparams.pem"
  cp /etc/letsencrypt/ssl-dhparams.pem.placeholder /etc/letsencrypt/ssl-dhparams.pem
fi

# Start the certbot renew process in the background
while :; do
  certbot renew
  sleep 12h # Sleep for 12 hours before checking again
done &
