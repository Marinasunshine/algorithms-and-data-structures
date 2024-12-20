def process_packets(S, packets):
    finish_time = []
    result = []

    for Ai, Pi in packets:
        finish_time = [t for t in finish_time if t > Ai]
        if len(finish_time) >= S:
            result.append(-1)
        else:
            if not finish_time:
                start_time = Ai
            else:
                start_time = finish_time[-1]

            finish_time.append(start_time + Pi)
            result.append(start_time)

    return result