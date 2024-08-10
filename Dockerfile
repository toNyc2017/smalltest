# Use the official NGINX image from Docker Hub
FROM nginx:latest

# Copy the HTML file to the NGINX web root
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80 to the outside world
EXPOSE 80

