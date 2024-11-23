def h_index(citations):
    """Вычисление индекса Хирша"""
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] < i + 1:
            return i
    return len(citations)
