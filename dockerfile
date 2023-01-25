# syntax=docker/dockerfile:1
# start by pulling the python image
FROM python:3.8-alpine

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt
COPY . /app
WORKDIR /app



# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt



# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]