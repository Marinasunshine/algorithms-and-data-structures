def vote(data):
    votes = {}
    for line in data:
        candidate, vote_count = line
        vote_count = int(vote_count)
        if candidate in votes:
            votes[candidate] += vote_count
        else:
            votes[candidate] = vote_count
    sorted_candidates = sorted(votes.items())

    return sorted_candidates