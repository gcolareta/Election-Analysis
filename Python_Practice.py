from __future__ import print_function


print('Hello World')
counties = list()
counties = ["Arapahoe", "Denver", "Jefferson"]
print(counties)
print(counties[0])
print(counties[2])  
print(counties[0:2])
counties.append("El Paso")
print(counties)
counties.insert(2, "El Paso")
print(counties)
counties.remove("El Paso")
counties.pop(3)
print(counties)
counties.insert(1, "El Paso")
counties.pop(0)
print(counties)
counties.remove("Denver")
counties.append("Denver")
print(counties)
counties.append("Arapahoe")
print(counties)
counties_dict = {}
counties_dict['Arapahoe'] = 422829
print(counties_dict)
counties_dict['Denver'] = 463353
counties_dict['Jefferson'] = 432438
print(counties_dict)
len(counties_dict)
print(len(counties_dict))
counties_dict.items()
print(counties_dict.items())
counties_dict.keys()
print(counties_dict.keys())
counties_dict.values()
print(counties_dict.values())
voting_data = []
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
voting_data.append({"county": "Denver", "registered_voters": 463353})
voting_data.append({"county": "Jefferson", "registered_voters": 432438})
print(voting_data)
voting_data.insert(1, {"county":"El Paso", "registered_voters":461149})
print(voting_data)
voting_data.pop(0)
print(voting_data)
voting_data.pop(1)
voting_data.insert(2, {"county":"Denver", "registered_voters":463353})
print(voting_data)
voting_data.append({"county":"Arapahoe", "registered_voters":422829})
print(voting_data)

counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties")
else:
    print("Arapahoe or El Paso are not in the list of counties")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties")
else:
    print("Arapahoe and El Paso are not in the list of counties")

for county in counties:
    print(county)

for county in range(3):
    print(county)

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys():
    print(county)

for county in counties_dict:
    print(counties_dict[county])

for county, voters in counties_dict.items():
    print(county, voters)

for k, v in counties_dict.items():
    print(k, "county has", v, "registered voters")

voting_data = []
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
voting_data.append({"county": "Denver", "registered_voters": 463353})
voting_data.append({"county": "Jefferson", "registered_voters": 432438})
print(voting_data)

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i])

for i in range(len(voting_data)):
    print(voting_data[i]["county"])

for i in range(len(voting_data)):
    print(voting_data[i])

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    print(county_dict["registered_voters"])

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters")


print(voting_data)
for county_dict in voting_data:
    print(
        f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters")

# if-else statement
temperature = int(input("What is the Temperature Outside?"))
if temperature > 80:
    print("Turn on the AC")
else:
    print("Open the window")

# while loop
x = 0
while x <= 4:
    print(x)
    x = x + 1

#count = 7
# while count < 1:
    # print("Hello World")
