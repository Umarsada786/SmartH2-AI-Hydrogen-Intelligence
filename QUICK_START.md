# Quick Start Guide

## Installation Steps
1. Ensure you have Docker and Docker Compose installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/Umarsada786/SmartH2-AI-Hydrogen-Intelligence.git
   cd SmartH2-AI-Hydrogen-Intelligence
   ```
3. Build the images:
   ```bash
   docker-compose build
   ```

## Configuration
- Adjust the `.env` file to set your configurations.
- Ensure the necessary environment variables are set according to your needs.

## Usage Examples
### Using Docker Compose
1. Start the application with Docker Compose:
   ```bash
   docker-compose up
   ```
2. Access the service through your browser at `http://localhost:YOUR_PORT`

### Manual Setup
1. If you prefer manual setup, install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Access the service through your browser at `http://localhost:YOUR_PORT`
   
---
Please refer to the documentation for more detailed instructions!