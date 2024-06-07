#!/bin/sh

# Check if we have existing certificates
if [ ! -f /etc/letsencrypt/live/$DOMAIN/fullchain.pem ]; then
  echo "Certificates not found, creating new ones..."
  certbot certonly --webroot -w /data/letsencrypt -d $DOMAIN --email $CERTBOT_EMAIL --agree-tos --no-eff-email
else
  echo "Certificates found, skipping generation."
fi

# Start the certbot renew process in the background
while :; do
  certbot renew
  sleep 12h # Sleep for 12 hours before checking again
done &
