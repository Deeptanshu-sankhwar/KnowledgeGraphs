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
			'domain': element.find_all('h5')[2].text.split(', ')
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

def scrape_students(department):
	html_page_students = requests.get('https://cse.iith.ac.in/people/students.html')
	soup = BeautifulSoup(html_page_students.text, 'html.parser')

	elements = soup.find_all(attrs = {'class' : 'row'})
	if department == 'btech':
		elements = elements[0]
	elif department == 'mtech':
		elements = elements[1]
	elif department == 'phd':
		elements = elements[2]	
	elif department == 'alumni':
		elements = elements[3]

	links = ['https://cse.iith.ac.in'+item.get('onclick').split("'")[1] for item in elements.find(attrs = {'class' : 'panel'}).find_all('button')]

	Students = []

	for link in links:
		html_page = requests.get(link)
		soup = BeautifulSoup(html_page.text, 'html.parser')

		inner_elements = soup.find_all(attrs = {'class' : 'col-sm-6'})
		for inner_element in inner_elements:
			Students.append({
				'name': inner_element.find('h3').text,
				'RollNumber': inner_element.find('h5').text,
				'Year': link.split('/')[-1].split('.')[0]
				})

	with open("students_"+department+".json", "w") as outfile:  
	    json.dump(Students, outfile, indent=4)
	

def scrape_publications():
	html_page = requests.get('https://cse.iith.ac.in/research/publications.html')
	soup = BeautifulSoup(html_page.text, 'html.parser')

	years = [item.text for item in soup.find_all('h2')]
	elements = soup.find_all('ol')
	
	Publications = []

	i = 0
	for element in elements:
		inner_elements = element.find_all(attrs = {'class': 'bib-entry'})
		for inner_element in inner_elements:
			Publications.append({
				'Title': inner_element.text.replace("\n", "").replace("  ", "").strip().split(', ('+years[i]+').')[1],
				'Authors': inner_element.text.replace("\n", "").replace("  ", "").strip().split(', ('+years[i]+').')[0],
				'Link': inner_element.find('a')['href'],
				"Year": years[i]
				})
		i = i+1

	with open("Publications.json", "w") as outfile:  
	    json.dump(Publications, outfile, indent=4)


if __name__ == '__main__':