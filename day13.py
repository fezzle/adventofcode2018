import sys

VERTICAL = '|'
HORIZONTAL = '-'

GOING_LEFT = '<'
GOING_RIGHT = '>'
GOING_UP = '^'
GOING_DOWN = 'v'
GOING_STRAIGHT = 'S'

TOP_LEFT = '/'
TOP_RIGHT = '\\'
BOTTOM_RIGHT = '/'
BOTTOM_LEFT = '\\'

INTERSECTION = '+'


input=r"""                      /---------\                                                             /-------------------------------\                       
                    /-+---------+------------------------------\                              |                               |                       
                    | |         |/-----------------------------+------------------------------+-------------------------------+--------------\        
                    | |         ||    /------------------------+------------------------------+-\                             |              |        
                    | |         ||    |     /------------------+------------------------------+-+-----------------------------+------------\ |        
              /-----+-+---------++----+-----+------------------+------------------------------+-+\                         /--+------------+-+------\ 
              |     | |         ||/---+-----+------------------+------------------------------+-++-------------------------+--+-\          | |      | 
    /---------+-----+-+---------+++---+-----+------\           |                              | ||                         |  | |          | |      | 
    |         |     | |    /----+++---+-----+------+-----------+------------------------------+-++-------------------------+--+-+\         | |      | 
    |         |     | |    |    ||| /-+-----+------+-----------+---------------\          /---+-++-------------------------+--+-++---\     | |      | 
    |       /-+-----+-+----+----+++-+-+-----+------+-----------+---------\     |          |   | ||                         |  | ||   |     | |      | 
    |       | |     | |    |    ||| | |     |      |           |      /--+-----+----------+---+-++-------------------------+--+-++---+-----+-+--\   | 
    |       | | /---+-+----+----+++-+-+-----+------+-----------+------+--+-----+----------+\  | ||        /----------------+--+\||   |     | |  |   | 
    |       | | |   | |    |    ||| | |     |      |           |      |  |     |          ||  | ||        |                |  ||||   |     | |  |   | 
    |       | | |   | |    |    ||| | |     |      |           |    /-+--+-----+----------++--+-++---\    |                |  ||||   |     | |  |   | 
    |       | | |   | |    |    ||| | |     |      |           |/---+-+--+-----+----------++--+-++---+----+-------\        \--++++---+-----+-+--+---/ 
   /+-------+-+-+---+-+----+----+++\| |     |      |          /++---+-+--+-----+----------++--+-++---+----+-------+-----------++++--\|     | |  |     
  /++-------+-+-+---+-+----+----+++++-+-----+------+----------+++-\ | |  |     |          ||  | ||   |    |       |           ||||  ||     | |  |     
  |||       | | | /-+-+----+----+++++-+-----+------+----------+++-+-+-+-\|     |          ||  | ||   |    |       |           ||||  ||     | |  |     
  |||       | | | | ^ |    |    ||||| |     |      |    /-----+++-+-+-+-++\    |/---------++--+-++---+----+-------+-----------++++--++----\| |  |     
  |||       | | | | | |    |    ||||| |     |      |    |     ||| | | | |||    ||         ||  | ||   |    |       |/----------++++--++-\  || ^  |     
  |||       | | | | \-+----+----+++++-+-----+------+----+-----+/| | | | |||    ||  /------++--+-++\  |    |       ||          ||||  || |  || |  |     
  |||     /-+-+-+-+---+--\ |    ||||| |     |      |    |     | | | | | |||    ||  |    /-++--+-+++--+----+-------++----------++++--++-+--++-+--+----\
  |||     | | | | |   |  | |    ||||| |     |      | /--+-----+-+-+-+-+-+++----++--+----+-++--+-+++--+----+-------++----------++++--++-+--++-+--+--\ |
  |||     | | | | |   |/-+-+----+++++-+-----+------+-+--+----\| | | | | |||    ||  |    | || /+-+++--+----+--\    ||          ||||  || |  || |  |  | |
  |||     | | | | |  /++-+-+----+++++-+-----+------+-+--+----++-+-+-+-+-+++----++--+----+-++-++-+++--+---\|  |    ||          ||||  || |  || |  |  | |
  |||     | | | | |  ||| | |    ||||| |     |      | |  |    || | | | \-+++----++--+----+-++-++-+++--+---++--+----++----------++++--++-+--++-+--/  | |
  |||     | | | | |  ||| | |    ||||| |  /--+------+-+--+----++-+-+-+---+++----++--+----+-++-++-+++--+---++--+----++----------++++--++-+\ || |     | |
  |||     | | | | |  ||| | |    ||||| |/-+--+------+-+--+----++-+-+-+---+++----++--+----+-++\|| |||  |   ||  |    ||          ||||  || || || |     | |
/-+++-----+-+-+-+-+--+++-+-+----+++++-++-+--+------+-+--+----++-+-+-+---+++----++--+--\ | ||||| |||  |   ||  |    ||          ||||  || || || |     | |
| |||     v | | | |  ||| | |    ||||| || |  |      | |  |    || |/+-+---+++----++--+--+-+-+++++-+++-\|   ||  |    ||          ||||  || || || |     | |
| |||     | | | | |  ||| | |    ||||| || |  |      | |  |    || ||| |   |||    ||  |  | | \++++-+++-++---++--+----++----------++++--+/ || || |     | |
| |\+-----+-+-+-+-+--+++-+-+----+++/| || |  |      | |  |    ||/+++-+---+++----++--+--+-+--++++-+++-++---++--+----++----------++++--+--++-++-+-----+\|
| | |     | | | | |  ||| | |    ||| | || |  |   /--+-+--+----++++++-+---+++----++--+--+-+--++++-+++-++---++--+----++\         ||||  |  || || |     |||
| | |     | | | | |  ||| | |    ||| | || |  |/--+--+-+--+----++++++-+---+++----++--+--+-+--++++-+++-++---++--+----+++--\      ||||  |  || || |     |||
| | |     | | | | |  ||| | |    ||\-+-++-+--++--+--+-+--+----++++++-+---+++----++--+--+-+--++++-+++-++---++--+----+++--+------++/|  |  || || |     |||
| | |     |/+-+-+-+--+++-+-+----++--+-++-+-\||  |  | |  |    |||||| |   |||    ||  |  | |  |||| ||| ||   ||  |    |||  |      || |  |  || || |     |||
| | |     ||| | | |  ||| | |    ||  | || | |||  |  | |  |/---++++++-+---+++----++--+--+-+--++++-+++-++---++--+----+++--+------++-+--+--++<++-+--\  |||
| | |     ||| | | |  ||| | |    ||  | || | |||  |  | |  ||   |||||| |   |||    ||  |  | |  |||| ||| ||   ||  |    |||  |      || |  |  || || |  |  |||
| | |     ||| | | |  ||| | |    ||  | || | ||| /+--+-+--++---++++++\|   |||   /++--+--+-+--++++\||| ||   ||  |    |||  |      || |  |  || || |  |  |||
| | |     ||| | | |  ||| | |    ||  | ||/+-+++-++--+-+--++---++++++++---+++---+++--+--+-+--++++++++-++---++--+\   |||  |      || |  |  || || |  |  |||
| | |     ||| | | |  ||| |/+----++--+-++++-+++-++--+-+--++---++++++++---+++---+++\ |  | |  |||||||| ||   ||  ||  /+++--+--\   || |  |  || || |  |  |||
| | |    /+++-+-+-+--+++-+++----++--+-++++-+++-++--+\|  ||   ||||||||   |||   |||| |  | |  |||||||| || /-++--++--++++--+--+---++-+--+\ || || |  |  |||
| | |    |||| | \-+--+++-+++----++--+-++++-+++-++--+++--++---++++++++---+++---++++-+--+-+--/||||||| || | ||  ||  ||||  |  |   || |  || || || |  |  |||
| | |    |||| |   |  ||| |||    ||  | |||| ||| ||  |||  ||   ||||||||   |||   |||| |  | |   ||||||| || | ||  ||  ||||  |  |   || |  || || || |  |  |||
\-+-+----++++-+---+--+++-+++----++--+-++++-+++-++--+++--++---++++++++---+++---++++-+--/ |   ||||||| || | ||  ||  ||||  |  |   || |  || || || |  |  |||
  | |    |||| |   |  ||| |||    |\--+-++++-+++-++--+++--++---++++++++---+++---++++-+----+---+++++++-++-+-++--++--++++--+--+---++-+--++-++-++-/  |  |||
  | |    |||| |   |  ||| |||    |  /+-++++-+++-++--+++--++---++++++++---+++---++++-+----+---+++++++-++-+-++--++--++++--+--+---++-+-\|| || ||    |  |||
  | |    |||| |   |  ||| |||    |  || |||| ||| ||  |||  ||   ||||||||   |||   |||| |/---+---+++++++-++-+-++--++--++++--+--+-\ || | ||| || ||    |  |||
  | |  /-++++-+--\|  ||| |||    |  || |||| ||| \+--+++--++---++++++/|   ||| /-++++-++---+---+++++++-++-+-++--++--++++--+--+-+-++-+-+++-++-++---\|  |||
  | |  | |||| |  ||  ||| |||    |  || |||| |||  |  |||  ||   |||||| |  /+++-+-++++-++---+---+++++++-++-+-++--++--++++--+--+-+-++-+-+++-++-++--\||  |||
  | |  | |||| | /++--+++-+++----+--++-++++-+++--+--+++--++---++++++-+--++++-+-++++-++---+---+++++++-++-+-++--++\ ||||  |  | | || | ||| || ||  |||  |||
  | |  | ||||/+-+++--+++-+++----+--++-++++-+++--+--+++--++---++++++\|  |||| | |||| || /-+---+++++++-++\| ||  ||| ||||  |  | | || | ||| || ||  |||  |||
  | |  | |||||| |||  ||| |||    |  || |||| |||  |  |||/-++---++++++++--++++-+-++++-++\| |   ||||||| |||| ||  ||| ||||  |  | | || | ||| || ||  |||  |||
  | |  | |||||| |||  ||| |||    |  || |||| |\+--+--++++-++---++++++++--++++-+-++++-++++-+---+++++++-++++-++--+++-++++--+--+-+-++-+-+++-++-+/  |||  |||
  \-+--+-++++++-+++--+++-+++----+--++-++++-+-+--+--++++-++---+++++/||  |||| | \+++-++++-+---+++/||| |||| ||  ||| ||||  |  | | || | ||| || |   |||  |||
    |  | |||||| |||  ||| |||    |  || |||| | |  |  ||||/++---+++++-++--++++-+--+++-++++-+---+++-+++-++++-++--+++-++++--+--+-+-++\| ||| || |   |||  |||
    |  | |||||| |||  ||| |||    |  || |||| | |  |  |||||||   ||||| ||  |||| |  ||| |||| |   ||| ||| |||| ||  ||| ||||  |  | | |||| ||| || |   |||  |||
    |  | |||||| |||  |||/+++----+--++-++++-+-+--+--+++++++---+++++-++--++++-+--+++-++++-+---+++\||| |||| ||  |||/++++--+--+-+-++++-+++-++-+---+++\ |||
    |  | |||||| |||  |||||||    |  || |||| | |  |  |||||||   ||||| ||  |||| |  ||| |||| |   ||||||| |||| ||  ||||||||  |  | | |||| ||| || |   |||| |||
    |  | |\++++-+++--++++/||    |  || |||| | |  | /+++++++---+++++-++--++++-+--+++-++++-+---+++++++-++++-++--++++++++\ |  | | |||| ||| || |   |||| |||
    |  | | |||| |||  |||| ||    |  || |||| | |  | ||||||||   ||||| ||  |||| |  ||| |||| |   ||||||| |||| ||/-+++++++++-+--+-+-++++-+++-++-+-\ ||^| |||
    |  | | |||| \++--++++-++----+--++-++++-+-+--+-++++++++---+++++-++--++++-+--+++-++++>+---+++++++-++++-+++-++/|||||| |  | | |||| ||| || | | |||| |||
 /--+--+-+-++++--++-\|||| ||    |  || |||| | |  | ||||||||   ||||| ||  |||| |  ||| |||| |   ||||||| |||| ||| || |||||| |  | | |||| ||| || | | |||| |||
 |  |  | | ||||  ^| ||||| ||    |  ||/++++-+-+--+-++++++++---+++++-++-\|||| |  ||| |||| |   |||||||/++++-+++-++-++++++-+--+-+-++++-+++-++-+-+\|||| |||
 |  |  | | ||||  || ||||| ||    |  ||||||| | |  | ||||||||   ||||| |\-+++++-+--+++-++++-+---+++++++++/|| ||| || |||||| |  | | |||| ||| || | |||||| |||
 |  |  | | ||||  || ||||| ||    |  ||||||| | |  | |||||||\---+++++-+--+++++-+--+++-++++-+---+++++++++-++-+++-++-++++++-+--+-+-++++-+++-++-+-++++/| |||
 |  |  | | ||||  || ||||| ||    |  ||||||| | |  | |||||||    ||||| |  ||||| |  ||| |||| |   ||||||||| || ||| || |||||| |  | | |||| ||| || | |||| | |||
 |  |  | | v|||  |\-+++++-++----+--+++++++-+-+--+-+++++++----+++++-+--++/|| \--+++-++++-+---+++++++++-++-+++-++-++++++-+--+-+-++++-+++-++-+-+++/ | |||
 |  |  | | ||||  |  ||||| ||    |  ||||||| | | /+-+++++++----+++++-+--++-++----+++-++++-+---+++++++++-++-+++-++-++++++-+--+-+-++++-+++-++-+-+++--+\|||
 |  | /+-+-++++--+-\||||| ||    |  ||||||| | | ||/+++++++----+++++-+--++-++----+++-++++-+---+++++++++-++-+++-++-++++++\|  | | |||| ||| || | |||  |||||
 |  | || | ||||  | |||||| || /--+--+++++++-+-+-++++++++++----+++++-+--++-++----+++-++++-+--\||||||||| || ||| || ||||||||  | | |||| ||| || | |||  |||||
 |  | || | \+++--+-++++++-++-+--+--+++++++-/ | ||||||||||    |||||/+--++-++----+++-++++-+--++++++++++-++-+++-++-++++++++\/+-+-++++-+++-++-+\|||  |||||
 |  | || |  \++--+-++++++-++-+--+--+++++++---+-++++++++++----+++++++--++-/|    ||| |||| |  |||||||||| || ||| || ||||||||||| | |||| ||| || |||||  |||||
 |  v || |   ||  | |||||| || |  |  |||||||   | ||||||||||    ||\++++--++--+----+++>++++-+--++++++++++-++-+++-++-+++++++++++-+-++++-+++-++-+++++--+++/|
 |  | ||/+---++--+-++++++-++-+--+--+++++++---+-++++++++++----++-++++--++--+----+++-++++-+\ |||||||||| || ||| || ||||||||||| | |||| ||| || |||||  ||| |
 |  | ||||   ||  | ||||\+-++-+--+--+++++++---+-++++++++++----/| ||||  ||  |    ||| ||||/++-++++++++++-++-+++-++-+++++++++++\| |||| ||| || |||||  ||| |
 |  | ||||   ||  | |||| | || |  |  |||||||   | ||||||||||     | ||||/-++--+----+++-+++++++-++++++++++\|| ||| || ||||||||||||| |||| ||| || |||||  ||| |
 |  | ||||   || /+-++++-+-++-+--+--+++++++---+-++++++++++-----+-+++++-++\ |    ||| ||||||| ||||||||||||| ||| || ||||||||||||| |||| ||| || |||||  ||| |
 |  | ||||   || || |||| | || |  |  |||||||   | ||||||||||     | ||||| ||| |    ||| ||||||| ||\++++++++++-+++-/| ||||||||||||| |||| ||| || |||||  ||| |
 |  | ||||   || || |||| | || |  |  |||||||   | ||||||||||     | ||||| |||/+----+++-+++++++-++-++++++++++-+++--+-+++++++++++++-++++-+++\|| |||||  ||| |
 |  | ||||   || || |||| | || |  |  |||||||/--+-++++++++++-----+-+++++-+++++----+++-+++++++-++-++++++++++-+++\ | ||||||||||||| |||| |||||| |||||  ||| |
 |  | ||||   \+-++-++++-+-++-+--+--++++++++--+-++++++++++-----+-+++/| |||||    ||| ||||||| || |||||||||| |||| | ||||||||||||| |||| |||||| |||||  ||| |
 |  | ||||    | || |||| | || |  |  |\++++++--+-++++++++++-----+-+++-+-+++++----/|| ||||||| || \+++++++++-++++-+-+++++++++++++-/||| |||||| |||||  ||| |
 |  | ||||    | || |||| | || |  |  | ||||||  | ||||||||||     | ||| | |\+++-----++-+++++++-++--+++++++++-++++-+-+++++++++++++--+++-++++++-++++/  ||| |
 |  | ||||    | || |||| | || |  |  | ||||||  | |||||||||\-----+-+++-+-+-++/     || ||||||| ||  |||||||||/++++-+-+++++++++++++\ ||| |||||| ||||   ||| |
 |  | ||||    | || |||| | || |  |  | ||||||  | |||||||||      | ||| | | ||      || ||||||| ||  |||||||||||||| | |||||||||||||| ||| |||||| ||||   ||| |
 |  | ||||    | || |||| | || |  |  | ||||||  | |||||||||      | ||| |/+-++-----\|| ||||||| ||  |||||||||||||| | |||||||||||||| ||| |||||| ||||   ||| |
 |  | |||| /--+-++-++++-+-++-+--+--+\||||||  | |||||||||      | ||| ||| ||     ||| ||||||| v|  |||||||||||||| | |||\++++++++++-+++-++++/| ||||   ||| |
 |  | |||| |  | \+-++++-+-++-+--+--++++++++--+-+++++++++------+-+++-+++-/|     ||| ||||||| ||  ||||||||||||||/+-+++-++++++++++-+++-++++-+-++++--\||| |
 |  | |||| |  |  | |||| | || |  |  |||\++++--+-+++++++++------+-+++-+++--+-----+++-+++++++-++--+/|||||||||||||| ||| ||||||||||/+++-++++-+-++++-\|||| |
 |  | |||| |  |  | |||\-+-++-+--/  ||| |||\--+-+++++++++------+-+++-+++--+-----+++-+++++++-++--+-+++++++++++/|| |\+-++++++/||||||| |||| | |||| ||||| |
 |  | |||| |  |  | |||  | || |     ||| |||   | |||||||||      | |\+-+++--+-----+++-+++++++-++--+-+++/||||||| || | | |||||| ||||||| |||| | |||| ||||| |
 |/-+-++++-+-\|  | |||  | || |     ||| |||   | |||||||||      | | | |||  |     ||| ||||||| ||  | ||| ||||||| || | | |||||| ||||||| |||| | |||| ||||| |
 || | |||| | ||  | |||  | || |     ||| |||   | |||||||\+------+-+-+-+++--+-----+++-++/||\+-++--+-+++-+++++++-++-+-+-++++++-+++++++-++++-+-++++-+++++-/
 || | |||| | ||  | |||  | || |     ||| |||  /+-+++++++-+-----\| | | |||  |     ||| || ||/+-++--+-+++-+++++++-++-+\| |||||| ||||||| |||| | |||| |||||  
 || | |||| | ||  | |||  | || |     ||| |||  || ||||||| |     || | | |||  |     |\+-++-++++-++--+-+++-+++++++-++-+++-++++++-+++++++-++++-+-/||| |||||  
 || | |||| | |\--+-+++--+-++-+-----+++-+++--++-+++++++-+-----++-+-+-+++--+-----+-+-++-++++-++--+-/|| ||||||| || ||| |||||| ||||||| |||| |  ||| |||||  
 || | |||| | |   | |||  | || |     ||| |||  || ||\++++-+-----++-+-+-+++--+-----+-+-++-++++-++--+--++-+++++++-++-+++-++/||| ||||||| |||| |  ||| |||||  
 || | |||| | |   | |||  | || |/----+++-+++\ || || |||| |     || | | |||  |     | | || |||| ||  |  || |||||\+-++-+++-++-+++-++++/|| |||| |  ||| |||||  
 || |/++++-+-+---+-+++--+-++-++----+++-++++-++-++-++++-+-----++-+-+-+++--+-\   | | || \+++-++<-+--++-+/||| | || ||| || ||| |||| || |||| |  ||| |||||  
 || |||||| | |   | |||  | || ||    ||| |||| || || |||| |     || | | |||  | |   | | ||  ||| ||  |  || | ||| | || ||| || ||| |||| || |||| |  ||| |||||  
 || |||||| | |   | |||  | |\-++----+++-++++-++-++-++++-+-----++-+-+-+++--+-+---+-+-++--+++-++--+--++-+-+++-+-++-+++-++-+++-++++-+/ |||| |  ||| |||||  
 || ||||||/+-+---+-+++\ | |  ||  /-+++-++++-++-++-++++-+----\|| | | |||  | |   | | ||  ||| ||  |  || | ||| | || ||| || ||| |||| |  |||| |  ||| |||||  
 || |||||||| |   | |||| | |  ||  | ||| |||| |\-++-++++-+----+++-+-+-+++--+-+---+-+-++--+++-++--+--++-+-+++-+-++-+++-++-/|| |||| |  |||| |  ||| |||||  
 || |||||||| |   | |||| | |  ||  | ||| |||| |  || \+++-+----+++-+-+-+++--+-+---+-+-++--+++-++--+--++-+-+++-+-++-+++-+/  || |||| |  |||| |  ||| |||||  
 || |||||||| |   | |||| | |  ||  | ||| |||| |  ||  ||| |/---+++-+<+\|||  | |   |/+-++--+++-++--+--++-+-+++-+-++-+++-+-\ || |||| |  |||| |  ||| |||||  
 || |||||||| |   | |||| | |  ||  | ||| |||| |  ||  ||| ||   ||| | |||||  | |   ||| ||  ||| ||  |  || | ||| | || ||| | | || |||| |  |||| |  ||| |||||  
 || |||||||| |   | |||| | |  ||  | ||| |||| |  ||  ||| ||   ||| | |||||  | |   ||| ||  ||| ||  |  || | ||| \-++-+++-+-+-++-++++-+--++++-+--+/| |||||  
 || \+++++++-+---+-++++-+-+--++--+-+++-++++-+--++--/|| ||   ||| | |||||  | |   ||| ||  \++-++--+--++-+-+++---++-+++-+-+-++-/||| | /++++-+--+-+-+++++-\
 ||  ||||||| |   | |||| | |  ||  | ||| |\++-+--++---++-++---+++-+-+++++--+-+---+++-++---++-++--+--++-+-+++---+/ ||| | | ||  ||| | ||||| |  | | ||||| |
 ||  |||||||/+---+-++++-+-+--++--+-+++-+-++-+--++---++-++---+++-+-+++++--+-+---+++-++---++-++-\|  || | |||   |  ||| | | ||  ||| | ||||| |  | | ||||| |
 ||  |||||||||   | |||| | |  ||  | ||| | || |  ||   ^| || /-+++-+-+++++--+-+-\ ||| ||   || || ||  || | ||| /-+--+++-+-+-++--+++-+-+++++-+-\| | ||||| |
 ||  |||||||||   | |||| | |  ||  | ||| | || |  ||   || || | ||| | |||||  | | | ||| ||   || || ||  || | ||| | |  ||| | | ||  ||| | ||||| | || | ||||| |
 ||  ||\++++++---/ |||| | |  ||  | ||| | || |  ||   || || | ||| \-+++++--+-+-+-+++-++---++-++-++--++-+-+++-+-+--++/ | | ||  ||| | ||||| | || | ||v|| |
 ||  || ||||||     ||\+-+-+--++--+-+++-+-++-+--++---++-++-+-+++---+++++--+-+-+-+++-++---++-++-++--++-+-++/ | |  ||  | | ||  ||| | ||||| | || | ||||| |
 ||  || ||||||     || | | |  ||  | ||| | || |  ||   || |\-+-+++---+/|||  | | | ||| |\---++-++-++--++-+-++--+-+--++--+-+-++--/|| | ||||| | || | ||||| |
 ||  || ||||||     || | | |  ||  | ||| | || | /++---++-+--+-+++---+-+++--+-+-+-+++\|    || || ||  || | ||  | |  ||  | | ||   || | ||||| | || | ||||| |
 ||  || ||||||     || | | |  ||  | ||| | || | |||   || |  | |||   | |\+--+-+-+-/||||    || || ||  || | ||  | \--++--+-+-++---++-+-+++++-+-++-+-+/||| |
 ||  \+-++++++-----++-+-+-+--++--+-+++-+-++-+-+++---++-+--+-+++---+-+-+--+-/ |  ||||    || || ||  || | ||  |    ||  | | ||   || | ||||| | || | | ||| |
 ||   | ||||||     || | | |  ||  | ||| | || | |||   || |  | |||   | | |  |   |  ||||    \+-++-++--++-+-++--+----+/  | | ||   || | ||||| | || | | ||| |
 ||   | ||||||     || | | |  ||  | ||| | || | |||   || |  | ||\---+-+-+--+---+--++++-----+-++-++--++-+-++--+----+---+-+-++---++-+-++/|| | || | | ||| |
 ||   \-++++++-----/| | | |  ||  | ||| | || | |||   || |  | ||    | | |  |   |  ||||     | || ||  || | ||  |    |   | | |\---++-+-++-++-+-+/ | | ||| |
 ||     ||||||      | | | |  ||  | ||| | || | |||   || |  | ||    | | |  |   |  ||||     | || ||  || | ||  |    |   | | |    || | || || | |  | | ||| |
/++-----++++++------+-+-+-+--++--+-+++-+-++-+-+++---++-+--+\||    | | |  |   |  ||||     | || ||  || | ||  |    |   | | |    || | || || | |  | | ||| |
|||     ||||||      | | | |  ||  | ||| \-++-+-+++---++-+--++++----+-+-+--+---+--++++-----+-+/ ||  || | ||  |    |   | | |    || | || || | |  | | ||| |
|||     ||||||      | | | |  || /+-+++---++-+-+++---++-+--++++---\| | |  |   |  ||||     | |  ||  |\-+-++--+----+---+-+-+----++-+-++-++-+-+--/ | ||| |
|||   /-++++++------+-+-+-+-\|| || |||   || | |||   || |  ||||   || | |  |   |  |||\-----+-+--++--/  | ||  |    |   | | |    || | || || | |    | ||| |
|||   | ||||||      | | | | ||| || |||   \+-+-+++---++-+--++++---++-+-+--+---+--+++------+-+--++-----+-++--+<---+---+-+-+----++-+-++-++-/ |    | ||| |
|||   | ||||||      | | | | ||| || |||    | | |||   || |  ||||   || | |  \---+--+++------+-+--++-----+-++--+----+---+-+-+----++-+-++-+/   |    | ||| |
|||   | ||||||      | | | \-+++-++-+++----+-+-+++---++-+--++++---++-+-+------+--+/|      | |  ||     | \+--+----+---+-+-+----++-+-++-/    |    | ||| |
|||   | ||||||      | | |   ||\-++-+++----/ | |||   |\-+--++++---++-+-+------+--+-+------+-+--++-----+--+--+---<+---+-+-+----++-+-++------+----+-++/ |
|||   | ||||||      | | |   ||  || \++------+-+++---+--+--++++---++-+-+------+--+-+------+-+--++-----+--+--+----+---+-+-+----++-+-+/      |    | ||  |
|||   | ||||||      | | |   ||  ||  ||      \-+++---+--+--+++/   ||/+-+------+--+-+------+-+--++-\   |  |  |    |   | | |    || | |       |    | ||  |
|||   | ||||\+------+-+-+---++--++--++--------+++---+--+--+++----++++-+------+--+-+------+-+--/| |   |  |  |    |   | | |    || | |       |    | ||  |
|||   | ||\+-+------+-/ |   |\--++--++--------+++---+--+--+++----++++-+------+--+-+------+-/   | |   |  |  |    |   | | |    || | |       |    | ||  |
|||   | \+-+-+------+---+---+---++--++--------+++---+--+--+++----++++-+------+--+-+------/     | |   |  |  |    \---+-+-+----++-+-+-------+----+-/|  |
|||   |  | | |      |   |   |   ||  ||        |||   |  |  \++----++++-+------/  | |            | |   |  \--+--------+-+-+----/| | |       |    |  |  |
|\+---+--+-+-+------/   |   |   \+--++--------+++---+--+---++----/||| |         | |            | |   |     \--------+-+-+-----+-+-+-------/    |  |  |
| |   |  | \-+----------+---+----+--/|        |||   |  |   ||     ||| |         | |            | |   |              | | |     | | |            |  |  |
| |   |  |   |          \---+----+---+--------+++---+--+---++-----+++-+---------+-+------------/ |   |              | | |     | | |            |  |  |
| \---+--+---/              |    |   |        ||\---+--+---++-----+++-+---------+-+--------------+---+--------------/ | |     \-+-+------------/  |  |
|     |  |                  |    |   \--------++----+--+---++-----+++-/         \-+--------------+---+----------------/ |       | |               |  |
|     |  |                  |    \------------++----+--+---+/     |\+-------------+--------------/   |                  |       | |               |  |
\-----+--+------------------+-----------------++----+--+---/      \-+-------------+------------------+------------------/       | |               |  |
      |  \------------------+-----------------++----/  |            |             |                  |                          | \---------------+--/
      |                     |                 ||       |            \-------------+------------------/                          |                 |   
      |                     |                 ||       \--------------------------+---------------------------------------------/                 |   
      |                     |                 |\----------------------------------+---------------------------------------------------------------/   
      \---------------------/                 \-----------------------------------/                                                                   """.split("\n")

input2 = r"""/->-\        
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/""".split("\n")


class Point(object):
    def __init__(self, road, cart):
        self.road = road
        self.cart = cart


class Cart(object):
    def __init__(self, x, y, direction, next_intersection):
        self.x = x
        self.y = y
        self.direction = direction
        self.next_intersection = next_intersection


width = max(*[len(v) for v in input])
chart = [Point(road=' ', cart=None)] * (len(input) * width)
carts = []


for i, line in enumerate(input):
    for j, c in enumerate(line):
        if c in (GOING_UP, GOING_LEFT, GOING_RIGHT, GOING_DOWN):
            cart = Cart(x=j, y=i, direction=c, next_intersection=GOING_LEFT)
            carts.append(cart)
            road = VERTICAL if c in (GOING_UP, GOING_DOWN) else HORIZONTAL
        else:
            cart = None
            road = c
        chart[j + i*width] = Point(road=road, cart=cart)


def print_chart(m, w):
    print("chart:")
    for i in range(0, int(len(m)/w)):
        for j, p in enumerate(m[i*w:(i+1)*w]):
            print(' ' if p is None else p.cart.direction if p.cart else p.road, end="")
        print("")
    print("")

next_spot = {
    GOING_UP: lambda x, y: (x, y - 1),
    GOING_DOWN: lambda x, y: (x, y + 1),
    GOING_LEFT: lambda x, y: (x - 1, y),
    GOING_RIGHT: lambda x, y: (x + 1, y),
    }
corner = {
    (GOING_UP, TOP_LEFT): GOING_RIGHT,
    (GOING_UP, TOP_RIGHT): GOING_LEFT,
    (GOING_DOWN, BOTTOM_LEFT): GOING_RIGHT,
    (GOING_DOWN, BOTTOM_RIGHT): GOING_LEFT,
    (GOING_RIGHT, TOP_RIGHT): GOING_DOWN,
    (GOING_RIGHT, BOTTOM_RIGHT): GOING_UP,
    (GOING_LEFT, TOP_LEFT): GOING_DOWN,
    (GOING_LEFT, BOTTOM_LEFT): GOING_UP,
    }
intersection = {
    (GOING_UP, GOING_LEFT): (GOING_LEFT, GOING_STRAIGHT),
    (GOING_UP, GOING_STRAIGHT): (GOING_UP, GOING_RIGHT),
    (GOING_UP, GOING_RIGHT): (GOING_RIGHT, GOING_LEFT),
    (GOING_RIGHT, GOING_LEFT): (GOING_UP, GOING_STRAIGHT),
    (GOING_RIGHT, GOING_STRAIGHT): (GOING_RIGHT, GOING_RIGHT),
    (GOING_RIGHT, GOING_RIGHT): (GOING_DOWN, GOING_LEFT),
    (GOING_LEFT, GOING_LEFT): (GOING_DOWN, GOING_STRAIGHT),
    (GOING_LEFT, GOING_STRAIGHT): (GOING_LEFT, GOING_RIGHT),
    (GOING_LEFT, GOING_RIGHT): (GOING_UP, GOING_LEFT),
    (GOING_DOWN, GOING_LEFT): (GOING_RIGHT, GOING_STRAIGHT),
    (GOING_DOWN, GOING_STRAIGHT): (GOING_DOWN, GOING_RIGHT),
    (GOING_DOWN, GOING_RIGHT): (GOING_LEFT, GOING_LEFT),
    }

done_part_one = False
while True:
    # next tick
    #print_chart(chart, width)

    cart_order = sorted(carts, key=lambda c: (c.y, c.x))
    removed = set()
    for cart in cart_order:
        if cart in removed:
            continue
        point = chart[cart.x + cart.y*width]

        if point.road in (TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT):
            cart.direction = corner[(cart.direction, point.road)]

        elif point.road == INTERSECTION:
            cart.direction, cart.next_intersection = (
                intersection[(cart.direction, cart.next_intersection)]
                )
        
        next_x, next_y = next_spot[cart.direction](cart.x, cart.y)
        #import pdb; pdb.set_trace()
        if chart[next_x + next_y*width].cart != None:
            assert(chart[next_x + next_y*width].cart != cart)
            if not done_part_one:
                print("Part 1 (Collision at): {},{}".format(next_x, next_y))
                done_part_one = True
            if chart[next_x + next_y*width].cart not in carts:
                import pdb; pdb.set_trace()
            carts.remove(cart)
            carts.remove(chart[next_x + next_y*width].cart)
            removed.add(cart)
            removed.add(chart[next_x + next_y*width].cart)
            if len(carts) == 1:
                print("Part 2 (Last Cart): {},{}".format(carts[0].x, carts[0].y))
                raise RuntimeError("Done")
            point.cart = None
            chart[next_x + next_y*width].cart = None
            continue
            
        point.cart = None
        chart[next_x + next_y*width].cart = cart
        cart.x = next_x
        cart.y = next_y


