from calculations import add
import json

def lambda_handler(event, context):
    result = add(5, 3)
    return {
        "statusCode": 200,
        "body": f"Result is {result}"
    }