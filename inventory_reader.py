def make_inventory():
    with open('./inventory.txt') as file:
        file.readline()
        lines = file.readlines()
    inventory = {}
    for line in lines:
        split_line = line.split(',')
        key = split_line[0].strip()
        value = float(split_line[1].strip())
        inventory[key] = value
        # inventory.update({key: value})
    return inventory


def main():
    inventory = make_inventory()
    for key, value in inventory.items():
        s = key + ' $' + str(value)
        print(s)

    item_name = input('which one? >>> ')
    print('price of', item_name, 'is', '$' + str(inventory.get(item_name)))


if __name__ == '__main__':
    main()
