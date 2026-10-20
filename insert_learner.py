
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("learners")


def lambda_handler(event, context):
    item = {
        "learner_id": str(event["learner_id"]),
        "name": event["name"],
        "location": event["location"]
    }

    table.put_item(Item=item)

    return {
        "statusCode": 200,
        "message": "Learner inserted successfully",
        "item": item
    }
