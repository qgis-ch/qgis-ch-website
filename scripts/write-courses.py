#!/usr/bin/env python3
#
#

import csv
from datetime import date
from jinja2 import Environment, FileSystemLoader
import sys

def run():

    environment = Environment(loader=FileSystemLoader("./"))

    for lang in ( "de", "fr" ):
        data = []

        # Get the jinia template to render HTML
        template = environment.get_template(f"template-%s.html" % lang)

        filename = f"../_includes/courstable-%s.html" % (lang)

        with open(f"../_data/kurse-cours.csv", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            
            # Skip header row
            next(reader, None)
            
            for row in reader:
                # Parse date
                # Date in CSV file must be in 'dd-mm-YYYY'
                date_cours = date(int(row[0].split(".")[2]),
                                  int(row[0].split(".")[1]),
                                  int(row[0].split(".")[0]))
                # Get today's date
                today = date.today()

                # Check if cours is in the future
                if today < date_cours:
                    match lang:
                        # Append the second column for German site
                        case "de":
                            data.append((row[0], row[1], row[3]))
                        # Append the third column for French site
                        case "fr":
                            data.append((row[0], row[2], row[3]))

        # Render the template with the data
        content = template.render(
            data=data
        )

        # Open the output file to write the rendered template
        with open(filename, mode="w", encoding="utf-8") as message:
            message.write(content)
            print(f"... wrote {filename}")

    return 0

if __name__ == "__main__":
    sys.exit(run())
