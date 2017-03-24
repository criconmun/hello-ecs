FROM python:2.7

# Create a working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Dependencies
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# Configure application
ENV BACKEND_URL="http://backend:5000"
EXPOSE 5000

# Install and run application
COPY app.py /usr/src/app
COPY templates/ /usr/src/app/templates
CMD [ "python", "./app.py" ]
