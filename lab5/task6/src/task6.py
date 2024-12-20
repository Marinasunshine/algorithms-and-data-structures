def priority_queue(operations):
    def heappush(heap, item):
        heap.append(item)
        heap.sort()

    def heappop(heap):
        return heap.pop(0) if heap else None

    queue = []
    results = []
    for i, operation in enumerate(operations):
        parts = operation.strip().split()
        if not parts:
            continue
        op_type = parts[0]
        if op_type == 'A':
            x = int(parts[1])
            heappush(queue, (x, i))
        elif op_type == 'X':
            min_elem = heappop(queue)
            if min_elem:
                results.append(str(min_elem[0]))
            else:
                results.append('*')
        elif op_type == 'D':
            idx = int(parts[1]) - 1
            new_val = int(parts[2])
            if idx < len(queue) and queue[idx][0] > new_val:
                queue[idx] = (new_val, i)

    return results
