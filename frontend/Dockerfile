# étape de build
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# étape de production
FROM nginx:stable-alpine as production-stage 
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY docker-bootstrap.sh .

EXPOSE 80
CMD ["./docker-bootstrap.sh", "/usr/share/nginx/html"]
