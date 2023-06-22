#Build chaque image (authentification, content)
docker build -t authentication_test -f Dockerfile_authentication_test .
docker build -t content_test -f Dockerfile_content_test .
#puis on compose
docker-compose up