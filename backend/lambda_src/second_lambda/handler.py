def handler(event, context):
    return {
        "statusCode": 200,
        'body': 'second-test-lambda - ATUALIZADO VIA CODEBUILD!' 
    }
