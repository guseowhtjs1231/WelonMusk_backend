import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "welonmusk.settings")
import django
django.setup()

from price.models import *

CSV_PATH = './car_interiors.csv'

with open(CSV_PATH, newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)

	for row in data_reader:
		print(row)
		CarInteriors.objects.create(
			interior_en_name = row['interior_en_name'],
			interior_ko_name = row['interior_ko_name'],
			img_url = row['img_url']
		)
