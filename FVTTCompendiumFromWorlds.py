# this creates a module from worlds and iterates it into a compendium.
# put this in /Data/ directory and run it with python3 FVTTCompendiumFromWorlds.py

# go through data/worlds and extract the databases and files to generate a compendium mod
import os
import json
BigDict = dict()
path = ".\\worlds"
for root, dirs, files in os.walk(path):
    for file in files:
        if(file.endswith(".db")):
            print(root + "\\" + file)
            myfile = open(root + "\\" + file, encoding="utf8")
            myline = myfile.readline()
            try:
                while myline:
                    myline = myfile.readline()
                    myjson = json.loads(myline)
                    BigDict[myjson['type']] = list()
            except (KeyError, json.decoder.JSONDecodeError):
                pass
            myfile.close()

for root, dirs, files in os.walk(path):
    for file in files:
        if(file.endswith(".db")):
            print(root + "\\" + file)
            myfile = open(root + "\\" + file, encoding="utf8")
            myline = myfile.readline()
            try:
                while myline:
                    myline = myfile.readline()
                    myjson = json.loads(myline)
                    BigDict[myjson['type']].append(myline)
                    # print(myline)
            except (KeyError, json.decoder.JSONDecodeError):
                pass
            myfile.close()

try:
    os.mkdir(".\\modules\\AutoGenerated\\")
except:
    pass

for k, v in BigDict.items():
    print(k, len(v))
    try:
        os.remove(".\\modules\\AutoGenerated\\" + k + '.db')
    except:
        pass
    with open(".\\modules\\AutoGenerated\\" + k + '.db', 'a', encoding="utf8") as the_file:
        for line in v:
            the_file.write(line)

# defines a pack that needs to be added to the main module.json
pack = {
      "name": "",
      "label": "",
      "system": "dnd5e",
      "path": "",
      "entity": ""
}
# the main module.json
module = {
  "name": "AutoGenerated",
  "title": "AutoGenerated",
  "description": "AutoGenerated",
  "version": "0.01",
  "author": "Andrew",
  "manifest": "",
  "download": "",
  "systems": ["dnd5e"],
  "scripts": [],
  "styles": [],
  "packs": [],
  "minimumCoreVersion": "0.6.5",
  "compatibleCoreVersion": "0.6.5"
}
for k, v in BigDict.items():
    pack = {
      "name": "",
      "label": "",
      "system": "dnd5e",
      "path": "",
      "entity": ""
    }
    pack['name'] = str(k)
    pack['label'] = str(k)
    pack['path'] = str(k) + '.db'
    if k == "Actor":
        pack['entity'] = "Actor"
    elif k == "JournalEntry":
        pack['entity'] = "JournalEntry"
    else:
        pack['entity'] = "Item"
    module['packs'].append(pack)

try:
    os.remove(".\\modules\\AutoGenerated\\module.json")
except:
    pass

with open(".\\modules\\AutoGenerated\\module.json", 'a', encoding="utf8") as the_file:
    the_file.write(json.dumps(module, indent=4))
