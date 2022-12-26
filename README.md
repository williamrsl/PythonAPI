# PythonAPI


Criando o bando de dados

docker pull mongo
docker run -v ~/docker --name mongodb -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=william -e MONGO_INITDB_ROOT_PASSWORD=1234 mongo
Connection String: mongodb://william:1234@localhost:27017/admin
