
import json
import decimalencoder
import todoList


def translate_text(event, context):
     # create a response
    item = todoList.translate(event['pathParameters']['id'])
    if item:
        response = {
            "statusCode": 200,
            "body": json.dumps(item,
                               cls=decimalencoder.DecimalEncoder)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    return response