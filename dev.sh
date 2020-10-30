docker-compose up --build -d 
docker-compose exec web python manage.py makemigrations detective
docker-compose exec web python manage.py migrate
cd frontend 
yarn install 
yarn start
