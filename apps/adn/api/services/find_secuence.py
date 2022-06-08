class FindSequence:
    def __init__(self, array, rows, columns, row, column):
        self._array = array
        self._rows = rows
        self._columns = columns
        self._row = row
        self._column = column

    def vertical(self):
        """ Movemos filas y mantenemos columna """
        val_ref = self._array[self._row][self._column]
        count = 1
        result = False
        for i in range(self._row + 1, self._rows - 1):
            count += 1 if val_ref == self._array[i][self._column] else 0
        if count >= 4:
            result = True
        return result

    def horizontal(self):
        """ Movemos columna y mantenemos fila """
        val_ref = self._array[self._row][self._column]
        count = 1
        result = False
        for i in range(self._column + 1, self._columns - 1):
            count += 1 if val_ref == self._array[self._row][i] else 0
        if count >= 4:
            result = True
        return result

    def obliquo(self):
        """ Movemos columna y  fila """
        val_ref = self._array[self._row][self._column]
        count = 1
        result = False
        for i in range(self._row + 1, self._rows - 1):
            count += 1 if val_ref == self._array[i][i] else 0
        if count >= 4:
            result = True
        return result
