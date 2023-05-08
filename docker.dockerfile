FROM python:3.9-slim

# Install required packages
RUN apt-get update && \
    apt-get install -y python3-tk

# Set environment variables for displaying X11 windows
ENV DISPLAY=:0
ENV XAUTHORITY=/tmp/.docker.xauth

# Copy your Python script to the container
COPY my_app.py /app/my_app.py

# Set the working directory
WORKDIR /app

#install the required files
RUN apt-get install python3-pip
run sudo apt-get install libgl1-mesa-glx
RUN apt-get install -y python3-tk
run pip install pyqt5
run pip install keyboard
run pip install pyqtwebengine
run pip install prompt_toolkit

RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libxrandr2 \
    libxcursor1 \
    libxi6 \
    libxtst6 \
    libssl-dev \
    libxcb-render0-dev \
    libffi-dev \
    libxcb-shm0-dev \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y libxcomposite1 libxcursor1 libxdamage1 libxfixes3 libxi6 libxrandr2 libxtst6 libnss3 libgconf-2-4 libasound2 libatk1.0-0 libcups2 libdbus-1-3 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libx11-xcb1 libxcb-dri3-0 libxcb1 libxkbcommon0 libxss1 libxt6 libgbm1 && \
    apt-get install -y python3-pyqt5.qtwebenginewidgets


# Run your Python script
CMD ["python", "shell.py"]



