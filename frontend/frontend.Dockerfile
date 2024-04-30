FROM node:node:20.10.0 as frontend

RUN apt-get update && apt-get upgrade -y
WORKDIR /
COPY . /frontend
RUN npm install



EXPOSE 8000