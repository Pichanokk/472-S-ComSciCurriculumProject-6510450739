FROM node:22-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm ci  # Use ci instead of install for more consistent results

COPY . .

RUN if [ -f /app/src/styles/InsertGradFile.css ] && [ ! -f /app/src/styles/insertGradFile.css ]; then \
    ln -s /app/src/styles/InsertGradFile.css /app/src/styles/insertGradFile.css; \
    fi

RUN npx vite build

FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]