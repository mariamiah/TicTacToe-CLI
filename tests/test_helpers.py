from main.computer import Computer
from main.helpers import Helper
from main.human import Human

players = ['x', 'o']
size = 3

class TestBoard(object):

  def setup(self):
      self.helper = Helper()
      self.board = self.helper.new_board()

  def test_draw(self):
      assert self.helper.new_board() == [' ',' ',' ',' ',' ',' ',' ',' ',' ']
