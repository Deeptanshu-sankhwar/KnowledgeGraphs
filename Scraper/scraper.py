import pandas as pd
import requests
from bs4 import BeautifulSoup
import argparse
from pathlib import Path
import json

def scrape_faculty():
	html_page = requests.get('https://cse.iith.ac.in/people/faculty.html')
	soup = BeautifulSoup(html_page.text, 'html.parser')

	elements = soup.find_all(attrs = {'class' : 'faculty-col'})

	Faculty = []

	for element in elements:
		Faculty.append({
			'name': element.find('h3').text,
			'image': 'https://cse.iith.ac.in'+element.find(attrs={'class' : 'faculty-img'})['src'][2:],
			'website': element.find(attrs={'class' : 'faculty-link'})['href'],
			'position': element.find('h4').text,
			'office': element.find_all('h5')[0].text,
			'email': element.find_all('h5')[1].text,
			'domain': element.find_all('h5')[2].text
		})

	with open("faculty.json", "w") as outfile:  
	    json.dump(Faculty, outfile, indent=4) 

def scrape_staff():
	html_page = requests.get('https://cse.iith.ac.in/people/staff.html')
	soup = BeautifulSoup(html_page.text, 'html.parser')

	elements = soup.find_all(attrs = {'class' : 'col-sm-12 col-md-6'})
	
	Staff = []

	for element in elements:
		Staff.append({
			'name': element.find('h3').text,
			'image': 'https://cse.iith.ac.in'+element.find(attrs={'class' : 'faculty-img'})['src'][2:],
			'position': element.find('h4').text,
			'email': element.find_all('h5')[0].text,
		})

	with open("staff.json", "w") as outfile:  
	    json.dump(Staff, outfile, indent=4)

if __name__ == '__main__':
	