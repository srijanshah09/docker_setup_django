# Base Image
FROM nginx:1.25

# Remove default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d

# Expose port for nginx
EXPOSE 80
