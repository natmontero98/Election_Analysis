x = 0 
while x <= 5:
    print(x)
    x = x + 1 #we're incrementing x by 1, as long as it is equal or lower than 5

counties = ["Arapahoe", "Denver", "Jefferson"]

for county in counties:
    print(county)

#To get only the keys from a dictionary using the keys method...
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)
#it doesn't matter what variable name we use in the for loop with the keys method

for county in counties_dict:
    print(counties_dict.get(county))


for county, voters in counties_dict.items():
    print(county, voters)

#Get each dictionary in a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)


for county in range(len(voting_data)):
      print(voting_data[county]['county'])

#Get the values from a list of dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

#Using f-strings to print dictionaries
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters")