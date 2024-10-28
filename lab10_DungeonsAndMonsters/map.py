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