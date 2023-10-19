
# A Dynamic Cloud-Based Application with Django and AWS Cloud Services


This is a cloud web application project that leverages AWS services to create a scalable and reliable web application. It used services like Elastic Beanstalk, S3, and AWS CodePipeline for implementation.

## Table of Contents
- [Overview](#overview)
- [Non-Functional Requirements](#non-functional-requirements)
- [Functional Requirements](#functional-requirements)
- [Getting Started](#getting-started)
- [Deployment](#deployment)

## Overview

This web application project is designed to showcase the capabilities of AWS services in creating a scalable and efficient web application. It uses Elastic Beanstalk for deployment and scaling, S3 for storage, and AWS CodePipeline for continuous integration and continuous deployment (CI/CD).

## Non-Functional Requirements
These are general conditions that the application must meet for users to have an optimal experience. The following are the non-functional requirements that have been considered for this application:

- **Performance**: Optimize the application's performance for responsiveness and minimal latency.

- **Scalability**: Elastic Beanstalk makes it easy to scale the application as traffic grows. This means that if an application experiences a sudden increase in traffic, Elastic Beanstalk will automatically add more resources (e.g., EC2 instances) to ensure that the application can continue to handle the increased load without crashing or experiencing significant delays. This will only come into play when the performance gain optimization approach has been exhausted.

- **Reliability**: Implement best practices to ensure the application is available and reliable.

## Functional Requirements

- **User Authentication**: Implement user authentication and authorization for account creation.
  
-  **Search Query**: Search for other users based on certain queries like creator's name and content

-  **Review**: Leave a review on another user's content

- **Data Storage**: Store and retrieve user data and content from Amazon S3.


## Getting Started

To get started on this project, follow these steps:

1. Clone the repository to your local machine.

2. Set up your AWS account and configure your credentials.

3. Install the required dependencies by running `pip install -r requirements.txt`.

4. Replace the following with your details:
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''
It is advisable to create an env file to store the variable details. 

## Deployment

The deployment of this project is fully automated through AWS CodePipeline. Any changes you push to the repository trigger a build and deployment process. You can also manually trigger the pipeline to deploy the latest changes to your Elastic Beanstalk environment.





