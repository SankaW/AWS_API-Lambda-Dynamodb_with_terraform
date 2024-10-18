<h1>AWS Serverless Data Logging with DynamoDB, Lambda, and API Gateway</h1>

## Fully Serverless Backend with Terraform 

This project demonstrates how to build a fully serverless backend using AWS Lambda, API Gateway, and DynamoDB, all provisioned and managed through Terraform, an Infrastructure as Code (IaC) tool. The serverless architecture ensures scalability, cost-effectiveness, and minimal management overhead, while Terraform allows for streamlined resource provisioning and easy reuse of code. 

By leveraging Terraform, the entire infrastructure can be defined in code, making it simple to replicate or modify the project for similar use cases with minimal changes. This approach not only improves efficiency but also enhances visibility into the resources used by the application, ensuring optimal resource management and enabling quick adjustments to meet varying project needs.

The reusability of the Terraform modules allows you to deploy similar serverless applications in just a few steps, making this project an excellent foundation for creating, managing, and scaling serverless services.


## Prerequisites

Before deploying this project, ensure you have the following set up:

1. **AWS Account**  
   You will need an active AWS account to provision the required services, such as Lambda, API Gateway, and DynamoDB.

2. **AWS CLI**  
   Install the [AWS CLI](https://aws.amazon.com/cli/) and configure it with your AWS user credentials. This ensures that Terraform can communicate with your AWS environment.
   
   To configure the AWS CLI, run the following command and follow the prompts to enter your AWS access key, secret key, and default region:
  
3. **Terraform CLI** 
    Install the Terraform CLI to define and manage your infrastructure as code. Ensure that it's properly configured to interact with your AWS account.

3. **Basic Python Knowledge**
    Familiarity with Python is required to write and understand the AWS Lambda function used in this project. This project includes a Lambda function written in Python to handle serverless logic.


![Architecture Diagram](Architecture.webp "System Architecture")
