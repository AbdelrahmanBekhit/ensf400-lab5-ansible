FROM nginx:alpine

COPY ./nginx.cfg /etc/nginx/conf.d/default.cfg

# Expose ports
EXPOSE 80
EXPOSE 443