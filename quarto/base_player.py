# Sample player class (for tests)
import numpy as np


class BasePlayer:
    def __init__(self, train_mode):
        """
        :param train_mode: bool
        """
        raise NotImplementedError

    def start(self, state, valid_actions):
        """
        :param state: np.array
        :param valid_actions: np.array 1D
        :returns: int
        """
        raise NotImplementedError

    def step(self, state, valid_actions, reward):
        """
        :param state: np.array
        :param valid_actions: np.array 1D
        :param reward: float
        :returns: int
        """
        raise NotImplementedError

    def end(self, state, reward):
        """
        :param state: np.array
        :param reward: float
        """
        raise NotImplementedError

    def get_freezed(self):
        """
        Create a copy of this player with train_mode = False
        :returns: BasePlayer
        """
        raise NotImplementedError


class RandomPlayer(BasePlayer):
    def __init__(self, train_mode):
        self.train_mode = train_mode

    def start(self, state, valid_actions):
        return np.random.choice(valid_actions)

    def step(self, state, valid_actions, reward):
        return np.random.choice(valid_actions)

    def end(self, state, reward):
        pass

    def get_freezed(self):
        return RandomPlayer(False)


class DummyPlayer(BasePlayer):
    def __init__(self, train_mode):
        self.train_mode = train_mode

    def start(self, state, valid_actions):
        return valid_actions[0]

    def step(self, state, valid_actions, reward):
        return valid_actions[0]

    def end(self, state, reward):
        pass

    def get_freezed(self):
        return DummyPlayer(False)

class HumanPlayer(BasePlayer):
    def __init__(self, env):
        self.env = env

    def start(self, state, valid_actions):
        return self._ask_action()

    def step(self, state, valid_actions, reward):
        return self._ask_action()

    def end(self, state, reward):
        from IPython.display import clear_output, display
        clear_output()
        display(self.env)

    def get_freezed(self):
        raise NotImplementedError()

    def _ask_action(self):
        from IPython.display import clear_output, display
        clear_output()
        display(self.env)
        return self.env.ask_action()
