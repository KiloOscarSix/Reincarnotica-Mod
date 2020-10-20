label episode2_intro:

    stop music

    scene black

    show ep_2_title at truecenter with dissolve
    $ renpy.pause(1.5, hard=True)
    hide ep_2_title with dissolve

    play music 'soundfx/night_ambiance.ogg' loop

    pause

    "..."
    "..."
    "(Hng..?)"
    "(Where the hell am... I?)"
    "(This is..?)"

    scene dream_bg1
    with slowfade

    show mc_sprite with dissolve:
        xalign 0.1
        yalign 0.6

    "(A forest?)"
    "(How did I get here?)"
    "(Hmm?)"
    "(Something seems to be glowing over there.)"

    play sfx1 'soundfx/walking_forest.ogg'

    show mc_sprite:
        xalign 0.1
        yalign 0.6
        linear 5 xpos 1.0

    "..."

    scene dream_bg2 with PushMove(2.0, "pushleft")

    stop sound

    play sound  'soundfx/campfire.ogg' loop

    show campfire:
        xalign 0.55
        yalign 0.6

    show oldman_sprite:
        xalign 0.72
        yalign 0.6

    show mc_sprite with dissolve:
        xalign 0.1
        yalign 0.6

    mx "O-Old man!?"
    old "Oh-ho! {p} Welcome, Chosen One."

    play sfx1 'soundfx/walking_forest.ogg'

    show mc_sprite:
        xalign 0.1
        yalign 0.6
        linear 3 xpos 0.35

    old "Want some meat?"
    mx "Meat? No, I don't want... wait."
    mx "Y-You can speak? My voice.."
    old "I've been always able to speak. It's just that you were too weak back then."
    old "Which forced me to communicate with you by other means."
    mx "Then those doors... those visions... are they?"
    old "They are one's desires that manifested on to you due to your brain's instability."
    mx "What do you mean?"

    hide all

    scene dream_bg3 with PushMove(3.0, "pushdown")

    old "You see..."
    old "Your power comes from your brain."
    mx "My brain?"

    show mc_sprite with dissolve:
        xalign 0.5
        yalign 0.5

    old "A human's brain has a fairly weak electric signal that it uses to create thoughts."
    old "Think of it as each people having their own personal broadcast station and television in their heads."

    show tv_01 with dissolve
    pause 0.2

    old "And each and every one has a frequency unique to them."

    show tv_02 with dissolve
    pause 0.2

    old "That only they can watch and hear."

    show tv_03 with dissolve
    pause 0.2

    old "No matter what someone does, they will be unable to reach it."

    show tv_04 with dissolve
    pause 0.2

    old "But..."
    show tv_05 with dissolve

    old "What if there's someone. {p} Someone who can tap on that frequency."

    show tv_06 with dissolve
    pause 0.2

    old "Someone like you, The Chosen One."
    mx "Me?"
    old "You have the power to read other people's thoughts albeit still unconsciously."
    old "You are still weak but with perseverance you can unlock that potential."

    show chicken with dissolve:
        xalign 0.5
        yalign 0.3

    old "And with a mere thought..."
    old "You can..."

    show tv_screen_chicken

    old "Change other's thoughts and even... {p} ...control them."
    mx "C-Control...?"
    old "Yes, control of one's thoughts."

    hide all with dissolve

    scene dream_bg2 with PushMove(3.0, "pushup")

    show mc_sprite:
        xalign 0.35
        yalign 0.6

    show campfire:
        xalign 0.55
        yalign 0.6

    show oldman_sprite:
        xalign 0.72
        yalign 0.6

    mx "Woah. {p} I don't know if..."
    old "You don't need to hurry, Chosen One."
    old "Power like that isn't something to hasten to acquire for."
    mx "Who exactly are you..?"
    old "I am the manifestation of that power..."
    mx "Huh? What do you mean by—"

    hide mc_sprite
    show mc_sprite_v with dissolve:
        xalign 0.35
        yalign 0.6

    mx "Urk! M-My body! It's..."
    old "So, you've run out of \"Tokens\", huh?"
    old "Train well."
    mx "W-Wait... noo..."

    show mc_sprite_v:
        xalign 0.35
        yalign 0.6
        linear 1 xpos 0.0

    scene dream_bg1 with PushMove(1.0, "pushright")

    show mc_sprite_v with dissolve:
        xalign 1.0
        yalign 0.6
        linear 1 xpos 0.0

    stop music

    stop sound

    scene black
    with fade

    jump episode2_dream_end



label episode2_dream_end:

    scene black
    with fade

    unk "...hey..."
    unk "...[mx]..."

    scene 01_priiwake_01
    with fade

    "(Who..?)"
    "(Who is..?)"

    scene 01_priiwake_02
    with fade

    mx "Hmm..mnng...?"
    p "[mx]?"
    mx "...Prii?"
    p "Are you okay?"
    mx "I'm... I'm fine."
    mx "What're you doing here?"

    scene 01_priiwake_04
    with dissolve

    p "Well, Mama asked me to get you for breakfast..."
    p "I was going to knock first but I heard you talking to yourself and grumbling..."
    p "So, I thought maybe... {p}you know?"
    mx "You know what?"
    p "Maybe you forgot everything again and was panicking where you are and I..."
    p "I was just afraid, I guess?."
    mx "Oh..."

    if notification_songs == True:
        $ renpy.notify("XNimVn - Sunny Day")

    $ renpy.music.play('music/xnimvn-sunny_day.mp3', channel='music3', loop=True)

    mx "Ahahaha!" with vpunch

    scene 01_priiwake_07
    with dissolve

    p "W-What's so funny!?"
    mx "That was pretty cute."
    p "I-I was worried! I-It's not cute at all!"
    mx "Thanks for the concern but I'm all right."

    scene 01_priiwake_02
    with dissolve

    p "Well then..."
    p "GOOD MORNING!" with vpunch
    mx "Good morning to you too."
    mx "You're quite excited this morning, huh..?"
    p "Of course! You're finally out of the hospital and..."
    mx "And?"
    p "You're now living here with us!"

    scene 01_priiwake_03
    with dissolve

    mx "Oh yeah.."
    p "I'm glad everything's okay..."
    p "Soooo... have you remembered anything yet?"

    menu:
        "Come to think of it, I remember everything now.":


            scene 01_priiwake_08
            with dissolve

            p "W-W-Wha? Really!?" with vpunch
            p "Y-you remember everything!?"
            p "T-Then the—"
            mx "Pfft!"
            p "???"
            mx "I'm sorry I was just teasing you."
            mx "I'm still clueless."
            p "H-Huh?"

            scene 01_priiwake_07
            with flash

            p "Argh!"
            p "[mx]!!" with vpunch

            scene 01_priiwake_07
            with flash

            mx "H-Hey! Hey!"
            mx "N-No punching the recovering patient!"
            p "You!"
            p "You're bad! Hmph!" with vpunch
            p "I'll just tell Mama that you won't eat breakfast!"
            mx "T-That's going too far, Prii!"
            p "Lying is bad!"

            scene 01_priiwake_06
            with dissolve

            p "I'm leaving!"
            mx "I'm sorry!"
            "(Ah. I pissed her off.)"

            $ lie_to_prii = True

            jump first_morning_cont
        "[gr]Sadly, I'm still clueless.":


            scene 01_priiwake_04
            with dissolve

            p "That's okay."
            p "Then, we'll just create new ones!"
            "(If I actually do remember this guy's memories that's something I want to see.)"

            scene 01_priiwake_03
            with dissolve

            p "Well, we have still lots of time to—"
            p "Oh, That's it!" with vpunch

            scene 01_priiwake_06
            with dissolve

            mx "Hey, what's \"it\"?"
            p "Ehehehe! That's a secret!"
            mx "Prii!"

            jump first_morning_cont

label first_morning_cont:

    scene 01_priiwake_long with dissolve:
        subpixel True
        yalign 1.0
        pause 1.0
        linear 5.0 yalign 0.0

    window hide

    pause

    p "Anyways! Get up already!"
    p "Mama's probably finished preparing by now."
    p "She cooked pancakes, you know?"
    mx "Alright! Just give me a minute, I need to dress up first."
    p "Then I'll be waiting downstairs."

    scene 02_dressup_01
    with slowfade

    mx "..."
    mx "{i}*sigh*{/i}"
    mx "A new life, huh?"
    "(A second chance of beginning anew...)"
    "(I feel so lost on where to start even.)"
    "(Those weird dreams for one...)"
    "(Then who in the world is this kid and this family...)"
    "(What ever happened to Quanto or my family's reaction...)"
    "(Yoshi and Louie...)"
    "(Even my old account and guild on Reincarnotica..)"
    mx "Argh!" with vpunch
    "..."
    mx "{i}*sigh*{/i}"
    mx "Well, first things first, let's just start getting settled into this home first."
    mx "Maybe I can investigate later on?"
    "(I should dress up first then go downstairs to join them.)"
    "(I think my clothes should be on that closet.)"

    $ intro_episode2 = True
    $ story_ongoing_fiona = True

    $ time = 1
    $ weekday = 1

    jump mc_room

label kitchen_intro:

    $ renpy.music.stop(channel='music3', fadeout=2)

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene 03_kitchenintro_long with fade:
        subpixel True
        yalign 1.0
        pause 1.0
        linear 5.0 yalign 0.0

    f "Well, well, well. Look who finally showed up?"
    mx "Um..."
    mx "Good morning, Mrs. Fitzgerald."
    f "Now, now! {p} Just call me Fiona."
    f "Mrs. Fitzgerald makes me sound like some old lady."
    f "Why don't you take a seat over there so we can start?"

    scene 03_kitchenintro_01
    with dissolve

    if notification_songs == True:
        $ renpy.notify("biosphere - let's be lazy together")

    $ renpy.music.play("music/biosphere-let's be lazy together.mp3", channel='music2', loop=True)

    $ story_music_ongoing = True

    p "Well, someone certainly took their time getting here!"
    p "Look how much Mama prepared for you!"
    mx "Yeah..."
    mx "It's quite... something."

    scene 03_kitchenintro_03
    with dissolve

    f "Well, we never had the chance yesterday to properly celebrate your release so..."
    p "She went all out today!"
    p "I wish she did this more often though..."
    f "Prii, if I did that then you'll get fat."

    scene 03_kitchenintro_02
    with dissolve

    p "But these pancakes look delicious."
    p "And besides, having a bit of fat is quite attractive nowadays!"
    f "Really..?"
    p "Yeah, I mean—"
    p "Wait!"

    scene 03_kitchenintro_04
    with dissolve

    p "What do you think, [mx]?"
    mx "M-Me!?" with vpunch
    p "Yeah!"
    p "What do you think?"
    mx "Uh... uhh..."

    menu:
        "Well, a girl with a bit of fat is attractive on her own.":


            scene 03_kitchenintro_02
            with dissolve

            p "See Mama! [mx] says so too!"
            f "Don't indulge her, [mx]. Look, she's gained a lot of weight recently."
            p "M-M-Mama! [mx], t-that's not true!" with vpunch
            f "Every time we visited you at the hospital, she'd immediately buy this pack of donuts downstairs."
            p "Because I was friends with the lady there and I don't wanna... not buy something."
            f "Why is that?"
            p "She'll feel hurt, so..."
            f "Ahahaha! {p} Oh, Prii. You're too cute." with vpunch
            p "N-No, it's not... hmph."

            scene 03_kitchenintro_03
            with dissolve

            f "I'd be happy to cook you a meal, [mx]. Not just pancakes though."
            mx "Yeah, thanks."

            jump kitchen_intro_cont
        "Living healthy is always the better option, Prii.":


            mx "Pancakes everyday would be bad for you, Prii."
            p "I-I know! B-But..."

            scene 03_kitchenintro_02
            with dissolve

            f "See? Starting tomorrow we'll be eating more vegetables..."
            p "Noo..."
            p "If he wants to eat healthy then..."
            p "I'll just eat [mx] pancakes right now!"
            mx "H-Hey!"

            scene 03_kitchenintro_01
            with dissolve

            p "Bleh! That's your fault!"
            p "You said you want to eat healthy."
            f "Now, now..."

            jump kitchen_intro_cont
        "Um... uhh... I wouldn't mind eating more of your food, Fiona.":


            scene 03_kitchenintro_03
            with dissolve

            f "Oh? That's nice to hear."
            "(Phew. I didn't need to answer that one.)"
            f "Well, I wouldn't want to cook pancakes everyday though."
            f "Knowing Prii, by the 4th day of eating pancakes, she'll be bored by it."

            scene 03_kitchenintro_02
            with dissolve

            f "Remember those muffins you wanted to eat?"
            p "Ah! Ehehehe..."
            p "B-But those are different from pancakes, you know?"
            f "Once a week would be fine."
            p "Yay!"

            jump kitchen_intro_cont


label kitchen_intro_cont:

    scene 03_kitchenintro_04
    with dissolve

    f "Well, enough chit-chat."
    f "We really should start eating while the meals are hot."
    mx "Alright."

    scene black
    with fade

    play sound "soundfx/finished_eating.ogg"

    "..."

    scene 03_kitchenintro_05
    with slowfade

    mx "Wow! Those were great."
    p "I told you. Those pancakes were to die for!"
    p "Mama, really outdid herself, huh?"
    mx "Yeah, you weren't kidding, Prii."
    f "Well, thanks for the compliment."

    play sound "soundfx/doorbell.ogg"

    window hide

    pause

    scene 03_kitchenintro_06
    with dissolve

    p "Hm? Who's that this early in the morning?"
    f "Prii, can you check up who is it?"
    p "Okay."

    scene 03_kitchenintro_07
    with dissolve

    f "So [mx]..."
    f "How are you holding up?"
    mx "Fine for the most part."
    mx "I'm still... assimilating? I guess?"
    mx "Everything still seems foreign to me."

    scene 03_kitchenintro_08
    with dissolve

    f "It's okay, dear. Priscilla and I will be here if you need anything."
    f "Consider us as your new family."
    mx "Honestly, I've never thanked you enough for letting me stay here with you two."
    f "It's the least I can do for you and your parents, dear."

    scene 03_kitchenintro_07
    with dissolve

    f "Both of them were my best friends since our university days."
    f "Especially now knowing that you have amnesia and no place to stay anywhere here in the city."
    f "It's the least I can do. I'm not that heartless to throw you out there."
    mx "Ahaha.. yeah."
    f "You can especially thank Prii on that."

    p "Miss Aanya!" with vpunch
    a "Good morning, Prii!"
    p "Wow! I love your dress!"
    a "It's quite cute isn't it? I've been waiting to try this on for some time."

    scene 03_kitchenintro_08
    with dissolve

    f "Oh, so it's Aanya?"
    f "She must be here for you or probably just to hang out and gossip."
    f "You probably should check with her, [mx]."
    f "I'll join you after cleaning up here."
    mx "Okay."

    $ kitchen_intro = True

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump kitchen

label living_room_intro:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene 03_living_intro_01
    with fade

    a "So, how's [mx] doing? \nAnything unusual since his discharge?"
    p "Same as usual... Oh! {p} He was having nightmares this morning. Does that count?"
    a "Nightmares? It's possible but highly unlikely."
    p "Oh.."
    a "Even though we're now versed on how our brains function but regarding the matters of memory and thought..."
    a "We're still in the dark."
    p "Uh... {p} ...huh."
    a "Ahahaha.. I was just speaking to myself there, Prii."

    play sound "soundfx/walking_wood.ogg"

    scene 03_living_intro_02
    with dissolve

    a "Well, speaking of the devil..."
    a "Here he comes."
    mx "The devil? Really?"

    scene 03_living_intro_03
    with dissolve

    if lie_to_prii == True:

        p "Yeah! He lied to me this morning!"
        mx "Uhh.. that was just a {i}teeny-tiny lie{/i}."
        p "Hmph! Devil."
        mx "Ugh."
        "(That was my fault.)"
        a "[mx]..."

        jump living_room_intro_cont
    else:

        p "[mx]!"
        p "Hm? Where's Mama?"
        mx "She's still cleaning up. \nShe'll join you afterwards."
        a "[mx]..."

        jump living_room_intro_cont

label living_room_intro_cont:

    scene 03_living_intro_04
    with fade

    mx "Morning Doc!"
    a "How are you, dear?"
    mx "I'm fine for the most part. \nMy memories on the otherhand..."
    a "No need to rush things. Just take your time, for now, just rest and let your body recover."

    scene 03_living_intro_10
    with dissolve

    mx "What brings you here?"
    mx "I hope you didn't go all the way out here just to check up on me?"
    a "Wha—?"

    scene 03_living_intro_07
    with dissolve

    a "Oh! \nAhahaha!"
    p "Eheeheehii!"
    mx "W-What's funny?"
    p "[mx], Miss Aanya's our neighbor. \nShe lives next door."
    mx "Oh! {p} You could've told me that Prii."

    scene 03_living_intro_06
    with dissolve

    p "Well, you didn't ask about it!"

    scene 03_living_intro_08
    with dissolve

    p "So it's your fault! \nBleh!"
    "(Well, I just lost that battle.)"

    scene 03_living_intro_05
    with dissolve

    a "Anyways, as I've nothing to do today, I thought I would check up on you and the girls over here."
    mx "Oh, you're not on duty today, Doc?"
    a "Yeah, after overseeing you for this past few months, I thought I would give myself a little vacation."
    a "I hoped me and my husband could go somewhere around the country this spring but..."
    a "...I think he's married more to his job than me."

    scene 03_living_intro_09
    with dissolve

    p "Isn't Mr. Rick a doctor like you too?"
    a "Yeah. A famous one at that."
    a "{i}*sigh*{/i}. {p} Why did I marry a doctor too."
    "(Being married to a famous doctor while being a doctor yourself must be tough, huh?)"

    scene 03_living_intro_05
    with dissolve

    a "Whatever he's doing currently is for a good cause, I guess?"
    a "So, I'm stuck now in the house finding ways to relax here and there..."
    a "But that's enough about me..."
    a "One of the reasons I came here is to check on how you're doing."
    a "Any stray memories or glimpses of your past that you're able to remember?"

    scene 03_living_intro_10
    with dissolve

    mx "Nothing really, Doc."
    a "I would've suggested you to atleast visit your old home, the one you grew up with but..."
    a "Fiona already told me that you were constantly moving from place to place growing up."

    scene 03_living_intro_09
    with dissolve

    p "Oh!"
    p "When we were kids, he often stayed here with us! Right here in this house. Does that count?"
    a "That's news to me. That could possibly help him."

    scene 03_living_intro_10
    with dissolve

    a "You could also explore around the neighborhood with Priscilla here."
    a "Locations that you have a strong emotional bond with, might trigger something inside of you."
    a "Memories can surface from unexpected places, you know?"
    mx "Oh.. uh.. okay..?"
    "(They're all doing this to help me recover my memories...)"
    "(But the truth is, how could I tell them that I didn't lose anything but rather I'm someone different entirely...)"
    "({i}*sigh*{/i}) {p} (I feel like I'm taking advantage of their kindness which I don't deserve.)"

    scene 03_living_intro_11
    with dissolve

    f "Well, well, well. {p} Looks like you are all enjoying yourselves."
    p "Mama!"
    a "You're late to the gossip, Fiona."
    f "Fashionably late and speaking of fashion..."

    scene 03_living_intro_12
    with dissolve

    f "That dress looks so \"chic\"! \nWhere did you get it from?"
    p "I know right?"
    a "Well, there's this new boutique that just opened up on..."
    "(I think it's better for me to leave right now...)"

    scene 03_living_intro_14
    with dissolve

    p "[mx]? Where're you going?"
    mx "Well, umm, I think I'm not qualified to be joining this conversation."

    scene 03_living_intro_13
    with dissolve

    a "Leaving so soon?"
    f "Ahahaha! I get it."

    scene 03_living_intro_12
    with dissolve

    f "He means that we're boring him out of our girl talk."
    mx "I-It's not that I don't like to listen..."

    scene 03_living_intro_13
    with dissolve

    f "Oh! Guilty as charged."
    mx "I just need to search for.. uh.. job openings on the Quantumnet! \nT-That's it!"

    scene 03_living_intro_14
    with dissolve

    a "Fiona, stop teasing the kid."
    f "What teasing? I was just..."

    p "Oh you already found your laptop?"
    mx "Laptop?"
    p "You know, the one I hid in your closet after getting your things from that dingy apartment."
    p "I forgot to tell you about it."
    mx "O-Oh yeah! I sure did!"
    p "Reeeeaalllyy?"
    p "Looks like your lying."
    mx "You know what? I-I'll check it again! S-So, goodbye ladies!"
    "(I should disappear already.)"

    $ renpy.music.stop(channel='music2', fadeout=2)

    if notification_songs == True:
        $ renpy.notify("XNimVn - Sunny Day")

    $ story_music_ongoing = False
    $ living_room_intro_fin = True

    jump ground_floor_hallway



label ep2_fquest_dishhelp:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    $ story_ongoing_fiona = True
    $ fquest_dishhelp_start = True

    scene 01_dishquest_01
    with fade

    $ renpy.music.stop(channel='music3', fadeout=2)

    if notification_songs == True:
        $ renpy.notify("biosphere - let's be lazy together")

    $ renpy.music.play("music/biosphere-let's be lazy together.mp3", channel='music2', fadein=1, loop=True)

    $ story_music_ongoing = True

    "(It's Fiona! Maybe I can help her around the house and not feel like a freeloader here.)"
    mx "Hey Fiona! Can I help you with that?"

    scene 01_dishquest_02
    with dissolve

    f "Oh, [mx]? It's okay, dear."
    mx "I insist. \nIt's just that..."
    mx "I'm not quite settled here yet and I'll start feeling like a burden if I just mope around."

    scene 01_dishquest_03
    with dissolve

    f "Ahahaha!" with vpunch
    mx "I-Is there any problem with that?"
    f "No, no! I just remembered something from the past."
    f "You know, when I asked you a favor you would respond with..."
    f "{i}\"My services cost a dollar an hour and 2 dollars after that...\"{/i}"
    mx "{i}*cough*{/i} {p} {i}*cough*{/i}" with vpunch
    f "If I didn't knew about your amnesia, I'd say you were planning to prank me or something."
    mx "Was I really that horrible of a person?"

    scene 01_dishquest_02
    with dissolve

    f "I wouldn't say you were {i}that{/i} bad."
    f "More of an ungrateful little twerp, I guess?"
    mx "You don't mince words, do you?"
    f "Comes with the perk of dealing with you."
    f "We've been at it since you were a kid, you know?"

    scene 01_dishquest_03
    with dissolve

    f "Now, it's just... refreshing to see you like this. I always thought you were kind inside."
    mx "Well, yeah. If I was an asshole after my memories disappeared then there's no hope for me."
    f "Ahahaha! I guess you're right."

    scene 01_dishquest_04
    with dissolve

    f "Well, if you insist in helping..."
    f "I just remembered that there were some dishes laying around the house I forgot to collect."
    f "There were around [[{color=#ff8cba}3{/color}], I guess?"
    f "Can you bring them here?"
    mx "Sure, no problem."
    "(Well, if it's just around the house then I'll start looking around where people would likely eat and drink.)"

    $ fquest_dishhelp = False

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump kitchen

label ep2_fquest_dishhelp_insufficient:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene 01_dishquest_02
    with fade

    f "Any luck finding all of them?"
    mx "No, not yet. I'm still searching for some of them."
    f "Well, come back if you find them, dear."
    mx "Yeah."

    if fquest_dishhelp_dishes == 0:
        "(I need to find atleast one of those dishes first.)"

    if fquest_dishhelp_dishes == 1:
        "(I found one. 2 more to go.)"

    if fquest_dishhelp_dishes == 2:
        "(I found two. Finally, one more to go.)"

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump kitchen

label ep2_fquest_dishhelp_cont:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene 01_dishquest_05
    with fade

    mx "Fiona, here's all of them."
    f "Well, aren't you fast?"
    f "Now go grab that dishrag and help me clean them up."
    f "Unless you're starting to regret offering your help?"
    mx "W-What? N-No! That help has no expiration date."

    scene 01_dishquest_03
    with dissolve

    f "If that's the case, then you'll be helping me for the rest of your life."
    mx "Ah!"
    f "Hahaha! I'm just teasing you." with vpunch
    f "You don't often see the {i}\"great badass\"{/i} [mx] being so helpful and humble."
    mx "You know, I don't remember too much about this guy—I mean, myself but if I was that of a \"badass\" then..."
    mx "It seems there might be people out there waiting to get their revenge on my ass, so to speak."

    scene 01_dishquest_04
    with dissolve

    f "To tell you the truth, they already knew you were hiding here and are just waiting for an opportunity to strike."
    mx "WHAT!?" with vpunch
    f "..."
    mx "..."
    mx "Fiona..."

    scene 01_dishquest_02
    with dissolve

    f "Pfft! Ahahaha!" with vpunch
    f "I'm sorry! I can't help it, teasing you is too much fun."
    mx "Ugh..."
    f "I'm one of the people waiting for their revenge on you, you know?"
    f "To be honest, I won't worry too much about that."

    scene 01_dishquest_03
    with dissolve

    f "It's true, you were an asshole that gets himself in trouble here and there but its certainly nothing serious like that."
    f "You often preferred to be alone most of the time and play that Reincarnotica game kids these days play."
    mx "I see..."
    "(Atleast I won't worry anymore that there's some psycho out there waiting to stab me in the back.)"
    "(Nevertheless, staying vigilant will be safer.)"

    scene 01_dishquest_01
    with dissolve

    f "Now, enough teasing around, let's get this cleaning started."
    mx "You know, you're the only one teasing here, right?"
    f "Not enough cleaning, [mx]! \nYou still have 99 years of help to do!"
    mx "{i}*exasparated sigh*{/i}"

    $ renpy.music.stop(channel='music2', fadeout=1)

    scene black
    with fade

    play sound "soundfx/dishes_01.ogg" fadeout 1

    "..."

    play sound "soundfx/dishes_03.ogg" fadeout 1

    "..."

    scene 01_dishquest_01
    with fade

    f "...[mx], here's the other—"
    mx "Hm? Oh shi—!"

    scene 01_dishquest_06
    with vpunch

    f "Be care—"
    f "[mx]!!"

    scene black with vpunch

    play sound "soundfx/falling_thud.ogg"

    pause

    scene 01_dishquest_07_blur
    with dissolve

    mx "Owww..."
    f "Are you okay?"
    mx "I'm..I'm alright."
    mx "The plate's safe."
    f "The plate— \nSeriously! Why were you spacing out?"

    if notification_songs == True:
        $ renpy.notify("biosphere - let's be lazy together")

    $ renpy.music.play("music/biosphere-let's be lazy together.mp3", channel='music2', fadein=1, loop=True)

    scene 01_dishquest_07
    with dissolve

    f "You should be more careful, you know?"
    f "And pay more attention. Jeez."
    "(Whoa..)"
    "(Big.) {p} (Very big.)"
    f "I don't want to admit you again to the hospital so soon after getting out."
    "(Wait. Does she not realize her breasts are out?)"
    mx "Umm... Fiona."
    f "What?"
    mx "Look down..."

    scene 01_dishquest_08
    with dissolve

    f "What do you mean dow—"
    f "Oh my God!" with vpunch
    f "Don't look!" with vpunch

    scene black
    with fade

    pause

    scene 01_dishquest_09
    with fade

    f "..."
    mx "Are you okay?"
    f "I'm fine. \nI should be the one asking you that as you were the one who fell."
    f "All I did was flash you with this old lady's ugly tits."
    mx "Ugly?"
    mx "They were beautiful, to be honest."
    f "W-Wha..?"

    scene 01_dishquest_10
    with dissolve

    mx "Oh shit! N-No, I mean..." with vpunch
    mx "They were the opposite of ugly, like, uh, very great to look at!"
    f "A-Ah.. U-Umm..."
    mx "N-N-No! \nW-what I meant your womanly parts are, uh-Shit!"

    scene 01_dishquest_09
    with dissolve

    f "Are shit?"
    mx "N-N-N-Nooo! Nope! Nuh-uh!" with vpunch

    scene 01_dishquest_10
    with dissolve

    f "Aha..pft.. \nAhahaha!"
    mx "You were teasing me again, aren't you?"

    scene 01_dishquest_11
    with dissolve

    f "I already understood what you meant the first time but you were so flustered, it was funny."
    f "Well, it looks like were done with the chores today."
    f "This was quite an eventful dish washing, huh?"
    mx "Yeah..."
    f "Anyways, thanks for the help. \nThen I'll be relying on you from now on."
    mx "Sure thing."

    scene black
    with fade

    $ renpy.music.stop(channel='music2', fadeout=2)

    "(Damn. That was such an amazing... view.)"
    "(Well, it's getting late.)"

    scene kitchen_evening
    with slowfade

    if notification_songs == True:
        $ renpy.notify("BROCKBEATS - september")

    $ story_music_ongoing = False

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    $ time += 1
    $ fquest_dishhelp_complete = True
    $ fquest_dishhelp_start = False
    $ story_ongoing_fiona = False

    jump kitchen



label ep2_fquest_missingpackage:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene ground_floor_morning

    f "What do you mean by that!?" with vpunch
    "(Was that Fiona?)"
    "(Who's she arguing with this early in the morning?)"
    "(The sound's coming from the living room.)"

    $ fquest_missingpackage = False
    $ fquest_missingpackage_start = True

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump ground_floor_hallway

label ep2_fquest_missingpackage_start:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene 02_missingpackage_01
    with fade

    f "Catriona! Where's the package!?" with vpunch
    f "Didn't I ask you to pick it up from Giuliani's tailor and deliver it to me today?"
    f "I called him awhile ago and he said you came and picked it up!"
    "... {w} ... {w} ..."

    scene 02_missingpackage_02
    with dissolve

    f "What do you mean by {i}\"Maybe you dropped it off here\"{/i}?"
    f "I wouldn't be calling you if I have it, would I?"
    "... {w} ... {w} ..."

    scene 02_missingpackage_04
    with dissolve

    f "Of course, its important! \nThose were for my clients's orders!" with vpunch
    f "They contain high quality fabrics and leathers straight from Italy!"
    f "So exclusive in fact that you needed to wait months before you can even put an order."
    f "Not the delivery. Just an order!" with vpunch
    f "And I waited 6-months for a slot to open up for that order."

    scene 02_missingpackage_02
    with dissolve

    "... {w} ..."
    f "Now you're not sure if you even brought it here!?" with vpunch
    f "Make up your mind, woman!" with vpunch
    "..."

    scene 02_missingpackage_03
    with dissolve

    f "Just because you lost a bottle of wine you immediately left? You can buy one at—"
    "... {w} ..."
    f "Oh."
    f "Isn't that a very expensive one? \nA 50 year old vintage, huh?"
    "..."
    f "Dammit, Cath! \nWhy did you pick the same day to get that and my package?"
    f "There's no such horoscope that says... \n{i}\"Sisterly instincts to get their luxury goods today\"{/i}"
    "..."
    f "I... You!!!"
    f "{i}*sigh*{/i}"
    f "Just... {p} Just call me if you find it?"
    f "Go take a look at Giuliani's shop or wherever you bought your wine."
    f "I swear to God, Catriona!"
    "..."
    f "Bye..."
    "..."
    f "Love you too, sis."

    scene 02_missingpackage_05
    with dissolve

    mx "Tough day?"
    f "Hmm?"

    scene 02_missingpackage_06
    with dissolve

    f "You heard that, huh?"
    mx "Yeah. It's not that hard to ignore with the shouting and all."
    f "{i}*chuckle*{/i}"
    f "Sorry about that. \nIt's just that the package I was expecting is misplaced or worse, lost by Catriona."
    mx "Catriona?"

    scene 02_missingpackage_07
    with dissolve

    f "Oh, I forgot you don't remember her. My older sister."
    f "She lives in the South but she comes here once in a while to visit but today she's here for a liquor order."
    mx "Liquor order?"
    f "Yeah. My family runs a bar there and as she's the eldest, she's the one running it now."

    scene 02_missingpackage_08
    with dissolve

    f "And it's also quite ironic because my father was a pastor."
    mx "How does that even work?"
    f "Well, I asked him that once and he said..."
    f "{i}\"Listen here pumpkin, you see, wine symbolizes the blood of Our Lord, and wine is alcohol, therefore all alcohol is his blood and we must spread it to the people.\"{/i} or something like that."

    scene 02_missingpackage_07
    with dissolve

    f "He was dead ass drunk too when he told me that."
    mx "Quite a family you have there."
    f "I know right? I'm surprised I turned out quite different."
    mx "Really?"

    scene 02_missingpackage_08
    with dissolve

    f "Hmmmmm? {p} Are you insinuating something, [mx]?"
    mx "N-No! Nothing! Nope!"
    f "Hmm..."
    f "Anyways! If we are to believe that Cath did indeed dropped the package here then it must be around somewhere."
    mx "What does it look like?"
    f "Well, Giuliani said he put them inside a cardboard box."
    mx "So, just a box, huh? \nI'll try looking around the house."
    f "Thanks, [mx]."
    "(Now then, where would someone put a box here.)"

    scene black
    with fade

    pause 0.3

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    $ fquest_missingpackage_start = False
    $ fquest_missingpackage_search = True
    $ story_ongoing_fiona = True

    jump ground_floor_hallway

label ep2_fquest_missingpackage_insufficient:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene 02_missingpackage_06
    with fade

    f "Oh. Have you found it?"
    mx "No, not yet."
    f "It's a carboard box, dear."
    "(It must be around here somewhere.)"

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump ground_floor_hallway

label ep2_fquest_missingpackage_cont:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene 02_missingpackage_09
    with fade

    mx "Hey Fiona, is this it?"
    f "Let me see."
    f "..!"
    f "It is! \nThis is Giuliani's logo printed here!"

    scene 02_missingpackage_10
    with dissolve

    f "Where did you find it?"
    mx "In the patio."
    f "Patio? How did it get there?"
    f "Anyways, case closed. Thank you for the help, dear."
    mx "Yeah. No problem."
    mx "Then I better get going."
    f "Thanks for the help again."

    play sound "soundfx/walking_wood.ogg"

    scene black
    with fade

    pause

    scene 02_missingpackage_11
    with fade

    f "Where to put this..."
    "...*tok*..." with vpunch
    f "Huh? Something's rolling inside?"
    f "Let me check..."

    scene 02_missingpackage_12
    with fade

    f "Well, well. What do we have here?"
    f "A {i}\"Verde Emiglia\"{/i}? \nIsn't this what Cath was talking about that she lost?"
    f "Wait a minute... {p}It's already opened and used!"
    f "Don't tell me that woman was drinking when she took my package."
    f "Catriona..."
    f "Well, as punishment for her, I'll have this wine for myself."
    f "{i}*giggle*{/i}"
    f "I'll probably taste a bit or two on the Weekend evenings."

    scene black
    with fade

    pause 0.2

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    $ story_ongoing_fiona = False
    $ fquest_missingpackage_search = False
    $ fquest_missingpackage_complete = True
    $ time += 1

    jump living_room



label ep2_fquest_nightdrinking:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene 03_nightdrink_02
    with fade

    mx "Fiona?"

    scene 03_nightdrink_01
    with dissolve

    f "[mx]? \nStaying up late, huh?"
    f "I'm just having a re-{i}*hic!*{/i} {p}...relaxing evening all by myself." with vpunch
    "(She's already tipsy...)"
    f "Care to join me?"

    menu:
        "Sure.":


            f "Ehehe!"
            f "As daddy once said \n{i}\"A drink is to be enjoyed with good company!\"{/i}—{i}*hic!*{/i}"

            $ renpy.music.stop(channel='music3', fadeout=3)

            jump ep2_fquest_nightdrinking_cont
        "I'll pass.":


            f "Well, suit yourself!"
            f "More for me then."

            show screen calendar_time
            show screen calendar_week
            show screen inventory_button

            jump patio

label ep2_fquest_nightdrinking_cont:


    if notification_songs == True:
        $ renpy.notify("BROCKBEATS - dream")

    $ renpy.music.play("music/BROCKBEATS-dream.mp3", channel='music2', fadein=3, loop=True)

    scene 03_nightdrink_05
    with dissolve

    f "Cath sure does know her alcohol."
    mx "Oh, is that her missing wine?"
    f "Yeah, she must've accidentally mixed it with the fabrics when Giuliani was packing it up."
    f "That woman becomes such a clutz when drunk."
    mx "Really?"
    f "Yeah..."

    scene 03_nightdrink_04
    with dissolve

    f "When I found this bottle, it was already opened and almost half of it was gone."
    f "I suspect that not even a minute passed after getting this that she chugged it all the way through Giuliani's."
    mx "That's just... reckless."
    f "Yeah. She was always the impatient one in our family."

    scene 03_nightdrink_03
    with dissolve

    f "Heck, she even got your parents in trouble by forcing them to fake their age so she could bypass the buying limit for some artsy craft beer."
    mx "Sheesh. \nMust be tough having an older sister like that?"
    f "You bet. Al would always tease me that I was practically the older sister disciplining her younger sister."
    f "{i}*chuckle*{/i}"
    mx "Al?"

    scene 03_nightdrink_05
    with dissolve

    f "Alphonse. {p} Your dad."
    f "You inherited a lot from him especially his...arrogance. \nWell, that and..."
    f "({i}...his looks too.{/i})"
    mx "Hm?"

    scene 03_nightdrink_04
    with dissolve

    f "{i}*hic!*{/i}"
    f "N-Nothing. I'm just rambling..."
    mx "Oh, okay."
    f "It must be quite heartbreaking to not remember them, huh?"
    mx "Well, to be honest..."
    mx "Not really."
    "(Well, if I was really an amnesiac, it must be truly heartbreaking to not know anyone after waking up.)"
    "(It's a different case for me however, it feels like playing a role in a movie.)"

    scene 03_nightdrink_05
    with dissolve

    mx "I mean, I forgot everything about them including any emotional attachment, you know?"
    mx "They're no different from strangers to me. It still makes you wonder though?"
    mx "That said, you must be very close to them to even treat me like family? I was wondering how you met them?"

    scene 03_nightdrink_04
    with dissolve

    f "Well.."
    f "Your mother was my roommate and my very first friend here."
    f "I was all alone after coming here from the South to attend college."
    f "I still had a heavy accent which made me so embarassed that I rarely spoke during my first semester."

    scene 03_nightdrink_03
    with dissolve

    f "Me and your dad, however, go way back to middle school."
    mx "Wait, really?"
    f "Yeah. We were classmates 'til the first year of highschool whereafter he just suddenly left out of nowhere."
    f "I later learned was because of his parent's, your grandparent's, divorce."
    f "Imagine my surprise when I saw him taking the same course as me. He was still annoying as ever."
    f "{i}*giggle*{/i}"
    mx "That's an incredible coincidence. So you must be the one who introduced my mother and him?"

    scene 03_nightdrink_04
    with dissolve

    f "Introduced..?"
    f "..."
    f "......yeah."
    "(What's with the long pause?)"
    f "I think it was around this time when we talked about \"that\"..."
    mx "\"That\"?"
    f "Just a stupid promise."
    f "Anyways, it was also that time your dad and mom first met each other."
    f "You see, your dad invited me to a party at his house and—"

    $ renpy.music.stop(channel='music2', fadeout=1)

    "(T-This feeling..!)"

    play sound "soundfx/glitch.ogg" loop

    show night_glitch with vpunch

    pause

    "(Shit!)"
    "(A glitch again!?)"

    pause

    "(Urgh!)"
    "(W-What's happ... enn.. ing....)"

    stop sound

    hide all

    scene black
    with fade

    "..."
    "(This feeling...shit.)"
    "(This.. This isn't the dreamworld or whatever that is...)"
    "(It's like that time. Inside their minds...)"
    "(Wait! N-No..)"
    "(Fiona?)"

    play sound "soundfx/knock_door.ogg"

    "{i}*knock*{/i} \n{i}*knock{/i}*"
    unk "Maria? I need a favor."

    scene 03_nightpast_01
    with fade

    f "Can you come with me to Al's party tonight?"
    f "Pretty please!"
    ma "Well, according to my schedule here, I have an appointment today for..."
    ma "...{i}\"Laze around my bed and have the best time of my life.\"{/i}."
    ma "Sooooo, I have to decline that favor but have a great time there!"

    scene 03_nightpast_02
    with dissolve

    f "PRETTY PRETTY PLEASE!" with vpunch
    ma "No, thank you! Have a—"

    scene 03_nightpast_03
    with dissolve

    f "I'm gonna start telling everybody that you like those gay Japanes—"
    ma "Okay! Okay! {p} Sheeesh woman!" with vpunch
    ma "You know I'm not a fan of huge parties like that."

    scene 03_nightpast_02
    with dissolve

    f "It's just that I'm embarassed to go by myself there."
    f "And it's mah first time to be invited in one of 'em huge parties dat 'em city girls keep talkin' 'bout—"
    ma "You're accent's leaking again."

    scene 03_nightpast_03
    with dissolve

    f "O-Oh! {p} That's why I need you Maria!"
    f "Come on! Maybe you'll find someone there!"
    ma "Ugh... I'd rather be single forever."
    f "You're too gloomy!"
    ma "Fine! I'll go with you but I'm not interacting with anyone there."
    f "Thank you!"

    scene black with fade

    "(That was... Fiona's memories?)"

    f_m "(If I just didn't invited her...)"

    "(And her thoughts too.) {p} (I can hear them.)"

    f_m "(Then...) {p} (Then he...)"
    f_m "(He could've kept his promise...)"
    "(Who's promise?)"

    $ renpy.music.play('soundfx/night_ambiance.ogg', channel='music1', loop=True, fadein=1)

    scene 03_nightpast_04 with slowfade

    f "{i}*sigh*{/i}"
    f "I thought going with Maria would help me fit in with 'em city folks but..."
    f "Why did dat girl ran away as soon as those fellas tried to flirt with her."

    scene 03_nightpast_05
    with dissolve

    f "If she just didn't run then... {p} I wouldn't ran away too."
    f "Now, why is this house pretty darn big? \nThey even 'ave them garden mazes..."
    f "More importantly..."
    f "Where in tarnation is that Alphonse anyway!?" with vpunch
    f "Inviting me ovah here then disappearing."

    scene 03_nightpast_06
    with dissolve

    f "{i}*sigh*{/i}"
    f "I've been here for a while now maybe I should just find Maria and go back—"

    play sound "soundfx/walking_wood.ogg"

    unk "Hey there pretty lady."
    f "Hm!?!"
    unk "Why is such a beautiful one such as yourself so lonesome in this beautiful evening."

    scene 03_nightpast_07
    with dissolve

    f "Uh.. uh... m-m-mah boyfriend.. he... {p} ...he went to the restroom s-so..."
    f "I-I'm not single, alright!" with vpunch
    unk "....Pfft!"
    unk "Ahahaha! {p} I'd like to see the face of that desperate guy that scored with someone like you."
    f "Wha!?!" with vpunch

    $ renpy.music.stop(channel='music1', fadeout=2)

    scene 03_nightpast_08
    with vpunch

    if notification_songs == True:
        $ renpy.notify("BROCKBEATS - magic spell")

    $ renpy.music.play("music/BROCKBEATS-magic spell.mp3", channel='music2', fadein=2, loop=True)

    f "Y-You!!"
    f "Gosh darnit, Alphonse!"
    f "Don't sneak up on me like that! You asshole!"
    al "Well, I didn't know little missy here had a date tonight?"
    f "I don't! I was just... t-that was an excuse, okay!?"
    f "Also, why are you here?! \nI was lookin' for ya!"
    al "This is where I live."
    f "You reckon' know what I mean!"
    al "Ahahaha!"

    scene 03_nightpast_09
    with dissolve

    al "I was looking for you too, duh?"
    al "I was asking others if they saw someone that would qualify for a Miss Librarian contest."
    f "Har! Har!"
    f "Why is this house so big anyways..."
    al "It's owned by my Mom's boyfriend..."
    al "Pretty cool dude, allowed me to use this while they're in the Caribbean."
    al "Why are you all alone up here anyways? You know the party's downstairs, right?"
    al "I invited you to help you meet new people from the university."
    f "I... I know but..."
    f "This is my first time going to a party and I felt... scared."
    f "Maybe they'll tease my accent or make fun of me."
    al "Psh! That's stupid. \nI tease you always and you ain't scared of me."

    scene 03_nightpast_08
    with vpunch

    f "Because you're an asshole!"
    al "H-Hey! No punching!"
    al "Hahaha! I'm just kidding!"
    f "Grr!"

    scene 03_nightpast_09
    with dissolve

    f "{i}*sigh*{/i}"
    al "Just be yourself. \nJust be that geeky, Texan chick who has a weird fascination with ling—"
    f "Y-You! T-That's a secret, stupid!"
    al "Atleast you're smiling now."

    scene 03_nightpast_10
    with dissolve

    al "Who cares what other people think? \nReal friends accepts who you are and you're looking for one, right?"
    al "If you take other's opinion too seriously you'll never get a boyfriend."
    f "W-W-Wha? I-I can get one!"
    al "Really? You?"

    scene 03_nightpast_08
    with dissolve

    f "W-What about you, huh!?"
    al "What about me?"
    f "You're too wild, arrogant, and... a-a-a manslut!"
    al "M-Manslut? \nWhere did that come from?"

    scene 03_nightpast_09
    with dissolve

    f "Maria said those are guys dat invite nice gals to their homes and then ditch them to tha curb afterwards!"
    f "L-Like what ya did!"
    al "What!? I... {p} Ahahaha!" with vpunch
    al "I think she forgot A LOT of explanation on that one."
    f "Hmph.."
    al "I'm single because of my circumstance. \nMy Mom's always moving with her boyfriends, you know?"
    al "And long distance relationships are just begging for breakups."
    al "And more importantly... \nI just haven't met \"{i}The one{/i}\", I guess?"
    f "The one, huh..?"
    f "..."
    al "Fiona, you seem out of it?"

    scene 03_nightpast_05
    with dissolve

    f "N-No. \nI'm... I'm just wonderin' if a boy could, you know, like-{i}like{/i} me like that?"
    f "I was nevah one for relationships, ya'know?"
    al "Of course they will. {p} Well, because I'm also one of them that likes you."
    f "!!!" with vpunch

    scene 03_nightpast_09
    with dissolve

    f "T-T-T-That's goin' too far for teasin' me, Al!" with vpunch
    al "I'm not! Believe it or not..."
    al "You're funny, smart, and, well, just amazing in general."
    al "A really great gal to be around with, really."
    f "Al..."
    al "..."
    al "Hey, how about a promise?"

    scene 03_nightpast_10
    with dissolve

    f "A promise?"
    al "That if we're still both single on graduation and maybe, even after that..."
    al "That we'll date each.. No! {p} I'll marry you."

    scene 03_nightpast_08
    with dissolve

    f "W-W-WHAT!?! THAT'S WAY TOO FAST!" with vpunch
    al "Yeah, that might be too soon. Hmm... {p} How about my fiancee then?"
    f "N-NO! I-I-I MEAN, WHY ME!?!"
    al "Because I like you?"
    f "DANGNABBIT ALPHONSE!! I-IF YOU'RE JUST PLAYING WITH ME I'LL—"
    al "So, it's a yes then?"

    scene 03_nightpast_09
    with dissolve

    f "I-I'm just agreeing to that... b-b-because..."
    f "I-It's just so I can kick your ass on graduation if you're lying to me..."

    scene 03_nightpast_10
    with dissolve
    al "Sure you do."
    al "But in all honesty, I just don't want you to end up on the hands of some scummy guy."
    f "And you aren't?"
    al "Oof! You got me there."
    al "Give me your hand..."

    scene 03_nightpast_11
    with dissolve

    al "To the stars above and to the universe beyond..."
    al "I, Alphonse, promise to marry Fiona, if were both still single by the time we graduate!"
    f "That's too cheesy—"
    al "I saw it in some movie once—"
    f "Look! {p} A shooting star!" with hpunch
    al "Oh yeah! It's quite something!"
    al "Which means that this promise has been approved by the universe!"
    f "W-Wha! N-No, it isn't.."
    al "Uh-huh! You know the saying, when you wish upon a shooting star, you dreams or maybe, promises, come true!"
    al "If you fail to uphold it, the universe will punish you. \nOr so they say."
    f "Ugh.."

    scene 03_nightpast_12
    with dissolve

    al "Ahahaha! No regrets now."
    al "Let's go back to the others."
    f "Hmm..."
    f "..."
    f "({i}...married with him, huh?{/i})"
    f "({i}That isn't so bad...{/i})"

    scene black
    with slowfade

    pause

    $ renpy.music.stop(channel='music2', fadeout=3)

    f_m "(If I just...)"
    f_m "(If I just never asked her to come with me...)"
    f_m "(If I just told him my true feelings...)"
    f_m "(If I just did something...)"
    f_m "(Maybe my life would be...)"

    "(Fiona...)"

    scene 03_nightpast_13
    with slowfade

    f "If Oliver just didn't got himself in trouble with the professor..."
    f "Well, I hope I'm not too late for the rehearsal."
    f "I just hope those two aren't fighting again."

    scene black
    with fade

    f_m "(I didn't noticed that ever since the party...)"
    f_m "(The two were already..)"

    scene 03_nightpast_14
    with dissolve

    ma "Ehehee! Stop it!"
    al "What? You don't want your boyfriend to kiss you?"
    ma "But what if the others see us?"
    al "Well, it's your fault for falling in love with me."
    ma "Excuse me? Aren't we quite presumptous? You're the one who fell heads over heels on me?"
    al "Hahaha! I won't deny that."
    ma "Ugh. \nJ-Just one kiss, okay?"
    al "Hahaha... Yeah, just \"one\"."
    ma "A french kiss is still a kiss, you jerk."

    show night_glitch

    play sound "soundfx/glitch.ogg" fadein 1 loop

    ma "Ehehehe..."
    "xc3xc1sn..Oh..dsd.."
    "zck..F..Fiona.. you...hx!$adssa"
    "7fD..saw it..!?...$.#"

    scene black
    with fade

    hide night_glitch with dissolve

    stop sound

    "(Dammit! My head...)"
    "(But anyways, \"my father\" is Fiona's first love.)"
    "(This guy's parents and Fiona are...)"
    "(Quite complicated.)"

    $ renpy.music.play("music/BROCKBEATS-dream.mp3", channel='music2', fadein=3, loop=True)

    scene 03_nightdrink_06
    with slowfade

    if notification_songs == True:
        $ renpy.notify("BROCKBEATS - dream")

    "(I'm... back.)"
    "(Fiona on the otherhand...)"
    f "...that's the story of that."
    f "As if it only happened yesterday. \n It's weird how I can remember it so clearly."
    "(It's like nothing happened, huh?)"
    mx "Uh... what was the promise again? {p} I-I just spaced out on that part!"
    f "You really need to get your attention checked by Aanya, [mx]. Hehe.."
    mx "Y-Yeah..."
    f "It's just a promise that {i}\"The four of us will graduate together\"{/i}. {p} And we did."
    f "Despite Maria getting pregnant..."

    scene 03_nightdrink_07

    f "{i}*glug*{/i} {p} {i}*glug*{/i}" with vpunch
    "(This woman...)"

    scene 03_nightdrink_08
    with vpunch

    f "Phew!"
    f "{i}*hic!*{/i}"
    f "Dammit!" with vpunch
    f "({i}Wasn't I \"The One\", Al...{/i})"
    f "({i}You promised me...{/i})"
    mx "Fiona?"

    scene 03_nightdrink_09
    with dissolve

    f "I-I'm sorry..."
    f "I'm just drunk right now. I need to go..."
    mx "Okay. Just watch your step—"
    mx "Careful!"

    scene 03_nightdrink_11
    with vpunch

    f "Oh..."
    f "A-Alphonse..."
    mx "Fiona, I said to watch your step."
    mx "Your wobbling..."

    scene 03_nightdrink_10
    with dissolve

    f "Oh, [mx]..."
    f "I... {i}*hic!*{/i}" with vpunch
    f "I thought for a moment you..."

    scene 03_nightdrink_11
    with dissolve

    f "{i}*sigh*{/i}"
    f "I can take care of myself now, dear."
    mx "Are you sure?"
    f "Y-Yeah."
    mx "Alright."
    f "Good night, dear."

    scene patio_evening
    with fade

    $ renpy.music.stop(channel='music2', fadeout=3)

    "..."
    "..."
    mx "It's quite a beautiful night."
    mx "{i}*yawn!*{/i}"
    mx "I better go to bed."

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    $ time += 1

    $ fquest_nightdrinking_complete = True
    $ fquest_nightdrinking = False

    jump patio


label ep2_fquest_gardenhelp:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    $ renpy.music.stop(channel='music3', fadeout=2)

    $ story_music_ongoing = True

    if notification_songs == True:
        $ renpy.notify("BROCKBEATS - frills & flowers")

    $ renpy.music.play("music/BROCKBEATS-frills & flowers.mp3", channel='music2', fadein=3, loop=True)

    $ map_time_skip = False

    scene 01_gardenquest_01
    with fade

    mx "Hey Fiona!"
    mx "Doing some gardening work?"
    f "Hmm?"

    scene 01_gardenquest_02
    with dissolve

    f "Oh [mx]!"
    f "Yeah. \nIt's been a while since I did a little bit of cleaning around here."
    f "You know, between work, visiting you at the hospital, and whatnot?"
    f "So, the weeds have started spreading here and there."
    mx "You need any help there?"

    scene 01_gardenquest_03
    with dissolve

    f "In fact..."
    f "I really do."

    scene 01_gardenquest_05
    with dissolve

    f "I was planning to do a little bit of landscaping after I finish removing the weeds here but..."
    f "It seems my [[ {color=#00cd67}Garden Trowel{/color} ] and my [[ {color=#6495ed}Watering Can{/color} ] is gone."
    f "I suspect Prii still has them."
    f "I saw her yesterday fixing up her little garden upstairs."

    scene 01_gardenquest_04
    with dissolve

    f "Could you kindly get it, dear?"
    mx "Sure, no problem."
    f "Thank you. Check up on her in her room."
    mx "Got it! I'll be back."
    "(A [[ {color=#00cd67}Garden Trowel{/color} ] and a [[ {color=#6495ed}Watering Can{/color} ])"

    $ fquest_gardenhelp_start = True
    $ fquest_gardenhelp_ongoing = True

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump patio

label ep2_fquest_gardenhelp_items:

    if garden_trowel in inventory.items and watering_can in inventory.items:

        jump ep2_fquest_gardenquest_found
    else:


        hide screen calendar_time
        hide screen calendar_week
        hide screen inventory_button

        scene 01_gardenquest_02
        with fade

        f "[mx]! Have you found both of the tools, dear?"
        mx "I'm still looking for them."
        f "I can't get started clearing and watering if I don't have them."
        f "Try asking Priscilla. I think I remember seeing her using them yesterday."
        f "It's a [[ {color=#00cd67}Garden Trowel{/color} ] and a [[ {color=#6495ed}Watering Can{/color} ]."
        mx "I'm on it."

        show screen calendar_time
        show screen calendar_week
        show screen inventory_button

        jump patio

label ep2_fquest_gardenask_prii:

    if fquest_gardenhelp_prii == False:

        hide screen calendar_time
        hide screen calendar_week
        hide screen inventory_button

        scene 02_priiask_01
        with fade

        mx "Hey Prii!"
        p "[mx]!"
        p "What's up?"
        mx "Well, Fiona asked me to help her get her missing tools."
        mx "She told me that you've borrowed them yesterday?"

        scene 02_priiask_04
        with dissolve

        p "Uhh-I mean, w-what tools did she ask for?"
        "(Hm?)"
        "(Why did she started getting nervous?)"
        mx "A [[ {color=#00cd67}Garden Trowel{/color} ] and a [[ {color=#6495ed}Watering Can{/color} ]."

        scene 02_priiask_02
        with dissolve

        p "I-I see..."
        p "I-I don't seem to remember anything like that..."
        mx "Are you sure?"
        mx "Hmmm?"

        window hide

        pause

        p "..."
        p "Okay, okay! \nI-It's just that I..." with vpunch
        mx "Yeah?"
        p "Lost them."
        mx "What?"

        scene 02_priiask_04
        with dissolve

        p "Not exactly lost per se but..."
        p "W-Well, after using the trowel, I went downstairs to wash it and left it there to dry afterwards."
        p "And when I came back here to return the watering can..."
        p "It was gone."
        mx "What do you mean \"gone\"?"

        scene 02_priiask_02
        with dissolve

        p "T-That is... I'm very sure I've left it on the flower table before I washed the trowel but when I came back it wasn't there anymore!"
        p "I thought that it might've fallen down at the patio and I went looking for it there."
        p "I spent hours combing every nook and cranny but I've no luck finding it."
        "(Well, this just got a lot harder.)"
        "(I was just asked to get the tools but now...)"
        mx "Was the [[ {color=#6495ed}Watering Can{/color} ] empty or full when you left it?"

        scene 02_priiask_03
        with dissolve

        p "I've used it all up so it was empty. Why?"
        "(So that's the case, it could've been easily blown by a strong wind.)"
        "(If not in the patio downstairs then where exactly did it fell?)"
        mx "Just a guess where it went. As for the [[ {color=#00cd67}Garden Trowel{/color} ], do you remember where you left it to dry?"
        p "Somewhere downstairs on a table. I was focused on finding the watering can that I forgot where..."
        "(It must be near where she washed it.)"

        scene 02_priiask_02
        with dissolve

        p "I'm sorry. If wasn't just a clutz..."
        mx "Hey now! It's nothing to beat yourself up over for. I'll try looking for them alright?"
        mx "So cheer up, okay?"

        window hide

        scene 02_priiask_05
        with dissolve

        pause 1

        p "Uh huh!"
        mx "Well then, I'm off."
        p "Hey [mx]... please don't tell Mama I've lost them."
        mx "It didn't even crossed my mind to be honest."

        scene 02_priiask_01
        with dissolve

        p "Thank you."
        p "Goodluck on your search."

        $ fquest_gardenhelp_prii = True
        $ fquest_gardentools_search = True
        $ fquest_gardentools_askaanya = True
        $ aanya_home_unlocked = True

        show screen calendar_time
        show screen calendar_week
        show screen inventory_button

        jump priscilla_room
    else:


        if garden_trowel in inventory.items and not watering_can in inventory.items:

            hide screen calendar_time
            hide screen calendar_week
            hide screen inventory_button

            scene 02_priiask_01
            with fade

            p "[mx]!"

            scene 02_priiask_03
            with dissolve

            p "H-Have you finally found Mama's [[ {color=#6495ed}Watering Can{/color} ] and the [[ {color=#00cd67}Garden Trowel{/color} ]?"
            mx "I've found the [[ {color=#00cd67}Garden Trowel{/color} ] in the bathroom downstairs but as for the [[ {color=#6495ed}Watering Can{/color} ], not yet."

            scene 02_priiask_04
            with dissolve

            p "Oh yeah, I remember now."
            p "Well, one down and one more to go?"
            mx "Remind me again where you've left the [[ {color=#6495ed}Watering Can{/color} ]?"

            scene 02_priiask_02
            with dissolve

            p "I clearly remember leaving the [[ {color=#6495ed}Watering Can{/color} ] at the terrace when I left to clean the trowel."
            p "It was gone when I came back."
            p "I've already checked if it fell on the patio but no luck."

            scene 02_priiask_03
            with dissolve

            mx "I see."
            mx "I'll try searching for it again."
            "(Hypothetically, if it fell and did not land on the patio downstairs then where?)"

            show screen calendar_time
            show screen calendar_week
            show screen inventory_button

            jump priscilla_room

        elif watering_can in inventory.items and not garden_trowel in inventory.items:

            hide screen calendar_time
            hide screen calendar_week
            hide screen inventory_button

            scene 02_priiask_01
            with fade

            p "[mx]!"

            scene 02_priiask_03
            with dissolve

            p "H-Have you finally found Mama's [[ {color=#6495ed}Watering Can{/color} ] and the [[ {color=#00cd67}Garden Trowel{/color} ]?"
            mx "I've found the [[ {color=#6495ed}Watering Can{/color} ] in Dr. Aanya's patio but as for the [[ {color=#00cd67}Garden Trowel{/color} ], not yet."

            scene 02_priiask_04
            with dissolve

            p "Oh! That's why I can't find it!"
            p "Well, one down and one more to go?"
            mx "Remind me again where you've left the [[ {color=#00cd67}Garden Trowel{/color} ]?"

            scene 02_priiask_02
            with dissolve

            p "I'm sure I left the [[ {color=#00cd67}Garden Trowel{/color} ] somewhere downstairs for it to dry but I forgot where."

            scene 02_priiask_03
            with dissolve

            mx "I see."
            mx "I'll try searching for it again."
            "(The [[ {color=#00cd67}Garden Trowel{/color} ] might be near where Prii washed it.)"

            show screen calendar_time
            show screen calendar_week
            show screen inventory_button

            jump priscilla_room

        elif garden_trowel in inventory.items and watering_can in inventory.items:

            hide screen calendar_time
            hide screen calendar_week
            hide screen inventory_button

            scene 02_priiask_01
            with fade

            p "[mx]!"

            scene 02_priiask_03
            with dissolve

            p "H-Have you finally found Mama's [[ {color=#6495ed}Watering Can{/color} ] and the [[ {color=#00cd67}Garden Trowel{/color} ]?"
            mx "As a matter of fact, yes I did!"

            scene 02_priiask_01
            with dissolve

            p "R-Really!? Where!?" with vpunch
            mx "I've found the [[ {color=#00cd67}Garden Trowel{/color} ] in the bathroom."

            scene 02_priiask_04
            with dissolve

            p "Oh yeah! I remember now."
            mx "While the [[ {color=#6495ed}Watering Can{/color} ] ended up in Dr. Aanya's patio."
            p "That's why I can't find it!"
            p "It's great you've found both of them!"

            scene 02_priiask_03
            with dissolve

            p "If I just wasn't careless with those, it would've saved you a lot of time."
            mx "It's fine. I better give these to Fiona already."

            scene 02_priiask_01
            with dissolve

            p "Ehehe! Yeah."

            show screen calendar_time
            show screen calendar_week
            show screen inventory_button

            jump priscilla_room
        else:


            hide screen calendar_time
            hide screen calendar_week
            hide screen inventory_button

            scene 02_priiask_01
            with fade

            p "[mx]!"

            scene 02_priiask_03
            with dissolve

            p "H-Have you finally found Mama's [[ {color=#6495ed}Watering Can{/color} ] and the [[ {color=#00cd67}Garden Trowel{/color} ]?"
            mx "No, not yet."
            mx "Remind me again where you left them?"

            scene 02_priiask_02
            with dissolve

            p "Um, okay!"
            p "I'm sure I left the [[ {color=#00cd67}Garden Trowel{/color} ] somewhere downstairs for it to dry but I forgot where."
            p "I clearly remember leaving the [[ {color=#6495ed}Watering Can{/color} ] at the terrace when I left to clean the trowel."
            p "It was gone when I came back."
            p "I've already checked if it fell on the patio but no luck."
            mx "I see."

            scene 02_priiask_03
            with dissolve

            p "I'm sorry for being not helpful."
            mx "No worries. I'll try searching for them."
            "(The [[ {color=#00cd67}Garden Trowel{/color} ] might be near where Prii washed it.)"
            "(The [[ {color=#6495ed}Watering Can{/color} ] on the otherhand is quite tricky. Hypothetically, if it fell and did not land on the patio downstairs then where?)"

            show screen calendar_time
            show screen calendar_week
            show screen inventory_button

            jump priscilla_room

label ep2_fquest_gardentools_trowel:

    if watering_can in inventory.items:

        hide screen calendar_time
        hide screen calendar_week
        hide screen inventory_button

        "(So, Prii left the [[ {color=#00cd67}Garden Trowel{/color} ] here.)"
        "(With the [[ {color=#6495ed}Watering Can{/color} ] with me now, I guess I could give both of these to Fiona.)"

        $ inventory.add(garden_trowel)
        $ fquest_gardentools_trowel_found = True

        show screen calendar_time
        show screen calendar_week
        show screen inventory_button

        jump bathroom
    else:


        "(So, Prii left the [[ {color=#00cd67}Garden Trowel{/color} ] here, huh?)"
        "(I better search for where the [[ {color=#6495ed}Watering Can{/color} ] is next)"

        $ inventory.add(garden_trowel)
        $ fquest_gardentools_trowel_found = True

        jump bathroom

label ep2_fquest_gardentools_watering_can:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    if garden_trowel in inventory.items:

        show 00_wateringcan_idle

        mx "Oh, it's on that tree."
        "(And quite high too.)"
        "(This is gonna take me a while...)"

        hide 00_wateringcan_idle

        scene black with fade

        play sound "soundfx/watering_can.ogg"
        $ renpy.pause(1, hard = True)

        scene aanya_patio_afternoon
        with fade

        "(There! With both of the tools with me now, I better give them to Fiona.)"

        $ inventory.add(watering_can)
        $ fquest_gardentools_wateringcan_found = True

        show screen calendar_time
        show screen calendar_week
        show screen inventory_button

        jump aanya_patio
    else:


        "(Damn. That [[ {color=#6495ed}Watering Can{/color} ] is quite well-hidden, huh?)"
        "(And quite high too.)"
        "(This is gonna take me a minute or so...)"

        scene black with fade
        play sound "soundfx/watering_can.ogg"
        $ renpy.pause(1, hard = True)

        scene aanya_patio_afternoon
        with fade

        "(There! The only thing left is finding where the [[ {color=#00cd67}Garden Trowel{/color} ] is.)"

        $ inventory.add(watering_can)
        $ fquest_gardentools_wateringcan_found = True

        show screen calendar_time
        show screen calendar_week
        show screen inventory_button

        jump aanya_patio


label ep2_fquest_gardenask_aanya:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene 03_aanyadoor_01
    with fade

    play sound "soundfx/doorbell.ogg"

    "{i}*ding*{/i} {i}*dong*{/i}"
    "(If it didn't land on the Fitzgerald's Patio then it means it must've landed here at the Doc's place."

    window hide

    pause

    play sound "soundfx/door_open.ogg"

    scene 03_aanyadoor_02
    with dissolve

    a "Who is it?"

    scene 03_aanyadoor_03
    with dissolve

    a "[mx]?"
    a "Well, what brings you over here?"
    mx "Well, you see..."
    a "Wait!"
    a "Where are my manners?"

    scene 03_aanyadoor_04
    with dissolve

    a "Come in first then we can talk."
    a "It's quite rude of me to let you stay here outside in the blistering sun like a stranger."
    mx "Um.. uh.. okay."
    a "Come on in."

    scene 04_aanyaindoor_01
    with fade

    a "So, what were you about to say?"
    mx "Yeah, umm, I'm looking for one of Fiona's tools, a [[ {color=#6495ed}Watering Can{/color} ]."

    scene 04_aanyaindoor_02
    with dissolve

    a "A Watering can?"
    mx "Yeah. You see, Priscilla was doing some gardening work and left it up on her terrace."
    mx "And I think the Watering can she was using was probably blown over here."

    scene 04_aanyaindoor_01
    with dissolve

    a "So that's the case!"
    a "Well, feel free to search around for it."
    mx "Is that okay?"

    scene 04_aanyaindoor_03
    with dissolve

    a "Of course! You're no stranger to this house."
    a "Before your amnesia, you've been quite helpful around here when Rick needed help."
    mx "Rick? \n Oh, your husband that Prii mentioned."
    a "Yeah."

    scene 04_aanyaindoor_01
    with dissolve

    a "Well, as you can see, he's not here."
    a "He's a Neurosurgeon and a very famous one at that on his field."

    scene 04_aanyaindoor_02
    with dissolve

    a "Ever since he received an invitation to become a speaker in some HEAD-Talk conference in Europe..."
    a "He rarely goes home anymore and is holed up in that lab of his working on his material."
    mx "Oh?"
    mx "You must be very proud of him then?"
    a "..."
    a "...Proud, huh?"
    a "I suppose so, I guess?"
    "(Well, that wasn't much of an enthusiastic response as I expected.)"
    "(It seems the Doc is having marital problems of her own.)"
    "(Best not to delve further into this.)"

    scene 04_aanyaindoor_03
    with dissolve

    a "Anyways, if you're looking for that [[ {color=#6495ed}Watering Can{/color} ] then I can only guess that Fiona's doing some gardening?"
    a "If that's the case, I don't need to hold you up here."
    a "If you need something from me, you can find me in the Living room."
    mx "Got it and thanks again, Doc."

    $ fquest_gardentools_askaanya = False

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump aanya_ground_floor

label aanya_ask:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    if fquest_gardenhelp_start == True:
        if watering_can in inventory.items:

            scene 04_aanyalounge_01
            with fade

            a "[mx]?"
            a "Have you found Fiona's [[ {color=#6495ed}Watering Can{/color} ]?"
            mx "I sure did."
            mx "It was stuck on a tree."
            a "Is that so?"

            scene 04_aanyalounge_02
            with dissolve

            a "I'm glad you found it."
            mx "Thanks for letting me search around, Doc."
            a "It's the least I can do, dear."
            mx "I'll take my leave then."
            mx "Bye."

            show screen calendar_time
            show screen calendar_week
            show screen inventory_button


            jump aanya_living_room
        else:


            scene 04_aanyalounge_01
            with fade

            a "[mx]?"
            a "Have you found Fiona's [[ {color=#6495ed}Watering Can{/color} ]?"
            mx "No, not yet."

            scene 04_aanyalounge_02
            with dissolve

            a "Well, you're free to search the house, dear."
            mx "Okay, I will."

            show screen calendar_time
            show screen calendar_week
            show screen inventory_button

            jump aanya_living_room
    else:
        scene 04_aanyalounge_01
        with fade

        a "Do you need anything, [mx]?"
        mx "Oh, nothing."
        mx "Umm... uhh... I just want to say hello."

        scene 04_aanyalounge_02
        with dissolve

        a "{i}*giggle*{/i}"
        a "Is that so?"
        a "Then, hello to you too."
        mx "Uh, yeah."
        "(Well, that was just embarassing.)"

        show screen calendar_time
        show screen calendar_week
        show screen inventory_button

        jump aanya_living_room

label ep2_fquest_gardenquest_found:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene 01_gardenquest_01
    with fade

    mx "Fiona!"

    scene 01_gardenquest_02
    with dissolve

    f "[mx], have you found them?"
    mx "Yeah."
    mx "Well, you certainly took your time."

    scene 05_fionafound_01
    with dissolve

    mx "Here you go."
    f "You're a life saver."
    mx "All in a day's work."

    scene 05_fionafound_02
    with dissolve

    f "Now let's move on to the second part!"
    mx "The... {p} ...second part?"
    f "Oh, what's this? \nYou didn't think that getting the tools are the only help you'll be offering now, didn't you?"
    f "Unless you don't want to help this frail and fragile lady to do the heavy lifting?"
    mx "Um.. uh.."
    f "Hmmm..."
    mx "{i}*sigh*{/i}"
    mx "Of course I'd be happy to help you."
    f "Ehehe.. that's more like it!"
    "(This woman...)"

    scene 05_fionafound_03
    with dissolve

    f "Hehe! That's the spirit!"
    f "First, get that bag of fertilizer over there and be sure to grab the shovel beside it."
    mx "Yes, Ma'am!"
    f "Let's go kill some weeds, shall we?"
    "(What have I gotten myself into now.)"

    $ renpy.music.stop(channel='music2', fadeout=2)

    scene black
    with slowfade

    show text "{size=36}{color=#A9A9A9} ( A few hours later... ) {/color}{/size}" at truecenter with dissolve

    pause

    scene 05_fionafound_04
    with fade

    if notification_songs == True:
        $ renpy.notify("biosphere - let's be lazy together")

    $ renpy.music.play("music/biosphere-let's be lazy together.mp3", channel='music1', fadein=1, loop=True)

    f "Whew!"
    f "I didn't knew that it would take that long."
    f "Still alive, [mx]?"
    f "It was honestly funny how you used that shovel like it's your first time using one."
    mx "{i}*huff*{/i} {p} {i}*huff*{/i}"
    mx "Y-Yeah..."
    mx "It's because of muscle atrophy and all that..."
    "(Damn. I've never thought that landscaping would be this hard.)"
    "(I've never even touched a shovel in my old life let alone use one.)"

    scene 05_fionafound_05
    with dissolve

    f "That was quite fun, huh?"
    f "Especially if you're not doing most of the heavy work."
    "(Damn that bag of fertilizer.)"
    "(Why did it have to smell so bad.)"
    "(Hm?)"
    mx "Uhh, Fiona?"
    f "What is it?"
    mx "You realize that your gloves are stained with mud, right?"
    f "Obviously, I can see that."
    mx "Then it's also obvious that using them to wipe your face is..."

    scene 05_fionafound_06
    with dissolve

    f "AHH!" with vpunch
    f "I'm so stupid! I forgot!"
    mx "Those weeds really did a number on you, huh?"
    f "Well, I didn't realize those stupid little things were deeply rooted down there."
    f "I thought a simple tug would be enough."

    scene 05_fionafound_07
    with dissolve

    f "Anyways, we're done here now. Time to clean up!"
    f "Oh! Thanks again for today, [mx]."

    scene 05_fionafound_05
    with dissolve

    f "You've been helpful to us for these past few days."
    mx "No problem. \nI'm honestly glad to help around here and not feel like a burden."
    mx "It also helps me adjust to this body—I MEAN, you know!"
    mx "The amnesia and the like!"

    scene 05_fionafound_07
    with dissolve

    f "Ahahaha! I understand."
    "(Phew! Me and my stupid mouth.)"
    f "It's a nice pace to have a man around here to help with stuff like this."
    f "Well, if you don't mind, I'll be taking a bath first. "
    mx "Yeah, you need it more than I do. All I got are stains in my hand and legs."
    f "I'm off then."

    $ fquest_gardenhelp = False
    $ fquest_gardentools_search = False
    $ fquest_gardenhelp_start = False
    $ fquest_gardenhelp_finish = True
    $ fquest_prii_lostjournal = True
    $ inventory.drop(garden_trowel)
    $ inventory.drop(watering_can)
    $ time += 1

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump patio

label ep2_fquest_lostjournal:

    "(What's this? A notebook?)"
    "(...)"
    "(It seems to be Priscilla's.)"
    "(It must've fallen from above.)"
    "(Well, I'll try giving this to her later.)"

    $ inventory.add(lost_journal)
    $ fquest_prii_lostjournal = False

    jump patio

label ep2_fquest_gardenfinish:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene kitchen_evening

    show steam_screen_kitchen

    "(Fiona's probably taking a bath already.)"
    "(The door's open? She must've been in a hurry.)"
    "(Taking a little peek is harmless, right?)"

    $ fquest_gardenhelp_finish = False
    $ fquest_gardenhelp_peek = True
    $ fquest_gardenhelp_ongoing = False

    hide steam_screen_kitchen
    show screen calendar_time
    show screen calendar_week
    show screen inventory_button


    jump kitchen

label ep2_fquest_lostjournal_placed:

    mx "I better leave this here for her to find out."

    $ fquest_prii_lostjournal_placed = True
    $ inventory.drop(lost_journal)

    jump ground_floor_hallway


label ep2_fquest_gardenfinish_peek_01:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene 06_fionabath_01
    with fade

    "(Great! She hasn't undressed yet.)"
    "(I'm dead if she catches me here watching her.)"

    scene 06_fionabath_02
    with dissolve

    f "Uh! Why the hell did I even ask [mx] for help just to end up getting mud all over myself."
    f "In the first place, I should've just asked him to pull out those weeds."
    f "It's gonna be hard washing off this mud stains tomorrow."

    scene 06_fionabath_03
    with dissolve

    "(W-Woah!)"
    "(That's a fine ass!)"
    "(But...)"
    "(Should I really keep on watching?)"

    menu:
        "Continue?":
            jump ep2_fquest_gardenfinish_peek_02
        "Nah, it's too dangerous.":

            jump ep2_priscilla_searching_stop

label ep2_fquest_gardenfinish_peek_02:

    "(Hnnnnnnnnngggggg!)" with vpunch
    "(One more won't hurt!)"

    scene 06_fionabath_04
    with dissolve

    f "Well, despite what happened, it was a good workout, I guess?"
    f "Next time, I should've just pulled out the weed dry instead of watering it down to weaken the soil."
    f "It only ended up backfiring unto me."

    scene 06_fionabath_05
    with dissolve

    f "Oof!"
    f "The mud stains seemed to have rubbed off."
    f "Now, then..."

    scene 06_fionabath_06
    with dissolve

    "(Oh man!)"
    "(I already saw her breasts but I wouldn't mind seeing them again... and again.)"
    "{i}*unclasp*{/i}"

    window hide

    scene 06_fionabath_07
    with dissolve

    pause

    f "Finally, a little breathing room..."
    "(Oh fuck! Oh fuck!)"
    "(My dick's about to burst down here.)"

    play sound "soundfx/walking_wood.ogg"

    "{i}*footsteps*{/i}"
    p "Uh... where is it?"

    scene 08_after
    with fade

    "(Wait! Is that Priscilla?)"
    "(Shit! What should I do?)"

    menu:
        "Damn it! Fortune favors the bold!":
            jump ep2_fquest_gardenfinish_peek_03
        "Nah, this is enough titillation for today.":

            jump ep2_priscilla_searching_stop

label ep2_fquest_gardenfinish_peek_03:

    "(HHHHNNNNNNGGGGGGGGGG!) {p} (Fine!)" with vpunch
    "(It's all or nothing, baby!)"

    window hide

    scene 06_fionabath_09
    with fade

    pause

    "(Jackpot!)"
    f "Well, I hope I didn't gain much weight this month."
    f "I should start doing yoga sooner."
    "(Please turn over!)"
    "(The question of the century is...)"
    "(Does she shave or is she a naturalist?)"
    "(My heart's beating like crazy here!)"

    play sound "soundfx/walking_wood.ogg"

    "{i}*footsteps*{/i}"

    scene 08_after
    with fade

    p "Maybe I left it in the kitchen?"
    "(No, no, no! Please no! She's coming over here!)"
    $ renpy.end_replay()
    jump ep2_fquest_gardenfinish_peek_branch

label ep2_fquest_gardenfinish_peek_branch:

    if fquest_prii_lostjournal_placed == True:

        p "Wait! That is.."
        p "Did I left this here?"
        p "Strange. Anyways, I'm glad I finally found it."
        "(Yes!) {p} (I'm glad I left that there.)" with vpunch
        "(Now, for the finale...)"

        window hide

        scene 06_fionabath_08
        with fade

        pause

        "(We've got bush! I repeat, we've got bush!)"
        f "Did my breasts grew again?"
        f "Oh no! \nI'm not getting fat, am I?"
        "(Ah! Fuck me sideways...)"
        "(That fire crotch is just... urgh!)"
        "(I don't regret working my ass off today.)"

        scene 06_fionabath_10
        with dissolve

        "(This is unbelievable!)"
        play sound "soundfx/splash.ogg"
        "{i}*splash*{/i}"

        scene 06_fionabath_11
        with dissolve

        f "It's been a long day."
        play sound "soundfx/splash.ogg"
        "{i}*splash*{/i}"
        f "Hmm..."
        f "I love the water on my skin..."
        f "Hmmm... hmm..."
        "(Damn! That's...so—)"

        scene 06_fionabath_11
        with flash

        scene 06_fionabath_11
        with flash

        "(...)"
        "(God! Seriously?)"
        "(The hell is with this body? It's too damn sensitive.)"
        "(I didn't expect to just cum in my pants.)"
        "(Well, it was a damn fine show.)"
        "(I better go back to my room and clean this mess up.)"

        jump ep2_fquest_gardenhelp_end
    else:


        if lost_journal in inventory.items:

            p "[mx]!"

            scene 07_priiinterrupt_01
            with fade

            mx "P-P-Prii? Uh, um, uh, h-hey there!"
            "(Goddamit! Erection begone!)"
            p "Are you okay?"
            mx "Y-Yeah! I'm just... practicing some Zen Buddhist breathing technique to balance the Chi of energy flowing through my body."
            p "Uh... {p}...okay?"
            mx "I heard you talking to yourself about finding something?"
            p "Ah, yeah! It seems I lost my [[ {color=#89ecda}Journal{/color} ] somewhere."

            scene 07_priiinterrupt_02
            with dissolve

            mx "Did it have a blue cover?"
            p "Sort of? It's more of a \"Turquoise\" color really."
            mx "I see."

            scene 07_priiinterrupt_04
            with dissolve

            mx "Something like this?"
            p "Oh my God!"
            p "Where did you find it!"
            mx "Back there at the patio. You seriously need to keep an eye on your things."
            mx "The tools and now this."
            p "Yeah..."
            p "But you're here now aren't you! Ehehehe!"
            mx "Prii..."
            p "Thank you! I'll try to write more plans!"
            p "See you later!"

            scene 08_after
            with fade

            mx "{i}*sigh*{/i}"
            "(Well, atleast I've seen some amazing things today.)"
            "(By this point, she's probably finished.)"
            "(I better go back.)"

            $ inventory.drop(lost_journal)

            jump ep2_fquest_gardenhelp_end
        else:


            p "[mx]!"

            scene 07_priiinterrupt_01
            with fade

            mx "P-P-Prii? Uh, um, uh, h-hey there!"
            "(Goddamit! Erection begone!)"
            p "Are you okay?"
            mx "Y-Yeah! I'm just... practicing some Zen Buddhist breathing technique to balance the Chi of energy flowing through my body."
            p "Uh... {p}...okay?"
            mx "I heard you talking to yourself about finding something?"
            p "Ah, yeah! It seems I lost my [[ {color=#89ecda}Journal{/color} ] somewhere."

            scene 07_priiinterrupt_02
            with dissolve

            mx "Did it have a blue cover?"
            p "Sort of? It's more of a \"Turquoise\" color really."
            mx "I see."

            scene 07_priiinterrupt_03
            with dissolve

            mx "Now that you mention it..."
            mx "I think I saw that it back there in the yard."
            p "Really! Then I'm off!"
            mx "You seriously need to keep an eye on your things."
            mx "The tools and now this."
            p "Yeah..."
            p "But you're here now aren't you! Ehehehe!"
            mx "Prii..."
            p "Thank you! I'll try to write more plans!"
            p "See you later!"

            scene 08_after
            with fade

            mx "{i}*sigh*{/i}"
            "(Well, atleast I've seen some amazing things today.)"
            "(I can't peek if Priscilla's back there.)"
            "(I better go back.)"

            jump ep2_fquest_gardenhelp_end

label ep2_priscilla_searching_stop:
    $ renpy.end_replay()
    if fquest_prii_lostjournal_placed == True:

        scene 08_after
        with fade

        play sound "soundfx/walking_wood.ogg"

        "{i}*footsteps*{/i}"
        p "Where is that notebook?"
        p "Wait! That is.."
        p "Did I left this here?"
        p "Strange. Anyways, I'm glad I finally found it."
        "(I'm glad I placed that there.)"
        "(Anyways, atleast I've seen some amazing things today.)"
        "(I better go back.)"

        jump ep2_fquest_gardenhelp_end
    else:


        if lost_journal in inventory.items:

            scene 08_after
            with fade

            play sound "soundfx/walking_wood.ogg"

            "{i}*footsteps*{/i}"
            p "Where is that notebook?"
            p "It might be in the kitchen."

            scene 07_priiinterrupt_01
            with fade

            p "[mx]! You're here!"
            mx "Hey Prii!"
            mx "I heard you talking to yourself about finding something?"
            p "Ah, yeah! It seems I lost my [[ {color=#89ecda}Journal{/color} ] somewhere."

            scene 07_priiinterrupt_02
            with dissolve

            mx "Did it have a blue cover?"
            p "Sort of? It's more of a \"Turquoise\" color really."
            mx "I see."

            scene 07_priiinterrupt_04
            with dissolve

            mx "Something like this?"
            p "Oh my God!"
            p "Where did you find it!"
            mx "Back there at the patio. You seriously need to keep an eye on your things."
            mx "The tools and now this."
            p "Yeah..."
            p "But you're here now aren't you! Ehehehe!"
            mx "Prii..."
            p "Thank you! I'll try to write more plans!"
            p "See you later!"

            scene 08_after
            with fade

            mx "{i}*sigh*{/i}"
            "(Well, atleast I've seen some amazing things today.)"
            "(I better go back.)"

            $ inventory.drop(lost_journal)

            jump ep2_fquest_gardenhelp_end
        else:


            scene 08_after
            with fade

            play sound "soundfx/walking_wood.ogg"

            "{i}*footsteps*{/i}"
            p "Where is that notebook?"
            p "It might be in the kitchen."

            scene 07_priiinterrupt_01
            with fade

            p "[mx]! You're here!"
            mx "Hey Prii!"
            mx "I heard you talking to yourself about finding something?"
            p "Ah, yeah! It seems I lost my [[ {color=#89ecda}Journal{/color} ] somewhere."

            scene 07_priiinterrupt_02
            with dissolve

            mx "Did it have a blue cover?"
            p "Sort of? It's more of a \"Turquoise\" color really."
            mx "I see."

            scene 07_priiinterrupt_03
            with dissolve

            mx "Now that you mention it..."
            mx "I think I saw that it back there in the yard."
            p "Really! Then I'm off!"
            mx "You seriously need to keep an eye on your things."
            mx "The tools and now this."
            p "Yeah..."
            p "But you're here now aren't you! Ehehehe!"
            mx "Prii..."
            p "Thank you! I'll try to write more plans!"
            p "See you later!"

            scene 08_after
            with fade

            mx "{i}*sigh*{/i}"
            "(Well, atleast I've seen some amazing things today.)"
            "(I better go back.)"

            jump ep2_fquest_gardenhelp_end

label ep2_fquest_gardenhelp_end:

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    $ renpy.music.stop(channel='music1', fadeout=2)

    $ story_music_ongoing = False

    $ fquest_prii_lostjournal_placed = False
    $ fquest_prii_lostjournal = False
    $ fquest_gardenhelp_peek = False
    $ fquest_gardenhelp_peek_end = True
    $ fquest_gardenhelp_end = True
    $ fquest_gardenhelp_complete = True

    $ map_time_skip = True

    jump kitchen

label ep2_fquest_gardenhelp_end_earlysleeper:

    $ renpy.music.stop(channel='music1', fadeout=2)

    $ story_music_ongoing = False

    $ map_time_skip = True

    $ fquest_gardenhelp_finish = False
    $ fquest_gardenhelp_peek = False
    $ fquest_gardenhelp_peek_end = False
    $ fquest_gardenhelp_ongoing = False
    $ fquest_prii_lostjournal_placed = False
    $ fquest_prii_lostjournal = False
    $ fquest_gardenhelp_peek = False
    $ fquest_gardenhelp_end = True
    $ fquest_gardenhelp_complete = True

    jump mc_room


label ep2_fquest_dresschoose_mail:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    "(Hm? What's this?)"
    "(A mail?)"
    mx "To Mrs. Fiona Fitzgerald."
    mx "From Capitalia University."
    "(Oh, its for Fiona.)"
    "(I better give this to her when I see her.)"

    $ inventory.add(mail_invitation)

    $ fquest_mailinvitation_taken = True

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump ground_floor_hallway

label ep2_fquest_dresschoose_start:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    if mail_invitation in inventory.items:

        scene 01_invitation_01
        with dissolve

        mx "Oh, Fiona."
        mx "There you are!"

        scene 01_invitation_02
        with dissolve

        f "[mx]?"
        f "Do you need something?"
        mx "A letter came for you."

        scene 01_invitation_03
        with dissolve

        f "A letter? Let me see..."
        f "From my alma mater, huh?"
        f "I'm curious what's inside?"

        scene 01_invitation_04
        with dissolve

        f "..."
        f "Greetings... blablabla... the university..."
        f "Ah! Here!"
        f "The university would like to inform you that in..."
        f "..."

        scene 01_invitation_05

        f "WHAT!?" with vpunch
        f "Oh no, no, no!"
        "(What's written in the letter?)"

        scene 01_invitation_06
        with dissolve

        mx "Are you alright, Fiona?"
        f "This is beyond terrible!"
        f "They should've sent this letter months ago."
        "(That's around the time I was hospitalized!)"
        mx "Did... did something happen?"
        mx "Something bad like... someone dying?"
        f "Worse. Much much worse!"
        mx "Much worse than someone dying?"
        f "Yes."
        mx "I'm sorry to hear—"
        f "Our class reunion is happening this weekend."
        mx "{i}*cough*{/i} \n{i}*cough*{/i}" with vpunch
        f "It basically robbed me time to prepare."
        mx "I think it's not that big of a deal—"

        scene 01_invitation_07
        with dissolve

        f "It's a pretty big deal, alright!" with vpunch
        f "You guys don't mind it too much but for us women? It's the greatest battle of passive-agressiveness!"
        f "I joined Catriona's alumni reunion and the women there aren't fooling around with their words!"
        f "And I'm surely meeting that bitch Brittany again!"
        mx "Uh... huh."

        scene 01_invitation_08
        with dissolve

        f "Well, I'm off to prepare."
        mx "Y-Yeah."
        "(Well, someone's really motivated this morning.)"
        "(I'll try checking up on her this evening.)"

        $ inventory.drop(mail_invitation)
        $ fquest_dresschoose_start = True
        $ fquest_mailinvitation_give = True

        show screen calendar_time
        show screen calendar_week
        show screen inventory_button

        jump kitchen
    else:


        hide screen calendar_time
        hide screen calendar_week
        hide screen inventory_button

        scene 01_invitation_01
        with dissolve

        mx "Hey, Fiona!"
        f "Hm?"

        scene 01_invitation_02
        with dissolve

        f "[mx]."
        mx "Doing some work?"
        f "Yeah. \nJust checking my e-mails and corresponding to some of them."
        mx "I see. Well, goodluck with that."

        scene 01_invitation_01
        with dissolve

        f "Thanks."

        show screen calendar_time
        show screen calendar_week
        show screen inventory_button

        jump kitchen

label ep2_fquest_dresschoose_evening:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene 02_dressroom_01
    with dissolve

    f "...the dress is one thing but that..."
    mx "Fiona."
    f "...wearing the glasses would give more a sophisticated look but..."
    mx "Fiona?"
    f "...then again, if I pair it with the..."
    mx "Fiona!"

    scene 02_dressroom_02
    with dissolve

    $ renpy.music.stop(channel='music3', fadeout=8)

    $ story_music_ongoing = True

    f "W-W-Wha!?" with vpunch
    f "[mx]!"
    f "D-Don't scare me like that!"
    mx "I've been calling you for quite awhile, y'know?"
    f "Oh, I'm sorry. \nMy mind's too busy thinking about the reunion..."
    mx "Yeah, I can see that."

    scene 02_dressroom_03
    with dissolve

    if notification_songs == True:
        $ renpy.notify("prima - june gloom.")

    $ renpy.music.play("music/prima-june gloom.mp3", channel='music2', fadein=1, loop=True)

    f "Well, after thinking about this for quite some time, it's down to 2 outfits, I guess?"
    f "Either I want to be much more conservative to the reunion like I was in college or go in quite the opposite, be more revealing."
    f "A more mature Fiona Fitzgerald vibe?"
    mx "Uh-huh."
    mx "So, which one will you choose?"
    f "That's... urgh!"
    f "I don't know! It's been so long since I've been in a large party like this and I don't know if my attire will—"

    scene 02_dressroom_04 with vpunch

    f "You!"
    mx "M-Me?"
    f "You're a guy, right!?"
    mx "Last time I checked, I still am unless the definitions changed?"
    f "N-No, I mean, you be the judge!"
    mx "Me be the judge?"
    f "Yeah! \nI can't ask Prii what she thinks about the dress 'cause she's too much of an angel to criticize me but you on the otherhand..."
    mx "Somehow that felt more of an underhanded insult than a compliment."
    f "Ahahaha!"

    scene 02_dressroom_05
    with dissolve

    f "Why don't you take a seat over there while I get ready."
    mx "Uh... sure."
    f "Oh, which one do you want to see first?"

    menu:
        "Let's start with the conservative one.":


            f "Really? I thought you boys would like to see the revealing one first? Hm?"
            mx "Wha? N-No! I just want to see it first."
            mx "Y-You were the one who asked!"
            f "Ahahaha! You're so teasable, [mx]."
            f "I'll get ready. \nNo peeking!"
            mx "I-I won't!"
            "(Time and time again, this woman...)"

            $ fquest_dresschoose_conservative = True

            jump ep2_fquest_dresschoose_wait_1
        "The, um, revealing one first?":


            f "Oh, you want to see the revealing one that badly?"
            mx "Wha? N-No! I just want to see it first."
            mx "Y-You were the one who asked!"
            f "Ahahaha! You're so teasable, [mx]."
            f "I'll get ready. \nNo peeking!"
            mx "I-I won't!"
            "(Time and time again, this woman...)"

            $ fquest_dresschoose_revealing = True

            jump ep2_fquest_dresschoose_wait_1

label ep2_fquest_dresschoose_wait_1:

    scene black

    show text "Half an hour later..." at truecenter with fade

    pause

    scene 02_dressroom_06
    with fade

    "(Oh man, when she said she was getting ready, I was expecting a few minutes at best.)"
    "(It's almost an hour now.)"
    "(How long does it take to wear a simple dress?)"

    scene 02_dressroom_07
    with dissolve

    play sound "soundfx/unlock.ogg"

    "{i}*kachik*{/i}"

    mx "Hmm?"

    play sound "soundfx/door_open.ogg"

    "{i}*door creaking*{/i}"

    if fquest_dresschoose_conservative == True:

        jump ep2_fquest_dresschoose_conservative

    elif fquest_dresschoose_revealing == True:

        jump ep2_fquest_dresschoose_revealing

label ep2_fquest_dresschoose_wait_2:

    scene black

    show text "Half an hour later... again." at truecenter with fade

    pause

    scene 02_dressroom_06
    with fade

    mx "{i}*sigh*{/i}"
    "(Sometimes I wonder if I'm just really a masochist.)"
    "(I'll never understand why women take this long dressing up.)"

    scene 02_dressroom_07
    with dissolve

    play sound "soundfx/unlock.ogg"
    "{i}*kachik*{/i}"
    f "Sorry for the wait!"
    mx "Nah, I was fine waiting."
    "(Yep. I really am a masochist and damn liar too.)"

    play sound "soundfx/door_open.ogg"
    "{i}*door creaking*{/i}"

    if fquest_dresschoose_conservative == True:
        jump ep2_fquest_dresschoose_conservative
    elif fquest_dresschoose_revealing == True:
        jump ep2_fquest_dresschoose_revealing

label ep2_fquest_dresschoose_wait_3:

    scene 02_dressroom_06
    with fade

    "(Back to the waiting game.)"
    "(I wonder how long would this take—)"

    play sound "soundfx/crash.ogg"

    "{i}*CRASH!*{/i}" with vpunch

    scene 02_dressroom_07
    with dissolve

    mx "Fiona!"
    mx "Are you alright?"
    "..."
    "(Shit! I better check up on her.)"

    $ fquest_dresschoose_start = False
    $ story_ongoing_fionaroom = True
    $ fquest_dresschoose_accident = True
    $ lingerie_room_unlocked = True

    jump fiona_room

label ep2_fquest_dresschoose_conservative:

    scene 03_attire_sweater_long with fade:
        subpixel True
        yalign 1.0
        pause 1.0
        linear 5.0 yalign 0.0

    pause

    window hide

    "{i}*gulp*{/i}"
    "(So, that's conservative nowadays? Damn.)"
    "(I mean, that sweater covers every inch of her skin but the fit is...)"
    "(Let's just say, those curves can't be hidden.)"

    scene 03_attire_sweater_02
    with dissolve

    f "S-So..."
    f "What do you think?"
    mx "Um... well..."
    mx "It looks... amazing."
    f "R-Really!?"
    mx "Yeah. I'd be lying if it isn't."
    mx "What's with the glasses though?"

    scene 03_attire_sweater_01
    with dissolve

    f "Oh, this?"
    f "Well, I actually have myopia you know?"
    mx "Myopia?"
    f "It's being \"nearsighted\", dear. \nMost of the time I'm wearing contacts for convenience."
    f "During university I wore glasses. \nIt wasn't until years after that I tried wearing contact lenses."
    f "So, it's kinda a call back to that time. \nDoes it look bad?"
    mx "No. It's kinda hot actually-I MEAN, it's cute! \nIt matches well with the sweater is what I meant to say."

    scene 03_attire_sweater_03
    with dissolve

    f "Oh, so you have a thing for girls with glasses, eh?"
    mx "N-No... that was... it was a subconscious thing."
    f "Ehehe.. alright then, glasses boy."
    mx "Hey!"

    $ fquest_dresschoose_counter += 1

    if fquest_dresschoose_counter == 2:

        scene 03_attire_sweater_03
        with dissolve

        f "Well, you've finally seen both of the outfits but maybe..."
        f "Umm... are you okay seeing another one? Just for an opinion!"
        mx "Uh..."
        f "I promise that this is the last one!"
        f "I know you're bored by now."
        mx "{i}*sigh*{/i}"
        mx "Do I really have any other option? Fine!"
        mx "Now that you brought it up, I'm now curious seeing it too."
        f "Thanks, [mx]."

        jump ep2_fquest_dresschoose_wait_3
    else:

        $ fquest_dresschoose_conservative = False
        $ fquest_dresschoose_revealing = True

        f "Finally, the dress is next."
        f "I hope you don't mind waiting a bit."
        f "It'll just take a few minutes at best."
        mx "Uh.. sure."
        "(A few minutes, huh?)"

        jump ep2_fquest_dresschoose_wait_2


label ep2_fquest_dresschoose_revealing:

    scene 03_attire_dress_long with fade:
        subpixel True
        yalign 1.0
        pause 1.0
        linear 5.0 yalign 0.0

    window hide

    pause

    mx "{i}*whistle*{/i}"
    "(Damn.)"
    "(That dress is just... wow.)"

    scene 03_attire_dress_01
    with dissolve

    f "Soooo?"
    mx "..."
    f "[mx]?"
    mx "....."

    scene 03_attire_dress_02
    with dissolve

    f "D-Does it look that bad?"
    mx "N-No, I'm just speechless."
    mx "You look gorgeous. Amazing even."

    scene 03_attire_dress_01
    with dissolve

    f "Uh...er... thank you."

    scene 03_attire_dress_02
    with dissolve

    f "I'm just wondering if this dress is too revealing?"
    f "I was thinking presenting myself as more \"mature\" now, so to speak."
    f "But I don't know if I just ended up looking like a... harlot?"
    mx "If I remember whores correctly, they don't exactly dress nicely like that."

    scene 03_attire_dress_03
    with dissolve

    f "Pfft! Ahahaha!"
    f "[mx]! Language please!"
    f "But seriously, thanks."

    $ fquest_dresschoose_counter += 1

    if fquest_dresschoose_counter == 2:

        scene 03_attire_dress_03
        with dissolve

        f "Well, you've finally seen both of the outfits but maybe..."
        f "Umm... are you okay seeing another one? Just for an opinion!"
        mx "Uh..."
        f "I promise that this is the last one!"
        f "I know you're bored by now."
        mx "{i}*sigh*{/i}"
        mx "Do I really have any other option? \n Fine, Fine!"
        mx "Now that you brought it up, I'm now curious seeing it too."
        f "Thanks, [mx]."

        jump ep2_fquest_dresschoose_wait_3
    else:


        f "Finally, the sweater is next."
        f "I hope you don't mind waiting a bit."
        f "It'll just take a few minutes at best."
        mx "Uh.. sure."
        "(A few minutes, huh?)"

        $ fquest_dresschoose_conservative = True
        $ fquest_dresschoose_revealing = False
        jump ep2_fquest_dresschoose_wait_2

label ep2_fquest_dresschoose_accident:

    scene 04_fionaaccident_01
    with fade

    mx "Woah! What is this room?"
    "(I thought it was just a small closet or something?)"
    "(This looks like more of a retail store.)"
    f "Mhm.."
    mx "Fiona!" with vpunch

    show screen fiona_accident_mannequins_overlay

    scene 04_fionaaccident_02
    with dissolve

    mx "Are you okay!?"
    f "...yeah."
    "(I need to remove this mannequins first from her.)"

label ep2_fquest_dresschoose_accident_help:

    if mannequin_taken_counter == 3:
        jump ep2_fquest_dresschoose_accidentafter
    else:

        hide screen fiona_accident_mannequins_overlay
        call screen fiona_accident_mannequins
        scene 04_fionaaccident_02

label ep2_fquest_dresschoose_accidentafter:

    scene 04_fionaaccident_03
    with fade

    f "Uhmmm..."
    f "Thanks for the help."
    mx "You all right? What happened?"
    f "Yeah, I'm fine."
    f "I wanted to try one of the dresses on the shelf but when I tried to grab one I..."
    f "Well, as you saw, fell down and knocked myself out."
    mx "The shelf? Speaking of which..."
    mx "What exactly is this place?"

    scene 04_fionaaccident_06
    with dissolve

    f "Ah.. well..."
    f "Welcome to my... \"Lingerie room\"?"
    mx "Lingerie... room?"
    mx "This is a lot of lingerie to wear..."
    f "Oh! No!no!no!" with vpunch
    f "I haven't even tried to wear a single one to be honest."
    f "Most of these are references and stocks I've yet to sell..."
    mx "Sell? You made these?"

    scene 04_fionaaccident_03
    with dissolve

    f "Y-Yeah..."
    mx "So, the fabrics that time were..?"
    f "Uh-huh. \nMost of my clients order through the Quantumnet."
    f "Sometimes the orders just keep on coming that I renovated this room as a storage of sort."
    f "I kinda styled it so that I can create a showcase to show the clients."
    mx "No wonder it looks like more of a boutique than a closet."
    mx "Does Prii know?"

    scene 04_fionaaccident_06
    with dissolve

    f "A little bit but she isn't one to snoop around in here."
    mx "I see."
    mx "Well then, I guess you better dress up before you catch a cold."

    scene 04_fionaaccident_04
    with vpunch

    f "O-Oh shoot!"
    f "I forgot I was still in my underwear!"

    scene 04_fionaaccident_05
    with dissolve

    f "Argh!!"
    f "Why is it that everytime I get into an accident, I always end up exposing myself!?"
    mx "Ah... hehe... sorry."

    scene 04_fionaaccident_06
    with dissolve

    f "Oh no, no..."
    f "I-It's not your fault. I'm just a..."
    f "A clutz, really."
    mx "Uh.. well..."
    mx "Let's get you up first, shall we?"

    scene 04_fionaaccident_07
    with dissolve

    f "Ah, yeah."
    mx "Did you hurt your feet?"
    f "A little but nothing major."
    mx "Here. One, two..."
    f "Ow!"
    mx "Three-woah!"

    scene black
    with vpunch

    play sound "soundfx/falling_thud.ogg"

    "{i}*bang*{/i}"
    mx "Uhh... what's this..?"
    mx "It feels soft.."
    mx "Must be one of Fiona's lingerie—"
    f "Ahn!"
    mx "! ! !"

    scene 04_fionaaccident_08
    with dissolve

    "(HOLY SHIT! T-T-THIS IS...)"
    "(FIONA'S BREAST!)"
    "(Lingerie my ass!)"
    f "Haaa... hnng..!"

    scene 04_fionaaccident_09
    with hpunch

    mx "Oh shit! I-I'm sorry, Fiona!"
    mx "T-T-That was just an accident!!"
    f "Haa... ha.."
    f "Uhh... umm... y-yeaah.."

    scene 05_accidentafter_01
    with slowfade

    f "..."
    mx "..."
    mx "You see.. umm... what happened was..."

    scene 05_accidentafter_02
    with dissolve

    f "It's alright. I'm not mad. \nIt was just embarassing."
    mx "Yeah, I'm sorry. I'm just gonna leave right now."

    jump ep2_fquest_dresschoose_choice

label ep2_fquest_dresschoose_choice:

    scene 05_accidentafter_03
    with dissolve

    f "Wait, [mx]!" with vpunch
    mx "I-Is there a problem? I swear that was—"
    f "N-No, not that. Its... {p} You still haven't..."
    mx "Um, haven't what?"

    scene 05_accidentafter_04
    with dissolve

    f "W-What dress do you think I should wear?"
    mx "Oh yeah, I... forgot."
    mx "Well..."

    menu:
        "I think the sweater suits you more.":

            mx "The sweater was cute on you."
            f "C-Cute, huh?"
            f "Hehehe.."

            scene 05_accidentafter_05
            with dissolve

            f "The sweater it is then."

            scene 05_accidentafter_06
            with dissolve

            $ fquest_sweater_chosen = True

            jump ep2_fquest_dresschoose_end
        "I think the dress would make more of an impact.":


            mx "The dress had more of an impact, personally."
            mx "It makes you more elegant, I guess?"
            f "Elegant, huh?"
            f "Hehehe.."

            scene 05_accidentafter_05
            with dissolve

            f "Well, if you say so."
            f "The dress it is."

            scene 05_accidentafter_06
            with dissolve

            $ fquest_dress_chosen = True

            jump ep2_fquest_dresschoose_end

label ep2_fquest_dresschoose_end:

    $ renpy.music.stop(channel='music2', fadeout=3)

    mx "W-Well, I've gotta go."
    f "Y-Yeah, I need to clean this mess up first."
    f "Thanks for the help, [mx]."
    mx "Anytime, Fiona. Take care."
    f "You too, dear."

    $ story_music_ongoing = False

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    $ story_ongoing_fionaroom = False
    $ fquest_dresschoose_accident = False
    $ fquest_dresschoose_complete = True
    $ fquest_dresschoose_doorlocked = True

    jump second_floor_hallway


label ep2_fquest_drunkenvisit:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    if fquest_dress_chosen == True:

        scene 01_nightstart_dress_01
        with fade

        mx "Looks like you're ready for the party, huh?"
        f "[mx]."
        f "Yeah... \nMy heart's beating too fast."
        f "By the way..."

        scene 01_nightstart_dress_02
        with dissolve

        f "H-How do I look?"

        menu:
            "You look amazing.":


                scene 01_nightstart_dress_03
                with dissolve

                f "R-Really? It doesn't look bad."
                mx "Yeah!"

                scene 01_nightstart_dress_04
                with dissolve

                f "You're not just teasing me are you?"
                mx "No! I'd be lying if I said otherwise."

                scene 01_nightstart_dress_03
                with dissolve

                f "I'm sorry.. \nThis party is just making me a mess."

                jump ep2_fquest_drunkenvisit_dress_cont
            "Wait! Is that a stain?":


                scene 01_nightstart_dress_06
                with dissolve

                f "Oh my God! Where!?" with vpunch
                f "I swear I should've just worn the—"
                mx "Got you!"
                f "Wha!?"

                scene 01_nightstart_dress_04
                with flash

                mx "Ow! ow! I'm kidding!" with vpunch

                scene 01_nightstart_dress_04
                with flash

                mx "Ow! {p} Ahahaha!" with vpunch
                f "[mx]!"
                mx "Ahahaha! You were just too tensed up to not tease."
                f "You ass!"
                f "T-That was scary."
                mx "What are you worried about? You look amazing."

                scene 01_nightstart_dress_03
                with dissolve
                f "R-Really?"
                mx "Yep."

                jump ep2_fquest_drunkenvisit_dress_cont


        label ep2_fquest_drunkenvisit_dress_cont:

        mx "It's just a party, Fiona."
        mx "Relax."

        scene 01_nightstart_dress_05
        with dissolve

        f "I know but..."
        f "It's been so long since I've been to a party like this."
        f "Meeting old friends and... old rivals."
        f "{i}*sigh*{/i}"
        mx "Hey now!"
        mx "Be more confident!"
        mx "Where did the outgoing and rude Fiona who kept teasin' me all this week go?"

        scene 01_nightstart_dress_03
        with dissolve

        f "Hehehe... yeah."
        f "I think overreacting to this is a bit much, huh?"
        f "I better—"

        play sound "soundfx/carhorn.ogg"

        window hide
        pause

        scene 01_nightstart_dress_04
        with dissolve

        f "Seriously! That woman should know manners!"
        f "She'll wake up the whole neighborhood honking like that."
        mx "Who?"
        f "Catriona. \nShe's driving me there while my car's in the shop right now."
        f "Anyways..."

        scene 01_nightstart_dress_07
        with dissolve

        f "Mwah!" with vpunch
        mx "U-Uhhh..."
        f "Take care of the house while we're away, okay?"
        f "Prii's with her classmates right now so you'll be all alone in here."
        f "Guard the house won't you?"
        mx "O-Of course.."
        f "I better go!"
        mx "Go get 'em tigress."
        f "Ehehe.. I will."

        scene black
        with fade

        scene fiona_room_evening
        with dissolve

        show screen calendar_time
        show screen calendar_week
        show screen inventory_button

        $ fquest_drunkenvisit_start = True
        $ fquest_drunkenvisit = False

        jump fiona_room

    elif fquest_sweater_chosen == True:

        scene 01_nightstart_sweater_01
        with fade

        mx "Looks like you're ready for the party, huh?"
        f "[mx]."
        f "Yeah... \nMy heart's beating too fast."
        f "By the way..."

        scene 01_nightstart_sweater_02
        with dissolve

        f "H-How do I look?"

        menu:
            "You look amazing.":


                scene 01_nightstart_sweater_03
                with dissolve

                f "R-Really? It doesn't look bad."
                mx "Yeah!"

                scene 01_nightstart_sweater_04
                with dissolve

                f "You're not just teasing me are you?"
                mx "No! I'd be lying if I said otherwise."

                scene 01_nightstart_sweater_03
                with dissolve

                f "I'm sorry.. \nThis party is just making me a mess."

                jump ep2_fquest_drunkenvisit_sweater_cont
            "Wait! Is that a stain?":


                scene 01_nightstart_sweater_06
                with dissolve

                f "Oh my God! Where!?" with vpunch
                f "I swear I should've just worn the—"
                mx "Got you!"
                f "Wha!?"

                scene 01_nightstart_sweater_04
                with flash

                mx "Ow! ow! I'm kidding!" with vpunch

                scene 01_nightstart_sweater_04
                with flash

                mx "Ow! {p} Ahahaha!" with vpunch
                f "[mx]!"
                mx "Hahaha! You were just too tensed up to not tease."
                f "You ass!"
                f "T-That was scary."
                mx "What are you worried about? You look amazing."

                scene 01_nightstart_sweater_03
                with dissolve
                f "R-Really?"
                mx "Yep."

                jump ep2_fquest_drunkenvisit_sweater_cont


        label ep2_fquest_drunkenvisit_sweater_cont:

        mx "It's just a party, Fiona."
        mx "Relax."

        scene 01_nightstart_sweater_05
        with dissolve

        f "I know but..."
        f "It's been so long since I've been to a party like this."
        f "Meeting old friends and... old rivals."
        f "{i}*sigh*{/i}"
        mx "Hey now!"
        mx "Be more confident!"
        mx "Where did the outgoing and rude Fiona who kept teasin' me all this week go?"

        scene 01_nightstart_sweater_03
        with dissolve

        f "Hehehe... yeah."
        f "I think overreacting to this is a bit much, huh?"
        f "I better—"

        play sound "soundfx/carhorn.ogg"

        window hide
        pause

        scene 01_nightstart_sweater_04
        with dissolve

        f "Seriously! That woman should know manners!"
        f "She'll wake up the whole neighborhood honking like that."
        mx "Who?"
        f "Catriona. \nShe's driving me there while my car's in the shop right now."
        f "Anyways..."

        scene 01_nightstart_sweater_07
        with dissolve

        f "Mwah!" with vpunch
        mx "U-Uhhh..."
        f "Take care of the house while we're away, okay?"
        f "Prii's with her classmates right now so you'll be all alone in here."
        f "Guard the house won't you?"
        mx "O-Of course.."
        f "I better go!"
        mx "Go get 'em tigress."
        f "Ehehe.. I will."

        scene black
        with fade

        scene fiona_room_evening
        with dissolve

        show screen calendar_time
        show screen calendar_week
        show screen inventory_button

        $ fquest_drunkenvisit_start = True
        $ fquest_drunkenvisit = False

        jump fiona_room

label ep2_fquest_drunkenvisit_disturbance:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button
    hide screen map_button

    $ fquest_drunkenvisit_start = False
    $ renpy.music.stop(channel='music3', fadeout=1)

    scene black
    with fade

    play sound "soundfx/door_locked.ogg"
    "{i}*clunking sounds*{/i}"

    mx "Hmmm...."
    "(What's that... noise..?)"

    scene 01_nightvisitroom_01
    with fade

    "(Is.... that.... my door..?)"

    play sound "soundfx/door_locked.ogg"
    "{i}*clunking sounds*{/i}"

    "(...making that noise?)"

    menu:
        "Check it out.":

            scene 01_nightvisitroom_02
            with dissolve

            mx "Ugh..."

    "(Shit! I'm only one left in the house at this moment!)"
    play sound "soundfx/door_locked.ogg"
    "{i}*clunking sounds*{/i}"
    "(I'm not ready for a battle of life and death, dammit!)"
    play sound "soundfx/door_locked.ogg"
    "{i}*clunking sounds*{/i}"
    "(HHHNNNNNGGGGGGG!)"
    "(Here goes nothing!)"

    menu:
        "Open door.":
            if fquest_dress_chosen == True:
                jump ep2_fquest_drunkenvisit_dress_path

            elif fquest_sweater_chosen == True:
                jump ep2_fquest_drunkenvisit_sweater_path




label ep2_fquest_drunkenvisit_dress_path:

    scene 01_nightvisitroom_dress_01
    with dissolve

    mx "HHYYYAAAAA...aah..."

    if notification_songs == True:
        $ renpy.notify("PerroFunky - C L O S E Y O U R E Y E S")

    $ renpy.music.play("music/perrofunky-closeyoureyes.mp3", channel='music2', fadein=1, loop=True)

    f "{i}*hic!*{/i}" with vpunch
    f "wWwhy i-Is t-thiis... dOorlocKed?"
    f "{i}*hic!*{/i}" with vpunch
    f "OhH... it'S opEn NoOW.."
    mx "Fiona?"
    f "HhmMm..?"

    scene 01_nightvisitroom_dress_02
    with dissolve

    f "[mx]? wHhat Aare yOu doInG hEere...?"
    mx "You're letting me stay here, remember?"
    mx "Wait. {p} You're wasted."
    f "{i}*hic!*{/i}" with vpunch
    f "NnNooOo I'Mm noOtt... ehEheehe..."
    f "jUsSt TiippPsSsyY..."
    mx "Yeah right."
    f "I fOrgOt YoU'rE StaYing hEre. ThEn I-I'lL jUsSst..."
    mx "Woah! Watch your step!"

    scene 01_nightvisitroom_dress_03
    with vpunch

    f "I'm SoWwWwyyy..."
    f "{i}*hic!*{/i}" with vpunch
    f "EheEheehii!"
    mx "Oof! Your breath..."
    mx "How much did you drink tonight?"
    f "Heeheehee! A lOt, I gUesS..?"

    scene 01_nightvisitroom_dress_04
    with dissolve

    mx "Okay. Let's go back to your room alright, Fiona."
    f "EhEhe... YoU'rE ReaAlly hAndSome lIke hiM yA knOW?"
    f "SoMetImeS I fOrGet thAt You'Re nOt HiM..."
    f "iT'sS sOo..."
    f "sO..."
    mx "So?"
    f "SoOo..."

    $ renpy.music.stop(channel='music2')

    scene black
    with vpunch

    f "{i}*bleurgh!*{/i}"
    mx "! ! !"
    mx "Ugh! Fiona..!"

    show text "A few minutes later..." at truecenter with fade

    pause

    scene 01_nightvisitroom_dress_08
    with fade

    if notification_songs == True:
        $ renpy.notify("dvdkm - lonely")

    $ renpy.music.play("music/dvdkm-lonely.mp3", channel='music2', fadein=1, loop=True)

    mx "I've cleaned up the mess."
    f "Oh my god!"
    f "That was...{i}*hic*{/i}! {w}...embarassing!" with vpunch
    mx "Well, atleast you've sobered up quite a bit."
    f "T-Thanks for the help, [mx]."
    mx "No problem. \nPartied quite hard at the reunion, huh?"

    scene 01_nightvisitroom_dress_10
    with dissolve

    f "No. Not exactly..."
    mx "Hm?"
    mx "What exactly happened at the reunion?"
    f "Someone from the past happened..."
    mx "Someone? From the past?"

    scene 01_nightvisitroom_dress_09
    with dissolve

    f "I'm sure you've noticed by now that Prii's father is not around?"
    mx "Yeah. I thought prying into something personal like that is rude."
    f "It's okay, you're family now. I think you should know it from me rather than from somebody else."

    scene 01_nightvisitroom_dress_10
    with dissolve

    f "Let's see... It's been 10 years since we separated."
    mx "And you met him at the reunion?"
    f "....Yeah."
    f "Me, Maria, Al, and... {p} Oliver."
    f "The four of us were friends since freshmen year of college. He was friends with Al while me and Maria were roommates."
    f "Your dad and me go way back so through the two of us, we just gradually clicked as a group."
    f "We felt like some gang out of a sitcom. Doing stupid stuff here and there like most college kids in those days."

    scene 01_nightvisitroom_dress_07
    with dissolve

    f "Until..."
    mx "Hm?"
    f "Maria got pregnant with you."
    f "They were forced to be adults before even reaching the age of 20."

    scene 01_nightvisitroom_dress_09
    with dissolve

    f "It was also funny seeing them making a mess of themselves taking care of you..."
    f "I also helped taking care of you, you know?"
    mx "Oh? T-Thanks?"
    f "Hehehe..."
    f "Atleast that experience helped me raise Prii..."
    f "As for me and Olly..."
    f "We just gradually... ended up with each other, I guess?"

    scene 01_nightvisitroom_dress_10
    with dissolve

    f "{i}\"He was sweet, funny, a man you could never go wrong with.\"{/i}"
    f "That we'll grow old together and have a happy ever after like something out of a movie."
    f "Those were my thoughts at that time."
    f "But reality is really cruel, you know?"
    f "It started—"

    $ renpy.music.stop(channel='music2')

    "(This feeling!!)"

    play sound "soundfx/glitch.ogg"

    show dress_glitch

    "(A glitch!)"
    "(Then another one of... those...)"

    jump ep2_fquest_drunkenvisit_fiona_memory

label ep2_fquest_drunkenvisit_dress_path_cont:

    play sound "soundfx/glitch.ogg"

    show dress_glitch

    f "FSxsr....We...dont..need......()0da31"
    f "vZ31x.......man...in..our.......*R3=1"
    f "540fd.......lives........*3dTGf"

    scene black
    with fade

    pause 0.2

    hide all
    stop sound

    scene 01_nightvisitroom_dress_07
    with fade

    "(Urgh!)" with vpunch
    "(Damn. That memory was pretty heavy.)"
    "(I can still recall the lingering pain that she felt.)"
    "(This \"memory dive\" or something is powerful stuff.)"

    if notification_songs == True:
        $ renpy.notify("dvdkm - lonely")

    $ renpy.music.play("music/dvdkm-lonely.mp3", channel='music2', fadein=1, loop=True)

    f "...and after that I just closed myself away. \nMy only focus then was raising Prii."
    f "But in my despair, I was deeply afraid of her turning into someone like me."
    f "That I just forbade her from interacting with boys and only enrolled her in all-girls schools just to protect her."

    scene 01_nightvisitroom_dress_05
    with dissolve

    f "I just didn't want to let her experience that pain, you know? The pain of your heart breaking..."
    mx "Fiona..."
    f "Looking back on it, it was an idiotic, No. {p} ....A very {i}very{/i} stupid idea."
    f "Prii grew up naive in the matters regarding guys that I'm afraid she'll end up worse than me but..."

    scene 01_nightvisitroom_dress_06
    with dissolve

    f "Thankfully, you're here."
    mx "Me?"
    f "She looks up to you like an older brother."
    f "Meeting Oliver there just brought a lot of memories from the past."

    scene 01_nightvisitroom_dress_07
    with dissolve

    f "Especially when I saw him and his partner."
    mx "Was it because of that you started drinking tonight?"
    f "Partly..."
    mx "Partly?"

    scene 01_nightvisitroom_dress_10
    with dissolve

    f "What Oliver did was extremely painful but time heals all wounds, dear..."
    f "It still hurts but I've already forgiven him."
    f "It's the fact that in those years..."
    f "I didn't move on."
    mx "What do you mean?"

    scene 01_nightvisitroom_dress_09
    with dissolve

    f "Well, I just realized that tonight."
    f "You know... this attire you chose attracted a lot of eyes on me?"
    mx "Well, yeah. I'm the foremost expert in women's clothing, as they say."
    f "Ehehehe.... don't let it get in over your head."
    f "I was just a bit in the limelight tonight."
    f "Catching up with old friends and classmates. I saw Brittany too staring at me coldy."
    mx "It seemed you had a good time."

    scene 01_nightvisitroom_dress_10
    with dissolve

    f "I did. \nIt was when everything settled down that I saw the reality of my life."
    f "As the night went on, I saw them go back to their spouses. Even Britanny with her sour face was happily smiling with her husband."
    f "It was then and there that it dawned on me how alone I was."
    f "I was so focused on not experiencing another heartbreak that I forgot how being in love felt."

    scene 01_nightvisitroom_dress_08
    with dissolve

    f "Ugh! {p} I was so miserable there that I ended up leaving before the event ended." with vpunch
    f "I went to a convenience store nearby and bought myself a bottle of whiskey and ended up in this state."
    f "And you know who found me there?"
    mx "Who?"
    f "Brittany!" with vpunch
    f "She and her husband helped and drove me here. \nShe comforted me that she heard about my divorce with Olly years ago."
    f "She thought that seeing him there must be the reason I was drinking."
    f "She was... {i}*sniff*{/i}! {p} ...really nice."
    mx "Oh..? {p} Ahahaha!"

    scene 01_nightvisitroom_dress_09a
    with vpunch

    f "H-Hey! It's not funny! \nA lady's telling you her problems, you meanie!"
    mx "I know."
    f "{i}*sniff*{/i}"
    mx "C'mon, what're you really afraid of?"
    f "I-It's just that..."

    scene 01_nightvisitroom_dress_08
    with dissolve

    f "I'll grow old, alone, and ugly."
    f "That no one will... {p} ...love me."
    mx "So, you're insecure about that?"
    f "O-Of course..."

    scene 01_nightvisitroom_dress_09a
    with dissolve

    mx "You know, being alone isn't that bad, you know?"
    f "Is that suppose to make me feel better?"
    mx "Hahaha! No, not exactly."
    mx "You see..."

    $ renpy.music.stop(channel='music2', fadeout=2)

    scene h_10
    with fade

    mx "I've felt that crushing feeling of loneliness before."
    mx "It's easy to lose in the fantasy that if you have someone beside you then that loneliness will go away."

    scene 01_nightvisitroom_dress_11
    with dissolve

    $ renpy.music.play("music/elijahwho-crush on you.mp3", channel='music2', loop=True)

    mx "But it's gonna be much lonelier if you settle for someone out of desperation and find out their true colors in the end."
    mx "Feeling lonely even if there's someone beside you."

    if notification_songs == True:
        $ renpy.notify("elijah who - crush on you")

    scene 01_nightvisitroom_dress_09a
    with dissolve

    f "{i}*sniff*{/i}"
    f "Since when did you become a such a romantic?"
    mx "Uh... umm... being amnesiac does things to you."
    mx "Besides, who wouldn't fall in love with you?"
    f "T-That's a lie..."

    scene 01_nightvisitroom_dress_11
    with dissolve

    mx "No, seriously!"
    mx "I admit that my stay here hasn't been that long..."
    mx "But in that time, I realize you're smart, funny, and a very caring woman..."
    f "..."
    mx "You're an amazing woman, Fiona. \nYou'll find the right one for you someday."
    f "What if maybe... just maybe... {p} ...that I don't?"
    f "What if they find me ugly or—"
    mx "Fiona, most people don't love someone because they're perfect but because they know they're not and they still loved them regardless."

    scene 01_nightvisitroom_dress_09
    with dissolve

    f "Really..?"
    mx "The thing is that after all these years, you saw yourself as something of no value but that's far from the case."
    mx "You know, Rubies are special because they're rare and one-of-a-kind. \nIt also means they're lonely too."

    scene 01_nightvisitroom_dress_11
    with dissolve

    mx "All great and precious things are. \nYou're just forgetting that you're special too."
    f "[mx]..."
    mx "I can't promise that \"the one\" will arrive tomorrow or whatnot..."

    scene 01_nightvisitroom_dress_12
    with dissolve

    mx "But I can promise you that I'll be here for you till he comes so you don't feel alone anymore."
    mx "Well, it's because I don't have any place to stay, really."
    f "Ehehehe... [mx]..."
    f "You idiot, I.."
    f "Why are you saying such things to me I.. I can't..."
    mx "Well, umm..."

    scene 01_nightvisitroom_dress_13
    with dissolve

    $ renpy.music.stop(channel='music2', fadeout=2)

    f "{i}*deep inhale*{/i}"
    mx "A-Are you alright?"
    f "Dammit, [mx]!"
    f "I'm sorry for this."
    mx "Sorry for—"

    jump ep2_fquest_drunkenvisit_dress_path_lovescene

label ep2_fquest_drunkenvisit_dress_path_lovescene:

    if notification_songs == True:
        $ renpy.notify("BROCKBEATS - magic spell")

    $ renpy.music.play("music/BROCKBEATS-magic spell.mp3", channel='music2', fadein=5, loop=True)


    scene 01_nightvisitroom_dress_14
    with dissolve

    mx "!!!" with vpunch
    f "Mhm..."
    mx "Mhmpph..."
    f "Mhrm.. hmmm..."

    scene 01_nightvisitroom_dress_15
    with dissolve

    mx "F-Fiona..."
    "(She's quite aggressive!)"
    f "Mhrmmm..."
    f "Haa.. ha... mhmm.. {i}*slurp*{/i}!" with vpunch
    "(What the.. tongue?)"
    f "Mhrmm... haa.. ha... mhmrm!"
    f "[mx]..."
    f "Kiss me more..."
    f "Mhmmm!"
    "(Shit! I'm getting a hard!)"
    f "!?!" with vpunch
    f "This is..."

    scene 01_nightvisitroom_dress_16
    with dissolve

    f "Ehehehe... You're getting hard."
    mx "I can't stop it after that... kiss."
    f "It's been far too long..."
    f "...since I've been initmate with someone."
    f "[mx]..."
    f "I..I want you to..."
    f "Wait..."

    scene 01_nightvisitroom_dress_17
    with dissolve

    mx "Fiona?"
    f "I want to show you..."
    mx "Hm?"
    "(What is she...?)"

    scene 01_nightvisitroom_dress_18
    with dissolve

    mx "{i}*gulp*{/i}" with vpunch
    mx "Wow..."
    f "I know you've already seen me so it's not much of a shock..."
    mx "N-No... you look absolutely amazing."
    f "[mx]..."

    scene 01_nightvisitroom_dress_19
    with dissolve

    f "[mx].."
    f "[mx]..."
    f "I want you..!"
    mx "Mhrmmph.."
    f "I want you so badly!" with vpunch
    f "Mhmm..ha..!"
    f "Haa..ah..haa!"
    mx "!!!"
    f "I want you to... touch me."
    f "Hold me closer..."



    f "Make me feel like a woman again, [mx]..."
    f "I want you, [mx]..."
    mx "What are you—"

    scene 01_nightvisitroom_dress_20
    with dissolve

    window hide

    pause

    mx "UGH!!" with vpunch
    mx "F-Fiona!"
    f "Ehehe..."
    "(Fuck! Her hands are...)"
    mx "Haaa.. haa..."
    f "I've never realized yours was this big..."
    f "It's so... good looking..."

    scene 01_nightvisitroom_dress_21
    with dissolve

    window hide

    pause

    mx "URK!" with vpunch
    f "D-Does it feel good, [mx]?"
    mx "Y-Yeah..."
    "(Damn! This feels waaayy too good!)"
    f "I've never done this to anyone before..."
    f "But I heard from my clients that guys love this..."
    mx "F-Fiona, s-slow down a bit..."
    mx "URGHH!!" with vpunch

    scene 01_nightvisitroom_dress_22
    with dissolve

    window hide

    pause

    f "{i}*slurp*{/i}"
    mx "GUUHHHHH!!" with vpunch
    "(Fuck!Fuck!Fuck!Fuck!)"
    "(Her tongue wrapping unto my dick like that...)"
    mx "AHHMMM!!"
    f "Mhmmpphh!!"
    f "Hnnnhnn!!"
    mx "F-F-Fiona, if you do that I'll—"
    f "!!!"

    scene 01_nightvisitroom_dress_22
    with flash

    pause 0.3

    scene 01_nightvisitroom_dress_22
    with flash

    pause 0.3

    scene 01_nightvisitroom_dress_23
    with dissolve

    mx "Haaa... haa... haa.."
    "(Fu..ck...it.. feels...so...good...)"
    f "{i}*gulp*{/i}" with vpunch
    f "Haaaa..."
    f "S-So bitter and salty..."
    f "But hearing your voice moaning was turning me so much on..."
    f "I hope you're ready for another round..."
    "(Another round!?)"

    scene 01_nightvisitroom_dress_24
    with dissolve

    f "Haa... haaah..."
    mx "Fiona? Are you okay?"
    mx "You're wobbling a bit?"
    f "I'm so.. excited.."
    f "It's just... it's been so long.."
    f "I want you inside me, [mx]..."
    mx "{i}*Gulp*{/i}!"
    mx "I-Inside you?"
    "(Fuck! This it!)"
    f "I.. I want to..."
    f "!!!"
    mx "Fiona? Your—"

    $ renpy.music.stop(channel='music2', fadeout=2)

    scene 01_nightvisitroom_dress_25
    with vpunch

    f "Oh no—"
    mx "Watch out!"
    $ renpy.end_replay()
    play sound "soundfx/falling_thud.ogg"

    scene black
    with flash

    $ renpy.pause(2, hard = True)

    scene 02_morningafter_dress_01
    with slowfade

    if notification_songs == True:
        $ renpy.notify("E66S - beachside")

    $ renpy.music.play("music/E66S-beachside.mp3", channel='music2', fadein=1, loop=True)

    window hide

    pause

    "..."
    "...."
    f "Hrm..."
    f "Urgh... ugh... my head..."

    scene 02_morningafter_dress_02
    with dissolve

    f "Owww... my head."
    f "It hurts... like... hell..."
    f "I drank again.. didn't...I?"
    f "What time... is it? \nI better prepare... break...fast.... hrmm?"
    f "This pillow... feels weird..."
    f "Why does it feel... warm... and...?"
    f "...muscular?"
    f "!!!" with vpunch

    scene 01_nightvisitroom_dress_21
    with flash

    pause 0.2

    scene 01_nightvisitroom_dress_22
    with flash

    pause 0.2

    scene 01_nightvisitroom_dress_23
    with flash

    pause 0.2

    scene 02_morningafter_dress_03
    with vpunch

    f "No!No!No! L-L-Last night we—!"
    f "Urgh! My head! \nI can't remember what happened afterwards!" with vpunch
    f "Did I... Did I have sex... with my... bestfriends' son."
    f "Oh my God! Oh my God! Oh my God!" with vpunch
    f "This is so immoral! What will people think!?"
    f "[mx]..."
    f "He's like a son to me and I..."

    scene 02_morningafter_mc
    with dissolve

    mx "Uh... hrm..."
    mx "Uhh... what time is it..?"
    mx "F-Fiona? Why are you in my room..?"
    f "[mx]..."
    f "It's the opposite, you're in mine."
    mx "What? Your room? I... {p}Oh.. Oh yeah."
    mx "Last night... \n...then what happened was not a dream."
    f "Y-Yeah..."
    f "Let's talk for a bit..."

    scene 02_morningafter_dress_04
    with fade

    f "What happened was..."
    f "It was a mistake. I shouldn't have..."
    mx "No, no. It was my fault too that I..."

    scene 02_morningafter_dress_05
    with dissolve

    f "You shouldn't blame yourself, dear. \nNo matter how you look at it, it was on me."
    f "I shouldn't have gotten drunk like an idiot last night."
    f "And went into your room and made a mess..."
    f "And then... {p} ...came on you aggressively."
    mx "..."
    f "{i}*sigh*{/i}"

    scene 02_morningafter_dress_06
    with dissolve

    f "I want to say more but can we..."
    mx "Hm?"

    scene 02_morningafter_dress_04
    with dissolve

    f "Can we... dress up first?"
    f "Being nude like this is..."
    mx "Ah!.. Y-Y-Yeah! Right!"
    f "Your clothes are over there."
    mx "T-Thanks.."

    scene black
    with fade

    show text "A few minutes later..." with fade

    pause

    jump ep2_fquest_drunkenvisit_morningafter_end




label ep2_fquest_drunkenvisit_sweater_path:

    scene 01_nightvisitroom_sweater_01
    with dissolve

    mx "HHYYYAAAAA...aah..."

    if notification_songs == True:
        $ renpy.notify("PerroFunky - C L O S E Y O U R E Y E S")

    $ renpy.music.play("music/perrofunky-closeyoureyes.mp3", channel='music2', fadein=1, loop=True)

    f "{i}*hic!*{/i}" with vpunch
    f "wWwhy i-Is t-thiis... dOorlocKed?"
    f "{i}*hic!*{/i}" with vpunch
    f "OhH... it'S opEn NoOW.."
    mx "Fiona?"
    f "HhmMm..?"

    scene 01_nightvisitroom_sweater_02
    with dissolve

    f "[mx]? wHhat Aare yOu doInG hEere...?"
    mx "You're letting me stay here, remember?"
    mx "Wait. {p} You're wasted."
    f "{i}*hic!*{/i}" with vpunch
    f "NnNooOo I'Mm noOtt... ehEheehe..."
    f "jUsSt TiippPsSsyY..."
    mx "Yeah right."
    f "I fOrgOt YoU'rE StaYing hEre. ThEn I-I'lL jUsSst..."
    mx "Woah! Watch your step!"

    scene 01_nightvisitroom_sweater_03
    with vpunch

    f "I'm SoWwWwyyy..."
    f "{i}*hic!*{/i}" with vpunch
    f "EheEheehii!"
    mx "Oof! Your breath..."
    mx "How much did you drink tonight?"
    f "Heeheehee! A lOt, I gUesS..?"

    scene 01_nightvisitroom_sweater_04
    with dissolve

    mx "Okay. Let's go back to your room alright, Fiona."
    f "EhEhe... YoU'rE ReaAlly hAndSome lIke hiM yA knOW?"
    f "SoMetImeS I fOrGet thAt You'Re nOt HiM..."
    f "iT'sS sOo..."
    f "sO..."
    mx "So?"
    f "SoOo..."

    $ renpy.music.stop(channel='music2')

    scene black
    with vpunch

    f "{i}*bleurgh!*{/i}"
    mx "! ! !"
    mx "Ugh! Fiona..!"

    show text "A few minutes later..." at truecenter with fade

    pause

    scene 01_nightvisitroom_sweater_08
    with fade

    if notification_songs == True:
        $ renpy.notify("dvdkm - lonely")

    $ renpy.music.play("music/dvdkm-lonely.mp3", channel='music2', fadein=1, loop=True)

    mx "I've cleaned up the mess."
    f "Oh my god!"
    f "That was...{i}*hic*{/i}! {w}...embarassing!" with vpunch
    mx "Well, atleast you've sobered up quite a bit."
    f "T-Thanks for the help, [mx]."
    mx "No problem. \nPartied quite hard at the reunion, huh?"

    scene 01_nightvisitroom_sweater_10
    with dissolve

    f "No. Not exactly..."
    mx "Hm?"
    mx "What exactly happened at the reunion?"
    f "Someone from the past happened..."
    mx "Someone? From the past?"

    scene 01_nightvisitroom_sweater_09
    with dissolve

    f "I'm sure you've noticed by now that Prii's father is not around?"
    mx "Yeah. I thought prying into something personal like that is rude."
    f "It's okay, you're family now. I think you should know it from me rather than from somebody else."

    scene 01_nightvisitroom_sweater_10
    with dissolve

    f "Let's see... It's been 10 years since we separated."
    mx "And you met him at the reunion?"
    f "....Yeah."
    f "Me, Maria, Al, and... {p} Oliver."
    f "The four of us were friends since freshmen year of college. He was friends with Al while me and Maria were roommates."
    f "Your dad and me go way back so through the two of us, we just gradually clicked as a group."
    f "We felt like some gang out of a sitcom. Doing stupid stuff here and there like most college kids in those days."

    scene 01_nightvisitroom_sweater_07
    with dissolve

    f "Until..."
    mx "Hm?"
    f "Maria got pregnant with you."
    f "They were forced to be adults before even reaching the age of 20."

    scene 01_nightvisitroom_sweater_09
    with dissolve

    f "It was also funny seeing them making a mess of themselves taking care of you..."
    f "I also helped taking care of you, you know?"
    mx "Oh? T-Thanks?"
    f "Hehehe..."
    f "Atleast that experience helped me raise Prii..."
    f "As for me and Olly..."
    f "We just gradually... ended up with each other, I guess?"

    scene 01_nightvisitroom_sweater_10
    with dissolve

    f "{i}\"He was sweet, funny, a man you could never go wrong with.\"{/i}"
    f "That we'll grow old together and have a happy ever after like something out of a movie."
    f "Those were my thoughts at that time."
    f "But reality is really cruel, you know?"
    f "It started—"

    $ renpy.music.stop(channel='music2')

    "(This feeling!!)"

    play sound "soundfx/glitch.ogg"

    show sweater_glitch

    "(A glitch!)"
    "(Then another one of... those...)"

    jump ep2_fquest_drunkenvisit_fiona_memory

label ep2_fquest_drunkenvisit_sweater_path_cont:

    play sound "soundfx/glitch.ogg"

    show sweater_glitch

    f "FSxsr....We...dont..need......()0da31"
    f "vZ31x.......man...in..our.......*R3=1"
    f "540fd.......lives........*3dTGf"

    scene black
    with fade

    pause 0.2

    hide all
    stop sound

    scene 01_nightvisitroom_sweater_07
    with fade

    "(Urgh!)" with vpunch
    "(Damn. That memory was pretty heavy.)"
    "(I can still recall the lingering pain that she felt.)"
    "(This \"memory dive\" or something is powerful stuff.)"

    if notification_songs == True:
        $ renpy.notify("dvdkm - lonely")

    $ renpy.music.play("music/dvdkm-lonely.mp3", channel='music2', fadein=1, loop=True)

    f "...and after that I just closed myself away. \nMy only focus then was raising Prii."
    f "But in my despair, I was deeply afraid of her turning into someone like me."
    f "That I just forbade her from interacting with boys and only enrolled her in all-girls schools just to protect her."

    scene 01_nightvisitroom_sweater_05
    with dissolve

    f "I just didn't want to let her experience that pain, you know? The pain of your heart breaking..."
    mx "Fiona..."
    f "Looking back on it, it was an idiotic, No. {p} ....A very {i}very{/i} stupid idea."
    f "Prii grew up naive in the matters regarding guys that I'm afraid she'll end up worse than me but..."

    scene 01_nightvisitroom_sweater_06
    with dissolve

    f "Thankfully, you're here."
    mx "Me?"
    f "She looks up to you like an older brother."
    f "Meeting Oliver there just brought a lot of memories from the past."

    scene 01_nightvisitroom_sweater_07
    with dissolve

    f "Especially when I saw him and his partner."
    mx "Was it because of that you started drinking tonight?"
    f "Partly..."
    mx "Partly?"

    scene 01_nightvisitroom_sweater_10
    with dissolve

    f "What Oliver did was extremely painful but time heals all wounds, dear..."
    f "It still hurts but I've already forgiven him."
    f "It's the fact that in those years..."
    f "I didn't move on."
    mx "What do you mean?"

    scene 01_nightvisitroom_sweater_09
    with dissolve

    f "Well, I just realized that tonight."
    f "You know... this attire you chose attracted a lot of eyes on me?"
    mx "Well, yeah. I'm the foremost expert in women's clothing, as they say."
    f "Ehehehe.... don't let it get in over your head."
    f "I was just a bit in the limelight tonight."
    f "Catching up with old friends and classmates. I saw Brittany too staring at me coldy."
    mx "It seemed you had a good time."

    scene 01_nightvisitroom_sweater_10
    with dissolve

    f "I did. \nIt was when everything settled down that I saw the reality of my life."
    f "As the night went on, I saw them go back to their spouses. Even Britanny with her sour face was happily smiling with her husband."
    f "It was then and there that it dawned on me how alone I was."
    f "I was so focused on not experiencing another heartbreak that I forgot how being in love felt."

    scene 01_nightvisitroom_sweater_08
    with dissolve

    f "Ugh! {p} I was so miserable there that I ended up leaving before the event ended." with vpunch
    f "I went to a convenience store nearby and bought myself a bottle of whiskey and ended up in this state."
    f "And you know who found me there?"
    mx "Who?"
    f "Brittany!" with vpunch
    f "She and her husband helped and drove me here. \nShe comforted me that she heard about my divorce with Olly years ago."
    f "She thought that seeing him there must be the reason I was drinking."
    f "She was... {i}*sniff*{/i}! {p} ...really nice."
    mx "Oh..? {p} Ahahaha!"

    scene 01_nightvisitroom_sweater_09a
    with vpunch

    f "H-Hey! It's not funny! \nA lady's telling you her problems, you meanie!"
    mx "I know."
    f "{i}*sniff*{/i}"
    mx "C'mon, what're you really afraid of?"
    f "I-It's just that..."

    scene 01_nightvisitroom_sweater_08
    with dissolve

    f "I'll grow old, alone, and ugly."
    f "That no one will... {p} ...love me."
    mx "So, you're insecure about that?"
    f "O-Of course..."

    scene 01_nightvisitroom_sweater_09a
    with dissolve

    mx "You know, being alone isn't that bad, you know?"
    f "Is that suppose to make me feel better?"
    mx "Hahaha! No, not exactly."
    mx "You see..."

    $ renpy.music.stop(channel='music2', fadeout=2)

    scene h_10
    with fade

    mx "I've felt that crushing feeling of loneliness before."
    mx "It's easy to lose in the fantasy that if you have someone beside you then that loneliness will go away."

    scene 01_nightvisitroom_sweater_11
    with dissolve

    $ renpy.music.play("music/elijahwho-crush on you.mp3", channel='music2', loop=True)

    mx "But it's gonna be much lonelier if you settle for someone out of desperation and find out their true colors in the end."
    mx "Feeling lonely even if there's someone beside you."

    if notification_songs == True:
        $ renpy.notify("elijah who - crush on you")

    scene 01_nightvisitroom_sweater_09a
    with dissolve

    f "{i}*sniff*{/i}"
    f "Since when did you become a such a romantic?"
    mx "Uh... umm... being amnesiac does things to you."
    mx "Besides, who wouldn't fall in love with you?"
    f "T-That's a lie..."

    scene 01_nightvisitroom_sweater_11
    with dissolve

    mx "No, seriously!"
    mx "I admit that my stay here hasn't been that long..."
    mx "But in that time, I realize you're smart, funny, and a very caring woman..."
    f "..."
    mx "You're an amazing woman, Fiona. \nYou'll find the right one for you someday."
    f "What if maybe... just maybe... {p} ...that I don't?"
    f "What if they find me ugly or—"
    mx "Fiona, most people don't love someone because they're perfect but because they know they're not and they still loved them regardless."

    scene 01_nightvisitroom_sweater_09
    with dissolve

    f "Really..?"
    mx "The thing is that after all these years, you saw yourself as something of no value but that's far from the case."
    mx "You know, Rubies are special because they're rare and one-of-a-kind. \nIt also means they're lonely too."

    scene 01_nightvisitroom_sweater_11
    with dissolve

    mx "All great and precious things are. \nYou're just forgetting that you're special too."
    f "[mx]..."
    mx "I can't promise that \"the one\" will arrive tomorrow or whatnot..."

    scene 01_nightvisitroom_sweater_12
    with dissolve

    mx "But I can promise you that I'll be here for you till he comes so you don't feel alone anymore."
    mx "Well, it's because I don't have any place to stay, really."
    f "Ehehehe... [mx]..."
    f "You idiot, I.."
    f "Why are you saying such things to me I.. I can't..."
    mx "Well, umm..."

    scene 01_nightvisitroom_sweater_13
    with dissolve

    $ renpy.music.stop(channel='music2', fadeout=2)

    f "{i}*deep inhale*{/i}"
    mx "A-Are you alright?"
    f "Dammit, [mx]!"
    f "I'm sorry for this."
    mx "Sorry for—"

    jump ep2_fquest_drunkenvisit_sweater_path_lovescene

label ep2_fquest_drunkenvisit_sweater_path_lovescene:

    if notification_songs == True:
        $ renpy.notify("BROCKBEATS - magic spell")

    $ renpy.music.play("music/BROCKBEATS-magic spell.mp3", channel='music2', fadein=5, loop=True)


    scene 01_nightvisitroom_sweater_14
    with dissolve

    mx "!!!" with vpunch
    f "Mhm..."
    mx "Mhmpph..."
    f "Mhrm.. hmmm..."

    scene 01_nightvisitroom_sweater_15
    with dissolve

    mx "F-Fiona..."
    "(She's quite aggressive!)"
    f "Mhrmmm..."
    f "Haa.. ha... mhmm.. {i}*slurp*{/i}!" with vpunch
    "(What the.. tongue?)"
    f "Mhrmm... haa.. ha... mhmrm!"
    f "[mx]..."
    f "Kiss me more..."
    f "Mhmmm!"
    "(Shit! I'm getting a hard!)"
    f "!?!" with vpunch
    f "This is..."

    scene 01_nightvisitroom_sweater_16
    with dissolve

    f "Ehehehe... You're getting hard."
    mx "I can't stop it after that... kiss."
    f "It's been far too long..."
    f "...since I've been initmate with someone."
    f "[mx]..."
    f "I..I want you to..."
    f "Wait..."

    scene 01_nightvisitroom_sweater_17
    with dissolve

    mx "Fiona?"
    f "I want to show you..."
    mx "Hm?"
    "(What is she...?)"

    scene 01_nightvisitroom_sweater_18
    with dissolve

    mx "{i}*gulp*{/i}" with vpunch
    mx "Wow..."
    f "I know you've already seen me so it's not much of a shock..."
    mx "N-No... you look absolutely amazing."
    f "[mx]..."

    scene 01_nightvisitroom_sweater_19
    with dissolve

    f "[mx].."
    f "[mx]..."
    f "I want you..!"
    mx "Mhrmmph.."
    f "I want you so badly!" with vpunch
    f "Mhmm..ha..!"
    f "Haa..ah..haa!"
    mx "!!!"
    f "I want you to... touch me."
    f "Hold me closer..."



    f "Make me feel like a woman again, [mx]..."
    mx "Well, let's make you feel good."
    f "What do you mea—"

    scene 01_nightvisitroom_sweater_20
    with dissolve

    window hide

    pause

    f "{i}HHIIIINNN!!!{/i}" with vpunch
    f "AAAHHHNNNN!!" with vpunch
    f "[mx]! No! Thats—"
    f "AAAAHHHHHHH! OHGOD!OHGOD!OHGOD!" with vpunch
    f "UUUUUNNNNGGHHH!"
    f "FUCK! IT'S SO GOOOOD!!!"
    "(Her moans are so damn erotic!)"
    "(I should...)"

    scene 01_nightvisitroom_sweater_21
    with dissolve

    window hide

    pause

    f "You're... haaa... tongue is... haa..."
    f "HNNGGG!" with vpunch
    f "That's—!!!"
    f "There!There!There!THERE!" with vpunch
    f "Haa..hah..haa....ahn!"
    f "[mx]?"
    mx "Fiona, I want a better view of you."

    scene 01_nightvisitroom_sweater_22
    with dissolve

    window hide

    pause 0.3

    f "NOOOO! Thats—"
    mx "Damn... Your pussy looks delicious."
    f "Stop looking! It's embarassing!"
    mx "It's beautiful. This little one's pretty cute too."
    f "HHYAAAA! UUNNGGG!! No, not my clit—"
    f "AAAHHHIIIIIIIII!!!" with vpunch
    f "You big lug! Don't! If you do.."
    f "Then, I'll...!"
    mx "Woah!" with vpunch
    "(Damn!)"
    "(She's stroking my cock vigorously while lifted up like this.)"
    f "OHMYGOD! I'mmmm... I'm cu-cum-cumming!" with vpunch
    mx "Fiona! If you stroke it much faster I'll..."
    f "MY FACE!"
    mx "What?"

    scene 01_nightvisitroom_sweater_23
    with dissolve

    f "Put it on my face!"
    mx "F-Fiona..!"
    f "[mx], cum on me..."
    "(Fuck! Her hands are...!)"
    mx "GUH!"

    scene 01_nightvisitroom_sweater_23
    with flash

    pause 0.2

    scene 01_nightvisitroom_sweater_23
    with flash

    pause 0.2

    scene 01_nightvisitroom_sweater_24
    with dissolve

    f "!!!" with vpunch
    f "Mwah.. ah... {i}*gulp*{/i}!"
    f "Mhm.. waah... so bitter.."
    mx "Uggh... haaa..."
    mx "Fuck... that was amazing."
    f "I hope you can go for another round..."
    "(Another round?)"

    scene 01_nightvisitroom_sweater_25
    with dissolve

    f "Haa... haaah..."
    mx "Fiona? Are you okay?"
    mx "You're wobbling a bit?"
    f "I'm so.. excited.."
    f "It's just... it's been so long.."
    f "I want you inside me, [mx]..."
    mx "{i}*Gulp*{/i}!"
    mx "I-Inside you?"
    "(Fuck! This it!)"
    f "I.. I want to..."
    f "!!!"
    mx "Fiona? Your—"

    $ renpy.music.stop(channel='music2', fadeout=2)

    scene 01_nightvisitroom_sweater_26
    with vpunch

    f "Oh no—"
    mx "Watch out!"
    $ renpy.end_replay()
    play sound "soundfx/falling_thud.ogg"

    scene black
    with flash

    $ renpy.pause(2, hard = True)

    scene 02_morningafter_sweater_01
    with slowfade

    if notification_songs == True:
        $ renpy.notify("E66S - beachside")

    $ renpy.music.play("music/E66S-beachside.mp3", channel='music2', fadein=1, loop=True)

    window hide

    pause

    "..."
    "...."
    f "Hrm..."
    f "Urgh... ugh... my head..."

    scene 02_morningafter_sweater_02
    with dissolve

    f "Owww... my head."
    f "It hurts... like... hell..."
    f "I drank again.. didn't...I?"
    f "What time... is it? \nI better prepare... break...fast.... hrmm?"
    f "This pillow... feels weird..."
    f "Why does it feel... warm... and...?"
    f "...muscular?"
    f "!!!" with vpunch

    scene 01_nightvisitroom_sweater_20
    with flash

    pause 0.2

    scene 01_nightvisitroom_sweater_22
    with flash

    pause 0.2

    scene 01_nightvisitroom_sweater_24
    with flash

    pause 0.2

    scene 02_morningafter_sweater_03
    with vpunch

    f "No!No!No! L-L-Last night we—!"
    f "Urgh! My head! \nI can't remember what happened afterwards!" with vpunch
    f "Did I... Did I have sex... with my... bestfriends' son."
    f "Oh my God! Oh my God! Oh my God!" with vpunch
    f "This is so immoral! What will people think!?"
    f "[mx]..."
    f "He's like a son to me and I..."

    scene 02_morningafter_mc
    with dissolve

    mx "Uh... hrm..."
    mx "Uhh... what time is it..?"
    mx "F-Fiona? Why are you in my room..?"
    f "[mx]..."
    f "It's the opposite, you're in mine."
    mx "What? Your room? I... {p}Oh.. Oh yeah."
    mx "Last night... \n...then what happened was not a dream."
    f "Y-Yeah..."
    f "Let's talk for a bit..."

    scene 02_morningafter_sweater_04
    with fade

    f "What happened was..."
    f "It was a mistake. I shouldn't have..."
    mx "No, no. It was my fault too that I..."

    scene 02_morningafter_sweater_05
    with dissolve

    f "You shouldn't blame yourself, dear. \nNo matter how you look at it, it was on me."
    f "I shouldn't have gotten drunk like an idiot last night."
    f "And went into your room and made a mess..."
    f "And then... {p} ...came on you aggressively."
    mx "..."
    f "{i}*sigh*{/i}"

    scene 02_morningafter_sweater_06
    with dissolve

    f "I want to say more but can we..."
    mx "Hm?"

    scene 02_morningafter_sweater_04
    with dissolve

    f "Can we... dress up first?"
    f "Being nude like this is..."
    mx "Ah!.. Y-Y-Yeah! Right!"
    f "Your clothes are over there."
    mx "T-Thanks.."

    scene black
    with fade

    show text "A few minutes later..." with fade

    pause

    jump ep2_fquest_drunkenvisit_morningafter_end

label ep2_fquest_drunkenvisit_morningafter_end:

    scene 03_morningafterleave_01
    with slowfade

    f "..."
    mx "..."
    f "Um..."
    f "What I want to say is..."

    scene 03_morningafterleave_02
    with dissolve

    f "About last night..."
    f "Let's just... forget everything, alright?"
    f "As if all those that happened were just a dream."

    scene 03_morningafterleave_03
    with dissolve

    "(Can we just easily forget things like that, Fiona?)"
    "({i}*sigh*{/i})"
    mx "I understand."
    f "We're... You're part of our family now."
    f "I'm like a mother to you. \nDoing things like those isn't..."

    scene 03_morningafterleave_04
    with dissolve

    mx "It's alright. \nIt was an accident."
    mx "It's not something that I'll go blabbering about to anyone anyways."
    f "Y-Yeah... you're right."
    f "So..."
    f "If you don't mind..."
    mx "I need to leave, right?"

    scene 03_morningafterleave_02
    with dissolve

    f "{i}*nods*{/i} {p} Before Prii sees us."
    mx "Well, before I go and put everything that happened behind us..."
    f "...?"
    mx "I just want you to remember the things I told you last night."
    mx "You still have Prii and, well, me. \nYou aren't alone, Fiona."
    f "Yeah. {p} I'll always cherish those words, [mx]."
    mx "See you around."

    scene 03_morningafterleave_05
    with fade

    window hide

    pause

    f "..."
    f "..."
    f "{i}\"Forget everything last night\"{/i}... {p} I wish... I wish I could."
    f "With this feelings I'm having right now..."
    f "I.. I don't know what to do."
    f "[mx]..."

    $ renpy.music.stop(channel='music2', fadeout=2)

    $ fquest_drunkenvisit_complete = True

    jump ep2_fquest_end

label ep2_fquest_end:

    scene mc_room_morning
    with fade

    $ time = 1

    if weekday == 7:
        $ weekday = 1
    else:
        $ weekday += 1

    show screen end_screen_fiona

    pause

    mx "Last night was..."
    mx "...just amazing."
    mx "I better get ready."

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    if notification_songs == True:
        $ renpy.notify("XNimVn - Sunny Day")

    $ story_music_ongoing = False

    jump mc_room


label ep2_fquest_drunkenvisit_fiona_memory:

    scene black
    with fade

    "(..visions..)"

    stop sound
    hide all

    f_m "(It was supposed to be just a typical morning. The same old routine...)"
    f_m "(Maybe if I just didn't...)"

    scene past_nightvisit_01
    with fade

    "{i}Turn on the left corner, madam.{/i}"
    f "I know where my home address is, Xerxes."
    "{i}Then turn right on that intersection.{/i}"
    f "{i}*sigh*{/i}"
    f "I should've let Olly turn this damn thing off."
    f "It was a great help when we moved here a few months ago but it's starting to annoy me now."
    f "Well, it's my damn fault for for forgetting my I.D. like an idiot and now I'm suffering the consequences."
    f "I hope I can still catch up with the others. I'll try taking the next train to the Capital later."

    play sound "soundfx/unlock.ogg"

    scene past_nightvisit_02
    with fade

    ol "Hey, stop that."
    f "Hmm?"
    f "Olly? I thought he left earlier than me?"
    f "Did he forget something too?"

    scene past_nightvisit_04
    with fade

    ol "Damn! I can't get enough of this ass of yours!"
    unk "You wanna go for another round?"

    play sound "soundfx/door_open.ogg"

    ol "We have all mornin—"
    f "O-O-Olly!?!" with vpunch

    scene past_nightvisit_03
    with dissolve

    f "Y-Y-You! T-That's—"
    f "Alejandro?"
    f "Since when... Olly?"
    ol "F-FIONA! Why are you...?"

    scene past_nightvisit_05
    with fade

    ol "N-N-No!! Th-This is..."
    ol "This isn't what it looks like!"
    f "Then what does it look like, Olly!?!"
    ol "It's..."
    ol "It's.... I'm sorry."
    f "Y-Y-Youu...Haaah...haa...huff...urgh..hng..!!!"
    ol "Fiona!"

    play sound "soundfx/walking_wood.ogg"
    pause 0.3
    play sound "soundfx/walking_wood.ogg"
    pause 0.6
    play sound "soundfx/stairs_down.ogg"

    scene black
    with slowfade

    f_m "(I wanted to runaway to the ends of the world...)"
    f_m "(I wanted to believe that this was all a dream...)"
    f_m "(Maybe if I just didn't forget that I.D. then I could've been ignorant of their affair...)"
    f_m "(And... and...)"
    "(Fiona...)"

    scene past_nightvisit_fight_02
    with fade

    if notification_songs == True:
        $ renpy.notify("dvdkm - her")

    $ renpy.music.play("music/dvdkm-her.mp3", channel='music2', fadein=1, loop=True)

    f "..."
    ol "..."
    ol "Fiona, I..."

    scene past_nightvisit_fight_04
    with dissolve

    f "Since when, Oliver."
    ol "I..."
    f "When... did you start... c-cheating?"
    ol "..."
    ol "Since last year..."
    f "Hngk!"

    scene past_nightvisit_fight_01
    with vpunch

    f "GOD FUCKING DAMMIT OLLY!"
    f "WERE YOU SO GODDAMN HAPPY CHEATIN' BEHIND MAH BACK!?" with vpunch
    ol "N-No, I..."
    f "How long have you been hiding that you're gay!?"
    ol "Ever since..."
    ol "Ever since we met, Fiona."

    scene past_nightvisit_fight_08
    with dissolve

    f "W-Wha..? What?"
    f "What do you mean?"
    ol "I mean.."
    ol "I thought that by marrying you and then having Prii, that I..."
    ol "That I can get over {i}\"this\"{/i}."
    ol "That being gay like this was just a phase."
    ol "That being a father and a husband would make these feelings disappear."
    f "Is that it, Olly? You used me?"
    ol "N-No, I..."

    scene past_nightvisit_fight_07
    with dissolve

    f "WHAT ABOUT MY FEELINGS, OLLY!?" with vpunch
    f "WHY DIDN'T YOU SAY SO YEARS AGO!" with vpunch
    ol "I...I..."
    f "DID YOU HAVE FUN USING ME AND PLAYING WITH MY FEELINGS, HUH!? OLLY!?" with vpunch
    f "WHEN DID YOU PLAN TO TELL US? IN 5 YEARS? 10? 20!?" with vpunch
    f "WHAT IF INSTEAD OF ME, PRII SAW YOU..."
    ol "I..."
    ol "..."

    scene past_nightvisit_fight_02
    with dissolve

    f "..."
    f "It hurts, Oliver."
    f "It hurts that the man you loved lied to you from the very start."
    f "It hurts that he can't love you back as a woman."
    ol "I'm... I'm sorry for all of this, Fiona. {p} I'm really sorry."

    scene past_nightvisit_fight_05
    with dissolve

    f "Get out."
    f "Just leave."
    f "We don't want to see you again."
    f "Just leave now that Prii doesn't—"

    play sound "soundfx/door_open.ogg"
    "{i}*door noise*{/i}"

    p "Papa! Mama! I'm home."

    scene past_nightvisit_fight_06
    with dissolve

    f "Oh no, no, no! Prii! \nI didn't want her to see this."
    ol "No, it's better this way. She has the right to know."
    ol "I'll talk to her."

    scene past_nightvisit_prii_01
    with fade

    p "Papa!"
    ol "How did school go today, rosebud?"
    p "It was great!"

    scene past_nightvisit_prii_02
    with dissolve

    p "[mx] helped me today!"
    ol "Oh, did he now?"

    scene past_nightvisit_prii_03
    with dissolve

    p "Yeah! Some meanies were at the park picking on me."

    scene past_nightvisit_prii_04
    with dissolve

    p "They were teasing my hair."

    scene past_nightvisit_prii_05
    with dissolve

    p "But then [mx] showed up!"
    p "He was like Wham!" with vpunch
    p "Bam!" with hpunch
    p "And then they ran off!"
    p "I want to be strong like him!"
    ol "Oh I see. \nHe's Al's kid alright."
    ol "Well, you're already a strong girl, Prii."
    p "Reeeeally?"
    ol "Of course you are! \nAnd its because of that strength that I want you to protect your Mama, alright?"

    scene past_nightvisit_prii_06
    with dissolve

    p "Hm?"
    p "But you're here already, Papa?"

    scene past_nightvisit_prii_06_1
    with dissolve

    ol "Well, you see, Papa's leaving."
    p "Leaving?"
    p "You'll just be back again, right?"
    ol "No, rosebud, Papa's going somewhere faraway."

    scene past_nightvisit_prii_06_2
    with dissolve

    p "W-Where? Do we need to pack up?"
    p "I need to tell [mx] and my classmates and..."
    ol "No, sweetheart. \nPapa's the only one leaving."
    ol "That's why you need to protect your Mama, okay?"
    ol "If you ever need my help. You can call me, alright?"

    scene past_nightvisit_prii_07
    with dissolve

    p "Papa! W-Why are you leaving!?"
    ol "Fiona, take care of Prii."
    f "..."
    p "PAPA!" with vpunch
    ol "Remember, I'll always love you, Prii. \nTake care of Mama, won't you?"

    scene past_nightvisit_prii_08
    with dissolve

    p "NOOOO!! DON'T GO!!!" with vpunch
    p "MAMA! Papa's.. Papa's leaving! Stop him!" with vpunch
    f "We don't need him, Prii."
    p "UUUWAAAAAH! PAPAAA!!" with vpunch
    f "It's gonna be alright, Prii."
    f "It's just the two of us now. \nWe can take care of ourselves."
    $ renpy.music.stop(channel='music2', fadeout=2)

    if fquest_dress_chosen == True:
        jump ep2_fquest_drunkenvisit_dress_path_cont

    elif fquest_sweater_chosen == True:
        jump ep2_fquest_drunkenvisit_sweater_path_cont

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
