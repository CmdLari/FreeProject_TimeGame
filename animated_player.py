import pygame

class AnimatedPlayer():
    def __init__( self, screen, imgpathlist):

        self.screen = screen

        # load all images into list
        self.frames = []
        for path in imgpathlist:
            self.frames.append( pygame.image.load( path ))

        # Start the animation at the first frame
        self.image = self.frames[0]
        self.rect  = self.image.get_rect()

        # Frame handling
        self.millisec_rate = 450   # inter-frame delay in milliseconds
        self.current_frame = 0
        self.last_frame_at = 0

        # Centering the player
        self.rect.center = self.screen.width/2, self.screen.height/2

    def update_player(self):
        """Animates and draws player on map"""
        # Compare the time of the last frame to time-now
        # and determine if it's time to show the next frame
        time_now = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if ( time_now > self.last_frame_at + self.millisec_rate ):
                    # new frame needed!
                    self.last_frame_at = time_now
                    # Advance to the next frame
                    self.current_frame += 1
                    if ( self.current_frame == len( self.frames ) ):
                        self.current_frame = 0                           # wrap frame loop index
                    # Set the new image
                    self.image = self.frames[ self.current_frame ]
                    self.rect  = self.image.get_rect()
                    self.rect.center = self.screen.width/2, self.screen.height/2
                    self.screen.screen.blit(self.image, self.rect)
        else: 
            self.screen.screen.blit(self.image, self.rect)

