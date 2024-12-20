def array_command(operations):
    data = {}
    order = {}
    head, tail = None, None
    result = []

    def insert_key(key):
        nonlocal head, tail
        if key in order:
            return
        order[key] = [tail, None]
        if tail:
            order[tail][1] = key
        tail = key
        if head is None:
            head = key

    def remove_key(key):
        nonlocal head, tail
        if key not in order:
            return
        prev_key, next_key = order.pop(key)
        if prev_key is not None:
            order[prev_key][1] = next_key
        if next_key is not None:
            order[next_key][0] = prev_key
        if key == head:
            head = next_key
        if key == tail:
            tail = prev_key

    def find_prev(key):
        if key not in order or order[key][0] is None:
            return "<none>"
        return data[order[key][0]]

    def find_next(key):
        if key not in order or order[key][1] is None:
            return "<none>"
        return data[order[key][1]]

    for op in operations:
        parts = op
        cmd, key = parts[0], parts[1]
        if cmd == "put":
            value = parts[2]
            if key not in data:
                insert_key(key)
            data[key] = value
        elif cmd == "get":
            result.append(data.get(key, "<none>"))
        elif cmd == "delete":
            if key in data:
                data.pop(key)
                remove_key(key)
        elif cmd == "prev":
            result.append(find_prev(key))
        elif cmd == "next":
            result.append(find_next(key))

    return result
