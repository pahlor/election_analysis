counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties." )
else:
    print("El Paso is not in the list of counties." )

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties." )
else: 
    print("Arapahoe or El Paso is not in the list of counties." )

for county in counties:
    print(county)

counties_dict = {"Arapahoe": 422289, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)
for voters in counties_dict.values():
    print(voters)

for county, voters in counties_dict.items():
    print(county, voters)

voting_data = [{"county": "Arapahoe", "registered_voters": 422829}, {"county": "Denver", "registered_voters": 463353}, {"county": "Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

candidate_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes. ")
print(message_to_candidate)



