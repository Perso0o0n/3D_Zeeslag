# row
# name a - z
# list [column]

from models.ColumnModel import ColumnModel


class RowModel:

  def __init__(self, name, columns):
    self.Name = name
    createColumns = []
    for x in range(0, columns):
      if(x == 0 and name == "A"):
        createColumn = ColumnModel(F"{self.Name}{x}",True)
      else:
        createColumn = ColumnModel(F"{self.Name}{x}")
      createColumns.append(createColumn)
    self.columns = createColumns

  def __str__(self):
    return str(self.columns)
  
  def __repr__(self) -> str:
    return str(self.columns)
  
  def removePlayer(self,width):
    self.columns[width].isPlayerposition = False

  def addPlayer(self,width):
    self.columns[width].isPlayerposition = True
    self.columns[width].isVisited = True
