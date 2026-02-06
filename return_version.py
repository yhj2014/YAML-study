from yaml import safe_load

with open('version.yml', encoding='UTF-8') as f:
    v = safe_load(f)

print(v['VERSION'])