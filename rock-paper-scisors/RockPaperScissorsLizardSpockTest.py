import unittest
from RockPaperScissorsLizardSpock import RockPaperScissorsLizardSpock

class MyTestCase(unittest.TestCase):
    def test_is_NOT_case_sensitive(self):
        rspls = RockPaperScissorsLizardSpock()
        self.assertEqual(rspls.play('rock', 'Paper'), 'You lose!')
        self.assertEqual(rspls.play('rOcK', 'papeR'), 'You lose!')

    def test_prints_a_feedback_message_when_wrong_arguments_passed(self):
        rspls = RockPaperScissorsLizardSpock()
        self.assertEqual(rspls.play('umpalumpa', 'scissors'), "Sorry, I didn't understand you! Make sure you wrote your choice well")
        self.assertEqual(rspls.play('pedra', 'paper'), "Sorry, I didn't understand you! Make sure you wrote your choice well")

    def test_outputs_draw_when_both_players_make_same_choice(self):
        rspls = RockPaperScissorsLizardSpock()
        self.assertEqual(rspls.play('rock', 'rock'), 'Draw!')
        self.assertEqual(rspls.play('spock', 'spock'), 'Draw!')

    def test_player1_win_when_chooses_rock_and_cpu_choose_scissors_or_lizard(self):
        rspls = RockPaperScissorsLizardSpock()
        self.assertEqual(rspls.play('rock', 'scissors'), 'You win!')
        self.assertEqual(rspls.play('rock', 'lizard'), 'You win!')

    def test_player1_win_when_chooses_paper_and_cpu_choose_rock_or_spock(self):
        rspls = RockPaperScissorsLizardSpock()
        self.assertEqual(rspls.play('paper', 'rock'), 'You win!')
        self.assertEqual(rspls.play('paper', 'spock'), 'You win!')

    def test_player1_win_when_chooses_scissors_and_cpu_choose_paper_or_lizard(self):
        rspls = RockPaperScissorsLizardSpock()
        self.assertEqual(rspls.play('scissors', 'paper'), 'You win!')
        self.assertEqual(rspls.play('scissors', 'lizard'), 'You win!')

    def test_player1_win_when_chooses_lizard_and_cpu_choose_paper_or_spock(self):
        rspls = RockPaperScissorsLizardSpock()
        self.assertEqual(rspls.play('lizard', 'paper'), 'You win!')
        self.assertEqual(rspls.play('lizard', 'spock'), 'You win!')

    def test_player1_win_when_chooses_spock_and_cpu_choose_scissors_or_rock(self):
        rspls = RockPaperScissorsLizardSpock()
        self.assertEqual(rspls.play('spock', 'scissors'), 'You win!')
        self.assertEqual(rspls.play('spock', 'rock'), 'You win!')

    def test_player1_loses_when_chooses_spock_and_cpu_choose_lizard_or_paper(self):
        rspls = RockPaperScissorsLizardSpock()
        self.assertEqual(rspls.play('spock', 'lizard'), 'You lose!')
        self.assertEqual(rspls.play('spock', 'paper'), 'You lose!')

    def test_player1_loses_when_chooses_lizard_and_cpu_choose_rock_or_scissors(self):
        rspls = RockPaperScissorsLizardSpock()
        self.assertEqual(rspls.play('lizard', 'rock'), 'You lose!')
        self.assertEqual(rspls.play('lizard', 'scissors'), 'You lose!')

    def test_player1_loses_when_chooses_scissors_and_cpu_choose_rock_or_spock(self):
        rspls = RockPaperScissorsLizardSpock()
        self.assertEqual(rspls.play('scissors', 'rock'), 'You lose!')
        self.assertEqual(rspls.play('scissors', 'spock'), 'You lose!')

    def test_player1_loses_when_chooses_paper_and_cpu_choose_scissors_or_lizard(self):
        rspls = RockPaperScissorsLizardSpock()
        self.assertEqual(rspls.play('paper', 'scissors'), 'You lose!')
        self.assertEqual(rspls.play('paper', 'lizard'), 'You lose!')

    def test_player1_loses_when_chooses_rock_and_cpu_choose_paper_or_spock(self):
        rspls = RockPaperScissorsLizardSpock()
        self.assertEqual(rspls.play('rock', 'paper'), 'You lose!')
        self.assertEqual(rspls.play('rock', 'spock'), 'You lose!')


if __name__ == '__main__':
    unittest.main()
