
import json
import boto3

codecommit = boto3.client('codecommit')

def lambda_handler(event, context):
    #Log the updated references from the event
    references = { reference['ref'] for reference in event['Records'][0]['codecommit']['references'] }
    print("References: "  + str(references))
    
    #Get the repository from the event and show its git clone URL
    repository = event['Records'][0]['eventSourceARN'].split(':')[5]
    try:
        response = codecommit.get_repository(repositoryName=repository)
        print("Clone URL: " +response['repositoryMetadata']['cloneUrlHttp'])
        return response['repositoryMetadata']['cloneUrlHttp']
    except Exception as e:
        print(e)
        print('Error getting repository {}. Make sure it exists and that your repository is in the same region as this function.'.format(repository))
        raise e

#unit test lambda code
# import json
# from LRLambda import lambda_function
# import unittest

# class TestLambdaHandler(unittest.TestCase):
#     def setUp(self):
#         self.event = {  "queryStringParameters": {
#                             "mode": "getDashboardList",
#                             "openIdToken": "RandomInvalidokenToVerifyValidationOfToken"
#                         }
#                     }

#     def test_lambda_handler(self):
#         print("testing the validation of openIdToken")
#         result = lambda_function.lambda_handler(self.event, '')
#         code = result["statusCode"]
#         print("data: ", code)
#         expected_response = 400
#         self.assertEqual(code, expected_response)