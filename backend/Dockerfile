FROM python:2.7

# Create a working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Dependencies
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# Configure application
ENV MOTD="Hello out there!"
EXPOSE 5000

# Install and run application
COPY app.py /usr/src/app
CMD [ "python", "./app.py" ]
