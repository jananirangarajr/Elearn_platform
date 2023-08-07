docker build  -t elearn .
docker stop elearn-container
docker rm elearn-container
docker run --name elearn-container --network new-network -d -p 8089:8089 elearn
