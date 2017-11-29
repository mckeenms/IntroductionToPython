"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Mason McKeen.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.delay(20)

notsatan = rg.SimpleTurtle()
notsatan.forward(100)
notsatan.left(36)
notsatan.backward(100)
notsatan.left(36)
notsatan.forward(100)
notsatan.left(36)
notsatan.backward(100)
notsatan.left(36)
notsatan.forward(100)

keepitPG = rg.SimpleTurtle()
keepitPG.pen_up()
keepitPG.forward(50)
keepitPG.left(90)
keepitPG.forward(34)
keepitPG.left(90)
keepitPG.pen_down()
keepitPG.draw_circle(50)

#DISCLAIMER: not a satanist, just thought these shapes would be kinda easy

window.close_on_mouse_click()