rivers = {
    'nile': 'egypt',
    'siene': 'paris',
    'ravi': 'india',
    'satluj': 'india',
}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

#print rivers only
for river in sorted(rivers.keys()):
    print(river.title())

#print countries only
for country in sorted(set(rivers.values())):
    print(country.title())
