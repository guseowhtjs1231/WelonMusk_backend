import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "welonmusk.settings")
import django
django.setup()

from price.models import *

CSV_PATH = './car_autopilot.csv'

with open(CSV_PATH, newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)

	for row in data_reader:
		print(row)
		CarAutoPilots.objects.create(
			autopilot_price = row['autopilot_price']
		)
