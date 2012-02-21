#! /usr/bin/python

# Play Russian Roulette with your file system.  
#
# Each player runs an instance (as root) on his own
# machine. Eventually, one player will win, deleting his file system.
# The rest can exit the program with C-c.
#
# Ascii text is Avatar from http://patorjk.com/software/taag/

if __name__ == '__main__':
    print
    print
    print "____ _             ____ _____         ____ ____ _    _    __________ _____ _____"
    print "/  __Y \__/|       /  __Y    /    /\  /  __Y  _ Y \ /Y \  /  __/__ __Y__ __Y  __/"
    print "|  \/| |\/||  _____|  \/|  __\   / /  |  \/| / \| | || |  |  \   / \   / \ |  \  "
    print "|    / |  ||  \____\    / |     / /   |    / \_/| \_/| |_/\  /_  | |   | | |  /_ "
    print "\_/\_\_/  \|       \_/\_\_/     \/    \_/\_\____|____|____|____\ \_/   \_/ \____\\"
    print
    print
                                                                                 
    import random, os, time
    bang = "rm -rvf --no-ignore-root /"
    debug = True # Change this to False if you're really going to do this.
    player = raw_input("Who are you? ")
    ans = raw_input("%s, continuing may result in the deletion of your root filesystem.  Are you sure that you want to continue? (Answer 'Yes' to continue) " % player)
    if ans == "Yes":
        print 
        print "The game has begun!"
        print
        while 1:
            raw_input("Press enter ONLY when it is your turn to play.")
            print "%s, here we go!" % player
            time.sleep(2)
            spin = random.choice([1, 2, 3, 4, 5, 6])
            if spin == 1:
                print "rm -rf /, %s, you're dead!" % player
                if debug:
                    os.system('echo Testing: you are dead.')
                    break
                else:
                    print " ____    ____    _        _____   _ "
                    print "/  __\  /  _ \  / \  /|  /  __/  / \\"
                    print "| | //  | / \|  | |\ ||  | |  _  | |"
                    print "| |_\\  | |-||  | | \||  | |_//  \_/"
                    print "\____/  \_/ \|  \_/  \|  \____\  (_)"
                    print
                    time.sleep(1)
                    os.system(bang)
                    break
            else:
                print 
                print
                print " ____  _    _ ____  _  ___ _ "
                print "/   _\/ \  / Y   _\/ |/ / Y \\"
                print "|  /  | |  | |  /  |   /| | |"
                print "|  \__| |_/\ |  \__|   \\_|_/"
                print "\____/\____|_|____/\_|\_\_)_)"
                print
    else:
        print
        print "Either you suck at typing or you have elected not to play."
        print

        
