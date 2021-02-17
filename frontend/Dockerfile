# Container used to build our final image (contains build tools)
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build


# Build production container
FROM nginx:stable-alpine as production-stage 

# copy nginx configuration to redirect all vuejs "virtual" pages to index.html
COPY nginx.conf /etc/nginx/nginx.conf
# startup script that inject environment variables before running nginx server
COPY docker-bootstrap.sh .
# copy built webapp at web server root
COPY --from=build-stage /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["./docker-bootstrap.sh", "/usr/share/nginx/html"]
