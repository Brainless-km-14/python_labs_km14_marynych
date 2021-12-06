import csv
with open('gorillaz.csv', 'w', newline='') as csvfile:
    fieldnames = ['Song','Year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Song": "Feel Good Inc",
                      "Year": "2016"})
    writer.writerow({"Song": "Clint Eastwood",
                      "Year": "2016"})
    writer.writerow({"Song": "Broken",
                      "Year": "2017"})
    writer.writerow({"Song": "Garage Palace",
                      "Year": "2017"})
    writer.writerow({"Song": "Hollywood",
                      "Year": "2018"})
with open("gorillaz.csv", newline = "") as csvfile:
    reader = csv.DictReader(csvfile)
    for heading in reader.fieldnames:
        print(heading, end=" ")
    print('\n------------------------------')
    for row in reader:
        print(row['Song'], row['Year'])