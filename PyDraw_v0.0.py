import pygame
import os
import sys
import csv
#import board
#import adafruit_dotstar as dotstar

# --- Set matrix variable
#dots = dotstar.DotStar(board.SCK, board.MOSI, 64, brightness=0.50)

class button:
    def __init__(self, nameplate, loc, size, color, border, screen, lfont, fsize=25, cen=True):
        self.nameplate = nameplate
        self.loc = loc
        self.size = size
        self.color = color
        self.border = border
        self.screen = screen
        self.lfont = lfont
        self.fsize = fsize
        self.cen = cen        

    def draw(self):
        bx = self.loc[0]
        by = self.loc[1]
        x = bx + self.border
        y = by + self.border
        bw = self.size[0]
        bh = self.size[1]
        w = bw - (self.border * 2)
        h = bh - (self.border * 2)
        tsize = self.lfont.size(self.nameplate)
        wcen = bx + ((bw - tsize[0]) / 2)
        if self.cen:
            hcen = by + ((bh - tsize[1]) / 2)
        else:
            hcen = by + 5

        textbox = self.lfont.render(self.nameplate, True, (0, 0, 0))
        # --- Draw border
        pygame.draw.rect(self.screen, (0, 0, 0), [bx, by, bw, bh])
        # --- Draw button face
        pygame.draw.rect(self.screen, self.color, [x, y, w, h])
        # --- Draw nameplate on button
        self.screen.blit(textbox,(wcen, hcen))

class label:
    def __init__(self, nameplate, loc, size, color, border, screen, lfont, fsize=25, align='CenMid'):
        self.nameplate = nameplate
        self.loc = loc
        self.size = size
        self.color = color
        self.border = border
        self.screen = screen
        self.lfont = lfont
        self.fsize = fsize
        self.align = align

    def draw(self):
        bx = self.loc[0]
        by = self.loc[1]
        x = bx + self.border
        y = by + self.border
        bw = self.size[0]
        bh = self.size[1]
        w = bw - (self.border * 2)
        h = bh - (self.border * 2)
        tsize = self.lfont.size(self.nameplate)
        wcen = bx + ((bw - tsize[0]) / 2)
        match self.align:
            case "UpLeft":
                wcen = bx + 5
                hcen = by + 5
            case "MidLeft":
                wcen = bx + 5
                hcen = by + ((bh - tsize[1]) / 2)
            case "LowLeft":
                wcen = bx + 5
                hcen = by + ((bh - tsize[1]) - 5)
            case "UpCen":
                wcen = bx + ((bw - tsize[0]) / 2)
                hcen = by + 5
            case "MidCen":
                wcen = bx + ((bw - tsize[0]) / 2)
                hcen = by + ((bh - tsize[1]) / 2)
            case "LowCen":
                wcen = bx + ((bw - tsize[0]) / 2)
                hcen = by + 5
            case "UpRight":
                wcen = bx + ((bw - tsize[0]) / 2)
                hcen = by + 5
            case "MidRight":
                wcen = bx + ((bw - tsize[0]) / 2)
                hcen = by + ((bh - tsize[1]) / 2)
            case "LowRight":
                wcen = bx + ((bw - tsize[0]) / 2)
                hcen = by + 5

        textbox = self.lfont.render(self.nameplate, True, (0, 0, 0))
        # --- Draw border
        pygame.draw.rect(self.screen, (0, 0, 0), [bx, by, bw, bh])
        # --- Draw button face
        pygame.draw.rect(self.screen, self.color, [x, y, w, h])
        # --- Draw nameplate on button
        self.screen.blit(textbox,(wcen, hcen))

# --- Define initial colors
BLACK = (0, 0, 0)
SILVER = (192, 192, 192)
ORANGE = (255, 96, 0)
WHITE = (255, 255, 255)
MAROON = (128, 0, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
FUCHSIA = (255, 0, 255)
GREEN = (0, 128, 0)
LIME = (0, 255, 0)
OLIVE = (128, 128, 0)
YELLOW = (255, 255, 0)
NAVY = (0, 0, 128)
BLUE = (0, 0, 255)
TEAL = (0, 128, 128)
CYAN = (0, 255, 255)

# --- Set Width and Height of each grid location
width = 52
height = 52

# --- Set Margin between cells
margin = 3

# --- Variable used to hold brightness level
brtIndex = 5
BrightLevel = 30
              
# --- Screen-clearing code goes here
CANVAS = [[BLACK]*8 for _ in range(8)]
    
# --- Palette initialization and setting
palette_data = [[BLACK]*8 for _ in range(2)]
PALETTE = [[BLACK]*8 for _ in range(2)]
PALETTE [0][0] = BLACK
PALETTE [0][1] = ORANGE
PALETTE [0][2] = MAROON
PALETTE [0][3] = PURPLE
PALETTE [0][4] = GREEN
PALETTE [0][5] = OLIVE
PALETTE [0][6] = NAVY
PALETTE [0][7] = TEAL
PALETTE [1][0] = SILVER
PALETTE [1][1] = WHITE
PALETTE [1][2] = RED
PALETTE [1][3] = FUCHSIA
PALETTE [1][4] = LIME
PALETTE [1][5] = YELLOW
PALETTE [1][6] = BLUE
PALETTE [1][7] = CYAN
    
pygame.font.init()
lrgFontSize = 45
smFontSize = 25
myfont = pygame.font.SysFont('Times New Roman MS', lrgFontSize)
myfontSm = pygame.font.SysFont('Times New Roman MS', smFontSize)

pygame.init()
 
# --- Set the width and height of the screen [width, height]:
size = (600, 600)
screen = pygame.display.set_mode(size)

# --- Background and screen objects (labels and buttons... so far):
BG = WHITE
lblRed = label('Red', [130, ((height + margin) * 8) + 20], [100, 50], BG, 0, screen, myfont, 45, 'MidLeft')
lblGreen = label('Green', [130, ((height + margin) * 8) + 60], [100, 50], BG, 0, screen, myfont, 45, 'MidLeft')
lblBlue = label('Blue', [130, ((height + margin) * 8) + 100], [100, 50], BG, 0, screen, myfont, 45, 'MidLeft')
butReset = button('Reset',[349, 539], [85, 33], ORANGE, 1, screen, myfontSm)
butBrightness = button('Brightness', [margin - 1, (margin + height) * 8 + 30], [100, 100], BG, 1, screen, myfontSm, smFontSize, False)
butMinus = button('-', [margin * 2 + 5, (margin + height) * 8 + 90], [30, 30], BG, 1, screen, myfont, lrgFontSize)
butPlus = button('+', [(margin * 2) + 50 + 5, (margin + height) * 8 + 90], [30, 30], BG, 1, screen, myfont, lrgFontSize)
lblBrtLvl = button(str(BrightLevel), [margin, (margin + height) * 8 + 60], [98, 30], BG, 0, screen, myfont, lrgFontSize)

# --- Paintbrush object(s):
brushR = button('', [522, 522], [76, 76], BLUE, 1, screen, myfont)
brushL = button('', [490, 490], [76, 76], PURPLE, 1, screen, myfont)

R,G,B = brushL.color

# --- Create dynamic labels
ioRed = label('= ' + str(R), [235, ((height + margin) * 8) + 20], [100, 50], BG, 0, screen, myfont, 45, 'MidLeft')
ioGreen = label('= ' + str(G), [235, ((height + margin) * 8) + 60], [100, 50], BG, 0, screen, myfont, 45, 'MidLeft')
ioBlue = label('= ' + str(B), [235, ((height + margin) * 8) + 100], [100, 50], BG, 0, screen, myfont, 45, 'MidLeft')

# --- Collision zones (using Rect objects):
zBrightness = pygame.Rect(butBrightness.loc, butBrightness.size)
zMinus = pygame.Rect(butMinus.loc, butMinus.size)
zPlus = pygame.Rect(butPlus.loc, butPlus.size)
zReset = pygame.Rect(butReset.loc, butReset.size)

# --- Other screen Zone constraints:
CanvasPos = [(margin + width) * 8, (margin + height) * 8]
PalettePos = [600 - ((margin + width) * 2), (margin + height) * 8]

# --- Set header text:
pygame.display.set_caption("Canvas")
 
# --- Loop until the user clicks the close button:
done = False
 
# --- Used to manage how fast the screen updates:
clock = pygame.time.Clock()

# --- Init screen:
screen.fill(BG)

# --- Mouse state variables:
lclick = False
lclickedge = False
mclick = False
rclick = False

# --- Program loop:
while not done:
    for event in pygame.event.get():  #User does something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        else: #If user did not quit....
        # --- Mouse event(s):
            lclickedge = False
            rclickedge = False
            scrlup = False
            scrldn = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    lclick = True
                    lclickedge = True
                if event.button == 2:
                    mclick = True
                if event.button == 3:
                    rclick = True
                    rclickedge = True
                if event.button == 4:
                    scrlup = True    
                if event.button == 5:
                    scrldn = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    lclick = False
                if event.button == 2:
                    mclick = False
                if event.button == 3:
                    rclick = False
                            
        # --- Position and collision detect variables:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            ctrlBright = pygame.Rect.collidepoint(zBrightness, x, y)
            ctrlMinus = pygame.Rect.collidepoint(zMinus, x, y)
            ctrlPlus = pygame.Rect.collidepoint(zPlus, x, y)
            ctrlReset = pygame.Rect.collidepoint(zReset, x, y)            
            cx = CanvasPos[0]
            cy = CanvasPos[1]
            px = PalettePos[0]
            py = PalettePos[1]
            p_off = size[0] - ((width + margin) * 2)

        # --- Canvas Updates:
            if (lclick and x < cx and y < cy):
            # Change the x/y screen coordinates to grid coordinates:
                col = x // (width + margin)
                row = y // (height + margin)
            # Set that location to one
                CANVAS[col][row] = brushL.color
            elif (rclick and x < cx and y < cy):
            # Change the x/y screen coordinates to grid coordinates:
                col = x // (width + margin)
                row = y // (height + margin)
            # Set that location to one:
                CANVAS[col][row] = brushR.color
            
            # --- Selected new color
            elif (lclickedge and x > px and y < py):
                col = (x - p_off) // (width + margin)
                row = y // (height + margin)
            # Set paintbrush color from palette
                brushL.color = PALETTE[col][row]
            elif (rclickedge and x > px and y < py):
                col = (x - p_off) // (width + margin)
                row = y // (height + margin)
            # Set paintbrush color from palette
                brushR.color = PALETTE[col][row]                

        # --- Reset clicked?
            elif (lclick and ctrlReset):
                CANVAS = [[BLACK]*8 for _ in range(8)]
                
        # --- Brightness modified?
            elif (lclickedge and ctrlMinus and BrightLevel > 0):
                BrightLevel -= brtIndex
            elif (lclickedge and ctrlPlus and BrightLevel < 100):
                BrightLevel += brtIndex
        # -- Brightness controls with scrollwheel    
            elif (scrlup and ctrlBright and BrightLevel < 100):
                BrightLevel += brtIndex
            elif (scrldn and ctrlBright and BrightLevel > 0):
                BrightLevel -= brtIndex
            else:
                pass
        # --- Set the screen background:
            lblBrtLvl.nameplate = str(BrightLevel)
            screen.fill(BG)

# --- Draw Canvas ---
    for row in range(8):
        for col in range(8):

            pygame.draw.rect(screen,
                                BLACK,
                                [(margin + width) * col + (margin - 1),
                                (margin + height) * row + (margin - 1),
                                width + 2,
                                height + 2])
            brR, brG, brB = CANVAS [col][row]
            brR *= (BrightLevel * 0.01)
            brG *= (BrightLevel * 0.01)
            brB *= (BrightLevel * 0.01)
            adjColor = brR, brG, brB
            pygame.draw.rect(screen,
                                adjColor,
                                [(margin + width) * col + margin,
                                (margin + height) * row + margin,
                                width,
                                height])    
            
# --- Draw palette for color choices ---
    file = open('palette.csv' , 'w', newline = '')
    for row in range(8):
        for col in range(2):
            pygame.draw.rect(screen,
                                BLACK,
                                [(margin + width) * col + (margin - 1) + (p_off - margin),
                                (margin + height) * row + (margin - 1),
                                width + 2,
                                height + 2])
            pygame.draw.rect(screen,
                                PALETTE [col][row],
                                [(margin + width) * col + margin + (p_off - margin),
                                (margin + height) * row + margin,
                                width,
                                height])
            palette_data [col][row] = PALETTE [col][row]
    with file:
        write = csv.writer(file)
        write.writerows(palette_data)
    file.close()
    
# --- Load I/O labels and draw RGB Values:
    R,G,B = brushL.color
    ioRed.nameplate = '= ' + str(R)
    ioGreen.nameplate = '= ' + str(G)
    ioBlue.nameplate = '= ' + str(B)
    
    # -- Draw labels & I/O labels:
    lblRed.draw(), ioRed.draw(), lblGreen.draw(), ioGreen.draw(), lblBlue.draw(), ioBlue.draw()
    
# --- Draw a Reset button:
    butReset.draw()
    
# --- Draw Brightness controls:
    # -- Main panel (not a button, but it works!);
    butBrightness.draw()
        
    # -- Brightness level display;
    lblBrtLvl.draw()
        
    # -- Minus and Plus keys;    
    butMinus.draw(), butPlus.draw()

# --- Draw paint brush display(s):    
    brushR.draw(), brushL.draw()

# --- Go ahead and update the screen with what we've drawn:
    pygame.display.flip()

# --- Limit to 60 frames per second:
    clock.tick(60)

 # --- Send list to Matrix
#    dots.brightness = 1.0
#    for row in range(8):
#        for col in range(8):
#            brR, brG, brB = CANVAS [col][row]
#            brR = (brR // 10) * (BrightLevel * 0.1)
#            brG = (brG // 10) * (BrightLevel * 0.1)
#            brB = (brB // 10) * (BrightLevel * 0.1)
#            adjColor = brR, brG, brB
#            dots[(col * 8) + row] = adjColor
#    #dots.brightness = BrightLevel / 10 #<<<<issue with new dotstar driver. lights flash red below 0.50 (50%)

# --- Close the window and quit.
pygame.quit()