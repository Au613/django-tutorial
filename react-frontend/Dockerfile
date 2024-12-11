# Use an official Node.js runtime as the base image
FROM node:16

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the application
COPY . .

# Expose the React development server port
EXPOSE 3000

# Start the React development server
CMD ["yarn", "start"]
