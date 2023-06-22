import os
import requests

# définition de l'adresse de l'API
api_address = 'localhost'
# port de l'API
api_port = 8000

# requête
r = requests.get(
    url='http://{address}:{port}/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'bob',
        'password': 'builder',
        'sentence': 'This is a test sentence.'
    }
)

output = '''
============================
    Authentication test
============================

request done at "/sentiment"
| username="bob"
| password="builder"
| sentence="This is a test sentence."

expected result = 200
actual result = {status_code}

==>  {test_status}


'''


# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output)