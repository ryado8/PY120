class Candidate:

    def __init__(self, name):
        self._name = name
        self._votes = 0

    @property
    def name(self):
        return self._name

    @property
    def votes(self):
        return self._votes

    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        self._votes += other
        return self


class Election:

    def __init__(self, candidates):
        self._candidates = candidates

    def _determine_winner(self):
        return sorted(list(self._candidates), key = lambda candidate: candidate.votes, reverse = True)[0]

    def results(self):
        total_votes = 0
        winner = self._determine_winner()
        for candidate in self._candidates:
            total_votes += candidate.votes
            print(f"{candidate.name}: {candidate.votes} votes")
        print('')
        print(f"{winner.name} won: {(winner.votes / total_votes) * 100:.1f}% of votes ")


mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()

# Mike Jones: 3 votes
# Susan Dore: 4 votes
# Kim Waters: 1 votes

# Susan Dore won: 50.0% of votes