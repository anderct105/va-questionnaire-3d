FROM python:3.6

# Install linux packages
RUN apt-get update -qqq
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Create working directory
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# Copy contents
COPY . .

# Set python project path
ENV PYTHONPATH=/usr/src/app

# Execute main
CMD ["python3", "main.py"]
