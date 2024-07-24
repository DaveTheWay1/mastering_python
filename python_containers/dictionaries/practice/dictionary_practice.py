where_my_things_are = {

}
print(len(where_my_things_are))

where_my_things_are["backpack"] = "living room"
where_my_things_are["work clothes"] = "bedroom"
where_my_things_are["shoes"] = "closet"
print(where_my_things_are)

print(where_my_things_are.items())

for key,value in where_my_things_are.items():
  if key == "work clothes":
    where_my_things_are["work clothes"] = "laundry bag"
    print(f"my {key} is in the {value}")
  else:
    print(f"my {key} is in the {value}")

print(where_my_things_are)