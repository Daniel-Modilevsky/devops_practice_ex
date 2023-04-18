# Authentication-API

This repository contains a simple HTTP API server application written in Python that tests authentication.
Automated Testing and Deployment with Docker, Jenkins, Python, Flask, and Selenium


## API Endpoints

- GET '/login' - returns HTML page with authentication form.
- POST '/login' - Submit the form with user details.
- GET '/dashboard' - This route should display a dashboard that only authenticated users can access.



### Running the Application
The application is dockerized and can be easily run using docker-compose.

Run the following command to start the API server:

```bash
- Clone the repository to your local machine.

- Get the .env file for the connection string params (from author).

- Open a terminal window and navigate to the root directory of the cloned repository.

  $ docker-compose up
  
- This command will start the application server and the database. 
- Open the browser and navigate to http://localhost:5050.
```


