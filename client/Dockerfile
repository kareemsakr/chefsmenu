# docker  build -t react-app  .
# docker run -it react-app sh
FROM node:12.0.0-alpine
# user and grouop have the same name # the RUN is executed during build
RUN addgroup app && adduser -S -G app app
# all following commands will be executed under this user
USER app
# all the following commands will be run in that directory
WORKDIR /app/
RUN mkdir data

# we are doing the copying in 2 stages because previously when this line was copy . . 
# npm i was run everytime we built the image, because it can't tell if anything has changed or not
# and since copy . . was run everytime, this means that all subsequent layers will have to be rebuilt as well
COPY package*.json .
RUN npm i
COPY . .

# this does not actually map the host's port to the container's port
EXPOSE 3000

# can only have one CMD
# this is called shell form (it is executed in a seperate shell), i.e. spins up an extra shell process
# CMD npm start

# does not spin an extra shell process 
# this is called exec form
# this can be overidden
CMD ["npm", "start"]

# this is the same as CMD but it CANNOT be overriden
# ENTRYPOINT [ "executable" ]







## ---------------
## to publish
## create new image with account_name/image_name
## docker login in terminal
## docker push image_name
## ---------------
## how to run a detached container
## docker run -d image_name
## now you can close the terminal without shutting down the container
## ---------------
## to give your container a name so you can refer to it without having to use the randomly generated ID
## docker run -d --name blue_sky image_name
## ---------------
## to map host:container ports
## docker run -d -p 3000:3000 --name any_name image_name
## ---------------
## to run a command on a currently runnin container
## docker exec container_name ls
## ---------------
## to run interactive shell 
## docker run -it react-app 
## ---------------
## to mount a volume from host to container
## docker run -d -p x:y -v local-dir:/app/container-dir image-name
## ---------------
## problem: for dev purposes, you don't wannat rebuild your image everytime you add a new line of code
## solution: map the pwd on your lcoal to the /app
## docker run -d -p xxxx:yyyy -v $(pwd):/app image_name

