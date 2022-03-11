import boto3
import simplejson as json #Makes dynamodb decimal value serializable

# import requests

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    __TableName__ = 'cloud-resume-challenge'
    Primary_Column_Name = 'ID'
    
    DB = boto3.resource('dynamodb')
    table = DB.Table(__TableName__)

    Primary_Key = 'visitors'
    ID = 'visitors'
    
    response = table.get_item(
        Key={
            'ID': ID
        }
    )

    item = response["Item"]
    print(item)
    
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "headers": {
            "Access-Control-Allow-Origin":  "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*",
        },
        "statusCode": 200,
        "body": json.dumps({
            "count": item['Visitors']
            # "location": ip.text.replace("\n", "")
        }),
    }