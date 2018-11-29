def make_grid(width, height):
    
    #create a grid that will hold all the tiles for a boggle game
    #this function creates a dictionary with a row/column tupple as the key and a space as the value
    return {(row, col): ' ' for row in range(height)
        for col in range(width)
        
}










# def make_grid(width, height):
    
#     # Make an empty boggle grid
#     #test by typing python3 -m unittest in the command line
    
#     return {}
    