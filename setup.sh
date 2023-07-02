LOGS_DIR="logs"
LOG_FILE="$LOGS_DIR/logs.txt"
exec > >(tee -a "$LOG_FILE") 2>&1
# Arrête et supprime les conteneurs existants
docker-compose down
#création du network
docker network create my_network
#Appel à l'image de l'api
docker image pull datascientest/fastapi:1.0.0
#docker container run -p 8000:8000 datascientest/fastapi:1.0.0
#Build chaque image (authentification, content)
docker build -t authentication_test -f Dockerfile_authentication_test .
docker build -t authorization_test -f Dockerfile_authorization_test .
docker build -t content_test -f Dockerfile_content_test .
#puis on compose
docker-compose up