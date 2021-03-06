import unittest
from training.agent import Agent


class TestAgent(unittest.TestCase):

    def test_add_state(self):

        state1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]]
        state2 = [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0.75]]
        state3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]]
        state4 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.8]]
        state5 = [[0, 0, 0, 0, 0, -1, 0, 0, 0], [0.5]]

        agent = Agent(1)
        agent.add_state(state1)
        agent.add_state(state2)
        agent.add_state(state3)
        agent.add_state(state4)
        agent.add_state(state5)

        self.assertEqual(len(agent.states), 5)

    def test_next_states(self):

        board = [1, 0, 0, 0, 0, -1, 0, 0, 0]

        state1 = [[1, 0, 0, 1, 0, -1, 0, 0, 0], [0.5]]
        state2 = [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0.75]]
        state3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]]
        state4 = [[1, 0, 0, 0, 0, -1, 0, 1, 0], [0.8]]

        agent = Agent(1)
        agent.add_state(state1)
        agent.add_state(state2)
        agent.add_state(state3)
        agent.add_state(state4)

        self.assertEqual(agent.next_states(board), [[[1, 0, 0, 1, 0, -1, 0, 0, 0], [0.5]],
                                                    [[1, 0, 0, 0, 0, -1, 0, 1, 0], [0.8]]])

        board = [1, 0, 0, 1, 0, -1, 0, -1, 0]

        state5 = [[1, 0, 0, 1, 0, -1, 0, 0, 0], [0.5]]
        state6 = [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0.75]]
        state7 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]]
        state8 = [[1, 0, 0, 0, 0, -1, 0, 1, 0], [0.8]]
        state9 = [[1, 0, 1, 1, 0, -1, 0, -1, 0], [0.8]]
        state10 = [[1, 0, -1, 1, 0, -1, 0, -1, 0], [0.8]]
        state11 = [[1, 0, 0, 1, 0, -1, 0, -1, 1], [0.9]]

        agent.add_state(state5)
        agent.add_state(state6)
        agent.add_state(state7)
        agent.add_state(state8)
        agent.add_state(state9)
        agent.add_state(state10)
        agent.add_state(state11)

        self.assertEqual(agent.next_states(board), [[[1, 0, 1, 1, 0, -1, 0, -1, 0], [0.8]],
                                                    [[1, 0, 0, 1, 0, -1, 0, -1, 1], [0.9]]])

        agent = Agent(-1)

        board = [1, 1, 0, 1, 0, -1, 0, -1, 0]

        state1 = [[1, 1, 0, 1, 0, -1, 0, -1, -1], [0.5]]
        state2 = [[1, 1, 0, 1, 0, -1, 0, -1, 0], [0.75]]

        agent.add_state(state1)
        agent.add_state(state2)

        self.assertEqual(agent.next_states(board), [[[1, 1, 0, 1, 0, -1, 0, -1, -1], [0.5]]])

        agent = Agent(-1)

        board = [1, 1, 0, 1, 0, -1, 0, -1, 0]

        state1 = [[1, 1, 1, 1, 0, -1, 0, -1, -1], [0.5]]
        state2 = [[1, 1, 0, 1, 0, -1, 1, -1, 0], [0.75]]

        agent.add_state(state1)
        agent.add_state(state2)

        self.assertEqual(agent.next_states(board), [])

    def test_greedy(self):

        agent = Agent(1)

        board = [1, 0, 0, 0, 0, -1, 0, 0, 0]

        state1 = [[1, 0, 1, 0, 0, -1, 0, 0, 0], [0.5]]
        state2 = [[1, 0, 0, 0, 1, -1, 0, 0, 0], [0.95]]
        state3 = [[1, 1, 0, 0, 0, -1, 0, 0, 0], [0.5]]
        state4 = [[1, 0, 0, 0, 0, -1, 0, 0, 1], [0.8]]

        agent.add_state(state1)
        agent.add_state(state2)
        agent.add_state(state3)
        agent.add_state(state4)

        self.assertEqual(agent.greedy(board), [[1, 0, 0, 0, 1, -1, 0, 0, 0], [0.95]])

        agent = Agent(-1)

        board = [1, 0, 0, 0, 0, -1, 0, 1, 0]

        state1 = [[1, 0, 0, 0, 0, -1, 0, 1, -1], [0.5]]
        state2 = [[1, 0, 0, 0, 0, -1, 0, 1, 0], [0.95]]
        state3 = [[1, 0, 0, -1, 0, -1, 0, 1, 0], [0.75]]
        state4 = [[1, 0, 0, 0, 0, -1, 0, 1, 0], [0.8]]

        agent.add_state(state1)
        agent.add_state(state2)
        agent.add_state(state3)
        agent.add_state(state4)

        self.assertEqual(agent.greedy(board), [[1, 0, 0, -1, 0, -1, 0, 1, 0], [0.75]])

        agent = Agent(-1)

        board = [1, 1, 0, 1, 0, -1, 0, -1, 0]

        state1 = [[1, 1, 1, 1, 0, -1, 0, -1, -1], [0.5]]
        state2 = [[1, 1, 0, 1, 0, -1, 1, -1, 0], [0.75]]

        agent.add_state(state1)
        agent.add_state(state2)

        self.assertEqual(agent.greedy(board), [[], [0]])

    # contains randomness
    def test_backprop_state_value(self):

        state1 = [[1, 1, 0, 1, 1, -1, -1, -1, 0], [0.5]]
        state2 = [[1, 1, 0, 1, 1, -1, -1, -1, 0], [0.7]]

        agent = Agent(1)
        agent.add_state(state1)
        agent.add_state(state2)

        board = [1, 1, 0, 1, 0, -1, -1, -1, 0]

        agent.turn(board)
        self.assertEqual(agent.pre_state[1], [0.7])
        self.assertEqual(agent.current_state[1], [0.7])

    # not used
    def test_update_state(self):

        agent = Agent(1)

        state1 = [[1, 0, 0, 1, 0, -1, 0, 0, 0], [0.5]]
        state2 = [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0.75]]
        state3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5]]
        state4 = [[1, 0, 0, 0, 0, -1, 0, 1, 0], [0.8]]

        agent.add_state(state1)
        agent.add_state(state2)
        agent.add_state(state3)
        agent.add_state(state4)

        new_state_2 = [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0.75]]
        new_state_4 = [[1, 0, 0, 0, 0, -1, 0, 1, 0], [0.15]]

        agent.update_state(new_state_2)
        agent.update_state(new_state_4)

        self.assertEqual(agent.states[1], new_state_2)
        self.assertEqual(agent.states[3], new_state_4)

    def test_is_state_in_states(self):

        agent = Agent(1)

        state1 = [[1, 0, 0, 1, 0, -1, 0, 0, 0], [0.5]]
        state2 = [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0.75]]
        state3 = [[1, 0, 0, 1, 0, -1, 0, 0, 0], [0.5]]
        state4 = [[1, 0, 0, 0, 0, -1, 0, 1, 0], [0.8]]

        state5 = [[1, -1, 0, 0, 0, -1, 0, 1, 0], [0.8]]

        agent.add_state(state1)
        agent.add_state(state2)
        agent.add_state(state3)
        agent.add_state(state4)

        self.assertEqual(agent.is_state_in_states(state3), True)
        self.assertEqual(agent.is_state_in_states(state5), False)

    # contains randomness
    def test_turn(self):

        agent = Agent(1)

        board = [1, 0, 0, 1, 0, -1, 0, -1, 0]

        state1 = [[1, 1, 0, 1, 0, -1, 0, -1, 0], [0.5]]
        state2 = [[1, 1, 0, 1, 0, -1, 0, -1, 0], [0.75]]
        state3 = [[1, 1, 0, 1, 0, -1, 0, -1, 0], [0.95]]
        state4 = [[1, 1, 0, 1, 0, -1, 0, -1, 0], [0.8]]

        agent.add_state(state1)
        agent.add_state(state2)
        agent.add_state(state3)
        agent.add_state(state4)

        self.assertEqual(agent.turn(board), [1, 1, 0, 1, 0, -1, 0, -1, 0])
