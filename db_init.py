# create database tesla character set utf8mb4 collate utf8mb4_general_ci;
import os

a = os.system('find . -path "*/migrations/*.py"')
print(a)
b = os.system('find . -path "*/migrations/*.py" -not -name "__init__.py" -delete')
print(b)

os.system('python manage.py makemigrations')
os.system('python manage.py migrate')

os.system('python initialize_total_database.py')




# select * from car_modes; select * from car_types; select * from car_type_prices; select * from car_colors; select * from car_color_prices; select * from car_wheels; select * from car_wheel_prices; select * from car_wheel_prices;