#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

# Install Nginx if it is not installed
sudo apt-get update
sudo apt-get -y install nginx

# Create required directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership of the /data/ directory to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content
sudo sed -i '/server_name _;/a location /hbnb_static {\n alias /data/web_static/current/;\n}' /etc/nginx/sites-available/default

# Restart Nginx to update the changes
sudo service nginx restart

# Always exit successfully
exit 0
