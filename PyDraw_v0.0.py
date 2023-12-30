import pygame
import os
import sys
import csv
#import board
#import adafruit_dotstar as dotstar

# --- Set matrix variable
#dots = dotstar.DotStar(board.SCK, board.MOSI, 64, brightness=0.50)

class button:
    def __init__(self, nameplate, loc, size, color, border, screen, lfont, fsize=25):
        self.nameplate = nameplate
        self.loc = loc
        self.size = size
        self.color = color
        self.border = border
        self.screen = screen
        self.lfont = lfont
        self.fsize = fsize

    def draw(self):
        bx = self.loc[0]
        by = self.loc[1]
        x = bx + self.border
        y = by + self.border
        bw = self.size[0]
        bh = self.size[1]
        w = bw - (self.border * 2)
        h = bh - (self.border * 2)
        wcen = bx - ((bw - (len(self.nameplate) * (self.fsize / 0.75))) / 2)
        hcen = by + ((bh - (self.fsize / 0.75)) / 2)

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
width = 45
height = 45

# --- Set Margin between cells
margin = 3

# --- Variable used to hold brightness level
BrightLevel = 0

# --- Screen Zone constraints
CanvasPos = [(margin + width) * 8, (margin + height) * 8]
PalettePos = [600 - ((margin + width) * 2), (margin + height) * 8]
ResetPos = [349, 539, 349 + 85, 539 + 34]
MinusPos = [(margin * 2) + 2, (margin + height) * 8 + 92,
            ((margin * 2) + 2) + 26, ((margin + height) * 8 + 92) + 26]
PlusPos = [(margin * 2) + 52, (margin + height) * 8 + 92,
           ((margin * 2) + 52) + 26, ((margin + height) * 8 + 92) + 26]
              
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

PaintBrush = BLUE
    
pygame.font.init()
lrgFontSize = 45
smFontSize = 25
myfont = pygame.font.SysFont('Times New Roman MS', lrgFontSize)
myfontSm = pygame.font.SysFont('Times New Roman MS', smFontSize)

pygame.init()
 
# --- Set the width and height of the screen [width, height]
size = (600, 600)
screen = pygame.display.set_mode(size)

ResetSurface = myfont.render('Reset', True, (255, 255, 255), (255, 165, 0))
RedSurface = myfont.render('Red = ', True, (0, 0, 0))
BlueSurface = myfont.render('Blue = ', True, (0, 0, 0))
GreenSurface = myfont.render('Green = ', True, (0, 0, 0))
PlusSur = myfont.render('+', False, (0, 0, 0))
MinusSur = myfont.render('-', False, (0, 0, 0))
BrightnessSur = myfontSm.render('Brightness', True, (0, 0, 0))

 
pygame.display.set_caption("Canvas")
 
# --- Loop until the user clicks the close button.
done = False
 
# --- Used to manage how fast the screen updates
clock = pygame.time.Clock()

# --- Init screen
screen.fill(WHITE)
 # --- Mouse state variables
lclick = False
mclick = False
rclick = False

# --- Program loop
while not done:
    for event in pygame.event.get():  #User does something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        else: #If user did not quit....
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    lclick = True
                if event.button == 2:
                    mclick = True
                if event.button == 3:
                    rclick = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    lclick = False
                if event.button == 2:
                    mclick = False
                if event.button == 3:
                    rclick = False
            
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            cx = CanvasPos[0]
            cy = CanvasPos[1]
            px = PalettePos[0]
            py = PalettePos[1]
            p_off = size[0] - ((width + margin) * 2)

            # --- Canvas Updates
            if (lclick and x < cx and y < cy):
                # Change the x/y screen coordinates to grid coordinates
                col = x // (width + margin)
                row = y // (height + margin)
                # Set that location to one
                CANVAS[col][row] = PaintBrush
                print("Click ", pos, "Grid coordinates: ", row, col, CanvasPos)
            
            # --- Selected new color
            elif (lclick and x > px and y < py):
                col = (x - p_off) // (width + margin)
                row = y // (height + margin)
                # Set paintbrush color from palette
                PaintBrush = PALETTE[col][row]
                print("Click ", pos, "Pal. coordinates: ", row, col, PalettePos)

            # --- Reset clicked?
            elif (lclick and pos[0] > ResetPos[0] and\
            pos[0] < ResetPos[2] and\
            pos[1] > ResetPos[1] and\
            pos[1] < ResetPos[3]):
                CANVAS = [[BLACK]*8 for _ in range(8)]
                print("Click ", pos, "Grid coordinates: ", row, col, CanvasPos)

            # --- Brightness modified?
            elif (lclick and pos[0] > MinusPos[0] and\
            pos[0] < MinusPos[2] and\
            pos[1] > MinusPos[1] and\
            pos[1] < MinusPos[3] and\
            BrightLevel > 0):
                BrightLevel = BrightLevel - 1
                print("Click ", pos, MinusPos)
            elif (lclick and pos[0] > PlusPos[0] and\
            pos[0] < PlusPos[2] and\
            pos[1] > PlusPos[1] and\
            pos[1] < PlusPos[3] and\
            BrightLevel < 10):
                BrightLevel = BrightLevel + 1
                print("Click ", pos, "Grid coordinates: ", row, col, CanvasPos)
            else:
                
                # Set the screen background
                screen.fill(WHITE)
        
    # --- Draw Canvas ---
    for row in range(8):
        for col in range(8):
            pygame.draw.rect(screen,
                                BLACK,
                                [(margin + width) * col + (margin - 1),
                                (margin + height) * row + (margin - 1),
                                width + 2,
                                height + 2])
            pygame.draw.rect(screen,
                                CANVAS [col][row],
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
    
    # --- Draw a Reset button and RGB Values
    R,G,B = PaintBrush
    RedSurface = myfont.render('Red = ' + str(R), True, (0, 0, 0), (255, 255, 255))
    GreenSurface = myfont.render('Green = ' + str(G), True, (0, 0, 0), (255, 255, 255))
    BlueSurface = myfont.render('Blue = ' + str(B), True, (0, 0, 0), (255, 255, 255))
    pygame.draw.rect(screen, WHITE, [149, ((height + margin) * 8) + 29,
                                        340, ((height + margin) * 8) + 160])
    screen.blit(RedSurface, (150, ((height + margin) * 8) + 30))
    screen.blit(GreenSurface, (150, ((height + margin) * 8) + 70))
    screen.blit(BlueSurface, (150, ((height + margin) * 8) + 110))

    butReset = button('Reset',[349, 539], [85, 33], ORANGE, 1, screen, myfontSm, smFontSize)
    butReset.draw()
    #pygame.draw.rect(screen, BLACK, [349, 539, 85, 33])
    #screen.blit(ResetSurface,(350, 540))

    # --- Draw Brightness controls
    pygame.draw.rect(screen, BLACK, [margin - 1, (margin + height) * 8 + 30, 100, 100])
    pygame.draw.rect(screen, WHITE, [margin, (margin + height) * 8 + 31, 98, 98])
    screen.blit(BrightnessSur,((margin * 2) + 3, (margin + height) * 8 + 35))
    
    BrightLevelSur = myfont.render(str(BrightLevel), True, (0, 0, 0))
    screen.blit(BrightLevelSur,((margin * 2) + 30 + 5, (margin + height) * 8 + 60))
    
    pygame.draw.rect(screen, BLACK, [margin * 2 + 5, (margin + height) * 8 + 90, 30, 30])
    pygame.draw.rect(screen, WHITE, [(margin * 2) + 2 + 5, (margin + height) * 8 + 92, 26, 26])
    screen.blit(MinusSur,((margin * 2) + 15, (margin + height) * 8 + 90))

    pygame.draw.rect(screen, BLACK, [(margin * 2) + 50 + 5, (margin + height) * 8 + 90, 30, 30])
    pygame.draw.rect(screen, WHITE, [(margin * 2) + 52 + 5, (margin + height) * 8 + 92, 26, 26])
    screen.blit(PlusSur,((margin * 2) + 57 + 5, (margin + height) * 8 + 88))

# --- Draw paint brush display
    pygame.draw.rect(screen, BLACK, [479 + margin, 479, 102, 102])
    pygame.draw.rect(screen, PaintBrush, [480 + margin, 480, 100, 100])
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

    # --- Send list to Matrix
#    for row in range(8):
#        for column in range(8):
#            dots[(column * 8) + row] = CANVAS[column][row]
#    dots.brightness = BrightLevel / 10
 
# --- Close the window and quit.
pygame.quit()
