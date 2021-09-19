# What's this

Demo how to serve a pre-trained simple RF classifier in batches with FastAPI and Docker.

## How to run

### Build the image

```bash
docker build -t fastapi_demo:with-batch . 
```

ou can use the `-t` flag to specify the name of the image and its tag. In this case the name is `fastapi_demo` and the tag is `with-batch`.
Note that evetytime you make changes to your app, you need to rebuild the image.

### Run the server

```bash
docker run --rm -p 80:80 fastapi_demo:with-batch 
```

- `--rm`: Delete this container after stopping running it. This is to avoid having to manually delete the container. Deleting unused containers helps your system to stay clean and tidy.
- `-p 80:80`: This flags performs an operation knows as port mapping. The container, as well as your local machine, has its own set of ports. So you are able to access the port 80 within the container, you need to map it to a port on your computer. In this case it is mapped to the port 80 in your machine.

Other userful options:

- `--mount type=bind,source=dir/in/your/pc,target=dir/in/container`: This flag allows you to mount a directory in your pc to a directory within the container. This is very important because containers usually have short lifetimes and without mounting files onto them there is no way of persisting changes done to these files when the container was running.

- `-e MODEL_NAME=half_plus_two`: Will create the environment variable `MODEL_NAME` and assign to it the value of `half_plus_two`.

- `-t`: Attaches a pseudo-terminal to the container so you can check what is being printed in the standard streams of the container. This will allow you to see the logs printed out by the standard streams of the container.

Now head over to `localhost:80` and you should see a message about the server spinning up correctly.

### Make requests to the server

Open a new terminal:

```bash
curl -X POST http://localhost:80/predict \
    -d @./wine-examples/batch_1.json \
    -H "Content-Type: application/json"
```

- `-X`: Allows you to specify the request type. In this case it is a `POST` request.
- `-d`: Stands for data and allows you to attach data to the request.
- `-H`: Stands for Headers and it allows you to pass additional information through the request. In this case it is used to the tell the server that the data is sent in a JSON format.

### Stop and clean and server

```bash
docker ps
dokcer stop name_of_container
```

To check out all images created you can use the following command:

```bash
docker images
```

Sometimes when checking all of your available images you will stumble upon some images with names and tags that have the value of none. These are intermediate images and if you see them listed when using the docker images command it is usually a good practice to prune them.

```bash
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
```
