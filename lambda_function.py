
import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("learners")


def lambda_handler(event, context):
    learner_id = str(event["learner_id"])
    name = event["name"]
    location = event["location"]

    table.put_item(
        Item={
            "learner_id": learner_id,
            "name": name,
            "location": location
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Learner inserted successfully",
            "learner": {
                "learner_id": learner_id,
                "name": name,
                "location": location
            }
        })
    }

import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("learners")


def lambda_handler(event, context):
    print(event["message"])

    response = table.get_item(
        Key={"learner_id": str(event["learner_id"])}
    )

    item = response.get("Item")

    print(item)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": event["message"],
            "learner": item
        }, default=str)
    }
