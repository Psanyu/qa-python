child1 = {"name" : "Emily", "year" : 2004}
child2 = {"name" : "Tobias","year" : 2007}
child3 = {"name" : "Linus","year" : 2011}

myfamily = {"child1" : child1,"child2" : child2,"child3" : child3}

print(myfamily["child2"]["name"])
print(myfamily["child1"]["name"])
print(myfamily["child3"]["name"])

print(myfamily["child2"]["year"])
print(myfamily["child1"]["year"])
print(myfamily["child3"]["year"])

print(myfamily["child2"])
print(myfamily["child1"])
print(myfamily["child3"])

print(len(myfamily))
print(type(child1))
print(type(child2))
print(type(child3))
print(myfamily["child1"].get("name"))
print(myfamily["child1"].get("year"))
print(myfamily["child2"].get("name"))
print(myfamily["child1"].keys())
print(myfamily["child1"].values())
print(myfamily["child1"].items())
myfamily["child1"].pop("name")
print(myfamily["child1"])
myfamily["child1"].update({"name": "Daniel"})
print(myfamily["child1"])
myfamily.update({"child4":{"name": "Sophia","year":2020}})
print(myfamily["child4"])
