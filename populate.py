import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','learning_users.settings')

import django
# Import settings
django.setup()

import random
from basic_app.models import IntitutionModel

from django.utils.text import slugify
import pandas as pd

import csv

dataset=pd.read_csv('Book1.csv')

x = dataset.iloc[:,0]

print(x[0].strip())

z = []

for pu in x:
    z.append(pu.strip())


for tpq in z:
    webpg = IntitutionModel.objects.get_or_create(name=tpq,slug = slugify(tpq))[0]
