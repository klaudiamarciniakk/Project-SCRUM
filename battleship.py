import unittest

boardWidth = 10
boardHeight = 10

class Ship():
  ships = {'carrier':1, 'battleship':4, 'cruiser':3, 'submarine':3, 'destroyer':2}
  def __init__(self, location = 0, type ='carrier', direction="horizontal"):
    self._loc = location
    self._len = self.ships[type]
    self.calculateOffset(direction)
    if not self.checkValidLocation():
      raise ValueError('Out of bounds loc: ' + str(location) + ' in creation, '
        + str(self._len * self._offset + self._loc) + '<=' + str(boardWidth*boardHeight))
    self.assignCells(location)

  def calculateOffset(self, direction):
    if direction == "horizontal":
      self._offset = 1
    else:
      self._offset = boardWidth

  def assignCells(self, location):
    self._cells = []
    for i in range(0, self._len):
      self._cells.append(self._loc + self._offset*i)

  def checkValidLocation(self):
    return (self._loc < boardWidth * boardHeight
      and self._loc >= 0
      and (((self._len + (self._loc % boardWidth) <= boardWidth)
          and self._offset == 1)
        or (((self._len-1) * self._offset + self._loc <= boardWidth*boardHeight)
          and  self._offset == boardWidth)))

  def checkExists(self, location):
    return location in self._cells

  def hit(self, location):
    for i in range(0, len(self._cells)):
      if self._cells[i] == location:
        self._cells[i] = -1
        return True
    return False

  def dead(self):
    for cell in self._cells:
      if cell != -1:
        return False
    return True

  def collision(self, ship):
    for cell in self._cells:
      if ship.checkExists(cell):
        return True
    return False



class Carrier(Ship):
  def __init__(self):
    self.special = True
    super(Carrier, self).__init__()

  def checkAddSpecial(self, turns):
    if turns % 5 == 0:
      self.special = True



class BattleshipGame():
  shipMaxCount = 10
  def __init__(self, player_id = "1"):
    self.current_player = 1
    self.players={}
    self.players[player_id] = 1
    self.player1 = []
    self.player2 = []

  def addPlayer(self, player_id = "2"):
    self.players[player_id] = player_id

  def addShip(self, player_id, ship):
    player = self.getPlayer(player_id)
    if (not self.checkIfColliding(player, ship)
      and len(player) < self.shipMaxCount):
      player.append(ship)
      return True
    if (len(player) >= self.shipMaxCount):
      raise ValueError("Already have " + str(self.shipMaxCount)
        + " ships assigned")

  def checkIfColliding(self, player, ship):
    for existingShip in player:
      if ship.collision(existingShip):
        raise ValueError('Collision with existing ship')

    return False

  def checkGameOver(self, player_id):
    player = self.getPlayer(player_id)
    for ship in player:
      if not ship.dead():
        return False
    return True

  def fire(self, locations):
    hit = False
    enemy_player = (~self.current_player) & 3
    for ship in self.getPlayer(enemy_player):
      for location in locations:
        if ship.hit(location):
          hit = True
    self.current_player = enemy_player
    return hit

  def getPlayer(self, player_id):
    if player_id == 1:
      return self.player1
    else:
      return self.player2

  def ready(self):
    return (len(self.player1) == self.shipMaxCount
      and len(self.player2) == self.shipMaxCount)


if __name__ == '__main__':
  main()
