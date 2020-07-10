class RockPaperScissorsLizardSpock:

    winnerMoves = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['paper', 'spock'],
        'spock': ['scissors', 'rock']
    }

    def play(self, player: str, cpu: str):
        choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        player = player.lower()
        cpu = cpu.lower()
        if player not in choices or cpu not in choices:
            return "Sorry, I didn't understand you! Make sure you wrote your choice well"
        if player == cpu:
            return 'Draw!'
        if cpu in self.winnerMoves[player]:
            return 'You win!'
        return 'You lose!'
