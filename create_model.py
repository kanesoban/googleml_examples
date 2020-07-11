import os
import argparse

from googleapiclient import discovery
from googleapiclient import errors


parser = argparse.ArgumentParser()
parser.add_argument('--project_id', required=True)
parser.add_argument('--credentials_path', required=True)
args = parser.parse_args()


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = args.credentials_path
project_id = args.project_id
'https://ml.googleapis.com/v1/projects/{}/models'.format(project_id)


model_name = 'tutorial_model'
request_dict = {'name': model_name, 'description': 'This is a machine learning model entry.'}

# Build a representation of the Cloud ML API.
ml = discovery.build('ml', 'v1')

request = ml.projects().models().create(parent='projects/{}'.format(project_id), body=request_dict)

try:
    response = request.execute()
    print(response)
except errors.HttpError as err:
    # Something went wrong, print out some information.
    print('There was an error creating the model. Check the details:')
    print(err._get_reason())
