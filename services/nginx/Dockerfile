# Use the Nginx image
FROM nginx:1.20-alpine

COPY ./static/index.html /usr/share/nginx/html/

# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

# Replace with our own nginx.conf
COPY default.conf /etc/nginx/conf.d/

# COPY ssl.csr /etc/nginx/ssl.csr
# COPY ssl.key /etc/nginx/ssl.key

EXPOSE 443
EXPOSE 80
