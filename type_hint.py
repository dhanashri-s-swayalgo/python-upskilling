def get_full_name(first_name: str, last_name:str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("joen", "mark"))

def process_items(items: list[str]):
    for item in items:
        print(item)

list1 = ["a", "b", "c"]
print(process_items(list1))