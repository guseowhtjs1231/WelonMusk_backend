import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "welonmusk.settings")
import django
django.setup()

from price.models import *

CSV_PATH = './car_type.csv'

with open(CSV_PATH, newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)

	for row in data_reader:
		print(row)
		CarTypes.objects.create(
			model_type = row['model_type']
		)

