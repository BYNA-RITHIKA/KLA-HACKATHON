import yaml
import datetime
import json
def time():
    now = datetime.datetime.now()
    print (now.strftime("%Y-%m-%d %H:%M:%S"),end=" ")
    print("000000",end=" ")
        
with open(r'C:\folders\KLA Hackathon\Milestone1\Milestone1A.yaml') as file:
    documents = yaml.full_load(file)


with open('Userdetails.json', 'w') as f:
    json.dump(documents, f, sort_keys=False)
with open('Userdetails.json', 'r') as f:
    data = json.load(f)
    


    for i in data.keys():
        '''now = datetime.datetime.now()
        print (now.strftime("%Y-%m-%d %H:%M:%S"),end=" ")
        print("000000",end=" ")'''
        time()
        print(i + " Entry")


    
    
    act=data['M1A_Workflow']['Activities']
    for j in act.keys():
        time()
        print("M1A_Workflow"+"."+j+" Entry")
        time()
        exe=act['TaskA']['Inputs']
        print(exe['FunctionInput'])
        print(exe['ExecutionTime'])
       

        time()
        print("M1A_Workflow"+"."+j+" Exit")

    
