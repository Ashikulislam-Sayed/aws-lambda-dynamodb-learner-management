
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("learners")


def lambda_handler(event, context):
    response = table.delete_item(
        Key={"learner_id": str(event["learner_id"])},
        ReturnValues="ALL_OLD"
    )

    deleted_item = response.get("Attributes")

    return {
        "statusCode": 200,
        "message": (
            "Learner deleted successfully"
            if deleted_item
            else "Learner not found"
        ),
        "deleted_item": deleted_item
    }

