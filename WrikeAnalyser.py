import json
import codecs

byid = {}
tbyid = {}
parents = {}

with codecs.open('folders.json', "r", encoding="utf-8", errors="ignore") as json_file:
    data = json.load(json_file)
    for x in data:
        id = x['id']
        byid[id] = x
        for y in x['children']:
            parents[y] = id

    with codecs.open('tasks.json', "r", encoding="utf-8", errors="ignore") as json_file:
        data = json.load(json_file)
        for x in data:
            id = x['id']
            tbyid[id] = x

    def showchildren(pid, indent):
        for y in byid[pid]['children']:
            if y in byid:
                print("| "*indent, end='')
                print("📁 "+byid[y]['title'])
                showchildren(y, indent+1)
            elif y in tbyid:
                print("| "*indent, end='')
                print("📝 "+tbyid[y]['title'])
                tbyid[y]['printed'] = True
            else:
                print("⚠️ MISSING ", end='')
                print(y)

    for x in byid:
        if not byid[x]['id'] in parents:
            print("📁 "+byid[x]['title'])
            showchildren(byid[x]['id'],1)

    print()
    print("Not in 📁s:")
    for x in tbyid:
        if not 'printed' in tbyid[x]:
            print("📝 " + tbyid[x]['title'])