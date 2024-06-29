
ALL CREDITS GO TOWARDS https://www.youtube.com/@spooderCode 
FOR MAKING THE ORIGINAL D-- SOURCE CODE

DMM Documentation - 6/28/2024

Make sure to install the keyboard module!

To run DMM programs you must run the command :(

-----------------------------
Keywords:
    PIZZA       
    BURGER      
    SALAD       
    SUSHI       
    TACO       
    STEAK       
    RAMEN       
    SANDWICH    
    CURRY       
    CHICKEN
    COOKIE     
    CHEESE

Command line args:
    dmm.py fileToRun screenWidth screenHeight

    fileToRun - File to execute. Must have the .dmm extension.
    screenWidth - Screen width in pixels
    screenHeight - Screen height in pixels

Examples:

    **to use a var as like a text or numberr you have to do $ before them, like $MyVar**                          

    BURGER X NUM                    | stores input in variable as a number, use TEXT to store as a string
    BURGER X TEXT

    SALAD Hello, World!             | no matter what you put in here it gets converted to a string.
    SALAD $MyVar                    | to print out a var you need to put a dollarsign then the var name    

    TACO X 8 NUM                   | if NUM is specified then it wont become a string, if TEXT is specified, it will become a string.
    TACO X SpooderCode TEXT    

    STEAK X NUM 64 SALAD hi         | if X is equal to 64 then print "hi". Using NUM or TEXT to check for a number or string.
    STEAK X TEXT cheese SALAD yum

    RAMEN MyVar 128 ADD             | add 128 to MyVar, dont forget to specify which type of math. ADD, SUB, MUL, DIV
    RAMEN MyVar 64 SUB
    RAMEN MyVar 2 MUL
    RAMEN MyVar 4 DIV               
    RAMEN MyVar 4 SET               | Set makes it so MyVar equals 4

    SANDWICH MyLabel                | Create label "MyLabel"
        
    CURRY MyLabel LABEL             | jump to label "MyLabel". LABEL = jump to a label, LINE = jump to a line.
    CURRY 10 LINE                   | 

    CHICKEN #080F03                 | Fills the screen with a hex color, or a predefined color
    CHICKEN red

    SUSHI                           | this will put you back to where you jumped, its sorta like a subroutine!

    PIZZA 60 60 50 50 #000000 5 #00FF00 SQUARE          | This "advanced" keyword will let you do 5 differant graphics!
    PIZZA 60 60 50 50 #000000 5 #00FF00 CIRCLE          | 
    PIZZA 60 60 10 10 #000000 5 #00FF00 LINE            |
    PIZZA 60 60 50 50 #000000 5 #00FF00 FILLED-SQUARE   |
    PIZZA 60 60 50 50 #000000 5 #00FF00 FILLED-CIRCLE   |

    PIZZA x y width height OUTLINE THICKNESS FILL SQUARE     
    PIZZA x1 y1 x2 y2 OUTLINE THICKNESS FILL LINE

    COOKIE D RAMEN MyVar 128 ADD        | This checks if a key is being pressed, super useful for stuff

    CHEESE 10                   | Wait 10 seconds