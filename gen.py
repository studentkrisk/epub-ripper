out = ""
for i in range(630):
    d = ""
    title = ""
    with open(f"chaps/chap{i}.html", "r") as f:
        d = f.read()
        # f.seek(0)
        d = d[d.index("<article"):d.index("</article") + len("</article")]
        title = d[d.index('<h1 class="entry-title">') + len('<h1 class="entry-title">'):d.index("</h1>")]
        d = list(filter(lambda x : x[:2] == "<p", d.split("\n")))
        # f.write(d)
        # f.truncate()
    out += f"<h1>{title}</h1>"
    out += "\n".join(d)
    print(i/630)
with open("out.html", "w") as f:
    f.write(out)

# print(subprocess.check_output([f"echo '{out}' | pandoc -f html -t epub -o apge.epub --metadata title='A Practical Guide to Evil'"]))