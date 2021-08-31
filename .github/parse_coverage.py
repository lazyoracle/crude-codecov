import xml.etree.ElementTree as ET
import json
import os

coverage_file = os.path.join(os.getcwd(), "tests", "cov.xml")
root = ET.parse(coverage_file).getroot()

filter_keys = ["lines-valid", "lines-covered", "line-rate"]

coverage_data = {key: value for key, value in root.attrib.items() if key in filter_keys}

print(coverage_data)

with open("coverage_data.json", "w") as outfile:
    json.dump(coverage_data, outfile)
