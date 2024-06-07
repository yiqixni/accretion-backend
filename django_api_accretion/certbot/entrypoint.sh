#!/bin/sh

# Check if we have existing certificates
if [ ! -f /etc/letsencrypt/live/$DOMAIN/fullchain.pem ]; then
  echo "Certificates not found, creating new ones..."
  certbot certonly --nginx -d $DOMAIN --email $CERTBOT_EMAIL --agree-tos --no-eff-email
else
  echo "Certificates found, skipping generation."
fi

# Check if options-ssl-nginx.conf is in place
if [ ! -f /etc/letsencrypt/options-ssl-nginx.conf ]; then
  echo "Missing /etc/letsencrypt/options-ssl-nginx.conf, creating it..."
  certbot --nginx -d $DOMAIN --agree-tos --email $CERTBOT_EMAIL --deploy-hook "cp /etc/letsencrypt/options-ssl-nginx.conf /etc/letsencrypt/options-ssl-nginx.conf"
fi

# Check if ssl-dhparams.pem is in place
if [ ! -f /etc/letsencrypt/ssl-dhparams.pem ]; then
  echo "Missing /etc/letsencrypt/ssl-dhparams.pem, creating it..."
  openssl dhparam -out /etc/letsencrypt/ssl-dhparams.pem 2048
fi

# Start the certbot renew process in the background
while :; do
  certbot renew
  sleep 12h # Sleep for 12 hours before checking again
done &
