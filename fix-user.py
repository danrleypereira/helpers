import json
import random

users_file = "./merged_json.json"

with open(users_file) as json_file:
    users_json = json.load(json_file)

with open("./cpfs.json") as json_file:
    cpfs_json = json.load(json_file)


rolesSet = [
    {
        "admin": True,
        "app:maker": True
    },
    {
        "app:maker": True
    },
    {
        "professor": True
    },
    {
        "coordinator": True
    },
    {
        "admin": True
    },
    {
        "student": True
    },
    {
        "professor": True,
        "coordinator": False
    },
    {
        "coordinator": False
    },
    {
        "apps:admin": True
    },
    {
        "professor": True,
        "apps:admin": True
    },
    {
        "guardian": True
    }
]


cpf_length = len(cpfs_json)-1

i = 0
# while(i< len(users_json)-1):
#     i+=1
#     print(users_json[i])


for user in users_json:
    user["active"] = True
    user["setRoles"] = {}
    user["rolesSet"] = rolesSet[random.randint(0, len(rolesSet)-1)]
    user["fields"] = {}
    i = i+1 if i < cpf_length else 1
    user["cpf"] = cpfs_json[i]
    print(user)


with open(users_file, 'w') as json_file:
    json.dump(users_json, json_file)