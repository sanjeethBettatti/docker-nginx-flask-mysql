docker ps -q -a | xargs docker rm -f
docker-compose up --build
