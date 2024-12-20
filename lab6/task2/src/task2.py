def phonebook_manager(numbers):
    phonebook = {}
    results = []

    for num in numbers:
        part = num
        command = part[0]
        if command == 'add':
            number, name = part[1], part[2]
            phonebook[number] = name
        elif command == 'del':
            number = part[1]
            phonebook.pop(number, None)
        elif command == 'find':
            number = part[1]
            results.append(phonebook.get(number, 'not found'))

    return results