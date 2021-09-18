# select a pre-existing image, a small one
FROM frolvlad/alpine-miniconda3:python3.7

# copy your local requirements.txt file into the image so it can be accessed by other processes
COPY requirements.txt .

# to run any command as you would on bash, use the RUN instruction
RUN pip install -r requirements.txt && \
	rm requirements.txt

# server will listen to requests on port 80
EXPOSE 80

# put your code within the image
COPY ./app /app

# spin up the server by specifying the host and port
# if without Docker you may do `uvicorn main:app --reload`
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]