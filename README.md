# Sudoku
A (brute-force) sudoku solver in Python. It models a Sudoku as a list (array under the hood) of length 81. It generates a further two-dimensional array (`[81][21]`), which maps cell locations to all other cell locations that that cell can "see". An empty cell takes the conveniently unused value of 0. Input sudoku is read from stdin, and should simply consist of 81 whitespace separated digits. The program comes with an option (`-e`) to print an "empty" sudoku for ease of entering a sudoku. With this as input (`ex.txt`)::

    0 0 0  2 6 0  7 0 1
    6 8 0  0 7 0  0 9 0  
    0 9 0  0 0 4  5 0 0  

    8 2 0  1 0 0  0 4 0  
    0 0 4  6 0 2  9 0 0  
    0 5 0  0 0 3  0 2 8

    0 0 9  3 0 0  0 7 4
    0 4 0  0 5 0  0 3 6
    7 0 3  0 1 8  0 0 0  

Done with this command:

    $ time cat ex.txt | python solve.py 

Produces, in a very respectable time-frame:

    4 3 5  2 6 9  7 8 1  
    6 8 2  5 7 1  4 9 3  
    1 9 7  8 3 4  5 6 2  

    8 2 6  1 9 5  3 4 7  
    3 7 4  6 8 2  9 1 5  
    9 5 1  7 4 3  6 2 8  

    5 1 9  3 2 6  8 7 4  
    2 4 8  9 5 7  1 3 6  
    7 6 3  4 1 8  2 5 9  


    cat ex.txt  0.00s user 0.00s system 0% cpu 0.003 total
    python3 solve.py  0.04s user 0.00s system 90% cpu 0.044 total

Of course, it's a stupid solver so if you give it a problem engineered to work against it the universe will probably collapse before it's finished.
