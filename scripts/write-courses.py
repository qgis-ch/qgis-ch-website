#!/usr/bin/env python3


import csv
import sys
from jinja2 import Environment, FileSystemLoader

def run():

    environment = Environment(loader=FileSystemLoader("./"))

    for lang in ( {"lang": "de", "dir": "kurse"}, {"lang": "fr", "dir": "cours"} ):
        data = []
	
        template = environment.get_template("template-%s.md" % lang['lang'])

        filename = "../_includes/courstable-%s.html" % (lang['lang'])

        with open("../_data/kurse-cours.csv", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            
            # Skip header row
            next(reader, None)
            
            for row in reader:
                data.append((row[0], row[1], row[2]))
        
        content = template.render(
            data=data
        )

        with open(filename, mode="w", encoding="utf-8") as message:
            message.write(content)
            print(f"... wrote {filename}")

if __name__ == "__main__":
    sys.exit(run())
