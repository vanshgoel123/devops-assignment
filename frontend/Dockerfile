FROM node:18
# Set working directory
WORKDIR /app
# Copy package files first (better caching)
COPY package*.json ./
# Install dependencies
RUN npm install
# Copy all frontend files
COPY . .
# Build the Next.js website
RUN npm run build
# Expose frontend port
EXPOSE 3000
# Start Next.js in production
CMD ["npm", "start"]
