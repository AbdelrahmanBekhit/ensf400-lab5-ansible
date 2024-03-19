FROM nginx:alpine

COPY ./nginx.conf etc/nginx/sites-available/nginx.conf

# Expose ports
EXPOSE 80
EXPOSE 443