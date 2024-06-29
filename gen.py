import json
d = {}
with open("kemono_su_api.json", "r") as f:
    d = json.load(f)[::-1]
d = list(filter(lambda x : x['title'][:2] == "B4" or "Book 4" in x['title'], d))

with open("out2.html", "w") as f:
    for i in d:
        f.write(f"<h1>Chapter {d.index(i)+1}: {i['title'].replace(' - ', ': ').split(': ')[-1]}</h1>\n")
        f.write(i['content'])

# pandoc -f html -t epub -o ats4.epub --metadata title='All the Skills Book 4' out2.html