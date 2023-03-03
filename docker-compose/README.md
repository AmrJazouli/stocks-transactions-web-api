## 1. Docker image of the application:

To build the Docker image of the application, I typed the following command:

```
docker build -t stocksapidevopsproject .
```
A message showing the building has finished will be displayed in the CLI:

![Web Page5](../images/Docker_DockerCompose/dockerbuildimage.png)

To list the Docker images, type the following:

```
docker images
```

I am able to see the recent docker image I have just created :

![Web Page5](../images/Docker_DockerCompose/dockerimages.png)

The docker image should be available in Docker Desktop as well.

I have run the Docker image I created as following:

```
docker run -d -p 8000:5000 stocksapidevopsproject
```
![Web Page5](../images/Docker_DockerCompose/dockerrun.png)

The web server should start on http://localhost:8000 as shown following:

![Web Page6](../images/Docker_DockerCompose/dockerrunsuccessful.png)

![Web Page7](../images/Docker_DockerCompose/dockerrunsuccessfulcurd.png)

Press CTRL+C to stop the web server.

I tagged the Docker image as following:

```
docker tag stocksapidevopsproject amrjazouli/stocksapiproject
```

where 'amrjazouli' - is my account on Docker Hub, stocksapiproject - the custom name of the image.

After logging in to DockeHub in CLI, I pushed the Docker image to my Docker Hub account:

```
docker push amrjazouli/stocksapiproject
```

The Docker image should be available on Docker Hub:

![Web Page8](../images/Docker_DockerCompose/dockerimagepushedtohub.png)

## 2. Container orchestration using Docker Compose:

Using the 'docker-compose.yml' file, from the project root directory, I typed the following command:

```
docker-compose up
```

The web server and MongoDB containers will start, I can check the CLI and the web browser on 
http://localhost:8000:

![Web Page9](../images/Docker_DockerCompose/dockercompose.png)

![Web Page10](../images/Docker_DockerCompose/flaskrunning.png)

![Web Page11](../images/Docker_DockerCompose/FrontPage.png)

I tried to insert a transaction to check if it is inserted correctly in the MongoDB instance:

![Web Page12](../images/Docker_DockerCompose/curdpage.png)

A successful message is displayed as following:

![Web Page13](../images/Docker_DockerCompose/insertsuccessful.png)

We query the database and check simultaneously if insertion, update and delete operations are performed successfully while we interact with the api through the browser webpage.

![Web Page131](../images/Docker_DockerCompose/New/DockerHub.png)

I tried to update and delete to check the other CURD operations:

![Web Page14](../images/Docker_DockerCompose/updateop.png)

![Web Page15](../images/Docker_DockerCompose/updatesuccessful.png)

![Web Page16](../images/Docker_DockerCompose/deleteop.png)

![Web Page17](../images/Docker_DockerCompose/deletesuccessful.png)