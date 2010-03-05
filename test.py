def tfun():
    t=[1,2,3]
    try:
        t.remove(4)
    except ValueError:
        None



def even_spacing(num_objs,boundary):
    """returns an array of evenly spaced positions for the passed number of objects from 0,boundary; it should be noted the intervals must be integers"""
    if num_objs == 1:
        return boundary/2
    else:
        interval=boundary/(num_objs+1)
        positions=[i for i in range(0,boundary,interval)]
        return positions[1:num_objs+1]
