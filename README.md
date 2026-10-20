# AWS Lambda and DynamoDB Learner Management

## Project Overview

This project demonstrates serverless database operations using AWS Lambda, Python, Boto3, and Amazon DynamoDB.

It contains three Lambda handler examples for managing learner records.

## Features

- **Insert Learner:** Adds a learner record to DynamoDB.
- **Show Learner:** Retrieves a learner by ID.
- **Delete Learner:** Deletes a learner by ID.

## Technologies Used

- AWS Lambda
- Amazon DynamoDB
- Python
- Boto3
- Git and GitHub

## Project Structure

```text
aws-lambda-dynamodb-learner-management/
├── lambda_function.py
├── insert_learner.py
├── delete_learner.py
├── README.md
└── screenshots/
```

## DynamoDB Table

Table name: `learners`

Partition key: `learner_id`

The partition key configuration must match the actual DynamoDB table.

## Example Insert Event

```json
{
  "learner_id": "2",
  "name": "Ashikul Islam",
  "location": "Chittagong"
}
```

## Learning Outcomes

- Working with event-driven AWS Lambda functions
- Reading and writing DynamoDB records using Boto3
- Understanding basic serverless application design
- Practicing Git and GitHub project documentation

## Security

AWS credentials and sensitive configuration values should never be committed to this repository.

## Project Status

Learning project. Deployment and testing status should be updated as each operation is verified.
