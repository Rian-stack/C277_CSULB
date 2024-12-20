class Map:
    '''
    Map – singleton – the map of the dungeon maze.
        a. __new__(cls) – if the map hasn’t been constructed, then construct it and store it in
        the instance class variable and return it. If it has, then just return the instance.
        b. __init__(self) – create and fill the 2D map list from the file contents. Create and
        fill the 2D revealed list with all False values. The map stores the contents of the
        file and the revealed list is used to determine whether the contents of the map are
        displayed or not (‘x’ if not displayed).
        c. __getitem__(self, row) – overloaded [] operator – returns the specified row from
        the map. (Note: this operator can be used to access a row (ex. m[r]) or can be
        used to access a value at a row and column (ex. m[r][c]).
        d. __len__(self) – returns the number of rows in the map list. (Note: if you want to
        know the number of rows, use len(m), if you need the number of columns, use
        len(m[r])).
        e. show_map(self, loc) – returns the map as a string in the format of a 5x5 matrix of
        characters where revealed locations are the characters from the map, unrevealed
        locations are ‘x’s, and the hero’s location is a ‘*’.
        f. reveal(self, loc) – sets the value in the 2D revealed list at the specified location to
        True.
        g. remove_at_loc(self, loc) – overwrites the character in the map list at the specified
        location with an ‘n’.
    '''
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Map, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_map'):
            self._map = []
            with open('/Users/rian/c277 Labs/C277_CSULB/lab10_DungeonsAndMonsters/map_lab10.txt') as file:
                for line in file:
                    self._map.append(list(line.strip()))
        self._revealed = [[False for _ in range(len(self._map[0]))] for _ in range(len(self._map))]
        self._map[0][0] = 's' # Set starting position

    def __getitem__(self, row):
        return self._map[row]

    def __len__(self):
        return len(self._map)

    def show_map(self, loc):
        '''
        Returns a list of strings representing the map, revealing only explored areas and the hero's location.

        loc: A tuple containing the hero's row and column (row, col).
        '''
        map_rows = []
        for row in range(len(self._map)):
            row_str = ""
            for col in range(len(self._map[0])):
                if row == loc[0] and col == loc[1]:
                    row_str += "*"
                elif row == loc[0] and col == loc[1]:
                    row_str += "*"
                elif row == 0 and col == 0 and self._map[row][col] == 's':
                    row_str += 's'
                elif self._revealed[row][col]:
                    row_str += self._map[row][col]
                else:
                    row_str += "x"
            map_rows.append(row_str)
        return map_rows

    def reveal(self, loc):
        '''Reveals the map at the given location.'''
        self._revealed[loc[0]][loc[1]] = True

    def remove_at_loc(self, loc):
        '''Removes an item from the map at the given location.'''
        self._map[loc[0]][loc[1]] = 'n'
