import time
import raildriver
from TwitchPlays.utils.keyboard import timedHoldRelease
from TwitchPlays.train_sim.train_profiles.class43 import LOCO
from raildriver.library import VALUE_CURRENT


def async_tasks():
    aws_watch()


def controller(line):
    try:
        chat_line = {"user":line[0], "type":line[1], "channel":line[2], "command":line[2:]}
        command = chat_line['command'][1][1:]

        # Process train related commands, LOCO is imported from Train Profile
        if command == "a":
            print "Received command: REGULATOR ACCELERATE"
            timedHoldRelease("a", LOCO['accelerator_duration']) #Accelerate
        elif command == "d":
            print "Received command: REGULATOR RETARD"
            timedHoldRelease("d", LOCO['retard_duration']) #Retard
        elif command == "w":
            print "Received command: REVERSER FORWARD"
            timedHoldRelease("w", LOCO['reverser_duration']) #Forward
        elif command == "s":
            print "Received command: REVERSER REVERSE"
            timedHoldRelease("s", LOCO['reverser_duration']) #Reverse
        elif command == "h":
            print "Received command: TOGGLE LIGHTS"
            timedHoldRelease("h", 1) #Lights
        elif command == "v":
            print "Received command: TOGGLE WIPERS"
            timedHoldRelease("v", 1) #Wipers
        elif command == "b":
            print "Received command: BELL"
            timedHoldRelease("b", LOCO['bell_duration']) #Bell
        elif command == "q":
            print "Received command: AWS RESET"
            timedHoldRelease("q", LOCO['aws_reset_duration']) #Bell
        elif command == ";":
            print "Received command: BRAKE RELEASE"
            timedHoldRelease(";", LOCO['brake_release_duration']) #Brake Release
        elif command == "t":
            print "Received command: OPEN DOORS"
            timedHoldRelease("t", LOCO['door_duration']) #Brake Release
        elif command == "'":
            print "Received command: BRAKE APPLY"
            timedHoldRelease("'", LOCO['brake_apply_duration']) #Brake Release
        elif command == "horn":
            print "Received command: HORN"
            timedHoldRelease("spacebar", LOCO['horn_duration'])
        ##elif command == "emergency":
            ##print "Received command: EMERGENCY BRAKE"
            ##timedHoldRelease("backspace", LOCO['emergency_duration'])

        # Stuff below here is for switching views.
        elif command == "view-cab":
            print "Received command: SWITCH VIEW"
            timedHoldRelease("1", 0.2)
        elif command == "view-chase":
            print "Received command: SWITCH VIEW"
            timedHoldRelease("2", 0.2)
        elif command == "view-flyby":
            print "Received command: SWITCH VIEW"
            timedHoldRelease("4", 0.2)
        elif command == "view-panleft":
            print "Received command: SWITCH VIEW"
            timedHoldRelease("left_arrow", 0.8)
        elif command == "view-panright":
            print "Received command: SWITCH VIEW"
            timedHoldRelease("right_arrow", 0.8)

        # If it's not a command dump the chat line for debug purposes.
        else:
            print "Received chat line: %s" % chat_line['command']
    except Exception, e:
        print "Received IRC chatter: %s" % line

def aws_watch():
    print "Starting aws watcher"
    rd = raildriver.RailDriver(dll_location="C:\\Program Files (x86)\\Steam\\steamapps\\common\\RailWorks\\plugins\\RailDriver.dll")
    while True:
        time.sleep(2)

        try:
            # Here we deal with AWS via RailDriver.dll as Twitch chatters usually see the AWS way to late to respond.
            aws_status = rd.get_controller_value("AWS", VALUE_CURRENT)
            aws_warn_count = rd.get_controller_value("AWSWarnCount", VALUE_CURRENT)
    
            if aws_status == 1.0 or aws_warn_count == 1.0:
                print "Auto command: AWS RESET"
                timedHoldRelease("q", 0.5)
        except Exception, e:
            print "RailDriver not up to speed yet :-P"
