docker build  -t user-auth .
docker stop user-auth-container
docker rm user-auth-container
#docker network create new-network --subnet 172.18.0.0/16
#docker run -d --name user-auth-container -p8080:8080 user-auth
docker run --name user-auth-container --network new-network -d -p 8080:8080 user-auth

