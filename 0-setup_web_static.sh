#!/usr/bin/env bash
# Setup script for deploying web_static on Nginx web servers.

# Install Nginx
apt-get -y update
apt-get -y install nginx

# Create directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create HTML file
echo "<html><head></head><body>Holberton School</body></html>" \
    > /data/web_static/releases/test/index.html

# Create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership
chown -hR ubuntu:ubuntu /data/

# Configure Nginx
sed -i '/listen 80 default_server/a\    location /hbnb_static/ {\n        alias /data/web_static/current/;\n    }' \
    /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart
