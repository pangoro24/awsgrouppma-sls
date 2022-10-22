import json
import traceback



def hello(event, context):
    ev = None
    try:
        ev = json.loads(event["body"])
    except TypeError:
        ev = json.loads(json.dumps(event["body"]))
    try:
        name = ev["name"]
        cloud = ev["cloud"]
        body = {
            "result": "{} uses {} as cloud provider".format(name,cloud),
        }
        print(body)
        return {"statusCode": 200, "body": json.dumps(body)}
    except Exception as error:
        body = {
            "result": "Error processing data",
            "error": error,
        }
        traceback.print_exc()
        return {"statusCode": 500, "body": json.dumps(body)}


