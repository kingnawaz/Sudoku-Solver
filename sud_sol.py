# -*- coding: utf-8 -*-


import sud_fun as sf


rows = 'ABCDEFGHI'
cols = '123456789'
boxes = sf.cross(rows, cols)

#print(boxes)
row_units = [sf.cross(r, cols) for r in rows]
column_units = [sf.cross(rows, c) for c in cols]
#print(row_units[0],column_units[0])
square_units = [sf.cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
#print(units['B6'][2])
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
#print(peers['A1'])

dt=sf.grid_values('4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......',boxes)

dt_new=sf.eliminate(dt,peers)
dt_new=sf.onlyCh(dt_new,units)

sf.display(sf.search(dt_new,boxes,peers,units),boxes,rows,cols)