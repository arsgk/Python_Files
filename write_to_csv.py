import os
import csv
import sys


with open('Results.csv', mode='a') as csv_file:
    fieldnames = ['Image_Name', 'Number_Of_Hotspots','X_Coordinates','Y_Coordinates', 'Radius','Issue','Severity_Stage']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Image_Name': 'name', 'Number_Of_Hotspots': '-', 'X_Coordinates': '-','Y_Coordinates': '-','Radius':'-','Issue':'No issue detected','Severity_Stage':'-'} )
