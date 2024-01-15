student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
student_grades={}
for i in student_scores:
  score=student_scores[i]
  if score>90:
    student_grades[i]="Outstanding"
  elif score>80:
    student_grades[i]="Exceeds Expectations"
  elif score>70:
    student_grades[i]="Acceptable"
  else:
    student_grades[i]="Fail"


print(student_grades)

travel_log={
    "France":{"cities visited":["Paris","Italy"],"no_of_times":12},
    "America":["New York","Mexico"]
}
print(travel_log)
print(travel_log["France"])


country = input("Enter the country name: ") # Add country name
visits = int(input("Enter the number of time you visited: ")) # Number of visits
list_of_cities=list(input("Enter the list of cities you visited: ").split())
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def add_new_country(country, visits, list_of_cities):
  new_country={}
  new_country["country"]=country
  new_country["visits"]=visits
  new_country["cities"]=list_of_cities
  travel_log.append(new_country)

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
