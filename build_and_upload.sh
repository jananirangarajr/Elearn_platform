docker build  -t courses .
docker stop courses-container
docker rm courses-container
#docker run -d --name courses-container -p81:81 courses
#docker run -d --name courses-container --network mynetwork -p81:81 courses
#docker run --ip 172.18.0.2 courses-container
docker run --name courses-container --network new-network -d -p 8001:8001 courses