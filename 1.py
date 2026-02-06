import yaml

with open('data.yml', 'r') as file:
    data = yaml.safe_load(file)

print(f"Name is {data['name']}")
print(f"Age is {data['age']}")
print(f"Hobby is {data['hobby']}")