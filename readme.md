# Comando para ejecutar el proyecto
python -m uvicorn main:app --reload

# Dockerizar mysql si es necesario...
docker run --name mysql-dev -e MYSQL_ROOT_PASSWORD=123 -e MYSQL_DATABASE=libreriadb -p 3306:3306 -d mysql:latest

username -> root por default
puerto por default -> 3306 (cambiar puerto si hay problema, PUERTOLOCAL:PUERTODOCKER)