# Use an official Node.js runtime as the base image
FROM node:16

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the application
COPY . .

# Set the environment variable for the backend API URL
ENV REACT_APP_BACKEND_URL=http://web:8000/api

# Expose the React development server port
EXPOSE 3000

# Start the React development server
CMD ["yarn", "start"]
