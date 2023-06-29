import os
import requests

# définition de l'adresse de l'API
api_address = 'localhost'
# port de l'API
api_port = 8000

# requête pour le modèle v1
r_v1 = requests.get(
    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params={
        'username': 'bob',
        'password': 'builder',
        'sentence': 'This is a test sentence.'
    }
)

output_v1 = '''
============================
    Authorization test (v1)
============================

request done at "/v1/sentiment"
| username="bob"
| password="builder"
| sentence="This is a test sentence."

expected result = 200
actual result = {status_code}

==>  {test_status}

'''


status_code_v1 = r_v1.status_code


if status_code_v1 == 200:
    test_status_v1 = 'SUCCESS'
else:
    test_status_v1 = 'FAILURE'
print(output_v1.format(status_code=status_code_v1, test_status=test_status_v1))

if os.environ.get('LOG') == '1':
    with open('api_test.log', 'a') as file:
        file.write(output_v1)

'''
CMD ["python", "authorization_test.py"]
'''