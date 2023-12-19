from ops import *

def apply_gravity(environment, subject):
    collidables = environment.get_collidable(subject.__class__)
    #move the player according to the velocity incrementally
    for step in range(abs(subject.yVelocity)):
        #change y coord by y velocity
        subject.updateCoord(0,sign(subject.yVelocity))
        for rect in collidables:
            #if the subject is colliding with anything
            check = rect.hitbox.collidepoint
            collidetop    = check(subject.hitbox.midtop)
            collidebottom = check(subject.hitbox.midbottom)
            if collidetop or collidebottom:
                #then undo the movement and negate y component of the velocity
                subject.yVelocity = 0
                subject.updateCoord(0,-1 * sign(subject.yVelocity))
                break
    #check to see if player is on the ground
    #if not increase yVelocity and prevent from crouching
    onGround = False
    for platform in collidables:
        collidebottom = platform.hitbox.collidepoint(subject.hitbox.midbottom)
        if collidebottom:
            onGround = True
    if not onGround:
        subject.yVelocity += 1