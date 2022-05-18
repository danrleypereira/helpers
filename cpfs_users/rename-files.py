import json
import glob

read_files = glob.glob("mocked_users/*.json")
output_list = []

for f in read_files:
    with open(f, "rb") as infile:
        output_list.append(json.load(infile))

all_items = []
for json_file in output_list:
    all_items += json_file

textfile_merged = open('merged_json.json', 'w')
json.dump(all_items, textfile_merged)
textfile_merged.close()