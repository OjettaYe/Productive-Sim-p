﻿# The script of the game goes in this file.
#python
init python:
    from datetime import datetime



# Declare characters used by this game. The color argument colorizes the
# name of the character.

define god = Character("God")
define YN = Character(name=None)
define healthgod = Character("God of Health")
define guide = Character("God of Guidance")
define guidep = Character("Caitlyn")
define unknown = Character("???")
define prezzz = Character("Prezzz")

define sleepstart = 0
define sleepend = 0
define sleeplength = 0
define firstTimeT5 = True
define isOvernight = False

define now = 0

define time1 = 0
define time2 = 0

# The game starts here.

label start:
    $ YN = ""
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #Scene 1
    scene bg-galaxy
    with fade

    $ YN = renpy.input("What is your name? ")
    $ YN = YN.strip()
    if YN == "":
        $ YN = "Y/N"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show god you died

    # These display lines of dialogue.

    "You're floating.​"

    "Around you is a horizon of stars stretching into the dark backdrop of the universe.​"

    "And in front of you is a woman with a halo above your head looking at you with an unreadable expression on her face.​"

    show god with fade

    god "Hmmm..."

    YN "What? Who are you?"

    god "Hello [YN]. I am what you call 'God' "

    YN "Where am I?"

    god "The afterlife. You were hit by a truck. Don't worry about it. "

    YN "What?! Am I dead?"

    god "Yes, unfortunately. But don't worry! You're going to go to a better place."

    YN "Where am I heading?"

    god "See, originally, you were supposed to be the savior of this neat little world I had going on, right?"
    god "The whole, classic, hero from another dimension versus demon kind of thing..."
    god "Though, looking at you, that's not happening anytime soon."

    YN "What? Why??"

    god "Well, how are you suppposed to save the world when you can't even save yourself?"
    god "I'm sending you to Health Camp. Off you go!"

    "{i}She punts you into the distance{/i} (cue Mario-like scream)?"

    # Scene 2
    scene gate
    with vpunch

    "You fall right in front of the gates of Health Camp. On the gates, a text is inscribed:"
    "HEALTH CAMP, HEALTH LIMBO (get your sh*t together)"

    "{i} The god of Health arrives in front of the gates to see what all the ruckus is about {/i}"

    show healthgod with moveinleft

    healthgod "What? Why do I get another slacker here again? The big god really doesn't pick the right
    people for her scenarios."
    healthgod "LISTEN HERE SLACKER. WELCOME TO HEALTH CAMP."
    healthgod "ONCE THIS CAMP IS FINISHED WITH YOU, YOU'LL BE THE PINNACLE OF HEALTH."
    healthgod "IF YOU EVER WANT TO LEAVE, YOU'LL HAVE TO GET A BADGE FROM ALL FIVE CAMP COUNSELORS."
    healthgod "IN THE MEANTIME, YOU CAN EXPECT TO GO THROUGH HELL IN ORDER TO GET RID OF THOSE BAGS UNDER YOUR EYES" with hpunch
    healthgod "THOSE SORRY EXCUSES FOR ARMS" with hpunch
    healthgod "AND THAT CRUSTY LOOK. EVEN A ROCK DRINKS MORE WATER THAN YOU DO " with hpunch
    healthgod "HAVE YOU UNDERSTOOD SLACKER?"

    YN "Uhh, what?"

    healthgod "WHAT DID YOU SAY SLACKER? NO QUESTIONS!" with hpunch
    healthgod "I WANT A 'YES GOD OF HEALTH' FROM YOU! DID YOU GET THAT SLACKER?"

    YN 'Yes God of Health'

    healthgod "LOUDER SLACKER. GET ALL THAT POLLUTION OUT OF YOUR LUNGS" with hpunch

    YN "YES GOD OF HEALTH" with hpunch

    healthgod "GOOD. GET OFF THOSE SORRY GLUTES, SLACKER, AND HEAD TO CAMPSITE 4. THAT'S WHERE YOU'LL
    BE STAYING DURING YOUR TRAINING ARC"
    healthgod "CAMPFIRE ORIENTATION IS AT 7PM SHARP. IF YOU'RE LATE, I'LL FINE YOU 500 PUSH UPS. DID YOU GET THAT SLACKER?"

    YN "YES GOD OF HEALTH" with hpunch

    healthgod "VERY WELL SLACKER. YOU'RE DISMISSED"

    hide healthgod with moveoutleft
    scene lake
    with slideleft

    "You walk over to campsite 4, sit down and look at the lake in the distance. What just happened to you?"
    "Did you really just die and get sent to a fitness bootcamp run by the most aggressive fitness trainer in the world? (or afterlife?)"
    "As you get lost in your thoughts, you slowly fall asleep. So much has happened, and you feel so, so tired."
    "A small nap wouldn't hurt right?"

    #Scene 3

    scene black
    with fade

    "You feel a slight chill run down your spine as you come back to consciousness. What is this ominous feeling you have?"
    
    scene sunset
    with fade

    "As you watch the sun set, you suddenly remember about the campfire orientation event!!!"
    YN "{b} OH NOOOO!!!!! {/b}" with hpunch

    "You look at your watch. 6:58 PM! Without skipping a beat, you dash across the tents and go sit by the campfire
    , sitting down on a log just as your watch indicates 7:00 PM!"

    show healthgod at right with moveinright

    "{i} The [healthgod] watches your antics with a disapproving look {/i}"

    hide healthgod at right with moveoutright

    "You look around. A handful of people sit on large wooden logs, chatting with each other or roasting marshmallows.
    Soft guitar strums are heard along with the crackling of the flames."

    "A tall woman with a bucket hat approaches you with a friendly smile."

    show guide at left with moveinleft

    guide "Well hello there! Welcome to Health Bootcamp! I'm the [guide], but you can just call
    me [guidep]!"
    guidep "Is there anything you'd like to know?"

    YN "What just happened to me?"

    guidep "Yeahhh, sorry about that. Our leaders can be quite eccentric, but I assure you that the normal folks here are great!"

    show healthgod at right with moveinright

    "The [healthgod] frowns. Is he able to hear your conversation? Are gods all-knowing? Can he read your thoughts?"

    hide healthgod at right with moveoutright

    guidep "Just neat people all around!"
    guidep "Don't worry too much okay? We're here to work on ourselves and have a good time!"

    YN "Could you show me around?"

    guidep "Of Course! We have 5 main tents here. Each one is adapted to a specific facet of your health."

    #show Shef
    scene tent1
    guidep "Tent 1 is dedicated to your nutritional habits."
    
    scene tent2
    #show h2uwu
    guidep "Tent 2 is for your hydration."

    scene tent3
    #show buff lad
    guidep "Tent 3 is the fitness space."

    scene tent4
    #show grass lass
    guidep "Tent 4 is for all your social needs."

    scene tent5
    show prezzz at right with moveinright
    guidep "And Tent 5 is to go to sleep."

    hide prezzz at right with moveoutright

    scene sunset
    guidep "I suggest you go meet them! Return to me afterwards if you have any other questions."
    hide guide at left with moveoutleft

    label mentorpick:
    python:
        now = datetime.now()
        hour = float(now.strftime('%H'))
        if hour >= 23.0 or hour <= 6.0:
            isOvernight =  True
        else:
            isOvernight = False
    if isOvernight:
        show prezzz with moveinleft
        if firstTimeT5:
            prezzz "Why in the afterlife are you awake?" with hpunch
            prezzz "If you don't go back to sleep now, I'll knock you unconscious" with hpunch
        else:
            prezzz "Why in the afterlife are you awake?" with hpunch
            prezzz "If you don't go back to sleep now, I'll knock you unconscious" with hpunch
        hide prezzz with moveinleft


    menu:
        "Which mentor would you like to know?"

        "Tent 1 councilor, Shef":
            "Mmmh, it seems she's not there yet. Maybe try another tent?"
            jump mentorpick
        "Tent 2 councilor, H2wu":
            "Mmmh, it seems she's not there yet. Maybe try another tent?"
            jump mentorpick
        "Tent 3 councilor, Buffie":
            "Mmmh, it seems she's not there yet. Maybe try another tent?"
            jump mentorpick
        "Tent 4 councilor, Grass Lass":
            "Mmmh, it seems she's not there yet. Maybe try another tent?"
            jump mentorpick
        "Tent 5 councilor, Prezzz":
            "You walk towards tent 5"
            jump tent5

label tent5:
    scene tent5
    "You arrive at the tent on the far right."
    show prezzz with moveinright
    if firstTimeT5:
        unknown "You must be the newbie. I'm assuming you're here for bedtime?"
        unknown "It's a little early for that, but hey, to each their own."
    
    
    label menutent5:
    menu:
        "Yes, sleep. Please":
            "What's your sleep schedule like?"
            $sleeptxt = ''
            $validtime = True
            $error=''
            $overnight=""
            $timeslept = 0
            label entersleep:
            $sleeptxt = renpy.input("Please enter when you go to bed (h:min) ")
            python:
                from datetime import datetime
                try:
                    sleepstart = datetime.strptime(sleeptxt, "%H:%M")
                    validtime = True
                except Exception as e:
                    error = e
                    validtime = False
            if validtime != True :
                "Sorry, that's an invalid time."
                jump entersleep
            $sleeptxt = renpy.input("Please enter when you wake up (h:min) ")
            python:
                import time
                try:
                    sleepend = datetime.strptime(sleeptxt, "%H:%M")
                    validtime = True
                except Exception as e:
                    error = e
                    validtime = False
            if validtime != True :
                "Sorry, that's an invalid time."
                jump entersleep
            #Time choices
            python:
                def timeAdd(t1, t2):
                    time1 = float(t1.strftime('%H')) + (float(t1.strftime('%M')))/60
                    time2 = float(t2.strftime('%H')) + (float(t2.strftime('%M')))/60
                    if float(t2.strftime('%H')) < float(t1.strftime('%H')):
                        time2 = 24 + time2
                    return (time2-time1)
                sleeplength = timeAdd(sleepstart, sleepend)
            if sleeplength < 6.0:
                "Yikes, you really do need to work on that huh?"
            else:
                "Hmm, and you actually stick to that?"
            jump menutent5

        "I just wanted to meet the mentor" if firstTimeT5:
            unknown "I am the mentor for your poor soul's sleep schedule. You can call me Prezzz.
            It's short for Sleep President"

            YN "... but you don't look sleepy"

            prezzz "Exactly. Because I get enough sleep."

            "She squints at your eyebags, pointedly"

            prezzz "Unlike {i}you{/i}"
            $firstTimeT5 = False
            jump menutent5
        "Mmh, actually no. (Return to all tents)":
            "See you later. (Whispers: {i}in your dreams{/i})"
    hide prezzz at right with moveoutright
    jump mentorpick


        







    #Scene 4

    # This ends the game.
    return
