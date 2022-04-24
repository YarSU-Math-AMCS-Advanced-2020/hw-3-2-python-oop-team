import Location

country, region, city, street, building = map(str, input().split())
apartments = int(input())
a = Location.Address(country, region, city, street, building, apartments)
s = a.get_location()
print(s)

