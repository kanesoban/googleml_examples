from oauth2client.client import GoogleCredentials
from googleapiclient import discovery
from googleapiclient import errors

project_id = 'tensorflow-course-256109'
'https://ml.googleapis.com/v1/projects/{}/models'.format(project_id)

# project_id = 'projects/{}'.format('your_project_ID')

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
