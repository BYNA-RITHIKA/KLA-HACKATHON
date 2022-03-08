import yaml

with open(r'C:\folders\KLA Hackathon\Milestone1\Milestone1A.yaml') as file:
    documents = yaml.full_load(file)

    for item, doc in documents.items():
        print(item, ":", doc)
import datetime
now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"),end="")
print("000000")

