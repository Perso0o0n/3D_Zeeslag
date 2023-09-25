# row 
# name a - z 
# list [column]
import ColumnModel


class RowModel:
  def __init__(self,name , columns):
    self.Name = name
    createColumns = []
    for x in range(0,columns):
      createColumn = ColumnModel(F"{self.Name}{x}")
      createColumns.append(createColumn)
    self.columns = createColumns

  def __str__(self):
    return F"{self.columns}\n"