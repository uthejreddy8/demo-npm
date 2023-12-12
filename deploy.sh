#!/bin/bash

# Stop any running services (replace 'your-service' with the actual service name)
sudo systemctl stop your-service

# Update the application code
cp -r /home/ubuntu/project/* /home/ubuntu/project/

# Start the services again
sudo systemctl start your-service

# Additional deployment steps as needed
