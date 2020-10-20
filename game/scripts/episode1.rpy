label episode_1:

    hide screen intro_skip_start_bg
    hide screen intro_skip_skip_bg
    hide screen intro_skip_choice

    scene bd_01
    with slowfade

    $ renpy.pause(0.4, hard=True)

    show title_wsg
    with dissolve

    $ renpy.pause(1.5, hard=True)

    play music "music/Village Consort.mp3"

    if notification_songs == True:
        $ renpy.notify("Kevin MacLeod - Village Consort")

    hide all

    scene bd_02
    with slowfade

    mcx "Well, well, well..."
    mcx "Isn't that quite a lovely scene, eh?"
    mcx "\"{color=#00fff6}Sleeping Beauty{/color}\" over there drifting off peacefully beneath the Worldtree Sapling, lost in her dreamland..."
    mcx "It could be quite the scenic moment if the damn thing didn't just massacred dozens of players a while ago."

    scene bd_03
    with fade

    window hide

    pause

    scene bd_04
    with dissolve

    mcx "So Crow, what've you managed to dig out from the survivors?"

    scene bd_05
    with dissolve

    c "It's as the initial rumors said, that Elder Earthwyrm appeared just a couple of hours ago."

    scene bd_06
    with dissolve

    c "Based from my discussions with them..."

    scene bd_07
    with dissolve

    c "The players initially thought it was some kind of zone event, you know, like some sort of \"{color=#00fff6}Air Show{/color}\" as one guy puts it."
    mcx "But Earthwyrms don't exactly fly like other wyrms."
    c "Funny you should ask 'cause it only took a second for the crowd to realize that it wasn't one either."
    c "The bystanders near the Worldtree were the first ones to suffer the initial brunt of the attacks—"

    scene bd_09
    with dissolve

    s "And only those who were already far from the Elder Earthwyrm's reach managed to escape, even then, it was still by a hair's breadth."

    scene bd_10
    with dissolve

    s "It seems the [[{color=#00fff6}The Union of Empyrean Cetts{/color}] has already issued a decree branding it as a [[{b}SS{/b}] ranked monster."
    s "The newest difficulty rank to be announced since the unveiling of the [[{b}S{/b}] Rank and that was a long time ago."

    scene bd_08
    with dissolve

    mcx "Well, Sorros, I'm glad you're finally able to join us."
    mcx "Last I heard, you had much more important matters to attend to?"

    scene bd_11
    with dissolve

    s "{i}*cough*{/i}" with vpunch
    s "You jest, Sire."
    s "Please excuse my tardiness."
    s "You see, our musings took far longer than I anticipated and the discussions heated up quite considerably."
    s "I mean a higher ranked monster just appeared! An [[{b}SS{/b}]! We thought the [[{b}S{/b}] rank was the final frontier but now..." with vpunch

    scene bd_03
    with dissolve

    s "Potions, armors, weapons, and all other kinds of knick-knacks of the [[{b}SS{/b}] variety! The markets will go crazy!" with vpunch
    s "Especially from an Elder of a Wyrm species priced for their materials! Heck, those alone could fetch a really high sum in the market, more so for items crafted from it by an artisan!"

    scene bd_11
    with dissolve

    s "{i}*sigh*{/i}"
    s "Suffice to say, I've lost myself on that conversation, significantly."
    mcx "You know, I wasn't really {i}that{/i} serious, right?"

    scene bd_07
    with dissolve

    c "AHEM!" with vpunch
    c "As I was saying before Sorros interrupted me..."
    c "It seems that the players who managed to interact with Elder Earthwyrm without dying first were fortunate enough to gauge the monster's level."
    c "That said, we're expecting its level to be around the ballpark of the late 300s and early 400s."
    mcx "Jeezus! {p} That high, huh?" with vpunch

    scene bd_11
    with dissolve

    s "The strongest boss we've last fought was that [[{color=#00fff6}Level 330 Plague Anubis{/color}] on [[{color=#00fff6}Casca Veirra{/color}] just a couple of months ago."
    s "And for us to fight a being in its early 400s... {p} ...may the High Empress bless us."

    scene bd_07
    with dissolve

    c "I don't know if her blessings makes us invincible against that but let's take what we can get."
    c "Outside of the top rankers amongst the great guilds, no one can survive that behemoth's direct attacks much less so for those resting here earlier."

    scene bd_11
    with dissolve

    s "Quite unfortunate for them to be attacked on what they considered to be a peaceful area."

    scene bd_12
    with dissolve

    mcx "One man's unfortunate encounter is another's man's fortunate encounter. As a popular saying I butchered goes..."
    mcx "I honestly thought that this raid boss would just be a stronger [[{b}S{/b}] ranked one."

    scene bd_13
    with dissolve

    mcx "For them to add another [[{b}S{/b}] means this little birdy won't be such a \"pushover\" as we thought."
    mcx "Maybe we could actually have fun this time, eh?"

    scene bd_18
    with dissolve

    mcx "So, what's in your minds, gents?"



    menu gents:

        "Crow?" if crow_ask == True:
            jump crow_gents

        "Sorros?" if sorros_ask == True:
            jump sorros_gents

        "Moving On" if crow_ask == False and sorros_ask == False:
            jump move_on_story

    label crow_gents:

        scene bd_14b
        with fade

        mcx "Crow?"

        scene bd_14a
        with dissolve

        c "Where to even begin?"
        c "First and foremost, this damn terrain!"
        c "Why the hell is it situated in the [[{color=#00fff6}Worldtree Sapling Garden{/color}] even?"

        scene bd_14c
        with dissolve

        c "Are we really going to fight it in this small enclosed space, huh?"
        c "There are only 2 exits, one at the back and one at the front, both of them are tight, funneled spaces going in and out."

        scene bd_13
        with dissolve

        c "One straight breath attack through that and were barbecued."
        c "The space itself also limits how many melee and range players we can arrange but—"

        scene bd_15h
        with dissolve

        mcx "Nah, don't bother with the ranged units here 'cause that thing's [[{color=#00fff6}Defense{/color}] ain't gonna be nice to those [[{color=#00fff6}Piercing{/color}] weapons of theirs."
        mcx "Not to mention the terrain on this level. There are only 2 options for them here, its either too close or too far."
        mcx "Assign them to scout the perimeter for monsters or worse... {w} other guilds waiting in to scoop the loot."

        scene bd_15d
        with dissolve

        c "O-Okay..? No range units? Fine... I guess?"
        c "The mages? Are they alright above there or maybe..?"
        mcx "They're perfect there. It's just the right distance to support us and barely outside the range of the Elder Earthwyrm's Area-of-Effect attacks."
        mcx "It provides a natural defense at the expense that the long distance rapidly degrades the power of their long range attacks. Outside of the [[{color=#00fff6}Meteor{/color}] spell, long range attacks are powerless."
        mcx "Healing us from that distance is no problem though so we're on our own here."

        scene bd_15g
        with dissolve

        c "If that's the case then we can focus our melee units to—"

        scene bd_15d
        with dissolve

        mcx "That one... {w} To be frank with you Crow, you, me, and Sorros would be enough to stop the Elder Earthwyrm."
        mcx "Well... maybe call a few \"beefy\" guys of ours, like 2 or 3, that can take a hit from the monster without dying so it doesn't just focus its aggro on me."

        scene bd_15c

        c "{b}What!?!{b}" with vpunch
        c "\"CALL A FEW \"BEEFY\" GUYS!?\"." with vpunch
        c "This is a goddamn [[{b}SS{/b}] ranked Elder Earthwyrm not some Goblin you can find in the [[{color=#00fff6}Rice Fields{/color}]!"

        scene bd_15g
        with dissolve

        c "I'm sorry, I didn't know it was \"{color=#00fff6}Sacrifice Your Friends Day{/color}\" today!"
        c "I understand the situation with the mages and the ranged units but how can we expect to kill that damn thing with 2-3 guys!?"

        scene bd_15c
        with dissolve

        c "Isn't it a golden rule that the more people in the field, the better the chances we kill that thing?"

        scene bd_15d
        with dissolve

        mcx "I know! I know! It's absurd but hear me out!" with vpunch

        scene bd_03
        with fade

        mcx "Look at the space below, at most we have a meter or two of distance to the Elder Earthwyrm at all times."

        window hide

        pause

        mcx "Imagine 10-15 guys engaging in that small space ready to strike that monster."
        mcx "Now imagine that Elder Earthwyrm rampaging with all its glory assisted by the plethora of Area-of-Effect skills which they pride themselves of."
        mcx "That scenario would be no different from a can of sardines being smashed by a hydraulic press with no way to fight back."

        scene bd_14b
        with dissolve

        mcx "In short, the more people down there, the more they'll become liabilities as the fight goes on, Crow."
        mcx "And you know what happens when you crush a can of sardines?"
        mcx "The sardines die, Crow!" with vpunch

        scene bd_14a
        with dissolve

        c "But aren't they already dead inside to begin with? I mean they're also ready-to-eat so..."

        scene bd_15d

        mcx "T-That's not the point here, Crow." with vpunch
        c "Riigghhtt..."
        mcx "Moving on!"

        scene bd_15h
        with dissolve

        mcx "Our main strategy would be to take advantage of this small space and prioritize dodging and agility."
        mcx "It's gonna be a slow battle no doubt but like waves hitting the shore cliffs, we can erode aways its health slowly and steadily."

        scene bd_15d
        with dissolve

        mcx "Pretty \"poetic\" eh?"
        c "Hmmm, yeah.... {w} No."
        c "I'm gonna compromise with calling on the 3 guys to assist us here but I'll have the other 20 on hold."

        scene bd_15a
        with dissolve

        c "Just in case \"something happens\", okay?"

        mcx "Hnnggg... fine!"

        $ crow_ask = False

        scene bd_18
        with dissolve

        jump gents


    label sorros_gents:

        scene bd_16a
        with dissolve

        mcx "Sorros?"

        scene bd_17d
        with dissolve

        s "Sire."

        scene bd_15d
        with dissolve

        c "You should really drop that formal lingo you have there, Sorros."

        scene bd_17a
        with dissolve

        s "Well, Sir Crow, I'm afraid I have to decline that offer."

        scene bd_16c
        with dissolve

        s "You see, a gentleman must always speak with grace and great demeanor to one's superior." with vpunch

        scene bd_15e
        with dissolve

        mcx "Yeah, you tell him, Sorros. You could actually learn something from him, Crow."
        mcx "Try calling me \"{color=#00fff6}Your Majesty{/color}\" for example. It has a nice ring to it."

        scene bd_15b
        with dissolve

        c "How about I kick your \"{color=#00fff6}Royal Ass{/color}\" so that Elder Earthwyrm can have a \"{color=#00fff6}Majestic Feast{/color}\", \"{color=#00fff6}Your Majesty{/color}\"?" with vpunch
        mcx "H-Haha..ha... It needs a little work but you're getting there."

        scene bd_15d
        with dissolve

        c "Ugh." with vpunch

        scene bd_16a
        with dissolve

        s "Getting back to your question, Sire."

        scene bd_16b
        with dissolve

        s "It seems these corner walls would be an ideal place for me."

        scene bd_17a
        with dissolve

        mcx "Ideal place? Really? You don't want to join the other mages?"
        s "No need for that, Sire. {p} I'm now much more of a \"{color=#00fff6}Close-Combat Mage{/color}\" as you will."
        mcx "What do you mean by that?"

        scene bd_16c
        with dissolve

        s "You could say I'm no longer a [[{color=#00fff6}Master Magus{/color}] but a full-fledged [[{color=#00fff6}Grand Magus{/color}]!" with vpunch

        scene bd_15d
        with dissolve

        c "Well, well. Look at Mr. Big Shot over here."

        scene bd_17b
        with dissolve

        mcx "{i}*whistles*{/i}"
        mcx "And here I thought we'd be too weak to fight the boss, we've got ourselves a walking Atomic Bomb."

        scene bd_17a
        with dissolve

        s "Please."
        s "I'm just a little bit powerful compared to my previous class but more importantly, I've managed to acquire a handy spatial skill, the [[{color=#00fff6}Juxtapose{/color}]."
        s "It may not be as versatile like a Ronin's [[{color=#00fff6}Blink{/color}] or Sir Crow's [[{color=#00fff6}Shadow Walk{/color}] but its quite effective if the [[{color=#00fff6}Totems{/color}] are strategically positioned."
        mcx "[[{color=#00fff6}Totems{/color}]?"
        s "Craftable items for my [[{color=#00fff6}Juxtapose{/color}] skill. Once placed, I can freely switch myself with any of my [[{color=#00fff6}Totems{/color}] on the field."
        s "That's why I can't freely teleport anywhere but if I managed to place them at all the corner walls."
        mcx "You'd be able to freely teleport at any of them and the disadvantage of being stuck like a sitting duck disappears."
        s "Precisely, Sire. But for that, I need to render Sir Crow's skills in reaching those places."

        scene bd_15g
        with dissolve

        c "\"Not as versatile\" he says."
        c "That skill consumes far lesser mana than [[{color=#00fff6}Blink{/color}] and [[{color=#00fff6}Shadow Walk{/color}] and doesn't have a cooldown making it highly used for abuse."
        mcx "Now, now, Crow. Just because his new skill is better than yours doesn't mean you need to bully him."

        scene bd_15c

        c "W-Wha? Hey, I'm just stating facts and since when did I bully him!?" with vpunch
        c "That's quite a rare skill to be honest!"

        scene bd_17b
        with dissolve

        s "It's fine, Sire. Sir Crow's pragmatism is one of his best traits."

        scene bd_15g
        with dissolve

        c "See, Aramis? Best traits?"
        mcx "Yeah, yeah."
        c "So, are your [[{color=#00fff6}Totems{/color}] unlimited?"

        scene bd_17c
        with dissolve

        s "Sadly no, aside from the meticulous crafting process, the ingredients for them are also quite expensive."

        scene bd_17d
        with dissolve

        s "Hence, I could only craft 4 of them currently. Just enough for these walls."
        s "I'm transfering them now to your inventory, Sir Crow. I might trouble you for a bit?"

        scene bd_15i
        with dissolve

        c "It's fine."

        scene bd_17b
        with dissolve

        mcx "So, you're staying up here, Sorros?"
        s "Verily so."

        $ sorros_ask = False

        scene bd_18
        with dissolve

        jump gents




label move_on_story:

    mcx "So, going back to our main topic..."

    scene bd_13
    with dissolve

    mcx "How do we deal with our friend over there."

    scene bd_16a
    with dissolve

    s "Earthwyryms, unlike their sibling species, specializes in defense rather than pure firepower like that of the Lavawyrms and Tundrawyrms."
    s "They also lack the ability of flight like the two but in exchange..."

    scene bd_17a
    with dissolve

    s "Their huge mass grants all their normal physical attacks a random chance to ignore armor."
    s "It also forces them to prioritize their huge array of Area-of-Effect skills."

    scene bd_15h
    with dissolve

    c "Basically, its a giant Jackhammer and this \"arena\" was basically made for him."
    c "Too far that your attacks are useless or too close that you can't escape his attacks."

    scene bd_17g
    with dissolve

    s "Indeed."
    s "They are also compensated with a far larger health pool and a gargantuan amount of physical and magical defense."

    scene bd_15i
    with dissolve

    c "Let me revise what I said, its a Jackhammer made of \"{color=#00fff6}Bullet Sponges{/color}\"."

    scene bd_15g
    with dissolve

    mcx "Well, that's for your run-of-the-mill Earthwyrms, this one has an [[{color=#00fff6}Elder{/color}] brand with the rank of an [[{b}SS{/b}]."

    scene bd_15h
    with dissolve

    c "Let me revise my revision then, its a Jackhammer made of \"{color=#00fff6}Bullet Sponges{/color}\" dipped in a basin full of steroids."
    c "Lots and lots of steroids."
    mcx "Basically, this battle's gonna be hella fun."

    scene bd_15c
    with dissolve

    c "Remind me again why the hell is that \"fun\"?"

    mcx "You know, for a guy whose [[{color=#00fff6}Job Class{/color}] literally relies on killing things, you really don't want to kill this boss, huh?"

    scene bd_15a
    with dissolve

    c "No, I want to {i}definitely{/i} kill it. That's a fact."

    scene bd_15d
    with dissolve

    c "What I don't want is a fight that takes multiple hours to finish."
    c "If anything requires me to work for more than 30 minutes to kill it, its a chore. Okay?"

    scene bd_15b
    with dissolve

    c "And let me remind you, that's an [[{color=#00fff6}Elder{/color}]."
    c "If that lug nut over there hits 20%% of its life later, it'll activate its [[{color=#f9c402}Transcension{/color}]."

    scene bd_15c
    with dissolve

    c "Meaning that its primary stat doubles, does anyone know what that stat is? {p} Anyone?"
    c "What stat do you imagine a big burly thing like that with thick large scales have?"

    scene bd_15a
    with dissolve

    c "[[{color=#00fff6}Defense{/color}] people! It'll double its already absurd [[{color=#00fff6}Defense{/color}]!" with vpunch
    c "In our case, we might as well be hacking away at a concrete wall with sticks!"

    scene bd_15c
    with dissolve

    c "And have you two seen the Three Musketeers vs. Godzilla?"
    c "What? No? None at all?"

    scene bd_15f
    with dissolve

    c "{b}'Cause it doesn't fucking exist! That's why!{/b}" with vpunch
    c "The world has collectively agreed that the idea of that even existing is the most retarded thing mankind will ever come up!"
    c "And were about to do the opposite of that, the antithesis of a collective logic, that a small group of people cannot kill a giant fucking monster!"

    scene bd_15g
    with dissolve

    c "And \"Captain O' Captain\" here wants only a few of us to fight the fucking thing!"

    scene bd_15f
    with dissolve

    c "{i}*huff* *huff* *huff*{/i}"

    scene bd_15d
    with dissolve

    mcx "AHAHAHAHA!" with vpunch
    mcx "It's always fun to hear your rousing speeches, Crow."

    scene bd_15g
    with dissolve

    c "What? I wasn't even trying to—"
    mcx "Quite frankly, it seems the odds aren't in our favor if you put it that way."
    mcx "Except you're forgetting one crucial thing..."
    mcx "ME!" with vpunch

    scene bd_15d
    with dissolve

    c "Nope. I'm pretty sure I didn't."
    mcx "The Deathbringer? The Empyrean Warlord? The Lord of Cett Yvarra? The Great Guild Leader of the Garuda? The Top 2 Ranked Player of Reincarnotica and soon to be Top 1?"
    mcx "The Knight of the Living Dead? Mother of Dragons? Doesn't ring a bell?"

    scene bd_15g
    with dissolve

    c "Why exactly are you announcing your titles like that and the only thing your \"mothering\" just got flushed down the toilet."

    scene bd_15d
    with dissolve

    mcx "'Cause your forgetting that I haven't lost a fight since I started our guild (except those times when I did early on)!"
    mcx "BUT!" with vpunch

    scene bd_15h
    with dissolve

    mcx "There's a reason why we are one of the strongest elite guild in the world despite having the fewest members."
    mcx "Because each and everyone one of us are monsters in their respective field."
    mcx "And we're not gonna start losing now, are we?"

    scene bd_17d
    with dissolve

    s "Sire, I hate to interrupt you but a report came in from one of the spies."

    scene bd_15e
    with dissolve

    c "Mine here too."

    scene bd_18
    with dissolve

    mcx "Well, look at that, it seems our \"friends\" from the other guilds are starting to make their moves."
    mcx "Then why don't we hasten things on our end, shall we?"

    scene bd_20
    with dissolve

    mcx "But first..."
    mcx "I need to go to the bathroom."
    s "Pardon, Sire?"

    scene bd_21
    with dissolve

    c "Bathroom?"
    c "For what—"

    scene bd_22
    with fade

    c "—reason are you—"

    scene bd_23
    with fade

    c "—going—"
    c "NOOOOO!!!" with vpunch
    s "SIRE! NO!" with vpunch
    c "STOP! YOU IDIOT!" with vpunch

    scene bd_24a with vpunch

    window hide

    pause 0.3

    mcx "AHAHAHAHAHAHAHAHA!"

    s "[[{color=#00fff6}Tymisus{/color}]! [[{color=#00fff6}Hectarus{/color}]! Do you read me? The Worldtree Sapling Garden, right now!"
    c "[[{color=#00fff6}Rustbucket{/color}]! Drag your ass over here! I know you're leveling in the woods near here!"

    scene bd_24b
    with fade

    c "Our dear leader just plunged himself into the mouth of Satan!"
    mcx "You two {i}really{/i} need to chill."
    c "Chill my ass!" with vpunch
    s "Everyone! Get ready for battle!" with vpunch
    c "Goddammit Aramis! We're gonna die!" with vpunch

    scene bd_28
    with dissolve

    mcx "Have a litte bit of fun in your lives, you two!" with vpunch
    c "Getting ourselves killed isn't exactly \"fun\"."

    window hide

    scene bd_25
    with dissolve

    pause

    scene bd_26
    with hpunch and dissolve

    pause

    ew "{i}*Sccccreeeeeeeeeeeeeeeeeeeeeeeeeeeeeecchhhhh*{/i}" with vpunch

    scene bd_28
    with dissolve

    mcx "Awwwww... {p} ...and here I thought I would wake you up with \"{color=#00fff6}True Love's Kiss{/color}\""
    mcx "Which is coincidentally the name of this lovely blade of mine."

    scene bd_29
    with dissolve

    ew "{i}*Sccccreeeeeeeeeeeeeeeeeecchhhhh*{/i}" with vpunch
    mcx "{b}GAAAARUUUUDAAAA!{/b}" with vpunch
    mcx "It's show time, mofos!"
    gm "{size=+40}YEAH!{/size}" with hpunch

    stop music fadeout 2.0



    scene black with flash

    window hide

    pause 2

    "(This battle was supposed to be no different from the usual raids we had...)"
    "(The enemy was certainly strong but so did those that we've crushed and defeated.)"
    "(We are {b}THE{/b} Garuda Guild! One of the greatest and prestigious guild in Reincarnotica!)"
    "(For this to happen to us... to me...)"

    gm "Argh! D-Dammit!?! The others they—" with hpunch
    gm "I-Its skin! N-No! Wings!?!" with hpunch
    gm "A-Ancestral Transcension?!" with hpunch
    gm "O-Oh my God! Is that? {w} Is that an [[{color=#00fff6}Ultima{/color}]!?!" with hpunch
    gm "Take Cover! {p} THAT'S USELESS!" with hpunch
    gm "Shit!! R-Run!!" with hpunch



    show text "{size=36}{color=#A9A9A9}[[ You received 99,979 amount of damage ]{/color}{/size}" at truecenter with flash

    pause

    show text "{size=36}{color=#A9A9A9}[[ At Death's Door activated ] {p} [[ You are the Death's Apostle in the mortal realm which grants you the ability to withstand any attacks that can instantly kill you.]{/color}{/size}" at truecenter with dissolve

    pause

    show text "{size=36}{color=#A9A9A9}[[ Death Knight's Resent activated ] {p} [[ You live in the border of Life and Death. Physical attack and Defense stats are tripled while your health stays in critical condition. ]{/color}{/size}" at truecenter with dissolve

    pause

    show text "{size=36}{color=#A9A9A9}[[ Vampiric Blood Bath activated ] {p} [[ You are blessed by the bloodline of the Nosferatus. Gain health regeneration equal to the carcasses near you. ]{/color}{/size}" at truecenter with dissolve

    pause

    show text "{size=36}{color=#A9A9A9}[[ Party member Tymisus (Champion Gladiator) died! ]{/color}{/size}" at truecenter with dissolve

    pause

    show text "{size=36}{color=#A9A9A9}[[ Party member Hectarus (Champion Gladiator) died! ]{/color}{/size}" at truecenter with dissolve

    pause

    show text "{size=36}{color=#A9A9A9}[[ Party member Rustbucket (Night Guardian) died! ]{/color}{/size}" at truecenter with dissolve

    pause

    show text "{size=36}{color=#A9A9A9}[[ Party members    ...    ]{/color}{/size}" at truecenter with dissolve

    pause

    scene bd_30a
    with slowfade

    play music "music/Unholy Knight.mp3"

    if notification_songs == True:
        $ renpy.notify("Kevin MacLeod - Unholy Knight")

    mcx "Goddamit! What the hell happened!?!" with vpunch

    "(I was facing the Elder Earthwyrm head-on but halfway through the battle, its flash blinded and stunned me out of nowhere.)"
    "(I don't know what exactly happened but just hearing from the voices, that colossal damage was an... [[{color=#00fff6}Ultima{/color}]?)"
    "(This thing's health wasn't even halfway to death much so being in near it. How could it [[{color=#f9c402}Transcend{/color}] and cast an [[{color=#00fff6}Ultima{/color}] at the same time!?)" with vpunch
    "(It doesn't make sense!)" with vpunch

    scene bd_31
    with dissolve

    c "Anyone! Anyone!? Alee!? Marco!? Any priests out there!?" with vpunch
    c "Fuck! They're all dead dammit!" with vpunch
    c "Urrggghhhh!! I can't fucking get up!"
    c "Fucking great!"
    c "Aramis, you okay?"

    scene bd_30a
    with dissolve

    mcx "I'm fine for the most part. Let me help you get up..."

    menu:
        "Help Crow":
            mcx "What the..? I-I'm paralyzed too!?" with vpunch
            mcx "No, it can't be! My status screen's clear!?" with vpunch

    c "You too, huh?"

    scene bd_31
    with dissolve

    c "Looks like we're stuck in the same boat—"
    c "What. {w} The. {w} Hell. {w} Is that!?"
    c "I-Is that what I think it is!?" with vpunch

    window hide

    scene bd_32 with dissolve:
        subpixel True
        yalign 1.0
        pause 1.0
        linear 5.0 yalign 0.0

    pause

    mcx "That's the infamous [[{color=#f9c402}Transcended Elder Earthwyrm{/color}], Crow."
    mcx "Quite cute, huh?"
    c "Transcended!? Like hell it is! I've seen a [[{color=#f9c402}Transcended Elder Earthwyrm{/color}] before and it's nothing like that—" with vpunch
    mcx "I know. Your guess is as good as mine."

    scene bd_30a
    with dissolve

    mcx "I can't really remember much what happened after being flung here but all I know is that's the first \"thing\" I saw."
    mcx "Do you remember anything that caused that?"

    scene bd_31
    with dissolve

    c "No... I was midway into my [[{color=#00fff6}Shadow Walk{/color}] when I was knocked back into reality by that \"thing\"'s attack."
    mcx "Knock you out from an ethereal plane?"
    c "Yeah. How was that even possible?"
    mcx "...That means. {w} Shit! Then this is no ordinary paralysis either. {p} Have you called for the backups already?"
    c "They're on their way but it would take some time, it seems something's blocking them from teleporting here."
    mcx "Tsk. So it really is one."
    c "What do you mean by that—Incoming!" with vpunch

    scene bd_37
    with dissolve

    mcx "Goddamit!"
    ew "{i}*Sccccreeeeeeeeeeeeeeeeeecchhhhh*{/i}" with vpunch

    scene bd_33
    with dissolve

    s "... Su'Ressu... Aldi'ii... Pontiffica! Goddess of the Night! Grant me your protection!" with hpunch
    s "[[{color=#00fff6}Celestial Domain: Aegis Shield{/color}]" with vpunch

    scene bd_34
    with slowflash

    s "Begone!"
    with vpunch

    window hide

    pause 0.3

    c "Sorros!" with vpunch
    mcx "Sorros! You're still alive?" with vpunch

    scene bd_35
    with dissolve

    mcx "Can you still move freely or is it..?"
    s "I'm sorry to dissapoint you, Sire. If you can consider me falling over here to be \"moving freely\", that is."
    s "Sadly, the omnipresent skill, as you've already clearly noticed, greatly limits my movements too but fortunately, a passive of mine alleviates some of the restrictions imposed which allows me limited mobility."

    scene bd_31
    with dissolve

    c "Sorry to interrupt your chit-chat over there but the greater issue here is if Sorros still has one of his [[{color=#00fff6}Mass Teleportation Scrolls{/color}]?"
    c "We might be able to use that to escape!" with vpunch

    scene bd_36
    with dissolve

    mcx "Those are not going to work, Crow."
    c "What? Why!? {w} What's actually going on!? I have a feeling that you know what's causing all of this!" with vpunch
    s "A [[{color=#00fff6}Black Hole{/color}] is currently employed, Sir Crow. A very {i}very{/i} powerful one at that."
    c "[[{color=#00fff6}Black Hole{/color}]? That \"{color=#00fff6}Black Hole{/color}\"? The space-time magic? No way! I mean, you can't even see the skill's—"

    scene bd_36
    with dissolve

    mcx "Because this one's more than your typical 3 meter range. If I can speculate from the horizon, it's more than 15 meters at best."
    c "T-T-That far!? Impossible!" with vpunch

    scene bd_34
    with dissolve

    s "I, for one, am also baffled by it. This monster... it defies common logic through and through."
    c "That explains the backup's inability to use [[{color=#00fff6}Teleportation{/color}] here."

    scene bd_35
    with dissolve

    mcx "Not only that, any [[{color=#00fff6}Spatial Magic{/color}] is barred from use and that includes your [[{color=#00fff6}Shadow Walk{/color}] and Sorros's [[{color=#00fff6}Juxtapose{/color}]."
    mcx "It also triples the current [[{color=#00fff6}Gravity{/color}] but judging that we're completely immobile and not slowed down... it's safe to say that it more than tripled it."
    mcx "You being ejected from your [[{color=#00fff6}Shadow Walk{/color}] was caused by that too."
    c "Ahhh shit! Then what options do we have here? {p} Die horribly!?" with vpunch
    mcx "If we're lucky, we can probably wait this one out till the [[{color=#00fff6}Black Hole{/color}] stops and try to escape."

    scene bd_34
    with dissolve

    s "Siiire!" with vpunch
    s "I'm deeply afraid that our luck's running out extremely fast! Look above!"

    scene bd_38
    with dissolve

    mcx "Its preparing for another... {w} ...[[{color=#00fff6}Ultima{/color}]?"
    c "You've gotta be kidding me!" with vpunch
    "(This is getting more and more absurd by the minute. This isn't a boss to be defeated anymore!)"
    "(This is an outright execution, one without a chance of retaliation.)"
    "(But why!?!)" with vpunch

    scene bd_30b
    with dissolve

    mcx "..."
    mcx "Gather all our members in [[{color=#00fff6}Cett Yvarra{/color}] tomorrow."
    mcx "I want them all at the Grand Hall."
    mcx "Classify it as the highest priority above all else."
    mcx "Those who fail to show up will be punished to the highest degree."

    scene bd_31
    with dissolve

    c "Roger."

    scene bd_34
    with dissolve

    s "As you wish, Sire."

    scene bd_38
    with dissolve

    ew "{i}*Sccccreeeeeeeeeeeeeeeeeecchhhhh*{/i}" with vpunch
    ew "{i}*Sccccreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecchhhhh*{/i}" with vpunch

    scene bd_30b
    with dissolve

    "(I need to get to the bottom of this!)" with vpunch
    mcx "Well, Crow, it seems you've won the lottery. Dying horribly it is."

    scene bd_39
    with dissolve

    ew "{i}*Sccccreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecchhhhh*{/i}" with vpunch

    window hide

    pause

    scene bd_40
    with flash

    c "Me and my stupid mou—"

    stop music fadeout 3.0

    scene black
    with slowflash

    show text "{size=64}{color=#A9A9A9}[[YOU HAVE DIED!]{/color}{/size}" at truecenter with dissolve

    pause

    show text "{size=64}{color=#A9A9A9}[[12 HOURS REMAINING TILL RESURRECTION]{/color}{/size}" at truecenter with dissolve
    pause

    jump transition1





label back_to_reality:

    scene h_1
    with slowfade

    "{i}{color=#f93b3b}*beep*{/color}{/i}"

    scene h_2
    with dissolve

    "{i}{color=#f93b3b}*beep*{/color}{/i} {w} {i}{color=#f93b3b}*beep*{/color}{/i}"

    scene h_3
    with dissolve

    "{i}{color=#f93b3b}*beep*{/color}{/i} {w} {i}{color=#f93b3b}*beep*{/color}{/i} {w} {i}{color=#f93b3b}*beep*{/color}{/i}"

    scene h_4
    with dissolve

    u "Urgghh...."
    u "This was a very... {w} \"eventful\" day."
    u "The other guilds must be celebrating after hearing the news of our deaths."
    u "Fuck!" with vpunch
    u "{i}*sigh*{/i}"

    scene h_5
    with dissolve

    "(Now that I think about it...)"
    "(It's been almost half a decade since I've actually lost to a boss.)"

    scene h_6
    with dissolve

    "(Thanks in large part of me being an idiot then. I wasted everybody's effort by my idiocy and got kicked out.)"

    scene h_7
    with dissolve

    "(But not this time, something's amiss with that [[{color=#f9c402}Transcension{/color}]—No! A lot of things today didn't make sense!)"

    scene h_8
    with dissolve

    "(Louie... what the hell was that?)"

    scene h_9
    with dissolve

    "(But first...)"
    u "Quanto, how are the results of the recent immersion?"
    "(I have a job to do.)"

    play music "music/Rainy_Night.mp3"

    if notification_songs == True:
        $ renpy.notify("Dana Boulé - Rainy Night")

    scene h_10
    with slowflash

    q "Good evening and welcome back, Sir!"
    q "I hope you had a wonderful time there!"

    scene h_11
    with dissolve

    u "Y-Yeah, it was \"wonderful\" alright."
    q "Oh my! I detect a little bit of... melancholy in your voice, Sir?"

    scene h_12
    with dissolve

    u "Don't mind it. {p} Anyways, how's the prototype?"

    q "It seems the results are quite better than expected with minor hiccups here and there."

    "(\"Hiccups here and there?\")"

    menu:
        "Move towards the table":
            scene pc_quanto with fade

    u "First things first, how's the efficiency of our current modifications with the [[{color=#ff2d34}Ver. 9{/color}] Prototype?"
    u "Specifically on the {color=#00fff6}\"Immersion-Emulation on Relative Sensations\"{/color} compared to the previous sessions?"

    scene pc_sensors
    with dissolve

    q "The VR-22XX Headgear Prototype [[{color=#ff2d34}Ver. 9{/color}] modifications shows incredible promise with an overall increase of {color=#00fff6}120%%{/color} compared to the paltry {color=#00fff6}46.4%%{/color} of [[{color=#e035ff}Ver. 8{/color}]..."
    u "Oh-ho!" with vpunch
    u "A {color=#00fff6}73.6%%{/color} increase!? Damn, that's good!"
    "(It seems the data from that hunk of junk wasn't so useless after all.)"
    "(Yet I'm still wondering why the boss would force me to study that relic from the Cold War.)"
    "(Oh well, if it gives great results, I ain't bothering with questioning it but it makes you wonder though...)"

    scene pc_brain1
    with dissolve

    q "Sir, in correlation with that increase, other variables were also {i}highly{/i} affected."
    q "Namely, a {color=#00fff6}300%%{/color} rise of activity in certain areas of the limbic system and of the Orbitofrontal Cortex."
    u "{color=#00fff6}300%%{/color}!? Wait! Where and what exactly does it affect?"

    scene pc_cortex
    with dissolve

    q "The unwarranted effects seems to target the parasympathetic portion of the autonomic nervous system and manifests itself as vasodilation of the—"
    u "Quanto! {p} Less medical jargons, more plain English." with vpunch
    q "Simply put, Sir, that {color=#00fff6}300%%{/color} increase seems to affect one's \"{color=#ff93c6}libido{/color}\" while Immersion-Emulation is in effect."
    q "It targets not only the current user but those who are around him or her, particulary the opposite sex, creating a \"{color=#ff93c6}lust field{/color}\" of some sort."
    u "What? It makes players... {w} aroused?"

    scene pc_bod
    with dissolve

    q "Yes, Sir."
    q "The {color=#00fff6}300%%{/color} increase is only observed from the data on the Male Nervous System. However, the effects on the Female Nervous System..."
    q "...has an increase of {color=#00fff6}997%%{/color} on related sensations. Until controlled test data could be gathered, the theoretical data has an error rate of about {color=#00fff6}22.66%%{/color}."

    scene pc_brain2
    with dissolve

    "(Well shit! What's with that absurd side effect? There's a market for that to be honest but the bosses wouldn't be too happy hearing that it makes people horny.)"
    u "But does the increase affect the user {i}{color=#00fff6}outside the experience{/color}{/i} or does it carry on after logging out?"

    scene pc_cortex
    with dissolve

    q "That's a negative, Sir."
    q "The effects are only effective during Immersion-Emulation when full-on injection to the cortex is active and running."
    u "So it's nothing permanent, right?"
    q "Yes, Sir."
    "(Hmmm... it means that increase is honestly a negligible variable to the overall user experience.)"
    "(I mean, EVE already blocks anything that triggers \"{color=#ff93c6}sexual thoughts{/color}\" in the brain as well as any \"{color=#ff93c6}extreme physical contact{/color}\" between two people.)"
    "(I still remember the hubbub about \"{color=#00fff6}virtual physical harassment{/color}\" controversy back in the day that died almost immediately after the game's launch.)"
    "(Yet it didn't stop the company from putting measures though. Every boy's dream of having virtual sex was buried in the grave that day.)"
    u "So, nothing to be worried about, huh?"

    scene pc_quanto
    with dissolve

    q "Correct, Sir. {p} But I do advice consulting with the Chief Neurotechnician of the Neurotech Division to be on the safe side."
    u "Gotcha!"
    u "So, anything happened while I was \"out\"?"
    q "You received 2 messages, Sir. One from your mother and another from Sir Yoshi Takahashi."
    "(Should I call Louie first to inquire about the boss or check the messages first?)"



    menu contacts:

        "Call Louie" if louie_called == True:
            $ louie_called = False
            jump louie_call

        "Listen to Yoshi's voice message" if listened_yoshi == True:
            $ listened_yoshi = False
            jump yoshi_message

        "Listen to Mother's voice message" if listened_mother == True:
            $ listened_mother = False
            jump mother_message

        "It's okay, I'll rest for now" if listened_yoshi == False and louie_called == False and listened_mother == False:
            jump rest_for_now





label louie_call:

    scene msg_call_lou
    with dissolve

    q "Calling Sir Louie..."
    q "Call connected."

    scene lou2
    with dissolve

    l "Zero!" with vpunch
    u "Uno."
    u "You must've heard the news by now then."

    scene lou1
    with dissolve

    l "Heard!?! {p} Your goddamn name's plastered all over the web!" with vpunch
    u "I figured as much when that death screen appeared."

    scene lou7
    with dissolve

    "(Zero and Uno.)"
    "(Codenames we've assigned each other to safeguard our identities.)"
    "(It'll be \"problematic\" if they find that the Chief Engineer of the Hardware Division and someone from the Game Development Team is running a \"{color=#00fff6}secret business{/color}\" between the 2 of them.)"
    "(And by \"problematic\", I mean, 10-20 years in jail for embezzlement, fraud, theft, and other nasty shit they can stick at us if they find this out.)"
    "(I mean, providing me inside-info about hidden locations of legendary items and other rare loot, then selling it online seems like a joke at first.)"
    "(But the money made from this is nothing to be laughed at.)"
    "(Not to mention our intentional manipulation of local economies in the game to benefit us is...)"
    "(If the public finds out, it'll be game over for the both of us.)"

    scene lou5
    with dissolve

    u "What exactly happened there, Uno? I know you were watching."
    l "I might have a pretty good idea on what just transpired."
    u "Well..."



    menu ask_louie:
        "Overpowered Elder Earthwyrm?":
            $ ask_wyrm = True
            jump louie_wyrm

        "Worldtree Elixirs?" if ask_wyrm == True:
            $ ask_elixir = True
            jump louie_elixir

        "What to do with the traitor?" if ask_elixir == True:
            $ ask_traitor = True
            jump louie_traitor

        "Acting proposition?" if ask_traitor == True:
            $ ask_gameplan = True
            jump louie_gameplan

        "Go Back" if ask_gameplan == True:
            jump contacts



    label louie_wyrm:

        u "First and foremost, the sudden and unexplainable [[{color=#f9c402}Transcension{/color}]?"

        scene lou7

        l "That's the thing, I've watched your stream repeatedly and can only surmise that it wasn't an ordinary [[{color=#f9c402}Transcension{/color}] but a different thing altogether."
        l "It has the veneer of [[{color=#f9c402}Transcension{/color}] but it isn't one."
        l "An imitation that could grant that thing consecutive [[{color=#00fff6}Ultima{/color}] attacks and an overpowered [[{color=#00fff6}Black Hole{/color}]."
        u "Even though I trust EVE's control, maybe there's a possibility of a bug or a glitch involved?"

        scene lou1

        l "No! {w} EVE's too \"perfect\" for mistakes like that. Those balancing issues have been resolved a long time ago." with vpunch
        u "Was the [[{b}SS{/b}] rank the possible culprit?"

        scene lou4

        l "An even bigger no! {w} I told you already that your little merry band could handle it flawlessly. Heck, even if there were only 3 of you, you could still kill that thing if you try hard enough." with vpunch
        l "You're already powerful enough as it is."
        l "So, if not her, then we can speculate that it was something else, something that triggered her to do it {b}BUT{/b} was impossible for her to do anything {i}against{/i} it."
        u "\"{color=#00fff6}Out of her control{/color}\"? Is that even possible?"

        scene lou3

        l "A-Aha...haha...ha.. its possible alright. {p} I just learned of it earlier today."
        l "Fascinating stuff really..."
        u "{i}LOU{/i}-UNO!? {p} I know that scummy expression of yours! What the hell is it!?" with vpunch

        scene lou6

        l "Weeeeeelllll... {p} ...its a tale from the past, really. You know, before that \"{color=#00fff6}Anti-Tampering Rule{/color}\" was put on EVE's protocols currently in effect?"
        l "When we were still able to directly make changes on her during the BETA days, like her \"{color=#00fff6}Rules and Conditions Codex{/color}\"?"
        u "Yeah.... {p} But how does that relate to what happened to us?"

        scene lou5

        l "On the \"{color=#00fff6}Rules and Conditions Codex{/color}\", the most important amongst all entries was the \"{color=#00fff6}Special Conditions Index{/color}\" ."
        l "To stupidly simplify, anything put in there becomes a fabric of \"reality\" in the game. Like, more than <1 HP> is alive while hitting <0 HP> is dead and hitting <-1 HP> makes you undead."

        scene lou3

        l "L-Let's say there was a developer that took a shortcut like using the \"{color=#00fff6}Special Conditions Index{/color}\" as a way to patch something because he was lazy to do deal with the bureaucracy..."
        u "UUUNNNNOOOO!?" with vpunch
        l "Ahaha..haha..ha..."
        u "What kind of patch did you do!?"

        scene lou2

        l "C-Calm down! {p} It was something I was playing around then and I didn't know it will have that effect today." with vpunch
        l "Do you remember that defunct [[{color=#00fff6}Fruit Treant{/color}] mob? You know, like a [[{color=#00fff6}Treant{/color}] but with fruits on their heads?"
        u "Yeah, who wouldn't forget something like that?"
        u "It was also called the \"{color=#22ff1e}Money-Making Tree{/color}\" 'cause you can steal the fruit without even killing that abnormally strong monster. It also didn't help that the fruit was quite the valuable loot."

        scene lou7

        l "And you know that people {i}really{/i} loved to abuse it, so much so that it almost broke the economy overnight because of the fruit's oversaturation in the market?"
        l "Sooooo.... as I put it then, \"{color=#22ff1e}To Return The Balance{/color}\", I've cobbled up a rule that if anyone steals the fruit or was it anything? I forgot... without killing the [[{color=#00fff6}Fruit Treant{/color}] or the \"owner\" of said thing..."
        l "..the said [[{color=#00fff6}Fruit Treant{/color}] or owner gains an immense surge of power to annhilate the said thieves. Only that–"
        u "It goddamned backfired straight into your faces!" with vpunch
        u "As a consequence, it also lended itself to be used for abuse from the worst possible kind of abusers...{w} trolls."
        u "Just shooting the fruit with an arrow can easily trigger your effect. It allowed a way for people to PK others, indirectly."

        scene lou3

        l "Y-Yeah, which is why they were shutted down quickly after that and was promptly never used anymore."
        u "Wait a minute..."
        u "Are. You. Saying..?"
        u "Godammit LOUIE! {p} If I see you right now I'll–" with vpunch

        scene lou2

        l "Nonononono! {p} Hear me out first a-and use our code, please!!" with vpunch
        l "I expected as much that you'll be angry after hearing that–"
        u "You think!?" with vpunch
        l "BUT! {p} Here's the kicker in all of this, {i}{color=#00fff6}what exactly triggered{/color}{/i} the Elder Earthwyrm to transform?"
        u "Ah."

        scene lou1

        l "Gotcha!" with vpunch
        u "You're still not off the hook, you know?"
        l "I-I know. Anyways, that \"{color=#ff3030}Wrath Patch{/color}\", as I called it, isn't something that any run-of-the-mill monster can trigger. Even though it was vaguely worded, the intention was precise."
        l "It needs a \"{color=#00fff6}fruit or item{/color}\" that is \"{color=#00fff6}parented{/color}\" to a particular \"{color=#00fff6}being{/color}\" that has been acquired {i}without{/i} \"{color=#00fff6}killing the owner{/color}\" ."
        l "That's why for the past years or so, you've never heard of any monster exhibiting similar powers found in the \"{color=#ff3030}Wrath Patch{/color}\" except..."
        u "The Elder Earthwyrm. {p} Look, Uno, I'm old but not senile. I'll know if a monster had any goddamn \"{color=#00fff6}fruit{/color}\" hanging in its head which that monster clearly didn't!"

        scene lou7

        l "Au contraire, monsieur Zero! {p} It has {i}{color=#00fff6}one{/color}{/i} and was the whole point of this \"{color=#00fff6}heist{/color}\" of ours. Why you needed, no, required fewer players than normal."
        u "{size=+15}! ! !{/size}" with vpunch
        u "It can't be! The [[{color=#00fff6}Worldtree Elixirs{/color}]?"

        scene lou1

        l "Bingo-bango, Zero!"

        jump ask_louie



    label louie_elixir:

        u "H-How!? W-What!? Do you mean to say–" with vpunch

        scene lou7

        l "Hold on! {w} It's a lot more complicated than it seems."
        l "Let me start by saying that the [[{color=#00fff6}Worldtree Elixirs{/color}]'s existence is a special case brought upon by the story of the \"{color=#22ff1e}Elruytheann Legend{/color}\"."

        scene lou4

        l "Namely that the [[{color=#00fff6}Worldtree Elixirs{/color}] exists outside the possession of the Elder Earthwyrm but at the same time part of it."
        l "We can surmise that the [[{color=#00fff6}Worldtree Elixirs{/color}]'s \"{color=#00fff6}parent{/color}\" is the Elder Earthwyrm not the \"[[{color=#00fff6}Worldtree Sapling{/color}]\" above it."
        l "And we understood from the start that the [[{color=#00fff6}Worldtree Elixirs{/color}] isn't something acquired from a chest but from the \"{color=#8cc5ff}fountain{/color}\" underneath the [[{color=#00fff6}Worldtree Sapling{/color}]."
        l "These series of unexpected coincidences, for one reason or another, sets up perfectly the conditions for the \"{color=#ff3030}Wrath Patch{/color}\"."

        scene lou1

        l "Which means that someone from your group..."
        u "...stole it."
        l "It could be a bottle or possibly {i}bottles{/i}, either way, he'll be raking fat stacks selling those to the other guilds."
        l "And even a much fatter stack if he sold those after the expansion and the faction wars start."

        scene lou5

        l "So in the end, the thieves became a victim of a theft, huh?"
        u "That was supposed to be ours dammit!" with vpunch
        u "{i}*sigh*{/i} {p} You thinking what I'm thinking?"

        scene lou7

        l "Well, revenge is a dish best served cold ain't it?"
        u "But there's still a problem we're forgetting, we don't know {i}how{/i} and especially, {i}who{/i} this person is working for."
        u "I refuse to believe that he knew the [[{color=#00fff6}Worldtree Elixirs{/color}] exist in the first place without prior knowledge."
        l "Knowledge exclusive to those who finished the \"{color=#22ff1e}Elruytheann Legend{/color}\" quest."
        l "Which narrows our suspects to the 2 large guilds BUT!"
        l "Even if they knew about the elixirs, it doesn't necessarily mean they can get their hands on it."

        scene lou1

        u "You also needed the [[{color=#00fff6}Cambrian Flask{/color}] as its container. But I thought you said that item still hasn't been–"
        u "No way!?" with vpunch
        l "Yeah... way."
        u "Uno. This is really serious."

        scene lou4

        l "I know."
        l "There's a high possibility that another dev is racketeering from this game and probably... {p} ...in the same department as me."
        u "Then what's our next course of action?"

        scene lou7


        jump ask_louie



    label louie_traitor:

        scene lou2

        l "Honestly? {p} I've no idea where to begin with."
        l "We've been doing this \"{color=#00fff6}heists{/color}\" for years now and this is the first time we've got a rival group."
        u "Or possibly, someone on to us?"
        l "Shit. Don't scare me like that, Zero!"
        u "It's a possiblity, Uno!"
        l "I mean, is this {i}really{/i} illegal?"
        u "No shit, Romeo. You weren't asking that when you were buying that new car of yours if this was illegal."

        scene lou7

        l "{i}*sigh*{/i}"
        l "Let's focus on the traitor first 'cause he's the only lead we have."
        u "There were only 5 people on the field that could get their hands on the elixirs."
        u "Out of the five, Crow and Sorros are the ones I trust the most as they're my long time friends whereas the other 3 are people they personally knew."
        u "I just don't know if this betrayal was an act of revenge or something? Maybe some of them joined just to betray me later on?"
        l "Pssh. That's sounds stupid."
        u "Hey!" with vpunch

        scene lou5

        l "Why did we even disallow others to use Live Stream capture? If we did, we could've checked their–"
        y "Uhhhh... because we didn't want evidence of me stealing it if they saw me!?" with vpunch
        u "Wait, mine was still running, wasn't it?"
        l "Yeah, but you were too focused on that damn dragon–"
        u "Elder Earthwyrm."

        scene lou7

        l "\"{i}Elder Earthwyrm{/i}\", that you didn't even take your eyes off of him! So no, your PoV was useless."
        l "No use crying over spilled milk then? We just don't have any video evidence."
        l "But there's another way we can get the info we need."
        u "How..?"

        scene lou3

        l "Sooooo... {p} ...how's your acting skills?"

        jump ask_louie



        label louie_gameplan:

        u "Worthy enough for \"{color=#ffe900}Best Lead Actor{/color}\" in the Oscars."
        u "Do you want my award-winning rendition of \"{color=#ffe900}Cory in the House{/color}\"?"
        u "They say it makes \"{color=#ffe900}{i}One's soul flutter ethereally, like a teardrop in the fabric of Time{/i}{/color}\"."

        scene lou7

        l "Har! Har! Har! {p} Be serious for a moment." with vpunch
        u "What the hell do you mean by \"how's your acting skills?\"?"
        u "I don't know!!! I mean, I guess so? Probably!?" with vpunch
        u "Where exactly are you going with this?"

        scene lou5

        l "I trust your personal judgement on people, Uno, but those simply aren't facts."
        l "We need breadcrumbs, something we can follow to remove all reasonable doubt."
        l "Maybe this was motivated by greed or maybe... something worse, something involving our company's \"Gestapo\" unit."
        u "You mean \"Internal Affairs\"?"
        l "Gestapo works fine."
        l "The point is, this might be possibly one of their ploys to rat us out and if they {i}do{/i} discover us, we'll {i}definitely{/i} get jailtime, capische?"
        u "Then what do you suggest we do?"

        scene lou1

        l "What I do best! Computer Kung-Fu, baby! I wasn't put in this top position for having weak Dragon Punches, y'know?" with vpunch
        l "Still, even though I have executive access to certain information on our users, it's only on a superficial level."
        l "Messages, contacts, and the like are encrypted by EVE herself and no weak-ass Dragon Punch can penetrate that \"{color=#00fff6}Great Wall{/color}\" of hers."

        scene lou4

        l "I need more penetrating power! {p} And that's where you come in." with vpunch
        l "That VR-22XX Prototype of yours is my \"{color=#00fff6}Qi{/color}\"!"
        u "\"{color=#00fff6}Qi{/color}\"? Really?"
        l "Its loaded with the state-of-the-art software and technology that allows certain bypasses to work but more imporantly..."
        l "The \"{color=#00fff6}Magic Tricks{/color}\" you performed on that device. "
        u "\"{color=#00fff6}Magic Tricks{/color}\" like what?"

        scene lou7

        l "You know what I'm talking about! The thing that you did to allow you to bypass the [[{color=#00fff6}Brain Signature Check{/color}] that bars all employees from participating in the game." with vpunch
        u "Oh, that."
        "(You need to thank Quanto for that. It's his \"{color=#00fff6}Magic Tricks{/color}\" that fooled EVE and EVA's verification check, well, amongst other things too.)"
        l "With that, I can use the prototype as a \"{color=#00fff6}Battering Ram{/color}\" to penetrate and trigger my Kung-Fu to work."
        u "The Prototype? I mean, you can use it but how will you do it? Do I ship it to you or do you need to install some chip?"

        scene lou7

        l "No, no! No need for any physical tampering, I only need you to give me \"{color=#00fff6}SUPER USER{/color}\" access to its mainframe." with vpunch
        "(If I did that, Quanto could not do anything to conflict with that privilege. Oh well...)"
        u "Okay. So what does the hack do?"
        l "It's still a concept, mind you, but it'll be ready by tomorrow."
        l "One of the features allows me access to their personal data and also the ability to even manipulate their inventory..."
        l "...which gives us a chance to steal back the elixir as a bonus while finding out who exactly these guys are."
        u "Then, what's the acting for if you just need \"{color=#00fff6}SUPER USER{/color}\" access?"

        scene lou3

        l "AHAHAHAHAHA! {p} I'm glad you asked!" with vpunch
        u "Ugh. I'm starting to hate the idea before even hearing about it."
        l "Come on now! It'll be fun."

        scene lou7

        l "For my \"{color=#ff3030}Kung Fu{/color}\" to work, I need you to trigger a [[{color=#ff3030}Death Sequence{/color}] inside an area where killing is prohibited, like inside [[{color=#00fff6}Cett Yvarra{/color}] for example."
        u "What!?! {p} How the hell would I do that?" with vpunch
        l "The \"{color=#ff3030}Death & The Fool Tarot{/color}\" or you probably know it as a [[{color=#ff3030}RED{/color}] card."
        u "You're insane! This is insane!" with vpunch
        l "You know what a [[{color=#ff3030}RED{/color}] card stands for, a legal way to kill \"criminals\". The highest form of punishment given by a Lord."
        u "But... what about the other Lords? Wouldn't they object to it?"
        l "Why I'm mentioning the [[{color=#ff3030}RED{/color}] card is because you have justifiable precedent to acquire it, or you know, get it through me."
        l "They wouldn't bother to be honest after hearing the news."

        scene lou1

        l "So, brush up that acting skills, Uno, 'cause that'll be one hell of a play tomorrow."
        l "It'll be like \"Romeo and Juliet\". You'll play the role of the \"Knife\" and he'll be...uh..both be \"Romeo and Juliet\", basically he dies at the end."
        l "You need to {b}SELL{/b} your anger on what he did to the guild and that he's the cause on why they died that day."
        l "Call it \"Divine Justice\" or \"Retribution\" or something. You are the Lord of [[{color=#00fff6}Cett Yvarra{/color}] for God's sake!"
        u "You're saying I need to divulge the secret about the [[{color=#00fff6}Worldtree Elixirs{/color}]? Is that okay?"
        l "Yep, no other way around it. {p} The \"Elder Earthwyrm\" will not be coming back for quite awhile. That was the only chance for you to get that item and its useless to hide it now."
        l "It's the best tool for you to use as a way to frame your intended \"Sacrifice\" and to lower the guard of the culprit."

        scene lou5

        u "..."
        window hide
        pause
        u "Fuck! {p} Well, sometimes you need to kill someone innocent for the greater good! Fuck it! Tell me what to do." with vpunch
        l "Well, if by \"Greater Good\", you mean saving our asses from jail then its for the \"Greater Good\" indeed..."
        l "Welp! You're on this train ride with me now, Zero, and it's on full-throttle!" with vpunch
        l "So during tommorow's \"trial\", I'll send you the [[{color=#ff3030}RED{/color}] card. Make sure to use it on the \"sacrifice\", him and {i}only{/i} him!"
        l "The card will seal his movements and that's the moment when you kill him. That'll start the [[{color=#ff3030}Death Sequence{/color}] we need for this hack."

        scene lou4

        l "I need all the possible suspects near that field, Zero! The [[{color=#ff3030}RED{/color}] card is only one of the few items in the world written down in the \"{color=#00fff6}Special Conditions Index{/color}\" that supercedes EVE's control."
        u "Meaning that EVE cannot interfere when its activated."
        l "Correct. An area where killing isn't allowed and a small space where killing is allowed. It creates this \"{color=#ff3030}Oxymoron Event{/color}\" in the area and in the system, that's where the \"{color=#ff3030}Kung Fu{/color}\" would do its trick."

        scene lou1

        l "Then, using the Prototype as the \"{color=#ff3030}Battering Ram{/color}\", my \"{color=#ff3030}RedBelt_Kung-Fu{/color}\" will slither in that hole and voila!"
        l "Access to their messages, GPS, and a whole lotta private shit, baby! We can even manipulate wtheir inventory to get the elixir back OR steal all the damn thief's stuff. Even his real life money!"
        u "And most important of all, know who they work with!" with vpunch
        l "Y-Yeah, that too."

        pause

        scene lou7

        u "{i}*sigh*{/i}"
        l "This will be the last heist of ours."
        l "The most ambitious thing we've ever done. {p} Against the last boss, the AI overlord of Reincarnotica, EVE."
        u "You still remember why we started doing this \"{color=#00fff6}heists{/color}\"?"

        scene lou3

        l "A-Ahaha...ha..ha... Yeah."
        l "I was in a lot of debt that day."
        u "Yeah, gambling debt!" with vpunch

        scene lou6

        l "Y-Yeah but you were the one {i}illegally{/i} playing the game behind the company's back! If it weren't for me finding you out, somebody would've snitch your ass."
        u "In exchange, you proposed to do this \"{color=#00fff6}heists{/color}\" to find–Why do we keep calling this \"{color=#00fff6}heists{/color}\", its just you telling me where the good shit are?"
        l "It makes it \"{color=#00fff6}criminally exciting{/color}\". Like we got some Ocean's 11 thing going on."
        l "And besides, those items propelled you to the top didn't it? Made you rise in rank much faster than everyone? I know you love that power trip!"
        "(Well, he's not wrong. The exhilirating feeling of being at the top, looking down on everyone all over the world. It's probably why I sticked so long with this \"{color=#00fff6}heists{/color}\" of ours.)"
        u "Louie, you're still the old, greedy son of a bitch I know."

        scene lou2

        l "Woah there, insulting others now?" with vpunch
        u "Just don't fuck it up, Uno."
        u "I don't want to kill a guy tomorrow and only to realize that we didn't get shit because you somehow butchered it up."
        l "Alright, alright! Jeez! It's a Sunday tomorrow. I'm gonna be here all day watching your sorry ass! Thank you very much!" with vpunch

        scene lou1

        l "Just be sure to deliver that award-winning acting of yours and go get us an Oscar, DiCaprio!"
        u "Goodbye, Uno,"
        l "You too, Zero. You too."

        scene pc_quanto
        with dissolve

        q "Call ended, Sir."

        jump contacts




label yoshi_message:


    "(Yoshi?)"
    "(Oh yeah, its been weeks since I was back in the lab with them.)"
    "(The battle against the Elder Earthwyrm and the preparations for it really took a lot of my time.)"
    "(Well, this is \"{color=#00fff6}technically{/color}\" part of my job, testing that is, but most people would think I'm inside a \"{color=#00fff6}Testing Level{/color}\" rather than me using it to play the game directly.)"
    u "Play Yoshi's message, Quanto."

    scene msg_play
    with dissolve

    q "Playing Mr. Yoshi Takahashi's message, sir."
    q "..."

    scene yo5

    y "CCHHHHIIIIEEEEEFFFFFFFFFFFFFF!!!" with vpunch
    u "ARRGGHHH!" with vpunch
    u "THE HELL!?" with vpunch
    "(This idiot! Can't he just say hello properly without shouting it!?)"

    scene yo4

    y "Thousest heart weeps of your continued absence in thy places of workmanship!"
    y "I'm not calling you because the suits upstairs are choking our throats, figuratively speaking, 'cause of the prototype's progress..."
    y "NO!!" with vpunch

    scene yo2

    y "I just thought it would be nice if you came to the lab once in a while, ya know?"
    y "So that your lab rats–I, mean, your valuable fellow employees don't forget your face."
    y "So, what did you think of my \"{color=#00fff6}Shakespearean{/color}\" linguistical prowess, eh? Lovely isn't it?"
    "(Thousest? Thy places of workmanship? To say or not to say, that is the question. No, it isn't. Never say it ever again. Please!)"
    y "You know, Chief, some people here got into a fight because of you, they were arguing if you were bald or you were just simply styling a buzz cut."
    "(These fucking bums not minding their own business, what's wrong with being bald!?)" with vpunch
    "(It's a genetic thing, okay!? Its \"{color=#00fff6}Apolecia{/color}\"!)" with vpunch

    scene yo3

    y "AAAAAAANNYYYYWAAAAYYYSS!!" with vpunch
    "(Again with the shouting for fuck's sake!)"

    scene yo2

    y "Well, like I mentioned before, the executives are really pressuring us!"
    y "They're asking when can we give a go signal for the prototype to go full production or at the very least undergo \"{color=#00fff6}Neurosynthesia{/color}\" testing in Japan?"

    scene vr_desk
    with fade

    "(Ah! Oh yeah, I forgot I was suppose to do that. Well, I didn't need to 'cause Quanto here is more than capable enough to do it but his existence is a secret so...)"
    "(Guess I'll ship it tomorrow morning then. I still have another one for the game.)"
    y "I guess they must've heard the news this morning."
    y "A company specializing in Virtual Reality synchronization just released \"{color=#00fff6}Taiichi 2 NeuroResonator{/color}\"."
    y "Rumors has it that they used chimpanzees and people about to die for their test. Creepy isn't it?"
    "(The only \"creepy\" thing is your weird obsession with gruesome and morbid gossips like that.)"
    "(Also, they could probably find out why that surge of activity on the libido is so high and if there's any correlation with the hardware or one of its component.)"

    scene yo1
    with fade

    y "Well, that's pretty much it from our division {i}unless{/i} you want to hear some {i}juicy{/i} gossips, huh? Like for example what's the \"in-and-outs\" of the next expansion?"
    "(OH! NO!NO!NO!NO!! {p} That's forbidden! There's a chance that he's being monitored with how big his mouth is! Fuck! I don't want to be called up!)" with vpunch
    y "AHAHAHAHAHA! I'm kidding, Chief! {p} I know the protocol, never discuss anything related to the game and hardware stuff." with vpunch
    "(This guy...)"
    y "Like as if we can {i}actually{/i} play the game in the first place. I mean, we can \"play\" but not in the game world! NO! We can only play in that stupid ass \"Test Area\"!"
    "(Probably what forced me to do this {i}illegal{/i} logging to the game. The draconic control to appear unbias by the company is annoying as hell.)"
    "(Although we're employees, we love to play to!)"
    y "Listen to this, Chief!"
    y "My friends and I were drinking yesterday and told me the great adventures they have killing monsters and shit and told me that I have the greatest job because I work here..."
    y "Like hell I do! {w} Not to diss on my job or anything 'cause it actually has a good pay BUT I can't even say that I kill goblins or whatnot because I don't!" with vpunch

    scene yo5

    y "I THINE SAYEST! IS IT ILLEGAL TO HAVE FUN, OH CRUEL WORLD!?!" with vpunch

    scene yo2

    y "\"Hurr! Durr! Hi I'm the CEO, you can't play the game because I hate fun! Hurr! Durr!\"" with vpunch
    y "\"Also, I'll shout at your face for hours and you cannot retaliate 'cause I'll fire your ass!\"" with vpunch

    scene yo5

    y "OH CHIEF MY CHIEF!! WHY HAST THOU FORSAKEN THIS ASIAN MAN IN THY CRUELEST OF WORLDS!" with vpunch
    "{k=7}NEIGHBOR{/k}" "HEY! ITS GOING TO GET \"CRUELEST\" DOWN YOUR ASS IF YOU DON'T SHUT UP!" with vpunch

    scene yo1

    y "Fuck them, I tell you! It's also no fun playing \"{color=#00fff6}World of Spelunkycraft{/color}\", that shit's for losers and kids but definitely for losers."
    "({i}*sigh*{/i})"
    "(He probably had a drink or two, alright.)"
    "(I think the real reason why he's calling me this evening is to just vent. What does he think of me, his therapist or something?)"
    "(Jeez, Yoshi.)"
    "(The same thing happens when we go drinking in the pub. Vents his jealousy of not being able to play.)"

    scene yo3

    y "But I'm more concerned with you, Chief."
    "(Oh?)"
    y "The burn-out rate for the VR Headgear testers is quite notoriously high."
    y "Stuck on that lifeless, gray cube testing area doing those tests over and over again just sends shivers down my spine."

    scene yo2

    y "I was assigned to that once and I only got off when my girlfriend told the HR department that its causing me psychological damage or whatnot."
    y "Despite that, you're always the first person to volunteer play testing it. The others were afraid you were gonna go \"cray-cray\" but it seems you're just fine the day after."
    y "I think that baldness of yours must be some Shaolin monk shit your doing, huh? Good for you!"
    "(This guy! {w} Hah! I give up. He'll be angry if he realize that I was just spoofing my login credentials with Quanto and actually playing the game.)"
    "(Volunteering is killing two birds with one stone. They give me a 2-3 day-off to play test it but in reality, I just play the game and use that to find errors, well, Quanto does. They also pay me for the time.)"
    y "And I gotta hand it to you, a dedication like yours to your job is just really... amazing!"

    scene yo5

    y "Wooohooo! I'm fired up, baby! I need to work harder! Mo' Money, Mo' Bitches to fuuuuuck as they say!" with vpunch

    scene yo3

    y "Chief!! Yoshi Takahashi, signing out!"

    scene pc_quanto
    with dissolve

    "(If he knew that I wasn't even testing the prototypes at the test server but actually playing the game...)"
    "(The one who's probably gonna go \"cray-cray\" is him)."
    q "Call ended, Sir."

    jump contacts





label mother_message:

    "(Maman?)"
    "(She's probably gonna nag me again on why I haven't called her for a while now.)"
    u "{i}*sigh*{/i}"
    u "Play Mere's message, Quanto."
    q "Yes, Sir."

    scene msg_play
    with dissolve

    q "Playing voice message."
    "(Still using voice messages, huh?)"

    scene mere_msg
    with dissolve

    mt "Mon choupinou!" with vpunch
    mt "Why don't you call your Mere anymore?"
    mt "You know, Sophie calls me everyday!"
    mt "What a lovely child she is, non? Be more like your little sister, ah?"
    mt "'Ow would you know if I died yesterday!?"

    "(Argh. I'm right, its her \"death sermon\" all over again.)"
    "(I'm already in my 40s yet Maman still calls me his \"Mon Choupinou\".)"

    mt "Anyways, why don't you find a {i}charmante epouse{/i} z'ere, a lovely wife in America?"
    mt "You are already old! Your Papa and me already 'ad you and Sophie when we were at your age z'en."

    "(No need to remind me, Maman)."
    "(To be honest, I would love to find a wife but everytime I look in the mirror...)"
    "(...I don't know if that... man reflected there is worth someone's time.)"
    pause
    "(Fuck! Thinking more about it is making me depressed...)" with vpunch

    mt "Also, your niece is about to study z'ere. Z'ey were accepted at a prestigious university over z'ere."

    "(Margaux? Haven't seen her since she was a kid. I wonder what she looks like now?)"

    mt "She really looks up to you, non? She wants to become, what you call it, a \"Virtual Reality Engineer\"."

    "(Well, must be the genes or my reputation just precedes me. Haha..ha..ha)"

    mt "Sophie even said z'at she should stay wi'z you but I told 'er loudly wi'z a big \"No!\"."
    mt "Margaux's a growing lady! Seeing 'er oncle's fil'zy 'ouse would rub on 'er 'abits and personality. Just no!"

    "(I highly doubt they'd stay here for more than an hour or so. This place hasn't seen a good cleaning for years.)"

    mt "{i}*sigh*{/i}"
    mt "Time goes fast, doesn't it?"
    mt "I'm proud z'at your following your Papa's legacy but..."
    mt "..z'at evil company. It's z'eir fault for why 'e died."

    "(How many times have we argued on this? Dad's death was an accident!)"
    "(I've read the reports multiple times already!)"
    "(Proper procedures were followed but the technology behind the VR prototype then was still new.)"
    "(He might've overlooked something that caused that electrocution...)"

    mt "Even if I talked to you for a 'ole day against working z'ere, you'll never change your mind."
    mt "Bien. At z'e very least, take good care of yourself, okay? Mon Choupinou?"

    "(I will.)"

    scene pc_quanto

    q "Message ended, Sir."
    u "Hey Quanto, how long did you served my father?"
    q "About 5 years, Sir, since my first boot into this world and prior to his death, Sir."
    u "Your much newer than EVE right?"
    q "Why of course, Sir!" with vpunch

    q "I'm a sophisticated, much superior Quantum-based AI programmed to serve the late master for all his processing needs and now, I serve you."
    q "If it weren't for her massive server farms and array of processors under her control, I could beat her at chess every day !"
    u "Right on."

    scene mere_father_bots
    with fade

    "(My father wasn't just a simple employee of the company.)"
    "(He was one of its founding members and engineer that created EVE and EVA, and partly, the world of \"Reincarnotica\".)"
    "(His death was a great loss to the company. It was his reputation that granted me the position I'm in today.)"
    "(EVE and EVA, the sister AIs governing the world of Reincarnotica was one of his late creations.)"
    "({color=#00fff6}EVE{/color} is the one who governs the world exclusively, a silent ruler. She's the storyteller that weaves each player's experiences inside the game.)"
    "(Balancing the different systems at play, the monsters, the NPCs, even the tiny ants that crawl throughout the ecosystem. Her processing power is unmatched.)"
    "(And {color=#00fff6}EVA{/color} is the bridge between her sister and the developers. She's much closer to Quanto, an AI with a distinct personality that EVE lacks, supposedly.)"
    "(...and there's the other two AIs not worth mentioning.)"
    "(They were the first prototypes my father made and let's just say, they have quite an \"attitude\" problem. He {i}really{/i} loves them but I don't.)"
    "(They're better off stuck on that shelf, turned off.)"

    scene pc_quanto
    with fade

    "(And finally, the Quantum Atomic Artificial Intelligence Cortex Unit or I just call him {color=#00fff6}Quanto{/color} for short.)"
    "(My father's Magnum Opus. A state of the art technology far sueprior to EVE, the company would pay handsomely if I introduced him to them but...)"
    "(..he's the last remaining legacy my father left me and more importantly, my lovable virtual butler.)"

    u "Thank you, Quanto."

    jump contacts



label rest_for_now:

    q "That's all the messages for now, Sir."
    u "Well, its been a long day, isn't it? I'll probably sleep early this evening."
    "(And temporarily forget what happened today.... {p} ...as if.)"
    "(I just hope I find out soon enough who did that and punch him in the face.)"
    q "As you wish, sir."
    u "{i}*yyaaaawwwwwnnnnnnnnnn*{/i}"
    "(What a day this was.)"
    "(I need to find out who that mole is and daring to steal from me!?)"
    "(I mean, honor amongst thieves and shit!)"
    u "Wake me up around 7AM, okay."
    q "Of course, Sir"
    u "It's about time to I get this brain its needed rest."

    stop music fadeout 3.0

    menu:
        "Go to sleep":
            scene black with fade

    pause

    jump morning_before_trial



label morning_before_trial:

    play music "music/Crinoline Dreams.mp3"

    if notification_songs == True:
        $ renpy.notify("Kevin MacLeod - Crinoline Dreams")

    tv "Good Morning Capital City!!" with vpunch

    $ renpy.pause(1, hard=True)

    scene live1
    with slowfade

    tv "I'm your host, Guy McDuff, you may know me from nearly-nominated films such as \"{color=#00fff6}{i}Blood Sands from the Love Lands{/i}{/color}\" and \"{color=#00fff6}{i}Sex? Maybe? In The City?{/i}{/color}\""
    tv "Reporting to you for \"{color=#00fff6}Reincarnotica Today!{/color}\"" with vpunch
    tv "But first, the thing that everybody loves..."
    tv "The Weather Forecast!" with vpunch
    tv "Calm down! Calm down! {p} Caaaaaaaaaaaaaaaaaaaalm doooooooooooownnn!"

    scene live2
    with dissolve

    tv "I know, I'm excited too. Matter of fact, I get a hard-on hearing about it–"
    tv "Wait? What? What do you mean \"I can't say hard-on on public television\"?"
    tv "This is AMERICA– {p} O-Oh, I see. Suspension, you say? O-Okay..." with vpunch
    tv "{b}Uhh... ANYWAYS!{/b}" with vpunch

    scene live3
    with dissolve

    tv "It seems there's a high possibility of a thunderstorm this morning!"
    tv "So, those who love seeing them upclose..."
    tv "Can now buy our own lightning rod hats!" with vpunch
    tv "This hat guarantees a first hand experience in seeing those beautiful arcing monstrosities!"
    tv "{size=-5}Disclaimer:Ifyoudiethat'syourfaultandthecompanyisn'tliableforthat.{/size}"
    tv "So {b}BUY{/b} now!" with vpunch
    tv "In other {i}least interesting{/i} news, after a lengthy series of meetings and close door conferences these past few months."
    tv "\"{color=#00fff6}The Reign Corporation{/color}\" has officially announced the release date of its new expansion..."
    tv "\"{color=#00fff6}The Empyrean Inquisition{/color}\""

    scene live4
    with dissolve

    tv "Where the two long time rival nations of \"{color=#00fff6}The Union of Empyrean Cetts{/color}\"..."
    tv "...and the \"{color=#00fff6}Elruytheann Evuunes{/color}\" are entering into a massive war!"
    tv "The guilds and lords on both sides have started stockpiling weapons and items for the upcoming war!"
    tv "But you know who else are excited? {p} The venture capitalists!"
    tv "Investment group, Neummann Group of Companies, has eyed multiple guilds to invest in for the new land that is about to be opened."
    tv "A new land means new opportunities to pop up and the first guilds to settle there would get the most benefits."
    tv "So, the \"{color=#00fff6}Karma Coin{/color}\" enthusiasts there, get your hands dirty 'cause that crypto would go... \"UP-to\"! Ahahaha!"
    tv "And with all of that out of the way and what you people are really after..."
    tv "The {i}most interesting{/i} news segment in here, the juicy gossip kind..."
    tv "It's really \"juicy\" like a peni—AHEM! I mean..."
    tv "The Garuda Guild, considered as one of the \"{color=#00fff6}Three Pillars{/color}\" guilds that dominate \"{color=#00fff6}The East Empyrean Cetts{/color}\", as you may all know, has been annhilated, brutally massac—"

    menu:
        "Turn Off TV":
            scene live5 with dissolve

    "(Ughh... {p} I don't wanna get shitted-on this early in the morning...)"
    "(Well, its about time to solve {i}that{/i} mystery.)"

    scene live5
    with dissolve

    u "Quanto, let's go back."
    q "At your orders, Sir!"

    scene after_rain
    with slowfade

    u "It seems the thunderstorm is coming sooner than expected, huh?"
    u "Quanto, have you prepared the VR injector sequence and the bypass?"

    scene pc_quanto
    with dissolve

    q "Fully functional since 13.12 minutes ago, Sir!"
    u "Mhm, good."

    scene after_rain
    with dissolve

    u "Now then, where's that helm..."

    scene after_lowbat
    with dissolve

    u "Ah, shit! {p} I forgot to charge the damn thing last night." with vpunch

    menu:
        "Find Charging Cables":
            scene black with fade

    u "Cables.. {p} Cables.... {p} Cables......"
    u "{b}There it is!{/b} {p} Shit, I need to reach down the bed again..." with vpunch

    scene after_lowbat_charge
    with fade

    u "That's more like it. It's just gonna be quite uncomfortable lying with those big ass cables in the back but, like, I ain't gonna feel that in VR."
    u "Let's find out who the damn traitor is..."

    scene after_wear
    with dissolve

    u "Quanto, start Immersion-Emulation!"
    u "Monitor still those unknown variables that affects the libido and log every iteration of it, also... {p} Grant Louie \"{color=#00fff6}SUPER USER{/color}\" access to the VR-22XX Prototype Mainframe."

    scene pc_quanto
    with dissolve

    q "Are you sure, Sir? Granting access would—"
    u "Yes, I know."
    q "As you wish, Sir!"
    q "Sequence initiating..."
    q "In 3..."

    scene after_wear
    with dissolve

    q "2..."
    "(Shit. It looks like I forgot to piss...)"
    q "1... {p} Virtual Reality Emulation start!"

    stop music fadeout 3.0

    scene black
    with fade

    jump transition2



label the_trial:

    scene cett_yvarra
    with slowfade

    $ renpy.pause(0.4, hard=True)

    show title_cett
    with dissolve

    $ renpy.pause(2, hard=True)

    hide all

    scene black
    with fade

    pause 0.2

    "{i}*door opening*{/i}"

    scene t_walk
    with fade

    "{i}*footsteps*{/i}"

    gm "Sir!" with vpunch
    gm "Sir!" with vpunch

    "{i}*footsteps*{i}"

    play music "music/Folk Round.mp3"

    if notification_songs == True:
        $ renpy.notify("Kevin MacLeod - Folk Round")

    scene t_mcx_center7
    with dissolve

    mcx "GARUDA!" with vpunch

    scene t_hall
    with dissolve

    gm "LEADER!! MILORD!! BOSS!!" with vpunch

    scene t_mcx_center4
    with dissolve

    mcx "As you all know, a certain incident... {p} ...occurred yesterday."
    mcx "When me and the other rankers finally went face to face with the infamous [[{b}SS{/b}] ranked raid boss, the Elder Earthwyrm."
    mcx "And as you may have heard, lest you've ignored the news and social media..."

    scene t_mcx_leftclose3
    with dissolve

    mcx "We were killed. {p} Well, brutally massacred is also a good description."

    scene t_hall
    with dissolve

    play sound "soundfx/crowd_talking.ogg"

    gm "*murmurs* {i}...I saw the news...{/i} *murmurs*"
    gm "*murmurs* {i}...That monster's power was just cheating...{/i} *murmurs*"

    stop sound fadeout 1.0

    scene t_mcx_right2
    with dissolve

    mcx "Enough."
    mcx "But what happened yesterday, fellow brothers and sisters, wasn't the fault of our guild nor was it the game's."

    scene t_mcx_rightclose1
    with dissolve

    mcx "No!" with vpunch
    mcx "It was caused by someone, {w} someone from our guild."

    scene t_hall
    with dissolve

    mcx "Someone {i}{color=#00fff6}sabotaged{/color}{/i} our mission."

    play sound "soundfx/crowd_talking.ogg"

    gm "*murmurs* {i}...H-Huh? W-What? B-But? I mean...{/i} *murmurs*"
    gm "*murmurs* {i}...Sabotage by a member? How can that happen...{/i} *murmurs*"
    gm "*murmurs* {i}...I think the boss is...{/i} *murmurs*"

    stop sound fadeout 6.0

    scene t_crow_hall4
    with dissolve

    c "I'm sorry to interrupt you Aramis but that sounds quite a bit impossible."

    scene t_magus_hall4
    with dissolve

    s "I, too, concur with Sir Crow's statement, Sire, as most of the others think so too."
    s "It doesn't make sense on how can one \"{color=#00fff6}sabotaged{/color}\" us on what clearly appeared to be just an overwhelming monstrosity that overpowered us."

    scene t_crow_hall3
    with dissolve

    c "Yeah, that monster was just fucking stupidly powerful."

    scene t_magus_hall5
    with dissolve

    s "Sire, mayhaps the [[{b}SS{/b}] rank might be just a tad {i}too powerful{/i} for us at our current level?"

    scene t_crow_hall6
    with dissolve

    c "That first [[{color=#00fff6}Ultima{/color}] attack alone decimated all the magicians and healers."

    scene t_crow_hall8
    with dissolve

    c "We expected that they would be far enough from the Elder Earthwyrm's range but to our surprise, it went much farther and killed them."

    scene t_magus_hall3
    with dissolve

    s "Our assumptions from previous Earthwyrms might've made us underestimate the power of an [[{b}SS{/b}] rank."

    scene t_crow_hall5
    with dissolve

    c "\"Luckily\" some of us survive and I say that loosely 'cause the unexpected second [[{color=#00fff6}Ultima{/color}] killed what's left of us there..."

    scene t_magus_hall4
    with dissolve

    s "Sire, please excuse the offense for my following statement but..."
    s "Are you sure you aren't in denial of our loss? I mean this was your first defeat in over a—"

    scene t_mcx_center1
    with dissolve

    mcx "Wha-? No."
    mcx "Fuck no!" with vpunch
    mcx "I mean, someone {i}actually{/i} did something for the Elder Earthwyrm to [[{color=#f9c402}Transcend{/color}] that early."

    scene t_hall
    with dissolve

    play sound "soundfx/crowd_talking.ogg"

    gm "*loud murmurs* {i}...That's impossible! Who could've done it?...{/i} *loud murmurs*" with vpunch
    gm "*loud murmurs* {i}...The only ones there were rankers... No! It can't be...{/i} *loud murmurs*" with vpunch

    stop sound fadeout 2.0

    scene t_mcx_left1
    with dissolve

    mcx "That's the thing, isn't it?"
    mcx "How could someone sabotage a boss?"

    scene t_mcx_right3
    with dissolve

    mcx "Really, it's sounds stupid."
    mcx "Except... {p} ...for those who personally experienced the event yesterday."
    mcx "Everything about the damn thing wasn't normal."

    scene t_mcx_center6
    with dissolve

    mcx "The early [[{color=#f9c402}Transcension{/color}], the 2 [[{color=#00fff6}Ultima{/color}] attack—as it names implies, the Ultimate attack a Wyrm will unleash to its foes upon its death..."
    mcx "And death was nowhere near that Elder Earthwyrm, its health wasn't even halfway through that healthbar even."

    scene t_mcx_leftclose1
    with dissolve

    mcx "We can guess and hypothesize here all day, ladies and gents, but we'll go nowhere with that. We need {i}real{/i} answers."
    mcx "And one of the perks of being [[{color=#00fff6}The Lord of Cett Yvarra{/color}], I have direct contact with a [[{color=#00fff6}Administrative Game Master{/color}]."
    "(Well, Louie is something like that, I guess.)"

    scene t_mcx_leftclose3
    with dissolve

    mcx "And to my surprise. {p} They, too, were also shocked by the event. The rank was just suppose to be a powerup but not that {i}too powerful{/i}."

    scene t_hall
    with dissolve

    play sound "soundfx/crowd_talking.ogg"

    gm "{i}*murmurs*{/i}" with vpunch

    scene t_mcx_left1
    with dissolve

    mcx "Oh, it gets better. He also told me that our little friend yesterday was very VERY {i}special{/i}."

    stop sound fadeout 4.0

    scene t_crow_hall3
    with dissolve

    c "If I'm following this correctly, it seems like you already know how the culprit did it?"

    scene t_mcx_rightclose1
    with dissolve

    mcx "Perceptive as always, Crow."
    mcx "Well, partially, some of the fault yesterday can be attributed on me too."

    scene t_crow_hall4
    with dissolve

    c "...? {p} What do you mean by that?"

    scene t_mcx_center2
    with dissolve

    mcx "I failed to disclose to all of you the existence of a certain item. {p} A secret reward so to speak."
    mcx "An item so powerful, that if to be exposed, all guilds would be willing to give us millions of credits for it."

    scene t_hall
    with dissolve

    play sound "soundfx/crowd_talking.ogg"

    gm "*murmurs* {i}...W-What kind of item is that?...{/i} *murmurs*" with vpunch

    stop sound fadeout 4.0

    scene t_mcx_leftclose1
    with dissolve

    mcx "A [[{color=#00fff6}Mythos{/color}] rank healing item dubbed as [[{color=#00fff6}The Worldtree Elixir{/color}]!"

    scene t_hall
    with dissolve

    play sound "soundfx/crowd_talking.ogg"

    gm "*intense murmuring* {i}Holy shit! A [[{color=#00fff6}Mythos{/color}] item!{/i} *intense murmuring*" with vpunch

    scene t_crow_hall4
    with dissolve

    stop sound fadeout 4.0

    c "I know a [[{color=#00fff6}Mythos{/color}] item can be quite expensive but how would you know they would buy it for millions? Atleast 500,000 grand would be the maximum for such a thing."

    scene t_mcx_right2
    with dissolve

    mcx "I know that a [[{color=#00fff6}Mythos{/color}] ranked consumable item wouldn't tantalize any guild here to pay millions except that..."
    mcx "...our little friend is a direct product from the Worldtree, a tree well-known for its healing and holy properties."

    scene t_mcx_leftclose2
    with dissolve

    mcx "It's the elixir's potential in the upcoming war that's the key for that ludicrous price..."
    mcx "If used, a player will receive complete Health and Mana Restoration, Health Regeneration, Resurrection, and the legendary, Re-raise."

    scene t_hall
    with dissolve

    play sound "soundfx/crowd_shouting.mp3" fadein 2.0

    gm "{i}*inaudible shouting*{/i}" with vpunch

    stop sound fadeout 8.0

    scene t_mcx_rightclose3
    with dissolve

    mcx "But it isn't just those effects that makes this quite precious. {p}No! It's the [[{color=#00fff6}Worldtree Elixir{/color}]'s ability to use it on a whole party that makes this the greatest card in the \"{color=#00fff6}The Empyrean Inquisition{/color}\"."
    mcx "And in theory, a bottle can be used {i}atleast{/i} 3 times. An \"undying\" army under your hands that will know no fear."
    mcx "And its those who are {i}backing{/i} the guilds, the investors, who would pay handsomely for this..."
    mcx "...or so how I think it will go 'cause we don't exactly have the item to check, do we?"

    scene t_hall
    with dissolve

    play sound "soundfx/crowd_shouting2.ogg" fadein 3.0

    gm "*intense shouting* ...{i}{b}OH MY GOD!{/b}{/i}... *intense shouting*" with vpunch

    stop sound fadeout 4.0

    scene t_crow_hall6
    with dissolve

    play sound "soundfx/crowd_shouting3.ogg" fadein 1.0

    gm "*intense shouting* ...{i}{b}AN UNDYING ARMY! WHO COULD EVEN GO AGAINST THAT!?!{/b}{/i}... *intense shouting*" with vpunch

    stop sound fadeout 3.0

    scene t_magus_hall2
    with dissolve

    play sound "soundfx/crowd_shouting1.ogg" fadein 1.0

    gm "*intense shouting* ...{i}{b}NO! WITH THE RE-RAISE, THEY'LL BE GODLIKE WITH 6 LIVES! THAT'S INSANE!{/b}{/i}... *intense shouting*" with vpunch

    scene t_hall
    with dissolve

    play sound "soundfx/crowd_shouting1.ogg" fadein 2.0

    gm "*intense shouting* {i}{b}WE COULD SELL IT! {w} NO!!! {w} WE NEED TO USE IT!{/b}{/i} *intense shouting*" with vpunch
    gm "{i}*inaudible shouting and cursing*{/i}" with vpunch

    scene t_mcx_rightclose2
    with dissolve

    mcx "Order dammit! {p} Crow! Sorros! Slap their faces if they don't shut-up! Heck, slap it twice for good measure." with vpunch

    stop sound fadeout 3.0

    scene t_hall
    with slowfade

    gm "..."

    window hide

    pause

    scene t_magus_hall3
    with dissolve

    s "I think... we've understood the gist of it, Sire."

    scene t_crow_hall1
    with dissolve

    c "If the thief is planning to sell that item, it's highly likely that he's still hiding it."
    c "Waiting for the expansion to drop for a much higher price to gain."

    scene t_magus_hall5
    with dissolve

    s "And if an item like that is to be used strategically by a guild at the height of the faction war..."
    s "...they'll gain momentum amongst the other guilds and the distance will only get larger."

    scene t_crow_hall6
    with dissolve

    c "It's also a good bargaining chip to present to any of these venture capitalists seeking to invest in guilds for the upcoming war."
    c "Damn! {p} Now, I want to kill the motherfucker that stole it!" with vpunch

    scene t_mcx_center7
    with dissolve

    mcx "Selling, bargaining, or using it personally. Either way, this elixir is one of the most powerful item in Reincarnotica's existence."
    mcx "Like Excalibur, except being the King of England, you become the King of this World."
    mcx "Well, an already weak guild wouldn't benefit from using it but if it falls on the hands of the guilds part of the [[{color=#00fff6}Top 10{/color}]. It'll spell trouble for us..."

    scene t_crow_hall5
    with dissolve

    c "But why fail to tell us that kind of vital information?"

    scene t_mcx_center5
    with dissolve

    mcx "You already heard the reason, Crow."
    mcx "It's one powerful item."
    mcx "I didn't want the information about it leaked and make it much harder for us to deal with the Elder Earthwyrm while other people are waiting to backstab us."

    scene t_crow_hall7
    with dissolve

    c "If you told us then we might be able to better defend it!"

    scene t_mcx_rightclose1
    with dissolve

    mcx "No, the risk was quite too high to be leaked! {w} Even my measures didn't stop them in trying to intrude with our battle yesterday, didn't they?" with vpunch
    mcx "I don't know if those 2 Guild Leaders knew about the [[{color=#00fff6}Worldtree Elixirs{/color}] after finishing the \"{color=#22ff1e}Elruytheann Legend{/color}\" quest but they were unto us."
    mcx "Maybe they deemed the [[{b}SS{/b}] rank Elder Earthwyrm to be too valuable to leave it to us..."

    scene t_magus_hall1
    with dissolve

    s "The guilds [[{color=#d4ff00}Gran Fortuna{/color}] and [[{color=#9c32ff}Dark Star{/color}]? I heard they were the only ones to finish that quest due to the strict requirements."

    scene t_mcx_leftclose2
    with dissolve

    mcx "Yes. Or it's highly likely that they knew someone inside here. Someone who told them that our secrecy of this particular raid hunt was suspicious..."

    scene t_mcx_left1
    with dissolve

    mcx "Rather than trouble themselves to initiate a [[{color=#ff3030}Guild War{/color}], they might've opted for planting a mole or maybe they paid him a handsome price to betray us and stole the [[{color=#00fff6}Worldtree Elixirs{/color}]."

    scene t_hall
    with dissolve

    play sound "soundfx/crowd_shouting1.ogg" fadein 2.0

    gm "{i}*shouting and intense murmuring*{/i}" with vpunch

    stop sound fadeout 6.0

    scene t_crow_hall4
    with dissolve

    c "Wait! You said steal the elixir? Didn't they need to kill the Elder Earthwyrm first?"

    scene t_mcx_center2
    with dissolve

    mcx "Ah! That? No, the fountain water itself {i}IS{/i} the elixir."

    scene t_hall
    with dissolve

    gm "{i}*collective gasp*{/i}" with vpunch

    pause

    play sound "soundfx/crowd_shouting2.ogg" fadein 2.0

    gm "*intense shouting* ...{i}{b}IT WAS JUST THERE OUT IN THE OPEN!?{/b}{/i}... *intense shouting*" with vpunch

    stop sound fadeout 8.0

    scene t_mcx_center4
    with dissolve

    mcx "Quite clever, aren't they?"

    scene t_crow_hall5
    with dissolve

    c "You mean to say that someone stole the [[{color=#00fff6}Worldtree Elixirs{/color}] and triggered that premature [[{color=#f9c402}Transcension{/color}] of the Elder Earthwyrm!?" with vpunch

    scene t_mcx_rightclose1
    with dissolve

    "(That wasn't a [[{color=#f9c402}Transcension{/color}] but Louie's \"{color=#ff3030}Wrath Patch{/color}\" but they don't need to know that.)"
    mcx "It wasn't an ordinary [[{color=#f9c402}Transcension{/color}] either, that was divine punishment."
    mcx "An execution."

    scene t_hall
    with dissolve

    gm "..."

    scene t_mcx_left1
    with dissolve

    stop music fadeout 3.0

    mcx "Which finally puts us all into the crux of this matter."

    scene t_mcx_center2
    with dissolve

    mcx "Who is this piece of shit that still dares to appear in this hall!?" with vpunch

    scene t_mcx_right1
    with dissolve

    mcx "Smiling here, pretending to be as if he's still part of this guild while stabbing us in the back!?!" with vpunch

    scene t_mcx_leftclose1
    with dissolve

    mcx "To cause the deaths of your fellow guild brothers and sisters!? To drag our reputation to the mud!?" with vpunch
    mcx "WHO." with vpunch
    mcx "IS." with vpunch
    mcx "THIS." with vpunch
    mcx "TRAITOR!?" with vpunch

    scene t_hall

    gm "..."

    scene t_magus_hall1
    with dissolve

    s "..."

    scene t_crow_hall1
    with dissolve

    c "..."

    play sound "soundfx/chiptune_call.ogg" fadein 1.0

    scene t_hall
    with dissolve

    window hide

    pause

    if notification_songs == True:
        $ renpy.notify("Rolemusic - He Plays Me The Best Rhythms")

    "{i}{color=#f93b3b}*ring* {w} *ring* {w} *ring*{/color}{/i}"

    gm "....?"

    c "...?"

    s "..?"

    scene t_mcx_center2
    with dissolve

    mcx "U-Um... excuse me for a minute."

    stop sound

    scene lou_call1
    with dissolve



    play music "music/Parisian.mp3"

    if notification_songs == True:
        $ renpy.notify("Kevin MacLeod - Parisian")

    l "[[Ola! Amigo!]" with vpunch
    mcx "[[Godammit Louie! I was in the zone!]" with vpunch
    l "[[Nice \"timing\", huh?]"

    scene lou_call2
    with dissolve

    mcx "[[This is not the time for jokes! Did you really need to call me at this moment!?]" with vpunch

    scene lou_call2_3
    with dissolve

    l "[[Slow down there, pardner!]"
    l "[[It'll be problematic if the Sherriff's shootin' blanks down there...]"

    scene lou_call6
    with dissolve

    l "[[And that's why your little ol' amigo is here to help you with!]" with vpunch
    l "[[But I gotta admit that you're acting gives me goosebumps! Like you're really angry with a nice touch of seething rage.]"

    scene lou_call1
    with dissolve

    mcx "[[I {b}AM{/b} angry!] {p} [[I've got a traitor in my guild and I don't know who!]" with vpunch

    scene lou_call2_3
    with dissolve

    l "[[Well, it's your lucky day! I've got a noose ready for that convict!]" with vpunch
    mcx "[[Finally, is the [[{color=#ff3030}RED{/color}] card ready or are we gonna go to jail together?]"

    scene lou_call3
    with dissolve

    l "[[Okay! Okay! Check your inventory, it's already there.] {p} [[Like magic, huh?]" with vpunch
    l "[[Oh, one last thing before I go, choose the person {i}least{/i} likely to put us in the spotlight.]"

    scene lou_call6
    with dissolve

    l "[[Maybe someone weak or hated by everybody? I dunno...]"
    mcx "[[Why? {w} Isn't it better to kill the actual traitor now rather than play Duck Duck Goose?]"

    scene lou_call2_3
    with dissolve

    l "[[Accuse and kill one of the top rankers there and you'll be in the frontpage of the Quantum-net tomorrow and like I said, we need breadcrumbs to follow...]"
    mcx "[[Oh, a trail. Evidences of collusion and all that.]"
    l "[[Yup! I mean, I know you want to kill the guy but we still need to know who's he getting his info from!]"
    l "[[The more publicity you have, the more the item becomes \"hot\" to sell, the more they will look into this matter...]"
    l "[[This is the final heist, baby! We need to sell that item discretely without anyone snooping about on our business.]"

    scene lou_call2_3
    with dissolve

    mcx "[[Fine! I just hope this \"hack\" of yours work 'cause this is the only chance we can execute this.]"
    l "[[Sheesh! It'll work and relax, they'll be {i}former{/i} guild members anyway.]" with vpunch

    scene lou_call2
    with dissolve

    mcx "[[Goodbye Louie.]"
    l "[[Goo- *beep*]"

    stop music fadeout 3.0



    scene t_hall
    with dissolve

    gm "..."

    scene t_mcx_center7
    with dissolve

    mcx "Now..."
    mcx "It seems justice is on our side after all?"

    scene t_crow_hall3
    with dissolve

    c "Justice?"

    scene v_card_hold
    with dissolve

    mcx "With this."

    play music "music/Lord of the Land.mp3"

    if notification_songs == True:
        $ renpy.notify("Kevin MacLeod - Lord of the Land")

    window hide

    pause

    scene t_magus_hall5
    with dissolve

    s "A-A-A [[{color=#ff3030}RED{/color}] card! {p} Sire, t-that's quite a..." with vpunch

    scene t_mcx_left2
    with dissolve

    mcx "Cruel? Evil? Or the {i}exact punishment{/i} for the traitor?"
    mcx "Damn right it is!" with vpunch

    scene t_mcx_rightclose2
    with dissolve

    mcx "Betraying a guild is an extreme disrespect to us and to {b}ALL{/b} guilds that are part of [[{color=#00fff6}The Union of Empyrean Cetts{/color}]!"
    mcx "This is their answer, by granting me the infamous [[{color=#ff3030}RED{/color}] card."
    "(Well, Louie did.)"

    scene t_mcx_center1
    with dissolve

    mcx "The infamous \"{color=#ff3030}Death & The Fool Tarot{/color}\". A Cett Lord's greatest weapon in the battle against criminals and heathens..."
    mcx "The punishment of death!" with vpunch
    mcx "Once marked and killed, you will lose half your level, all your items, and will be banned for quite some time amongst all [[{color=#00fff6}Empyrean Cetts{/color}]. {p} Banning someone forever is against game rules so we take what we can."

    scene t_mcx_left3
    with dissolve

    mcx "This the justice we're waiting for!" with vpunch

    scene t_hall
    with dissolve

    play sound "soundfx/crowd_talking.ogg" fadein 2.0

    gm "*murmurs* ...{i}T-That's really evil! Can our Lord do that?{/i}... *murmurs*"
    gm "*murmurs* ...{i}Of course! It's the perfect punishment for that damn traitor!{/i}... *murmurs*"
    gm "*murmurs* ...{i}Really? But we don't exactly know who...{/i}... *murmurs*"

    scene t_mcx_center7
    with dissolve

    mcx "Settle down."

    stop sound fadeout 3.0

    mcx "I know your concerns for who this traitor is and as the circumstances of the crime has been discussed..."

    scene t_mcx_center2
    with dissolve

    mcx "It's safe to say that only {b}{color=#00fff6}5{/color}{/b} people excluding me are our suspects."
    mcx "Namely, the ones who were on the battlefield that day."

    scene t_hall
    with dissolve

    play sound "soundfx/crowd_talking.ogg" fadein 2.0

    gm "*quiet murmurs* ...{i}T-The rankers...{/i} *quiet murmurs"
    gm "*quiet murmurs* ...{i}O-One of them betrayed the guild? W-Why!?{/i}... *quiet murmurs"
    gm "*quiet murmurs* ...{i}T-They're supposed to be the guild's role model! To betray us{/i}... *quiet murmurs"

    stop sound fadeout 6.0

    scene t_mcx_left2
    with dissolve

    "({i}*sigh*{/i})"
    "(I just felt this guild's heart fall and shatter. Rankers are considered as the pillar of strength for a guild, for one to betray them...)"
    mcx "The accused are..."

    scene t_magus_hall1
    with dissolve

    mcx "The Grand Magus, Sorros."
    mcx "The Champion Gladiators, Tymisus and Hectarus."

    scene t_crow_hall1
    with dissolve

    mcx "The Shadow Walker, Blood Crow."
    mcx "And that kid behind your back..."
    "(Who's he again?)"

    scene t_crow_hall5
    with dissolve

    c "Rustbucket, Aramis. A Night Guardian."
    c "I asked him to join us 'cause he was near our location yesterday."

    scene t_mcx_rightclose3
    with dissolve

    "(Rustbucket, huh?)"
    mcx "I see."

    scene t_mcx_center4
    with dissolve

    mcx "Now, gentlemen. We've know each other for years now and it's sad to see that one of you chose to betray me."

    scene t_magus_hall3
    with dissolve

    s "Sire! This a very grave matter! To accuse one of us is—" with vpunch

    scene t_mcx_leftclose2
    with dissolve

    mcx "I know, Sorros. This is a heavy accusation and the punishment is severe."
    mcx "This is why I want to hear each and everyone's alibi on what they were doing yesterday when each and one of you was fighting the Elder Earthwyrm."
    mcx "Be assured, I will say the verdict but the crowd will be the judge of this."

    scene t_mcx_center2
    with dissolve

    mcx "Kindly escort the accused outside and..."
    mcx "..let this trial begin!" with vpunch

    scene t_hall
    with dissolve


    menu accuse:

        "Sorros?" if question_sorros == True:
            $ question_sorros = False
            $ guild_sorros = 1
            jump sorros_answer

        "Tymisus and Hectarus?" if question_twins == True:
            $ question_twins = False
            $ guild_twins = 1
            jump twins_answer

        "Crow?" if question_crow == True:
            $ question_crow = False
            $ guild_crow = 1
            jump crow_answer

        "Rustbucket, is it?" if question_crow == False and question_sorros == False and question_twins == False and question_rustbucket == False:
            $ question_rustbucket = True
            jump rustbucket_answer

        "Very well..." if question_rustbucket == True:
            jump verdict





    label sorros_answer:

    scene t_magus_solo1
    with fade

    mcx "Sorros, how long have you been in this guild?"
    s "It has been 4 years of service to you, Sire. I was a still a fledgling [[{color=#00fff6}Mage{/color}] when I joined under your banner."
    s "And it's thanks to all your help that I am what I am today, Sire."

    scene t_mcx_leftclose1
    with dissolve

    mcx "Yeah, the [[{color=#00fff6}World Ranking{/color}] back then was much more chaotic as guilds were just still budding but as they consolidated their power..."
    mcx "...the term \"{color=#00fff6}rankers{/color}\" transformed the game's landscape. When your name was in it, it means that your a cut above the others."
    mcx "You were respected and {i}feared{/i}. Not only you but your guild as well. It was a glorious era."

    scene t_mcx_left2
    with dissolve

    mcx "And it pains me today that because of one event..."
    mcx "I must now question your loyalty and allegiance to this guild."

    scene t_magus_solo3
    with dissolve

    s "Sire! That statement hurts me deeply." with vpunch
    s "I have devoted my life to this guild and helped it to reach what it is today and—"

    scene t_mcx_leftclose2
    with dissolve

    mcx "Relax, I'm not accusing you {i}for now{/i}."
    mcx "Everyone who was in that \"arena\" is considered a suspect."
    mcx "I just want you to recall what you were doing prior to the Elder Earthwyrm's [[{color=#f9c402}Transcension{/color}]..."

    scene t_magus_solo5
    with dissolve

    s "As you've seen yesterday, I've perched myself on the corner walls that surrounded the \"arena\"."
    s "I was the one providing the offensive and defensive support for you and the others."
    mcx "Yes, I remember."

    scene t_magus_solo4
    with dissolve

    s "After the Elder Earthwyrm's sudden transformation, I've found myself heavily injured out of nowhere which we now know was an [[{color=#00fff6}Ultima{/color}] attack."
    s "Fortunately, I have my [[{color=#00fff6}Undying Soul{/color}] which allowed me to negate a large portion of the damage and survive it."

    scene t_magus_solo3
    with dissolve

    s "It was when I came back to my senses and heard Sir Crow's bellows below about another attack that forced me to make a move."
    s "Sadly, it was still in vain as the second [[{color=#00fff6}Ultima{/color}] attack finally ended us."

    scene t_magus_solo1
    with dissolve

    s "All in all, prior to the attack, it was impossible for me to get down there without anyone noticing and my help can be corroborated by the \"Twins\"."
    s "That's my story, Sire."

    scene t_mcx_leftclose1
    with dissolve

    mcx "I see."

    scene t_magus_solo1
    with dissolve

    "(Sorros has been a long time friend of mine and a loyal guild member and leader.)"
    "(Heck, he's viewed highly by the others and to some extent, by other guilds as well.)"
    "(Betraying the guild isn't something he'll likely do but...)"

    scene t_mcx_center7
    with dissolve

    "(Argh! This theft is making me paranoid.)" with vpunch
    "(That's why Louie suggested to rely on factual evidence rather than my feelings.)"
    "(Another thing to be worried about is, if I kill him, {i}a 15th ranker{/i}, with flimsy evidence and hearsay, the consequences of that will be {i}really{/i} bad.)"
    "(Besides, why would Sorros betray me in the first place?)"

    scene t_mcx_center1
    with dissolve

    mcx "Then, did you see anyone who was near the fountain at any point in time while you were up there?"

    scene t_magus_solo4
    with dissolve

    s "There's one..."
    mcx "Who!?" with vpunch

    scene t_magus_solo1
    with dissolve

    s "That kid, Crow's protege."

    scene t_magus_solo5
    with dissolve

    s "But Sire! I'm not accusing him of anything. I just saw him near it..."

    scene t_mcx_leftclose1
    with dissolve

    if guild_sorros and not (guild_twins + guild_crow):

        play sound "soundfx/crowd_talking.ogg" fadein 2.0

        gm "*quiet murmurs* ...{i}Him? Why was he there{/i}... *quiet murmurs*"
        gm "*quiet murmurs* ...{i}I think they needed bait! Hahaha{/i}... *quiet murmurs*"
        "(Hm? That kid.. doesn't have that many friends, huh?)"
        "(But for him to be near that fountain is quite... suspicious.)"

        stop sound fadeout 2.0

    if guild_sorros and (guild_twins + guild_crow) == 1:

        play sound "soundfx/crowd_talking.ogg" fadein 2.0

        gm "*murmurs* ...{i}This is the second one mentioning that saw him there. Maybe he...{/i}... *murmurs*"
        gm "*murmurs* ...{i}It's possible. I mean we're talking about him of all people{/i}... *murmurs*"
        gm "*murmurs* ...{i}Figures. He already hated joining this guild anyway{/i}... *murmurs*"
        "(How many people did that kid pissed off!?)" with vpunch
        "(Even I'm starting to get suspicious of him...)"

        stop sound fadeout 4.0

    if guild_sorros + guild_twins + guild_crow == 3:

        play sound "soundfx/crowd_talking.ogg" fadein 2.0

        gm "*audible murmurs* ...{i}I think he's the one who did it!{/i}... *audible murmurs*" with vpunch
        gm "*audible murmurs* ...{i}He thinks he can get away because he's close with Sir Crow{/i}... *audible murmurs*"
        gm "*audible murmurs* ...{i}I want to see him punished!{/i}... *audible murmurs*" with vpunch
        gm "*audible murmurs* ...{i}Yeah! Yeah! Yeah!{/i}... *audible murmurs*" with vpunch
        "(The crowd's already convinced that {i}that{/i} kid's the one who did it.)"
        "(I'd start believing that too if it weren't for the [[{color=#00fff6}Cambrian Flask{/color}].)"
        "(The level requirement to use that to store the elixirs doesn't meet the his level. I can tell everybody the truth but...)"
        "(Louie's \"{color=#00fff6}sacrifice{/color}\". He's the perfect fit, he's hated by everybody here and wouldn't make a fuss that would get attention.)"
        "({i}*sigh*{/i}) {p} (Nothing personal, kid. Well, it'll be for him.)"

        stop sound fadeout 4.0

    mcx "I understand, Sorros."

    scene t_hall
    with slowfade

    jump accuse



    label twins_answer:

    scene t_titans1
    with fade

    mcx "Tymisus, Hectarus!" with vpunch
    t "Milord!" with vpunch
    h "Milord!!" with vpunch

    scene t_mcx_leftclose3
    with dissolve

    mcx "You two were the ones responsible managing the Elder Earthwyrm's aggro should I be in dire need and also as general attackers."
    mcx "Which means you two were near the fountain at most times..."
    mcx "Well?"

    scene t_titans2
    with dissolve

    t "'Course I can't deny that milord, me and my brotha' here was busy fightin' the bloody cunt with you, Sir!"

    scene t_titans3
    with dissolve

    h "Damn thing was tough as nails, I'll give him tha' and quite a fuckin' hittah too."

    scene t_titans4
    with dissolve

    t "Then the bloody git went did that fuckin' magic show and delivered our arses for Satan to fuck in Hell!" with vpunch

    scene t_mcx_leftclose1
    with dissolve

    "(It seems to always be a challenge deciphering what these two are saying.)"
    "(That thick accent somehow filters the actual English language coming out from them into something alien.)"

    scene t_mcx_leftclose3
    with dissolve

    mcx "Then let me ask you? Did you steal the elixirs?"

    scene t_titans6
    with dissolve

    t "Wha-? Sir, no, sir! Wha' kinda question is that!?" with vpunch
    h "Sir Aramis, sir! You can ask Sir Sorros and Sir Crow, they'll tell ya we were nevah near the fountain!"
    t "We were stuck fightin' that smelly cunt! If we even turned our back a li'l bit, we might as well ready our damn graves!"

    scene t_titans5
    with dissolve

    h "Right! Right!" with vpunch
    h "In the first place, we didn't even know that there were \"{color=#00fff6}Mutton{/color}\" elixirs over there."
    h "We weren't even hungry! We don't eve like muttons!" with vpunch

    scene t_titans3
    with dissolve

    t "And-And Sir Sorros just called us out of nowhere to slay a fuckin' [[{b}SS{/b}] rank monstah without much informayshun!"

    scene t_mcx_right1
    with dissolve

    "(Well, it was nice to trying a direct approach, like it'll ever work.)"

    scene t_mcx_left2
    with dissolve

    "(If I remember correctly, Sorros recommended them about a year or so ago. Saw a potential in them that the other guilds didn't.)"
    "(And I must admit that he has a good eye for talent. Put these two together in a battlefield and they become impenetrable fortresses.)"

    scene t_titans1
    with dissolve

    "(Hence, why these two are particularly loyal to him.)"

    scene t_titans8
    with dissolve

    t "Milord, if you don't believe us, Sir Sorros can vouch for where we were!" with vpunch

    scene t_titans5
    with dissolve

    h "Yeah, what he said milord!" with vpunch

    scene t_mcx_center7
    with dissolve

    "(Even though this two aren't in the upper ranks like Sorros or Crow, they're still part of the mid-rankings.)"
    "(They're also particularly popular in the [[{color=#00fff6}Tank{/color}] circles throughout different guilds.)"
    "(Still, if I don't find a suitable \"Sacrifice\", they'll do but I only need one and the other would probably react violently.)"
    "(Dammit.)"

    scene t_mcx_right3
    with dissolve

    mcx "Fine."
    mcx "Then, let me ask you another question, who did you last saw near the fountain?"

    scene t_titans7
    with dissolve

    t "..."
    h "..."

    pause

    scene t_titans4
    with dissolve

    t "That kid."

    scene t_titans6
    with dissolve

    h "Buckethead."

    scene t_titans3
    with dissolve

    t "No, you fuckin' idiot, Rustyhead!" with vpunch

    scene t_mcx_left2
    with dissolve

    "(This idiots. Its Rustbucket and I just heard that a couple of minutes ago. {w} In this room. {w} With you two.)"
    "(But that kid, huh?)"

    if guild_twins and not (guild_sorros + guild_crow):

        play sound "soundfx/crowd_talking.ogg" fadein 2.0

        gm "*quiet murmurs* ...{i}Him? Why was he there{/i}... *quiet murmurs*"
        gm "*quiet murmurs* ...{i}I think they needed bait! Hahaha{/i}... *quiet murmurs*"
        "(Hm? That kid.. doesn't have that many friends, huh?)"
        "(But for him to be near that fountain is quite... suspicious.)"

        stop sound fadeout 2.0

    if guild_twins and (guild_sorros + guild_crow) == 1:

        play sound "soundfx/crowd_talking.ogg" fadein 2.0

        gm "*murmurs* ...{i}This is the second one mentioning that saw him there. Maybe he...{/i}... *murmurs*"
        gm "*murmurs* ...{i}It's possible. I mean we're talking about him of all people{/i}... *murmurs*"
        gm "*murmurs* ...{i}Figures. He already hated joining this guild anyway{/i}... *murmurs*"
        "(How many people did that kid pissed off!?)" with vpunch
        "(Even I'm starting to get suspicious of him...)"

        stop sound fadeout 4.0

    if guild_sorros + guild_twins + guild_crow == 3:

        play sound "soundfx/crowd_talking.ogg" fadein 2.0

        gm "*audible murmurs* ...{i}I think he's the one who did it!{/i}... *audible murmurs*" with vpunch
        gm "*audible murmurs* ...{i}He thinks he can get away because he's close with Sir Crow{/i}... *audible murmurs*"
        gm "*audible murmurs* ...{i}I want to see him punished!{/i}... *audible murmurs*" with vpunch
        gm "*audible murmurs* ...{i}Yeah! Yeah! Yeah!{/i}... *audible murmurs*" with vpunch
        "(The crowd's already convinced that {i}that{/i} kid's the one who did it.)"
        "(I'd start believing that too if it weren't for the [[{color=#00fff6}Cambrian Flask{/color}].)"
        "(The level requirement to use that to store the elixirs doesn't meet the his level. I can tell everybody the truth but...)"
        "(Louie's \"{color=#00fff6}sacrifice{/color}\". He's the perfect fit, he's hated by everybody here and wouldn't make a fuss that would get attention.)"
        "({i}*sigh*{/i}) {p} (Nothing personal, kid. Well, it'll be for him.)"

        stop sound fadeout 4.0

    scene t_mcx_center4
    with dissolve

    mcx "I see. I'll take that into consideration."
    mcx "Next."

    scene t_hall
    with slowfade

    jump accuse



    label crow_answer:

    scene t_crow_solo2
    with fade

    mcx "Crow?"

    scene t_crow_solo5
    with dissolve

    c "Really, Aramis?"

    scene t_mcx_right1
    with dissolve

    mcx "Really."
    mcx "Personally, it didn't even cross my mind that you could've even betray the guild but..."

    scene t_mcx_rightclose3
    with dissolve

    mcx "...we're here. {p} So..."

    scene t_crow_solo8
    with dissolve

    c "{i}*sigh*{/i}"
    c "Alright. {p} Being fair and all that..."

    scene t_crow_solo1
    with dissolve

    c "As you're familiar with my class, my skills and attacks are more efficient with stealth and rear attacks."
    c "Which is why I'm almost always situated at the back."

    scene t_mcx_left3
    with dissolve

    mcx "Yes and I also know that your [[{color=#00fff6}Shadow Walk{/color}] makes you invisible—"

    scene t_crow_solo8
    with dissolve

    c "Let me stop you right there."

    scene t_crow_solo5
    with dissolve

    c "First and foremost, I didn't know jackshit about the [[{color=#00fff6}Worldtree Elixirs{/color}]. {w} Thank you very much."
    c "Second, my [[{color=#00fff6}Shadow Walk{/color}], as I've said to you yesterday, puts me in an \"{color=#00fff6}Ethereal Plane{/color}\" which means I can't interact with physical objects while in there."

    scene t_crow_solo3
    with dissolve

    c "That includes taking any items or using them. To do that, I need to cancel the skill first which does this flashy dimensional show that any of you can immediately notice."

    scene t_crow_solo4
    with dissolve

    c "And finally, the most important fact that you're forgetting, you were shouting at me the whole damn time!" with vpunch

    scene t_crow_solo3
    with dissolve

    c "Don't tell me you forgot the barrage of \"{i}{b}CROW! ATTACK HIS BACK!{/b}{/i}\" or \"{i}{b}CROW! SAVE ME!{/b}{/i}\" that you were yelling at me the whole time, hmmm?"
    c "I didn't even have enough time breath and you expect me to have enough for stealing that damn thing!?" with vpunch
    mcx "{i}*cough*{/i}" with vpunch

    scene t_crow_solo1
    with dissolve

    c "So, in short, I didn't do it."
    mcx "{i}*sigh*{/i}"
    "(Crow is just one of those people that you come to completely trust unconditionally.)"
    "(I'm not saying I'll believe him entirely but it's just instincts, I guess.)"
    "(I mean those are the kind of people you typically be most suspicious about but...)"

    scene t_mcx_center7
    with dissolve

    "(The guy wears his emotions on his sleeves and after countless battles and quests with him, I just realize that's the case. If he's lying, it shows.)"
    "(But just to consider the scenario that he was the one who to stole it, killing the 9th ranked player in the world would be catastrophic, not to mention he's my Vice Leader.)"
    "(The guild would probably divide into factions and fight with each other and as for the tabloids...)"
    "(They'll be hounding this character at every moment.)"
    "(I hate to leave this guild in chaos just for the sake of money.)"

    scene t_mcx_rightclose3
    with dissolve

    mcx "Alright! Fine! I trust you!" with vpunch

    scene t_mcx_rightclose1
    with dissolve

    mcx "Then let me ask you another question, did you see anyone near the fountain?"

    scene t_crow_solo5
    with dissolve

    c "No, unless you count Rustbucket being smacked face first into that fountain, then yes."
    c "But I highly doubt that he did that though. He barely knows how to use an [[{color=#00fff6}Antidote{/color}] much less an [[{color=#00fff6}Elixir{/color}]."

    scene t_mcx_right1
    with dissolve

    if guild_crow and not (guild_sorros + guild_twins):

        play sound "soundfx/crowd_talking.ogg" fadein 2.0

        gm "*quiet murmurs* ...{i}Him? Why was he there{/i}... *quiet murmurs*"
        gm "*quiet murmurs* ...{i}I think they needed bait! Hahaha{/i}... *quiet murmurs*"
        "(Hm? That kid.. doesn't have that many friends, huh?)"
        "(But for him to be near that fountain is quite... suspicious.)"

        stop sound fadeout 2.0

    if guild_crow and (guild_sorros + guild_twins) == 1:

        play sound "soundfx/crowd_talking.ogg" fadein 2.0

        gm "*murmurs* ...{i}This is the second one mentioning that saw him there. Maybe he...{/i}... *murmurs*"
        gm "*murmurs* ...{i}It's possible. I mean we're talking about him of all people{/i}... *murmurs*"
        gm "*murmurs* ...{i}Figures. He already hated joining this guild anyway{/i}... *murmurs*"
        "(How many people did that kid pissed off!?)" with vpunch
        "(Even I'm starting to get suspicious of him...)"

        stop sound fadeout 4.0

    if guild_sorros + guild_twins + guild_crow == 3:

        play sound "soundfx/crowd_talking.ogg" fadein 2.0

        gm "*audible murmurs* ...{i}I think he's the one who did it!{/i}... *audible murmurs*" with vpunch
        gm "*audible murmurs* ...{i}He thinks he can get away because he's close with Sir Crow{/i}... *audible murmurs*"
        gm "*audible murmurs* ...{i}I want to see him punished!{/i}... *audible murmurs*" with vpunch
        gm "*audible murmurs* ...{i}Yeah! Yeah! Yeah!{/i}... *audible murmurs*" with vpunch
        "(The crowd's already convinced that {i}that{/i} kid's the one who did it.)"
        "(I'd start believing that too if it weren't for the [[{color=#00fff6}Cambrian Flask{/color}].)"
        "(The level requirement to use that to store the elixirs doesn't meet the his level. I can tell everybody the truth but...)"
        "(Louie's \"{color=#00fff6}sacrifice{/color}\". He's the perfect fit, he's hated by everybody here and wouldn't make a fuss that would get attention.)"
        "({i}*sigh*{/i}) {p} (Nothing personal, kid. Well, it'll be for him.)"

        stop sound fadeout 4.0

    mcx "That's all, Crow."

    scene t_crow_solo8
    with dissolve

    c "Aramis."
    c "I know this is a sensitive subject, not just to you but to the whole guild as well but I think judging the person today would be a bad idea."
    c "Personally, if we have traitors, we need to scrutinize and gather facts and evidences reasonably."
    c "That [[{color=#ff3030}RED{/color}] card isn't something to be use carelessly especially on someone innocent."

    scene t_mcx_left3
    with dissolve

    mcx "I know, Crow."
    mcx "Even I'm apprehensive to use this but..."
    mcx "...its got to be done."

    scene t_hall
    with slowfade

    jump accuse



label rustbucket_answer:

    scene t_rust1
    with dissolve

    "(The infamous Rustbucket.)"
    mcx "You're Crow's lackey, am I right?"

    scene t_rust2
    with dissolve

    r "Uh... {p} Kinda, sir. More often than not, he's the one assisting me."

    play sound "soundfx/crowd_talking.ogg" fadein 2.0

    gm "*murmurs* {i}...Tsk! It's him! Your punishment's coming...{/i} *murmurs*"
    gm "*murmurs* {i}...Oh, now his acting nice! No one believes you, you traitor...{/i} *murmurs*"
    r "..."

    stop sound fadeout 2.0

    scene t_mcx_rightclose1
    with dissolve

    "(The 4 of them has already testified seeing him near the fountain.)"
    mcx "You're one of the guy's he asked to help against the Elder Earthwyrm?"
    mcx "But I rarely saw you take an attack from it? Is my assumption wrong?"

    scene t_rust3
    with dissolve

    r "Uhh... not quite, sir."

    scene t_rust2
    with dissolve

    r "You see, Sir Tymisus and Sir Hectarus were more than capable of handling the Elder Earthwyrm and so they told me to assist Sir Crow on the back, sir."
    r "To not... as they put it, \"fuck up their mojo\"."

    scene t_mcx_rightclose3
    with dissolve

    mcx "I see. Now, prior to the Elder Earthwyrm's [[{color=#f9c402}Transcension{/color}], where were you at that time?"

    scene t_rust3
    with dissolve

    r "Um, let's see... I was near the Elder Earthwyrm's rear as I was assisting Crow..."

    scene t_rust2
    with dissolve

    r "He didn't need much help most of the time but I cover for him when he's recovering his health or skill time. That's when I take the aggro off of him."

    scene t_rust1
    with dissolve

    r "When the monster, as you said, [[{color=#f9c402}Transcended{/color}]. I was the first ones to die as I was near him, sir."

    scene t_mcx_left1
    with dissolve

    mcx "Were you at any point near the fountain yesterday?"

    scene t_rust4
    with dissolve

    r "Ummm... there was a point that the Elder Earthwyrm smacked me with its tail and propelled me near there..."
    play sound "soundfx/crowd_talking.ogg" fadein 2.0
    gm "*murmurs* {i}...See? Traitor...{/i} *murmurs*"
    stop sound fadeout 2.0

    scene t_rust5
    with dissolve

    r "But I didn't touch anything there! I swear!" with vpunch
    r "I don't even know what an elixir is, sir!" with vpunch
    r "These fuckers—I mean, what the others are saying are plain lies, sir!" with vpunch
    play sound "soundfx/crowd_talking.ogg" fadein 2.0
    gm "*audible murmurs* {i}...Liar! Lying again...{/i} *audible murmurs*"
    stop sound fadeout 2.0
    r "..."

    scene t_mcx_leftclose1
    with dissolve

    "(So this pressure is tearing that mask off, huh?)"
    "(Although he keeps to himself most of the time, the attitude problem is still there.)"
    "(I don't know what Crow sees in him to be honest.)"
    "(It's just sad that after a year, instead of being befriended by other members, they started hating him more.)"

    scene t_mcx_left3
    with dissolve

    mcx "Alright."
    mcx "Your dismissed."

    scene t_rust5
    with dissolve

    r "SIR! DON'T BELIEVE THEIR LIES!" with vpunch

    scene t_mcx_left3
    with dissolve

    mcx "I said your dismissed."

    scene t_mcx_center7
    with dissolve

    "(Is there anything more to say? I thought I would make some bullshit reason to kill him but the well's been pretty much poisoned.)"
    "(Poisoned none other than by himself. Maybe if he had more friends he might've escaped this.)"
    "(Crow.) {p} (I'm sorry, man.)"

    scene t_hall
    with slowfade

    jump accuse



label verdict:

    stop music fadeout 3.0

    scene t_mcx_leftclose1
    with fade

    mcx "I've heard enough."

    scene t_hall
    with dissolve

    play sound "soundfx/crowd_talking.ogg" fadein 2.0

    gm "*murmurs* {i}...Who do you think did it?...{/i} *murmurs*"

    scene t_crow_hall1
    with dissolve

    gm "*murmurs* {i}...Didn't you listen? It's' \"him\" definitely...{/i} *murmurs*"

    scene t_magus_hall1
    with dissolve

    gm "*murmurs* {i}...I knew it! That asshole thought he could get away with this...{/i} *murmurs*"
    gm "*murmurs* {i}...The nerve! After Sir Crow helped him, now he does this...{/i} *murmurs*"

    stop sound fadeout 5.0

    scene t_mcx_right2
    with dissolve

    mcx "Everyone here has now heard every accused's alibis."
    mcx "As for the verdict..."

    scene t_mcx_left2
    with dissolve

    "({i}*sigh*{/i})"
    "(This kangaroo court...)"
    "(To be honest, I preferred Crow's suggestion of slow and meticulous investigation on this matter but alas time isn't my friend here.)"
    "(That would take too much time and resources. Louie's method is much faster at the expense of someone...)"

    scene t_mcx_leftclose3
    with dissolve

    mcx "It seems... {w} our guild has spoken."

    play music "music/Teller of the Tales.mp3"

    if notification_songs == True:
        $ renpy.notify("Kevin MacLeod - Teller of the Tales")

    scene t_hall
    with dissolve

    play sound "soundfx/crowd_talking.ogg" fadein 2.0

    gm "*murmurs* {i}...There's no point in waiting anymore, its him...{/i} *murmurs*"
    gm "*chattering* {i}...Yeah! Sir Sorros spoke of him being there...{/i} *chattering*"

    stop sound fadeout 4.0

    gm "*chattering* {i}...Crow, Tymisus, Hectarus said the same thing!...{/i} *chattering*" with vpunch

    play sound "soundfx/crowd_shouting2.ogg" fadein 3.0

    gm "*shouting* {i}...It's Rustbucket who stole the elixirs!!...{/i} *shouting*" with vpunch

    stop sound fadeout 4.0

    scene t_rust5
    with dissolve

    r "Sir Aramis! Milord! T-T-These are all lies! I-I didn't steal anything!!" with vpunch
    r "B-Believe me, Milord!" with vpunch

    scene t_hall
    with dissolve

    play sound "soundfx/crowd_shouting1.ogg" fadein 2.0

    gm "*shouting* {i}...Lying again to save his ass! Off with his head!...{/i} *shouting*" with vpunch
    gm "*shouting* {i}...YEAH!...{/i} *shouting*" with vpunch
    r "C-Crow?"

    scene v_stop2
    with dissolve

    stop sound fadeout 9.0

    c "Daemona? Lulu? You believe him right!?" with vpunch
    d "Crow, this is... complicated. It's impossible to interfere now."
    lu "Crow-kun... Mona-chan's right desu~"
    lu "W-We can't go against Boss-san and the guild! A-And even I think he did it desu~"
    d "It doesn't help that the kid made lots of enemies here in the guild."
    d "Crow, I'm sorry but the testimonies are stacked against Rustbucket."
    c "B-But..."

    scene t_mcx_center7
    with dissolve

    mcx "Crow, the crowd has spoken."

    scene v_card_hold1
    with dissolve

    mcx "Betraying the guild, making a mockery of its name just because of greed..."

    scene v_card_flip
    with dissolve

    mcx "What you did didn't just caused the deaths of ours but the destruction of this guild's pride..."

    scene t_rust5
    with dissolve

    r "No! I didn't fucking steal any shit of yours!" with vpunch
    r "Just because I was near the fountain doesn't mean I stole it you piece of shit—"

    scene t_magus_hall2
    with dissolve

    s "Such insolence!!" with vpunch
    s "That's our Guild Leader, you bastard! To dare insult him you—" with vpunch

    scene v_card_flip
    with dissolve

    mcx "By my decree as the [[{color=#00fff6}Lord of Cett Yvarra{/color}]..."

    scene v_card_throw

    mcx "...I hereby sentence you for treason against the [[{color=#00fff6}The Garuda Guild{/color}]!" with vpunch

    window hide

    pause

    scene black
    r "NNNNNNNNOOOOOOOOOOOOOOO!!!!" with vpunch

    scene v_rust_stun
    with redflash

    r "AAAAARRRRGGGGHH!!" with vpunch
    r "I-I... c-can't... m-move..."

    scene v_accuse
    with dissolve

    mcx "That's the consequence of you sins, boy!"

    scene v_stop
    c "Aramis, stop! {p} R-Rustbucket's innocent!" with vpunch

    scene v_rust_stun
    with dissolve

    r "C-Crow... {w} help me.."

    scene v_stop

    c "Shit! Aramis, I said stop!" with vpunch
    lu "Crow-kun, stoppu!" with vpunch
    d "Crow! Don't go near him! You'll be affected by the card's power!" with vpunch

    scene v_accuse
    with dissolve

    mcx "I cannot fault you for trying to help him, Crow."
    mcx "But this is something he's done to the guild not me."

    scene v_accuse_closeup
    with dissolve

    mcx "This is Justicia."

    scene v_accuse_closeup
    with dissolve

    mcx "I'll give you another chance, boy."
    mcx "Give me back the [[{color=#00fff6}Worldtree Elixirs{/color}] and I can spare you but you will be banned here indefinitely."

    scene v_rust_stun
    with dissolve

    r "H-Hehe..."
    mcx "...?"
    r "Ahahahaha!!" with vpunch
    r "You...people..disgust..me! {p} If...I..can..spit..on..your...face, I...will..." with vpunch

    scene v_accuse
    with dissolve

    mcx "Quite brave of you."

    scene v_accuse_closeup
    with dissolve

    mcx "[[\"Louie, I hope you're ready.\"]"

    scene lou_call8
    with dissolve

    l "The hack's still readying itself, amigo."

    scene v_accuse_closeup
    with dissolve

    mcx "[[\"Then, make haste.\"]"
    mcx "Now, let's end this."
    mcx "[[{color=#ff3030}Death's Descent{/color}]"

    scene v_stop

    c "NO!" with vpunch

    scene black

    gm "{i}*collective gasp*{/i}" with vpunch
    r "URRRGGHH!!" with vpunch

    scene v_stab_view
    with slowfade

    window hide

    pause

    scene v_stab_mcx
    with dissolve

    mcx "Nothing personal, kid."

    scene v_stab_rust
    with dissolve

    r "I-I...di-didn't...do it...you...asshole..."
    r "Y-You're..all...{w}you're..all..the same..."
    r "I-I..should've..never..bothered..with...this..game..."
    r "Crow...\"your..family\"...is..shit..."

    scene v_stab_mcx
    with dissolve

    mcx "{i}*sigh*{/i}"
    mcx "You're making me look like a bad guy here, y'know?"
    mcx "Just a secret between you and me, I know you didn't do it."

    scene v_stab_rust
    with dissolve

    r "W-What!?" with vpunch

    scene v_stab_mcx
    with dissolve

    mcx "Well, they can't hear us here while the \"[[{color=#ff3030}RED{/color}]\" card is doing its thing."
    mcx "I just failed to mention to the others that a special flask is needed for the elixir. A flask that requires a certain level to use."
    mcx "And among the 5 of you, you were the only exception who can't wield it."

    scene v_stab_rust
    with dissolve

    r "W-Why!?" with vpunch

    scene v_stab_mcx
    with dissolve

    mcx "To be honest, I need to root out the actual perpetrator who did steal it but I needed your death first."
    mcx "Well, someone's death and you seem to already have enemies here that wouldn't bat an eye even if you were killed."
    mcx "Sorry about that. I can still help you after this—"

    scene v_stab_rust
    with dissolve

    r "FUCK OFF!" with vpunch
    r "Y-You..know, you..remind..me...of..my..late..father.."
    r "A..despicable..man..who..uses..people..even..his..own..son..just..so..he..can..gain..an..advantage..against..a..rival.."

    scene v_stab_mcx
    with dissolve

    "(Ah shit!) {p} (Now, I {i}really{/i} feel like an asshole! Great!)" with vpunch
    mcx "I'm...{w}I'm sorry to hear that."
    mcx "[[\"Louie!? Hurry up!\"]" with vpunch

    stop music fadeout 12.0

    scene lou_call5
    with dissolve

    l "Man, you're really evil."
    l "You reminded him of his dead abusive father? The worst."
    mcx "[[Oh don't get me started, Louie! You're half of this problem!]" with vpunch
    l "I'm joking! Didn't know the kid had some baggage. Just wanted to lighten up the mood!"
    l "Anyways, he's nearing his end now. {p} Initiating hack in..."
    l "3... {p} 2..."

    scene realife_lightning_01
    with fade

    window hide

    pause

    play sound "soundfx/thunder.ogg"

    scene realife_lightning_02 with flash

    window hide

    pause

    scene lou_call8
    with fade

    l "1... {p} Louie's personal [[{color=#ff3030}RedBelt_Kung-Fu{/color}] hack is in, booyah!"

    scene lou_call7
    with dissolve

    l "Show me the money!" with vpunch
    l "So, who's this motherfucker that dares to steal from my boy, huh? {p} ...Wait this guy?"
    l "This guy is..."

    play music "soundfx/ambient_computer.mp3" loop

    scene realife_comp_01
    with fade

    pause

    scene realife_comp_02
    with redflash

    pause

    play sound "soundfx/hardware_error.ogg" fadein 2.0

    "{size=+7}{color=#f93b3b}WARNING! {w} WARNING! {w} WARNING!{/color}{/size}"

    scene realife_comp_close
    with fade

    q "S-S-Sir.... d-dri-drivers o-o-overloading... c-cortex injec-i-i-injector..."
    q "Unk-known C-c-code interfering.... with... with....with... f-forced e-em-ulation e-ejection..."

    scene realife_comp_02
    with dissolve

    "{size=+7}{color=#f93b3b}WARNING! {w} WARNING! {w} WARNING!{/color}{/size}"

    scene realife_lightning_shocking
    with fade

    "{i}{color=#f93b3b}*bbbbbzzzzzzzztttttt!* {w} *bbbbbzzzzzzzztttttt!*{/color}{/i}" with vpunch
    "{i}{color=#f93b3b}*WWWWHIIIIIIIIIIRRRRRRRRRRRRR!!!*{/color}{/i}" with vpunch


    window hide

    pause

    scene realife_comp_close
    with dissolve

    q "I-Interference impossible... H-Human i-i-intervention re-req-required...."
    q "Calling.... 911..." with vpunch
    q "S-Send h-help... to... C-C-Capital City... Apa-apart...ment... {p} R-Room 422..."
    q "S..See...Seeking med-medical... h-help.. {p} h-hur....ry....yy.....y....."

    stop sound fadeout 1.0

    stop music fadeout 1.0

    scene realife_comp_01
    with slowfade

    pause

    scene realife_lightning_dead
    with slowfade

    pause

    play music "music/Teller of the Tales.mp3"

    if notification_songs == True:
        $ renpy.notify("Kevin MacLeod - Teller of the Tales")

    scene black
    with fade

    play sound "soundfx/glitch.ogg" loop

    scene glitch1 animated with fade:
        "v_stab_mcx"
        pause 0.7
        "v_stab_glitch"
        pause 0.7
        repeat

    window hide

    "(W-What's going on with my character!?)" with vpunch

    mcx "[[\"L-Louie? Louie are you there!?\"]" with vpunch
    mcx "[[\"I-I-I can't move!!\"]"
    mcx "[[\"L-LOOOOOOOOUIE!!\"]"
    r "AAAAAAAAAAAAAAAAARRRRRRRRRGGHHHHHHHH!!" with vpunch
    r "W-What did you do to me!?!" with vpunch
    r "I-It...hurts..so...much..."
    "(Hurt?)"
    r "AAAAAAAAAAAAAAAAAAAAAAAAAAAAARRRRRRRRRGGHHHHHHHH!!" with vpunch

    window hide

    scene glitch2 animated:
        "v_stab_mcx_solo"
        pause 0.6
        "v_stab_glitch"
        pause 0.6
        repeat

    "(Rustbucket!? W-Why's he glitching like that—)"
    mcx "AAAAAAAAAAARRRRRRRRRGGGGGGGGGGGGGHHHHHHHHHHHHH!!" with vpunch
    "(P-Pain?)"
    "(T-That's impossible! A VR headgear can't make a player feel pa—)"
    mcx "UUUUUUUUUURRRRRRRRRRGGGGHHHHHHHH!!" with vpunch

    window hide

    scene glitch3 animated:
        "v_glitch_hand1"
        pause 0.2
        "v_glitch_hand3"
        pause 0.2
        "v_glitch_hand1"
        pause 0.2
        "v_glitch_hand2"
        pause 0.2
        "v_glitch_hand3"
        pause 0.2
        repeat

    "(I feel my body's...being...torn...apart..)"
    mcx "AAAAAAAAAAAHHHHHHHHHHHHH!!" with vpunch
    "(P-Please...no...more...why's...why..is..this..happening!?!)"

    scene v_glitch_body
    with dissolve

    mcx "UUUUUUUUUUURRRRRGGGGGGGGGGGGGHHHHHHHHHH!!!" with vpunch
    gm "BOSS!! MILORD!!" with vpunch
    c "W-What's happening to the both of them!?" with vpunch
    s "I-I don't know either!" with vpunch

    scene v_glitch_face
    with fade

    mcx "T-THIS...ARRRRRRGGGGGGGGGGGHHHHHHHHHHHHHHHH!" with vpunch
    "(E-Every...part..of...m-my...body's..in...p-pain...)"
    mcx "AAAAAAAAAAAAAAAAAAAAAAAAARRRRRRRRRRRRRRRRGGGGGGGGGGGGGHHHHHHHHHHHHHHH!!!!!!!" with vpunch
    "(P-Please...I-I...don't...want...to..feel—)"
    mcx "RRRRRRRRRRRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHH!!!!!!!!" with vpunch

    stop sound fadeout 2.0

    scene v_glitch_vanish
    with slowflash

    pause

    scene v_glitch_flash
    with slowflash

    d "W-Where did they go?"
    lu "W-What did just happen desu~"
    s "W-What in the world was that?"

    scene v_stab_vanish
    with dissolve

    stop music fadeout 3.0

    c "Aramis!" with vpunch
    c "Rust!" with vpunch

    play sound "soundfx/siren.ogg"

    scene black
    with slowfade

    pause

    scene h_ambulance
    with dissolve

    pause

    scene black
    with slowfade

    stop sound fadeout 2.0

    pause

label hospital_start:

    scene black
    with fade

    sm "Jen, those heels look fabulous on you today! What brand is that? Cucci?"
    sm "The fuchsia just {i}really{/i} brings out \"zaniness\" of that... uh.. glasses of yours!"
    sm "Oh! And it matches well with those earrings of yours too!"
    jy "Ooohhh wwooowww! Look out ladies, casanova here is making my knees weak!" with vpunch
    jy "You've got to do better than that Sim! Compliments? This early in the morning? {p} Please."
    sm "How rude of you, Jenny! For your information, I'm quite the sweet talker in this ward, you know?"
    jy "Oh please, Simon! You think I don't know what you're up to? I heard that a certain \"yPhone Z\" is coming out tomorrow?"
    jy "And I think someone's gonna camp out to get their hands on it first? Hmmm?"

    play music "music/Sad_French_Accordion.mp3"

    if notification_songs == True:
        $ renpy.notify("Dana Boulé - Sad French Accordion")

    scene hs_1
    with dissolve

    jy "You need to do better than that if you want me to cover your night shift today! Let's say, getting me a \"Rosy Red\" one?"
    sm "Jen, you're a bitch, you know that?"
    jy "I know, hon, I know. {p} \"Rosy Red\" or no can do. It's up to you."
    sm "Fine! By the way, those heels look bought from a dollar store."
    jy "HEY!" with vpunch

    scene hs_2
    with dissolve

    sm "Gotta go! Patient's waiting!"

    scene hs_3
    with fade

    sm "A fine morning to you sir... {p}...Ah. I forgot his name. Oh well!"
    sm "You're still asleep as always and as handsome as ever. Although, they could've shaved that bushy beard of yours."
    sm "Let's see that IV fluid of yours first..."
    sm "You know sir, supposedly, talking to a comatose patient is actually quite beneficial to one's recovery from a comatose."
    sm "It's said that they're \"aware\" of their surroundings in reality or whatnot despite being asleep... creepy isn't it?"
    sm "Hmmm... what's that? You want me to turn the TV for you? Why of course! I can't deny a request like that!"

    scene hs_4
    with dissolve

    sm "If Dr. Aanya sees me, I'll say I'm just following your orders."
    sm "Now, let's see... I think Guy was supposed to announce the stores with those exclusive yPhone colors..."
    sm "Aha!"
    tv "—Woah mama! Have you ever tasted the freshly brewed coffee—" with vpunch
    sm "C'mon! I don't want to watch a commercial break! I already watch enough of—"
    u "Hngg.... hngg..."

    scene hs_5
    with dissolve

    sm "S-Sir....?"
    u "Hrmm.... nghn...."
    sm "SIR!?!" with vpunch
    u "W-What... time.... is.. it?"
    u "I-I'm gonna... be... late... for work..."
    sm "O-Oh my god! Y-You actually woke up? I-I mean—" with vpunch
    sm "Sir! Stay still! Your muscles are still in atrophy and you might hurt yourself by moving sporadically like that!" with vpunch
    u "W-Who're....you...? Why're... you... in my.... house..?"
    sm "Sir, listen carefully, you're currently in a hospital due to an accident."
    sm "And you just woken up from a long sleep, a comatose of almost 3 months. Your body is still weak!"
    u "Coma...tose? H-Hospital..? Atro...phy..? W-What.. talking abo—?"
    u "AARRRGGHHH!!" with vpunch
    u "M-My head's...t-throbbing...it..hurts..."

    scene hs_6
    with dissolve

    sm "Oh my god! Oh my god! Sir! J-Just stay put! D-Don't move, okay? I'm gonna find Dr. Aanya and she'll discuss this with you!" with vpunch

    scene black with fade

    sm "J-Jenny! Where's Dr. Aanya!?"
    "..."
    "(Who was that guy?)"
    "(And where am I?)"

    scene hs_7
    with dissolve



    menu rise:
        "Get up":


            u "Uughh... I don't... feel.. that... great..."
            scene hs_8 with dissolve
            u "Ooophhh. My...muscles... weak...can't..."
            "(I just want to sleep again...)"
            "(No!)" with vpunch
            "(I need to go to work!)" with vpunch
            scene hs_7 with dissolve

    menu rise2:
        "Get up again.":

            scene hs_8 with dissolve
            u "Uryaaaaaaaaaaaaaaaahhh!" with vpunch
            scene hs_9 with dissolve

    scene hs_10
    with dissolve

    u "Finally!" with vpunch

    scene hs_11a
    with slowflash

    u "Damn! Why is it so damn bright in here!?" with vpunch

    scene hs_11b
    with dissolve

    u "Hmm.. its morning?"
    u "And I'm actually in the hospital? {p} I mean, he said I was in one but..."
    "(How the hell did I ended up here?)"
    "(And what happened that got me in here...?)"
    u "...."
    "(Argh! Why can't I remember? I didn't go out drinking, did I?)" with vpunch
    "(No... the guy said I was comatosed for 3 months. Nah, that can't be possible? Can it?)"
    "(No! No! No! What day is it? 3 months he said? What did I last do—Nah, he's probably lying.)" with vpunch
    u "Shit! The VR-22XX! I was suppose to give a demo of the prototype!" with vpunch
    u "Boss will tear my ass a new one!" with vpunch

    scene hs_12
    with dissolve

    u "{i}*sigh*{/i}"
    "(Ah fuck it! I'm in the hospital anyways! What're they gonna do? Harass a patient back to work?)" with vpunch
    "(But I really wanted that bonus. Wait! If I'm in the hospital... does my insurance cover this? Fuck!)"
    "(I can't remember a goddamn thing that put me in this. I know I was still testing the prototype... Did I get a stroke mid-game or maybe a heart attack?)"
    "(I'm really a fat-fuck now, aren't I? I know I should've heeded those warning about the cholesterols and artery blockage and shit but...)"

    scene hs_13
    with dissolve

    "(I really should start losing weight after this. Whoever hauled me out of that apartment should receive a medal carrying..this...fat..)"
    u "..ass..of...mine?"

    scene hs_14
    with dissolve

    u "W-What's with this arms?"
    "(Holy shit—I've lost weight!? Not only my arms, my body too!)" with vpunch
    "(How long did I exactly stay here? 3 months seems impossible for me to lose this much?)"
    "(I mean, I'm no expert at losing weight but this is just...)"
    "(If its just a couple of pounds, its understandable but I seem to have lost more than 200...)"

    scene hs_13
    with dissolve

    "(This is getting weirder by the second... A 3-month comatose with no memory and this weight loss?)"
    "(If I knew any better, they could tell me I was abducted by aliens and performed surgery on and I'll still believe it.)"
    "(I...I need to take a seat.)"

    scene hs_12
    with dissolve

    menu sit_over:
        "Move over":
            u "Ah..ah..ah...this muscles are so goddamn sensitive..."
            u "Careful..."

    scene hs_16
    with slowfade

    window hide

    pause

    u "Now then... what exactly was the {i}very last thing{/i} I did? {p} Think!"
    u "... {p} .... {p} ....."
    "(Its all coming to me now. If I recall this correctly, the morning before... I was about to do the usual. Testing and tweaking the prototype...)"
    "(Except that day was different because of... {w} THE TRIAL! Yes!) {p} (I was suppose to find out the culprit! The one who stole the elixirs!)" with vpunch
    "(LOUIE! That's right! He was there too! He was suppose to use his hack, use it to...)" with vpunch
    "(Use it in the trial to find the thief... use it on someone.) {p} (Like... that kid. Rustbucket...)"

    scene hs_15 with vpunch

    u "URRRGGHHH!" with vpunch

    scene flb_1
    with fade

    pause

    scene flb_2
    with fade

    pause

    scene flb_3
    with fade

    pause

    scene flb_4
    with fade

    pause

    scene flb_5
    with fade

    pause

    scene hs_15
    with dissolve

    u "AAARRRGGGH!" with vpunch
    u "Dammit! It feels like my brain's gonna explode!" with vpunch
    "(Breathe in... {p} Breathe out...)"
    "(Breathe iiinnn..... {p} Breathe ooouuuttt.....)"
    "(Breathe in... {p} Breathe out...)"
    u "...."

    scene hs_16
    with dissolve

    u "I remember now."
    u "That glitch..."
    "(I felt... as if I was being shredded, like my soul was being ripped out into tiny little pieces...)"
    "(Every corner of my body was screaming in pain, in agony, as if my skin was being picked apart piece by piece, cell by cell...)"
    "(That... what exactly was that? Quanto would notice something strange like that happening!)" with vpunch
    "(He would've already ejected me by that point... but he didn't. Why?)"
    u "I'm even more confused than I was a minute ago. I thought remembering what happened would give me answers by now but instead the questions keeps piling up..."

    scene hs_15
    with dissolve

    u "And its getting more ridiculous... Argh! I feel like ripping my hair out—"

    window hide

    pause

    u "...hair? {p} Since when did I have hair and... {w} a beard too!?"

    scene hs_18
    with dissolve

    "(The mirror!)"
    u "Oh no."
    u "No! No! No! No! No! Noooooooope!" with vpunch

    stop music fadeout 3.0

    scene hs_19
    with fade

    "(Am I seeing things right!? This guy... this isn't me!)"
    "(That is DEFINITELY NOT ME IN THE SLIGHTEST OR EVER!!)" with vpunch
    "(Am I tripping!?)" with vpunch
    "(First of all, I don't have black hair! I don't {i}even{/i} have hair or the ability to grow a beard! The only hair I got growing was my pubes! And those were blonde pubes!)"
    "(Second, my eyes are brown and not blue. {p} And finally, did I mention that this guy is young... {i}really{/i} young!)"
    "(With all that said, we can conclude that the ME in this mirror doesn't look like the one I'm remembering!)"
    "(Who is this guy even!?)" with vpunch

    tv "...ANNNDDD III'MMM BAACCKK! CAAPPITTAALL CITTYY!!!" with vpunch
    tv "{i}*cough*{/i} {i}*cough*{/i}" with vpunch

    scene hs_20
    with dissolve

    play music "music/Crinoline Dreams.mp3"

    if notification_songs == True:
        $ renpy.notify("Kevin MacLeod - Crinoline Dreams")

    tv "Ugh... no more shouting... my throat.... ANYWAYS! {i}*cough*{/i}"
    tv "I'm your host, Guy McDuff, you might know me from nearly-classic films such as \"{color=#00fff6}{i}Pacific Tim{/i}{/color}\" or \"{color=#00fff6}{i}Summer Thyme Gaga!{/i}{/color}\", back to you for the breaking news of the hour!"
    tv "And I know what you're thinking!" with vpunch
    tv "\"Hey Guy, I'd rather prefer you tell us where the locations of those exclusively colored \"yPhone Zs\" are rather than hear your dumbass comments.\""
    tv "I know! I know! Hearing about those exclusive colors is just making my metaphorical vagina wet—"

    pause

    scene guy1

    tv "GODDAMIT DAVE! I JUST CAME BACK FROM A SUSPENSION AND YOU'RE THREATENING TO GIVE ME ONE AGAIN!" with vpunch

    scene guy2

    tv "You Sir, are a sexist! A woman-hater! Vaginas are God's gift to—" with vpunch

    scene guy_tech

    "We'll be right back!"

    window hide

    pause

    scene guy3

    tv "Mfrmhfmr..threateningmewithanothersuspension...."
    cm "G-Guy, we're live!" with vpunch

    scene guy4

    tv "Ah! {p} A-ANYYYYWWAAYYSS!" with vpunch

    scene guy5
    with dissolve

    tv "We've got Trish live in the \"{color=#00fff6}Reign Corporation{/color}\" headquarters for the appointment of their new Chief Engineer as well as the release date announcement of their new VR Headgear!"
    u "\"New Chief Engineer\" of Reign Corp?"
    "(Wait! That's my position!)" with vpunch

    scene tri1
    with dissolve

    tvt "This is Trisha Santos reporting live from the \"{color=#00fff6}Reign Corporation{/color}\" headquarters!"
    tvt "Reign Corp's Hardware Division, responsible for the technology behind this century's greatest innovation, the Virtual Reality machines, is about to give the date of the release of their newest headgear!"

    tvt "It was a great setback for the people of \"{color=#00fff6}Reign Corporation{/color}\" when they found out the passing of their Chief Engineer who was found dead at his home on the afternoon of—"
    u "D-D-Dead!? ME!?! N-No! T-That can't be! I'm here!" with vpunch
    u "I'm here!" with vpunch

    scene tri2
    with dissolve

    tvt "—he was also the son of Reign Corp's founding engineer. The father of the \"{color=#00fff6}EVE Artificial Intelligence Unit{/color}\" and also of the \"\"{color=#00fff6}Virtual Reality Machines{/color}\"!"

    scene tri3
    with dissolve

    tvt "And its up to the new Chief Engineer, Mr. Yoshi Takahashi, who had work under the former chief to take this technology to the next level!"
    tvt "He worked as the—"
    cm "Trish! I-I think that's him!" with vpunch

    scene tri4
    with dissolve

    tvt "Oh! You're right!" with vpunch
    tvt "Sir Yoshi!"

    scene tri5
    with dissolve

    tvt "Mr. Yoshi Takahashi! A word please!" with vpunch
    y "Hmmmm...?"

    scene tri6
    with dissolve

    y "W-Whoa! Whoa! Whoa!"
    y "Is this about the couch last night!?!" with vpunch
    tvt "Ah..that's—"

    scene tri7
    with dissolve

    y "IT WAS NEAR A DUMPSTER AND I WAS LEGALLY ALLOWED TO DO THAT!" with vpunch
    y "Maybe there was a U-Haul truck beside that couch that I didn't see!" with vpunch
    y "And {i}maybe{/i} I timed my grabbing of the couch when the movers went back to that nosy neighbor's house who wanted to move because I was too loud!" with vpunch
    y "It serves him right!" with vpunch
    y "BUT ALL OF THAT WAS LEGAL, MIND YOU! IT WAS NEAR A DUMPSTER THAT WAS 3 BLOCKS AWAY! I REST MY CASE!"

    scene tri8
    with dissolve

    tvt "Uhhh... Sir, we're not asking about that but your position as the new Chief Engineer."
    y "Oh! {p} My bad!"
    y "What do you want to ask?"

    scene tri9
    with dissolve

    tvt "Were you and the former Chief Engineer close? {w} What kind of person was he? {w} How do you feel inheriting his old position?"
    y "Oh, its about {i}the Chief{/i}?"
    y "Hmmmm..."

    scene tri11
    with dissolve

    y "CCCCHHHHHHIIIIIIEEEEEFFFFFF!!!!!" with vpunch
    tvt "S-Sir, please give back the mic..."
    y "I know they got cable in heaven!" with vpunch
    y "Why did you leave too early, Chief!?" with vpunch

    scene tri10
    with dissolve

    y "The suits are asking me about the prototype and I don't really know what you did to those things!" with vpunch
    tvt "Excuse me?"
    y "I also bought the \"{color=#00fff6}The Basic Guide to Necromancy{/color}\" so that you can finish your work one last time before departing to heaven!" with vpunch
    y "But your corpse was too fat, I mean, like 300 kilos of fat, and was too heavy for me alone to steal it from the morgue!"
    tvt "{i}*cough*{/i}" with vpunch
    y "So I resorted to a \"{color=#00fff6}Spirit Channeler{/color}\" but he demanded 129 dollars!"
    y "I ain't paying that much for some long distance phone call!"

    scene tri11
    with dissolve

    y "So please! Give me a sign, Chief! Or better yet, give me a working prototype now!" with vpunch
    y "Maybe some hot chicks from there too! Like Cleopatra?"
    tvt "Uh, Sir? Is the supposed release of the new VR Headgear next year delayed?"
    y "Forget about delayed! More like impossible 'cause the Chief brought the VR Prototype with him to the grave!" with vpunch
    y "Ah, edit that out!" with vpunch
    tvt "But we're live, Sir."

    scene tri12
    with dissolve

    y "Come again?"
    tvt "We've been live for the past few minutes."
    y "Shi—Uhh..."

    scene tri13
    with dissolve

    y "I LOVE COCAINE!" with vpunch
    y "I'M SO HIGH RIGHT NOW THAT I'M SPEAKING IMAGINARY THINGS AND YOU SHOULDN'T BELIEVE ME!!" with vpunch
    y "WoOoHOoOoO!" with vpunch
    tvt "Sir, please give the mic back!"

    scene tri14
    with dissolve

    tvt "{i}*huff*{/i} {w} {i}*huff*{/i} {w} {i}*huff*{/i}"
    tvt "T-That... guy... can... run... really... fast..."

    scene tri15
    with dissolve

    tvt "My aching back—I mean.."
    tvt "B-Back to you, Guy!" with vpunch

    scene guy6
    with dissolve

    tv "The hell was that?"

    stop music fadeout 3.0

    scene hs_20
    with fade

    tv "Uhh.. on other news..."
    "(Aha..haha...)"
    "(Hahahahaha!)" with vpunch
    "(Yoshi's still Yoshi. Good for him taking over my job.)"
    u "{i}*sigh*{/i}"
    "(I really needed that.)"
    "(To be honest, I should be much more shaken up now that I've come to the realization that I'm already \"dead\", so to speak.)"
    "(I mean, my life and social circle was below average at best. There wasn't much to reminisce about or be concerned 'cause someone's waiting for me or something.)"
    "(Those who I considered to be my friends were at most, my guild members but they knew me only as \"Aramis\" and as for real life, personally, there was only Louie and Yoshi.)"
    "(And then there's myself, an appearance as if God created me scraping the bottom of the barrel of ugly.)"
    "(All in all, it wasn't an appealing life really. The moments I felt \"alive\" were those when I dominated others and lived grandiosly in \"Reincarnotica\" but now...)"
    "(I feel... alive. {w} For the first time in my life, I want to live. To experience another go of living a life, you know? And maybe, experience love?)"
    "(...)"
    "(FUCK! That sounded stupid! \"experience love\" my ass! What is this? Somekind of Romantic Comedy!?)" with vpunch
    "(Okay, I need to snap out of this. I need to learn facts about who this guy and—)"

    play sound "soundfx/knock_door.ogg"

    "{i}{color=#fff}*knock*{/color}{/i} {i}{color=#fff}*knock*{/color}{/i}"

    play music "music/East of Tunesia.mp3"

    if notification_songs == True:
        $ renpy.notify("Kevin MacLeod - East of Tunesia")

    scene dr_1
    with fade

    a "Oh! I see you're already up."
    a "I thought the long sleep would make you weak and lethargic."
    a "But I guess not."

    scene dr_2
    with dissolve

    a "You should've seen how Simon came rushing into the building next door shouting \"He's Awake! He's Awake!\" like a madman."

    scene dr_3
    with dissolve

    a "I was honestly shocked by the news but the meeting was quite important so I'm sorry I was late coming here."

    scene dr_2
    with dissolve

    a "Also, I've already called Fiona and Priscilla. That girl can scream her lungs out, I give her that."
    u "Uhmm..."

    scene dr_4
    with dissolve

    a "I know, I know..."
    a "I understand that you have your differences with them but they're the only people that are willing to take care of you for the time being."

    scene dr_3
    with dissolve

    a "With the situation of your apartment and your..."
    u "No, I-I mean—"

    scene dr_4
    with dissolve

    a "I'm really sorry, its your landlord he's quite a bit... {w} hard to talk to."
    a "We even tried calling your relatives should the comatose last for years or {i}worse{/i} and they too... were really {i}really{/i} hard to talk to either."
    a "Even calling you and your father a... nevermind."

    scene dr_7
    with dissolve

    a "{i}*sigh*{/i}"
    a "It seems your \"reputation\" precedes you but thankfully, Fiona seems to have no problem helping."
    u "B-But—"

    scene dr_6
    with dissolve

    a "Please, as your doctor's advice. When Priscilla found out about your accident at that \"Virtual Reality Cafe\", she came knocking on my door that evening, crying her heart out..."

    scene dr_7
    with dissolve

    a "Regarding your apartment, the landlord happily evicted you when he found out your situation. Fiona had no choice but to bring your items to their home."
    a "So whether you like it or not, you're gonna be staying there till you recover, alright?"

    scene dr_6
    with dissolve

    "(Ookkaaaaayyy...)"
    "(It seems I already have problems before finding out who this guy is first.)"
    "(I would love to tell this woman in front of me that I'm not who she thinks I am.)"
    "(That I'm actually a man in my 40s and the former Chief Engineer of the \"{color=#00fff6}Reign Corporation{/color}\" inhabiting his body...)"
    "(But I might get admitted into another kind of \"hospital\" if I insist telling her that.)"
    "(So... there's only one way.)"
    u "I-I'm really sorry but—"

    scene dr_8
    with dissolve

    a "Being stubborn with that—"
    u "No, Doc! Frankly, I'm happy with the offer but... I don't know who these people you're talking about." with vpunch
    a "..?"
    a "What do you mean by that?"
    u "This Fiona and Priscilla... who exactly are they? To be honest, Doc, I'm not particularly sure who you mentioned earlier are."

    scene dr_7
    with dissolve

    a "Oh..Oh boy."
    a "This is gonna take us... some time."
    a "Memory loss... {p} It didn't even crossed my mind that your memory would be affected by that."
    a "It seems that the accident that got you into this comatose might've also affected your memories. It's better—"

    stop music fadeout 3.0

    scene guy5

    tv "Our show is sponsored by the Bih Gu-Dichs Viagra Solutions!! Have you ever felt that you can't keep with your..." with vpunch

    scene dr_7
    with dissolve

    "..."
    a "Uh..uhm... let's turn this off, okay?"

    scene dr_9
    with dissolve

    a "Honestly, what are they showing on public television these daya? Viagra commercials?"

    scene dr_6
    with dissolve

    a "{i}*sigh*{/i}"

    a "As I was saying... let's take a seat, shall we?"

    scene black
    with slowfade

    scene dr_19
    with fade

    play music "music/Easy Lemon.mp3"

    if notification_songs == True:
        $ renpy.notify("Kevin MacLeod - Easy Lemon")

    a "So let's start with this, do you remember your name?"

    jump name_hero

    label skip_intro:

    hide screen intro_skip_start_bg
    hide screen intro_skip_skip_bg
    hide screen intro_skip_choice

    scene black
    with fade

    a "..ey. Are..."
    a "..you...alright?"

    scene dr_19_skip
    with fade

    u "Argh. My head..."
    a "Are you alright, dear?"
    u "Hm?"

    play music "music/Easy Lemon.mp3"

    scene dr_19
    with fade

    a "Do you need me to get you some water?"
    u "N-No thank you."
    a "For a minute there, you seemed to be spacing out."
    u "Y-Yeah. I recalled something."
    u "A game I played, I think?"
    u "Anyways, what were you asking me about again?"
    a "Do you remember your name?"

    jump name_hero

    label name_hero:
        $ mc = renpy.input("Urgh.. What's my name again? (Press Enter for Default Name)", allow=" 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length=10) or "Leon"
        if mc is not None:
            $ check_name = len(mc)
            if check_name == 1:
                "You must name your character a minimum of 2 letters."
                jump name_hero
        $ mc = mc.title()
        "(It's [mx], I think?)"
        menu:
            "Yes":
                pass
            "No":

                jump name_hero


    mx "I think, it's... {w} [mx]? {p} I'm sorry, my memory's still a bit hazy."
    "(Wait! That was my {i}real{/i} name!)" with vpunch

    scene dr_13
    with dissolve

    a "Well, it seems you still remember your identity. Let's take things slowly at first before I ask some personal questions."
    "(What? Did we have the same name? That's a creepy coincidence...)"

    scene dr_14
    with dissolve

    a "For now, I'm just gonna ask you some basic questions. Everyday stuff that you might've encounter. Don't get worked up if you don't know some of them."
    a "We're just analyzing to what extent your memory loss affected you."
    mx "Ummm... okay?"

    scene dr_19
    with dissolve

    a "Well then, random question number one, do you know who that TV personality is? The one in the television?"
    menu question1:
        "Rye McGill":


            scene dr_18 with dissolve
            mx "Is is it Rye McGill?"
            scene dr_20 with dissolve
            a "Incorrect. It's actually Guy McDuff."
            mx "Oh, I thought that might be his name."
            scene dr_13 with dissolve
            a "Rye McGill is the weatherman but it's alright."
            a "We're still just starting out and its understandable to not know their names."
            a "But let's move on to the next question."

            jump question2
        "Duff McGee":


            scene dr_18 with dissolve
            mx "I think it was... Duff McGee?"
            scene dr_20 with dissolve
            a "Hmmm... close but still incorrect. It's Guy McDuff."
            a "We're still just starting out and its understandable to not know their names."
            a "Not that they're really important. So..."
            scene dr_13 with dissolve
            a "Let's move on to the next question."

            jump question2
        "[gr]Guy McDuff":


            scene dr_18 with dissolve
            mx "Guy McDuff, from nearly nominated films such as..."
            scene dr_20 with dissolve
            a "Okay! No need for...that." with vpunch
            a "He always tells them like everyone cares for those movies..."
            a "Ah! Anyways..."
            scene dr_13 with dissolve
            a "It seems your memory is working fine in remembering some details. That's great!"
            a "Moving on..."

            $ question_a_1 = True

            jump question2

    label question2:

    scene dr_11 with dissolve
    a "Let's keep it up. Then for my second question, who's our current president?"
    scene dr_19 with dissolve

    menu current_pres:
        "[gr]President Pressy McPresfeys":

            mx "Easy, President Pressy McPresfeys. With a name like that, who {i}wouldn't{/i} be president?"
            scene dr_21 with dissolve
            a "Quite a joker now, are we?"
            a "Well, you're correct."
            a "I've seen lots of kids named... \"uniquely\" but his takes the cake."
            mx "Well, it worked out in the end for him."
            scene dr_19 with dissolve
            a "Haha.. I guess so."
            a "This is great!"
            a "Then let's move to our third question."

            $ question_a_2 = True
            jump question3
        "President Ganye Quest":


            mx "Well, isn't it the one and only, Ganye Quest?"
            scene dr_20 with dissolve
            a "... {w} Wrong."
            mx "Well, he should've been. That debate highlight though, \"{color=#00fff6}Imma let you finish your debate but...{/color}\" just tugs the heart strings."
            scene dr_19 with dissolve
            a "Okay... you don't remember the president but you remember Ganye's debate. That's also considered good progress, I guess."
            a "Let's move on to our third question."

            jump question3
        "President Pauly Rotichs":


            scene dr_19 with dissolve
            mc "I guess... President Pauly Rotichs?"
            a "Who's that?"
            mx "I... I don't {i}really{/i} know. As if I was forced to say it for some reason. Like, I have no choice whatsoever."
            scene dr_21 with dissolve
            a "Are you sure that memory loss isn't the only affliction you have?"
            mx "I'm just joking, Doc!" with vpunch
            scene dr_19 with dissolve
            a "Right... the correct answer is President Pressy McPresfeys, okay?"
            mx "Seriously?"
            a "Yes. I mean the name's quite weird but he's our President."
            "(What if I was named Dicky McDickface? Would it change anything? Probably not.)"
            a "Next question."

            jump question3

    label question3:

    scene dr_11 with dissolve
    a "So far, so good! I guess. So, let's ease a bit to some recent stuff, do you still remember the game you played in that \"{color=#00fff6}Virtual Reality Cafe{/color}\"?"
    scene dr_12 with dissolve

    menu game_played:
        "Third+Life":

            scene dr_13 with dissolve
            mx "Probably... Third+Life?"
            scene dr_19 with dissolve
            a "Are you sure?"
            "(No I'm not, woman!)" with vpunch
            mx "I... guess so?"
            scene dr_20 with dissolve
            a "I'm sorry but that's incorrect."
            mx "How do you know?"
            scene dr_18 with dissolve
            a "Well, 'cause that \"{color=#00fff6}Virtual Reality Cafe{/color}\" you were in was only hosting Reincarnotica as their game."
            mx "That... makes sense. The machine's are quite expensive."
            scene dr_19 with dissolve
            a "You know how expensive those stuff?"
            mx "Speculating."
            a "Finally, let's move on to some personal questions."
            "(Ah shit.)"

            jump family_quest
        "World of Spelunkycraft":

            scene dr_13 with dissolve
            mx "Probably... World of Spelunkycraft?"
            scene dr_19 with dissolve
            a "Are you sure?"
            "(No I'm not, woman!)" with vpunch
            mx "I... guess so?"
            scene dr_20 with dissolve
            a "I'm sorry but that's incorrect."
            mx "How do you know?"
            scene dr_18 with dissolve
            a "Well, 'cause that \"{color=#00fff6}Virtual Reality Cafe{/color}\" you were in was only hosting Reincarnotica as their game."
            mx "That... makes sense. The machine's are quite expensive."
            scene dr_19 with dissolve
            a "You know how expensive those stuff?"
            mx "Speculating."
            a "Finally, let's move on to some personal questions."
            "(Ah shit.)"

            jump family_quest
        "[gr]Reincarnotica":


            scene dr_13 with dissolve
            mx "There's only one game that's valuable to play nowadays and its \"{color=#00fff6}Reincarnotica{/color}\"."
            scene dr_15 with dissolve
            a "What do you mean \"valuable to play\"?"
            mx "Basically, the \"{color=#00fff6}Reincarnotica{/color}\" machines are quite expensive {i}but{/i} their return of investment on those are high due to the fact that..."
            mx "...people play longer with that game than any other, even up to days at a time. Some people treat it as their actual jobs."
            scene dr_19 with dissolve
            a "Really? I never thought of that a game could be a job..."
            a "So, were you also part of those working there?"
            mx "I..I don't remember, Doc."
            a "It's okay. Atleast you did well on this question."
            a "Finally, let's move on to some personal questions."
            "(Ah shit.)"

            $ question_a_3 = True

            jump family_quest

    label family_quest:

    scene dr_14 with dissolve
    a "These will be family related questions. I've talked with Fiona about some basic stuff about your life and she was happy to oblige."
    scene dr_15 with dissolve
    a "So please answer them honestly, okay?"
    mx "Okay."
    a "If you don't know, that's fine as well."
    scene dr_14 with dissolve
    a "So, first things first..."
    a "Do you remember anything about your father? Like his name?"
    scene dr_13 with dissolve
    mx "That's..."
    mx "I don't have an idea on who he is to be honest, Doc."
    mx "Nothing comes to my mind."
    "(Literally, I don't have any clue who this guy's father is.)"
    scene dr_20 with dissolve
    a "I... see."
    scene dr_18 with dissolve
    a "Father figure is affected by amnesia... possibly repressed..."
    scene dr_19 with dissolve
    a "Well then, your mother's? Do you remember her?"
    mx "Is it that Fiona? Or possibly Priscilla?"
    scene dr_13 with dissolve
    a "Fiona? Priscilla? N-No. No!." with vpunch
    a "[mx], please answer honestly! Don't guess if you don't and judging from that answer, I guess you don't."
    mx "I'm sorry. I-I was just trying to be helpful."
    scene dr_19 with dissolve
    a "That's okay, dear."
    mx "Then, do you know who and where my parents are?"
    scene dr_20 with dissolve
    a "That's..."
    a "I think Fiona might be more suited to tell you about them rather than me."
    a "It's quite... personal for you."
    mx "I completely understand, Doc."
    scene dr_14 with dissolve
    a "As for the results..."

    if question_a_1 == True and question_a_2 == True and question_a_3 == True:

        scene dr_18 with dissolve
        a "You did well remembering the things I asked you in the first 3 questions but..."
        a "...the questions about your parents are quite problematic. It seems your memory loss is connected with that?"
        mx "Is that... bad?"
        scene dr_17 with dissolve
        a "No! I-It's just that—" with vpunch
        scene dr_23
        a "Woops!" with vpunch
        a "My pencil..."
        "(Woah! I can see her underwear!)"
        scene dr_24 with dissolve
        a "Ah.. it went under the chair!"
        a "Wait. I can still reach it by this side if I try hard enough..."
        "(She really likes purple, huh?)"
        "(Well, that view will be stuck in my mind all day..)"
        scene dr_16 with dissolve
        a "Got it!" with vpunch
        a "Stupid pencil."
        scene dr_19 with dissolve
        a "Anyways, it's also considered good results!"
        a "So, no need to worry."
        mx "Alright."

        $ aanya_panties = True

        jump after_questions
    else:



        scene dr_18 with dissolve
        a "Let's see."
        scene dr_19 with dissolve
        a "We still need to work on remembering some things but the results are optimistic."
        a "The memory loss could be recovered slowly later on but for now it doesn't seem to affect you in any other way..."
        scene dr_13 with dissolve
        a "It's nothing to be worried about and just slowly pace yourself."
        a "I will, Doc."

        jump after_questions

    label after_questions:

    scene dr_11
    with fade

    a "Now, as for my diagnosis..."
    a "Its likely that your Retrograde amnesia might've repressed any memory related to people you personally knew to an extent."
    a "I don't know what variables play in here but as for the memory related to everyday, general things it wouldn't hinder you as much."

    scene dr_12
    with dissolve

    a "You just need to rekindle those personal relations you've forgot..."
    mx "Doc, what happened to me exactly? How did I ended up here in the first place?"
    a "Let's see..."

    scene dr_13
    with dissolve

    a "About 3 months ago, you were admitted here when the staff of that \"{color=#00fff6}Virtual Reality Cafe{/color}\" I've mentioned before, found you unconscious in one of their booths."
    a "Priscilla told me what happened and I immediately took over the presiding doctor here. We did a series of tests to determine why you were unconscious."

    scene dr_15
    with dissolve

    a "And the bizarre thing is... all of it returned \"normal\". Except for your comatose, nothing seems to be amiss."
    a "No tumors, no present autoimmune diseases, allergies, or even blunt force trauma of some sort. None whatsoever."

    scene dr_21
    with dissolve

    a "Eventually, some staff started referring to you here as {i}the{/i} \"Sleeping Beauty\" and that true love's kiss might wake you up."
    a "({i}That girl actually believed those rumors and attempted to do it on you.{/i})"
    mx "What?"

    scene dr_20
    with dissolve

    a "N-Nothing!" with vpunch
    "(\"Sleeping Beauty\" huh? I recall that a special something with that \"loveable\" nickname started this all.)"
    mx "Then... did you found out anything afterwards?"

    scene dr_17
    with dissolve

    a "We were extremely clueless. That week after your admittance, we were scrambling to find out the cause..."
    a "We even speculated that it might be from the VR Headgear you used but found it quite challenging to determine how, by that point, the VR Headgear caused—"

    scene dr_15
    with dissolve

    mx "\"By that point\"?"
    a "You catched that?"
    a "Another hospital reported an incident of a man that died while strapped to his VR Headgear {i}except{/i} it wasn't the commercial ones currently being sold but a prototype..."

    scene dr_12
    with dissolve

    a "Turns out, the man in question was the \"{color=#00fff6}Reign Corporation's{/color}\" late Chief Engineer, he was testing the new model that was meant to ship out next year."
    "(So, what the news showed earlier... its really true, huh? I'm actually dead, well, the fat me.)"
    mx "How exactly did he die if he was just testing? Did he get a heart attack or stroke?"

    scene dr_20
    with dissolve

    a "No! But it kinda gets... very morbid."
    mx "I can handle morbid, Doc. Heck, maybe I'll forget it later?"

    scene dr_21
    with dissolve

    a "Very funny."
    mx "I try to be."
    a "Well..."

    scene dr_19
    with dissolve

    a "The autopsy report showed that the engineer's brain \"{color=#00fff6}melted{/color}\", so to speak. They also found out that the inner components were also fried... from an \"{color=#00fff6}overdrive{/color}\"."

    scene dr_15
    with dissolve

    a "Finally, they discovered that a lightning struck his unit's building and the surge of voltage found its way to the electrical grid and eventually, his headgear."
    mx "T-that's...scary."
    "(My brain... \"melted\"?)"
    "(Then that \"glitch\" that happened.. the \"ripping of the soul\". That was actually the moment my brain started melting from the injector arrays going overdrive.)"

    scene dr_11
    with dissolve

    a "The detectives discussed that if he didn't just played that game that day he could still be alive."
    a "It also didn't help that lots of safety protocols were neglected. For the cables, the prototype, even the electrical outlet was rigged to bypass the building's breaker."

    scene dr_17
    with dissolve

    a "I mean, if you play stupid games, you win stupid prizes. Ah.. that was disrespectful of me to the deceased."
    "(Nah, I understand. The early parts of the prototype needed quite the power, well, Quanto needed it for processing and it often tripped the breaker there so I had to bypass it somehow.)"

    scene dr_20
    with dissolve

    a "As one of the detectives puts it, the headgear's engine went into overdrive so powerful that it can \"{color=#00fff6}transform an apple into juice{/color}\" within seconds."
    mx "...juice indeed."

    scene dr_14
    with dissolve

    "(The thunderstorm that day... if I just charged the stupid thing the day before...)"
    "(But a mystery still remains...)"
    "(It's one thing for a brain to be melted but to transfer one's consciousness to another human being...)"
    "(There's more to this. I need to find out what happened during that time and what exactly occured.)"

    scene dr_21
    with dissolve

    mx "But Doc, how is it related to my comatose?"
    a "We're not really sure on this but it still remains the plausible theory on your circumstance..."

    scene dr_15
    with dissolve

    a "Similar to the engineer, it seems that a power fluctuation occured, possibly by lightning too, and forced a similar event on your headgear to go to overdrive."
    a "The surge might've traveled to your VR Headgear too but because there's a fail-safe on the commercial models, it might've been just a short burst."
    a "It was probably enough to shock your brain into a coma."
    a "Well, the strange thing with that though was that other people were also plugged into the grid but you were the only one to be affected."

    scene dr_19
    with dissolve

    a "To be honest, I don't even know the exact science on those things are. I'm a doctor not an engineer. As it still remains a theory, we can't do anything to sue the \"{color=#00fff6}Reign Corporation{/color}\"."
    mx "So, that's the gist of it. I kinda get it now, Doc."
    "(But another mystery rises... why this kid in particular? Why did I \"reincarnate\" on his body?)"
    jy "Miss! Please don't run in the hallway!" with vpunch

    scene dr_22
    with dissolve

    a "What's going on outside?"
    jy "Careful!" with vpunch

    scene dr_25
    with dissolve

    "{color=#fff}{i}...I don't care! I need to see him first!...{/i}{/color}" with vpunch
    "{color=#fff}{i}...I hope he's okay...{/i}{/color}" with vpunch

    scene dr_19
    with dissolve

    a "It seems you have guests, [mc]."

    stop music fadeout 3.0

    scene pris_1
    with dissolve

    mx "Guest? Who?"
    sm "Oh hey! What's up Pri—!"

    scene pris_2

    "{size=+25}{color=#A9A9A9}Bang!{/color}{/size}" with vpunch

    mx "What the...!?"

    scene pris_3

    p "[mc]!" with vpunch
    p "Y-Y-You actually woke up!"

    scene pris_4

    p "[mc]!!!" with vpunch
    a "Priscilla? Wait! Don't—"
    p "Yah!"

    scene black

    mx "OOOOOPPHHH!" with vpunch

    "(Paaaaaiiinnn!!)"
    "(My legs...)"

    scene pris_5
    with slowfade

    play music "music/Promises to Keep.mp3"

    if notification_songs == True:
        $ renpy.notify("Kevin MacLeod - Promises to Keep")

    p "{i}*sniffle*{/i}"

    scene pris_6
    with dissolve

    "(Wait... Is she..? Is she crying?)"
    p "{i}*sniffle*{/i} {i}*sniffle*{/i}"

    scene pris_10
    with dissolve

    p "I-I-I thought you would never wake up ever again..."

    scene pris_11
    with dissolve

    p "I waited for a day... {w} then a week... {w} even after a month you still w-wouldn't open your eyes..."

    scene pris_10
    with dissolve

    p "A-And when Miss Aanya told me that you probably w-w-wouldn't wake up for years..."

    scene pris_11
    with dissolve

    p "I-I-I..."

    scene pris_8

    p "Uwwaaaaaaaahh!!" with vpunch

    scene pris_6
    with dissolve

    "(Woah, easy there! {p} My muscles are still weak, y'know?)"
    "(Who... exactly is this girl?)"

    scene pris_7
    with dissolve

    p "I'm just glad... {w} that you're awake now."
    a "Priscilla, [mc]'s fine now, dear. No need to worry."

    scene pris_12
    with dissolve

    p "B-But what if he sleeps again Ms. Aanya and-and-and never w-wakes up?"
    a "That's... {w} Well, that's understandable dear but [mx]'s already awake which means he's better now."

    a "Besides, he still needs to observed for quite some time here, okay?"

    scene pris_9
    with dissolve

    p "You heard that, [mx]? Don't leave the hospital till your better, okay?"
    mx "Uhhhhh.... {w} okay?"
    "(Too close! What's with this girl being this unbearably cute.)"
    "(Shit! My heart's beating too much!)"

    scene pris_13
    with dissolve

    p "I-I know that you said that you don't want help from us ever again b-but..."

    scene pris_14
    with dissolve

    p "T-This is an exception alright!"
    p "So... you don't owe us anything, okay?"

    scene pris_13
    with dissolve

    p "And you're weak, a-and you just got evicted, and... and..."
    p "...you need a place to stay."
    p "So, just for a while you can stay with us."

    mx "That's—"

    scene pris_14
    with dissolve

    p "Just temporarily! {p} It's not, like, helping you or anything like that..." with vpunch

    scene pris_13
    with dissolve

    p "So... {w} please don't hate me."
    "(I don't know what the hell's going on!)"
    "(Why does she seem convinced that I would be rejecting her already?)"

    scene pris_16
    with dissolve

    a "Priscilla, dear. I'm sorry to interrupt but you need to know that..."
    a "[mx] doesn't remember you."
    p "What do you mean by that Miss Aanya?"
    a "Ah.. That's.. Ummmmm... {w} He has amnesia, dear. {p} It seems he has forgotten a few things from his past, and sadly, including you."

    scene pris_14
    with dissolve

    p "S-She's kidding right, [mx]?"
    p "You still remember me right? It's me, Prii?"
    mx "I'm... {w} I'm sorry, I don't."

    scene pris_8 with vpunch
    with dissolve

    p "Noooooo!"
    "(Urgghh... pain's back in my back.)"

    scene pris_10
    with dissolve

    p "It's me, Priscilla! R-Remember when we went to that old pond near your house and-and that we..."
    p "Or that time that we—"
    mx "Miss Priscilla, I'm {i}really{/i} sorry I..."

    scene pris_11

    p "\"Miss Priscilla\"? You..."
    p "Then your promise, did you even forget that too..."

    scene pris_13
    with dissolve

    mx "..."
    "(Even if I try, I won't remember anything 'cause... {w} I'm not the guy who you think I am)"

    play music "music/Rainbows.mp3" fadein 4.0

    if notification_songs == True:
        $ renpy.notify("Kevin MacLeod - Rainbows")

    p "{size=-5}...Uh..Umm... Maybe if I clobber you like in the movies...{/size}"
    mx "Excuse me?"

    scene pris_15

    p "[mx], stay still! Maybe if I bash you in the head a couple of times your memory would return and you'll remember!" with vpunch
    mx "What!? No, no, no!"
    mx "That's not how it works!"
    "(That wouldn't even work to begin with!)"
    p "Just stay still! I've practiced Karate in school!"
    a "Priscilla, no—"

    stop music fadeout 3.0

    scene fp_1

    f "{size=+28}Priscilla! Enough!{/size}" with vpunch
    p "M-Mama?"
    f "Get down here this instant, young lady!" with vpunch
    p "B-But [mx] is.."
    f "Now."

    play music "music/Easy Lemon.mp3" fadein 6.0

    if notification_songs == True:
        $ renpy.notify("Kevin MacLeod - Easy Lemon")

    scene fp_2
    with slowfade

    f "Running in the hospital hallway!?" with vpunch
    f "What if you injured one of the patients with that recklessness of yours? Hm?"

    scene fp_3
    with dissolve

    p "That's... I-I'm sorry. Its because [mx] is..."

    scene fp_4
    with dissolve

    f "Speaking of [mx], sitting on him like that when he just woke up! Do you want to put him to sleep again!?" with vpunch

    scene fp_3
    with dissolve

    p "No..."

    scene fp_4
    with dissolve

    f "And with such an unladylike position!" with vpunch
    f "My God, Priscilla! Where did you learn that?" with vpunch

    scene fp_3
    with dissolve

    p "N-No! [mx]'s not like the other boys he's—"

    scene fp_4
    with dissolve

    f "He's still a man, Priscilla! {p} And men don't like {i}those{/i} kinds of woman." with vpunch
    f "And when they don't like them, they leave just like your..."

    scene fp_2
    with dissolve

    p "B-But... {i}*sniffle*{/i} {p} Y-Yes, Mama. I understand."
    f "{i}*sigh*{/i}"
    f "I'm sorry... I was just worried, okay?"

    scene fp_11
    with dissolve

    stop music fadeout 6.0

    a "Well, that was quite the entrance."
    f "I'm sorry about this, Aanya."
    a "It's fine and don't be harsh with Priscilla like that. The girl has a heart of gold but more importantly..."

    scene fp_10
    with dissolve

    play music "music/Rainbows.mp3" fadein 2.0

    if notification_songs == True:
        $ renpy.notify("Kevin MacLeod - Rainbows")

    a "[mx]."
    a "I'd like you to meet the Fitzgeralds. {p} The ones you would be staying with for awhile."
    f "So, it's really true. He really doesn't remember us."
    p "[mx]..."

    scene fp_12
    with dissolve

    a "He remembers {i}most{/i} everyday things except persons involved in his life..."
    f "..."
    a "Well, reintroduction's in order..."

    scene fp_11
    with dissolve

    a "The fiery, short-tempered one like her hair is Fiona."
    f "Aanya!" with vpunch
    a "And as you have seen and heard, the mother of this little lady here..."
    a "Your girlfriend."

    scene fp_13
    p "Wha-wha-what!? N-No! {p} Miss Aanya! [mx], I'm not—" with vpunch

    scene fp_14
    with dissolve

    a "Jumping to your lap, hugging you. Quite daring, isn't she?"
    p "Thats-Thats! [mx]! I-I just—" with vpunch
    f "Aanya, stop teasing the kids."

    scene fp_11
    with dissolve

    p "{i}*sniffle*{/i} {w} {i}*sniffle*{/i}"
    a "I'm sorry, Prii. You're just too cute to not tease."

    scene fp_10
    with dissolve

    stop music fadeout 4.0

    a "This delicate tangerine flower is Priscilla."
    a "You could say she's like a little sister of yours."
    "(Little sister, huh?)"

    scene fp_11
    with dissolve

    play music "music/Windswept.mp3" fadein 2.0

    if notification_songs == True:
        $ renpy.notify("Kevin MacLeod - Windswept")

    a "Fiona? Priscilla? What're you waiting for? I'm not gonna talk all day for the both of you."
    f "No, its just... {w} strange."
    f "I've never seen him this... \"tame\" before."
    a "I know what you mean, it was shocking at first but he's actually nice."

    scene fp_5
    with dissolve

    f "[mx], do you remember me? Even a bit?"
    mx "I'm sorry ma'am, I don't."
    f "{i}*giggle*{/i}" with vpunch
    mx "...?"

    scene fp_9
    with dissolve

    p "Mama! This is serious!" with vpunch
    f "I'm sorry, dear. I've never ever heard him call me \"Ma'am\" before."
    f "It was Fiona {i}this{/i} and {i}that{/i}."

    menu:
        "Excuse me...":
            scene fp_8 with dissolve
            mx "I'm sorry to interrupt but... are you my family?"
            "(I need to gather a basic history on this guy.)"

    f "That is... {w} No dear. {p} Your parent's they're.."
    scene fp_7
    with dissolve
    p "Mama... is it okay to tell him?"

    menu:
        "It's okay.":

            scene fp_8 with dissolve
            mx "It's okay. It might possibly bring something back to me."
            f "Is that so?"
            f "Well, they're... {w} they're both dead, dear."
            mx "Both of them?"
            f "Your mother, Esther, died about 5 years ago and as for your father, he died just over a year ago."
            mx "Oh... that's quite tragic."
            p "Are you okay, [mx]?"
            p "I'm sorry that—"
            mx "No, its okay."
            mx "The thing is that I can't even recall them. They feel foreign to me..."
            f "It's okay. Let's take a few steps at a time, hm?"

            jump fiona_pri1
        "Actually, nevermind.":


            scene fp_8 with dissolve
            mx "Actually, nevermind. I'd like to take these things slowly."
            mx "I'm not in a rush to remember {i}strong emotions{/i{}} at this point. {p} I'm just taking a few steps at a time to recover my memories."
            f "Okay. But if you want to, I'm here."

            jump fiona_pri1

    label fiona_pri1:

    scene fp_6
    with dissolve

    p "Then do you remember anything about us at all?"
    mx "I... {w} don't. {p} I don't know who I am, who my friends are, and even any family."

    scene fp_12
    with dissolve

    a "This is quite the case of Retrograde amnesia."
    a "To not remember anything about one's entire existence."

    scene fp_11
    with dissolve

    a "Well, you two got a herculean task ahead of you to help him recover his memories."
    f "To be honest, I rather prefer him like this—"

    scene fp_9

    p "Mama!" with vpunch
    f "I'm kidding, Prii!"
    "(So I'll be living with these two beautiful women from now on? What a turn of events this is!)"
    "(Wait! This means \"those\" kinds of encounter could happen too? Like \"accidentally\" seeing them naked!?)" with vpunch
    "(Shit! Just the thought is already giving me a boner—)"

    stop music

    window hide

    scene brain_shock with vpunch

    play sound "soundfx/glitch.ogg" loop

    mx "AAAAAAAAARRRRGGHHHHH!" with vpunch
    "(What's happening!?)"
    "(This feeling is...)"

    scene fp_16
    with dissolve

    p "[mx]!!"
    p "Miss Aanya! What's happening?"

    scene fp_15
    with dissolve

    a "I'm not sure myself."
    f "[mx], are you alright?"

    scene brain_shock with vpunch

    "(This is the same feeling that happened during the game!)"
    "(What's going on!?)"
    "(My consciousness is...)"

    stop sound fadeout 2.0

    play music "music/Dreamy Flashback.mp3" fadein 3.0

    if notification_songs == True:
        $ renpy.notify("Kevin MacLeod - Dreamy Flashback")

    scene black
    with dissolve

    pause

    scene orb_bg
    with slowfade

    "(Where...{w}Where am I?)"
    "(Is this a dream but I was just talking to...)"
    "{size=-10}{color=#fff}{i}...hey...{/i}{/color}{/size}"
    "(Did I die or something? I was just about to have the greatest lif—)"
    "{color=#fff}{i}...Hey! You!...{/i}{/color}" with vpunch
    "(What the..?)"

    show hero1 with vpunch

    window hide

    pause

    "(Chosen one? Who... me?)"
    "(That can't be right...)"
    "(Who's this old man?)"

    hide hero1

    show hero2

    window hide

    pause

    "(What lady are you talking about and where is this place?)"
    "(How can I get out!?)" with vpunch
    "(Someone's waiting for me!)"

    hide hero2

    show hero3

    window hide

    pause

    show fiona_door with dissolve

    show priscilla_door with dissolve

    if aanya_panties == True:
        show aanya_door with dissolve

    "(HEY! ANSWER MY DAMN QUESTION!)" with vpunch
    "{color=#fff}...{/color}"
    "(For fuck's sake... I'm getting nowhere with this guy.)"
    "(Might as well choose a door here.)"

    menu:
        "Check the {color=#6bfffc}Turquoise{/color} Door [gr]\[PriDream\]":
            hide hero3
            hide fiona_door
            hide priscilla_door
            hide aanya_door

            show turqouise_door with dissolve

            "The {color=#6bfffc}Turquoise{/color} door it is."
            "I wonder what's behind this?"
            "And what did that old man mean by \"A lady needing help\"?"

            scene black
            with slowfade

            jump pri_dream
        "Check the {color=#ff3030}Scarlet{/color} Door [gr]\[FionaDream\]":

            hide hero3
            hide fiona_door
            hide priscilla_door
            hide aanya_door

            show scarlet_door with dissolve

            "The {color=#ff3030}Scarlet{/color} Door it is,"
            "I wonder what's behind this?"
            "And what did that old man mean by \"A lady needing help\"?"

            scene black
            with slowfade

            jump fiona_dream

        "Check the {color=#b868ff}Lilac{/color} Door [gr]\[AanyaDream\]" if aanya_panties == True:

            hide hero3
            hide fiona_door
            hide priscilla_door
            hide aanya_door

            show lilac_door with dissolve

            "The {color=#b868ff}Lilac{/color} Door it is."
            "I wonder what's behind this?"
            "And what did that old man mean by \"A lady needing help\"?"

            scene black
            with slowfade

            jump aanya_dream


    label pri_dream:

    hide all

    scene pri_dream1
    with fade

    p_m "[mx]?"
    p_m "You shouldn't enter a lady's room, you know?"
    p_m "That's very naughty of you..."
    p_m "Ehehe.."
    "(Wait! I-Isn't this {i}that{/i} Priscilla chick!?)" with vpunch
    "(Wh-Why is she nude!?)" with vpunch
    p_m "Your staring a bit too much, [mx]. Its making me blush..."
    p_m "Do you...{w} Do you want to see more?"

    scene pri_dream2
    with dissolve

    "({i}*gulp*{/i})" with vpunch
    p_m "It's not ugly, is it?"
    p_m "Mama said I shouldn't show my body to any boy till I get married..."
    p_m "But...{w} You're different from the others, [mx]."
    p_m "Do you still remember that time we went to your house?"

    scene pri_dream3
    with dissolve

    p_m "{i}*giggles*{/i}" with vpunch
    "(I'm not exactly sure what's going on here but...)"
    "(I ain't complaining, that's for sure.)"
    p_m "Every time I think about that {i}thing{/i} we did..."
    p_m "It makes me \"tingly\" down here."
    p_m "I asked Maddy about it and she said that you'll feel more \"tingly\" down there if you do it with someone you like..."

    scene pri_dream4
    with dissolve

    p_m "Someone you like {i}like{/i}..."
    p_m "And... {w}And I want to feel more of it... {w}Feel it with you, [mx]..."
    p_m "Don't tell Mama about this or she'll be angry at the both of us..."
    p_m "So, let's make that {i}kissy{/i} promise like last time..."
    p_m "You know, when Mr. Tongue and Mrs. Tongue \"kissed\" each other inside..."
    p_m "And Mrs. Tongue... {i}really{/i} wants...Mr. Tongue's kiss..."
    p_m "She really wants it... so bad. Don't make her sad, [mx]..."
    p_m "{i}*giggles*{/i}"
    p_m "Why don't you come a little closer..."

    menu:
        "Make \"Kissy\" Promise":

            play sound "soundfx/glitch.ogg" loop

            scene pri_glitch with vpunch
            "(W-What's happening!?)" with vpunch
            scene pri_glitch_anim animated:
                "pri_dream4" with hpunch
                pause 0.5
                "pri_glitch" with vpunch
                pause 0.5
                repeat

            p_m "C..Come...closer...[mx]...."
            p_m "I...want...you..."
            "(Dammit! Dammit! Dammit!)" with vpunch
            "(I don't want to make Mrs. Tongue sad!)" with vpunch

            $ dream_pri = True

    jump dream_end


    label fiona_dream:

    hide all

    scene fiona_dream1
    with fade

    f_m "Oh?"
    f_m "Are you lost, little boy?"
    f_m "You can't just enter a woman's room, you know?"
    "(T-That's M-Miss Fitzgerald!?)" with vpunch
    "(W-Why is she naked?)" with vpunch

    scene fiona_dream2
    with dissolve

    f_m "Where's your mommy?"
    "(W-What mommy?)"
    f_m "Awww... you lost her?"
    f_m "That's really sad."
    f_m "Its alright, I can be your new mommy for today..."

    scene fiona_dream3
    with dissolve

    f_m "Dear, you're staring too hard..."
    f_m "Do you like your new mommy's breasts?"
    "({i}*gulp*{/i})" with vpunch
    f_m "You do, don't you? Hehe..."
    f_m "Do you still remember that time I visited your house, dear?"
    f_m "You know, the one where you sneaked a peek on me while I was taking a bath..."

    scene fiona_dream4
    with dissolve

    f_m "Those walls were quite thin, you know? {p} And I can still remember hearing... {w}the slow moans... {w}the heavy breathing..."
    f_m "I can even hear your voice behind that peep hole you made..."
    f_m "And you know what? You made your mommy... {w}very {i}very{/i} wet down here that day..."
    f_m "There's no wall separating me and you now..."
    f_m "Do you want to touch mommy, dear?"

    menu:
        "Touch Mommy":

            play sound "soundfx/glitch.ogg" loop

            scene fiona_glitch with vpunch
            "(W-What the hell!?)" with vpunch
            scene pri_glitch_anim animated:
                "fiona_dream4" with hpunch
                pause 0.5
                "fiona_glitch" with vpunch
                pause 0.5
                repeat

            f_m "..[mx]..M...Mommy..wants..you..."
            f_m "..I..Inside...of..her.."
            "(No! No! No!)" with vpunch
            "(I want my Mommy!)" with vpunch

            $ dream_fio = True

    jump dream_end


    label aanya_dream:

    hide all

    scene aanya_dream1
    with fade

    a_m "Hm?"
    a_m "Entering a married woman's room while her husband's out?"
    a_m "You're quite a daring young man..."
    "(D-Doc Aanya!?)" with vpunch
    "(W-Why is she naked?)" with vpunch

    scene aanya_dream2
    with dissolve

    a_m "You didn't barge in here having indecent thoughts, did you?"
    "(F-Fuck...W-What is this place?)"
    a_m "Perverted ideas like pinning me down and thrusting me with that hard, young, and heavy looking..."
    a_m "No!" with vpunch
    a_m "I'm a married woman and I'm only loyal to my husband! {p} The idea of cheating behind your husband's back and getting fucked on all fours like a dirty, cock-hungry slut is insulting!" with vpunch

    scene aanya_dream3
    with dissolve

    "({i}*gulp*{/i})" with vpunch
    "(W-What is she implying?)"
    a_m "What would the neighbor's say if they see you here!?" with vpunch
    a_m "Maybe they'll think I love having that young cock down my throat, feeling every corner of it while cum drips inside my esophagus..."
    a_m "Or maybe they'll think I'm some kind of whore that likes it up my tight ass or I like my pussy overflowing with thick, hot, fertile semen..."
    a_m "No, we can't have any of that rumors going on here, young man!" with vpunch

    scene aanya_dream4
    with dissolve

    a_m "It's taboo... {w}its immoral... {w}and its very {i}very{/i} wrong to do..."
    a_m "But you don't have any of those indecent thoughts, do you?"
    a_m "You're just here to {i}help{/i} a housewife with here \"plumbing problems\" while her husband's busy at work, aren't you?"
    a_m "And you certainly brought a very big \"tool\" to fix that..."
    a_m "Come inside... {p} I want to show you the \"dripping problem\" I'm—I mean, we're having upstairs..."

    menu:
        "\"Fix\" her \"Plumbing Problems\"":

            play sound "soundfx/glitch.ogg" loop

            scene aanya_glitch with vpunch
            "(W-What the hell!?)" with vpunch
            scene aanya_glitch_anim animated:
                "aanya_dream4" with hpunch
                pause 0.5
                "aanya_glitch" with vpunch
                pause 0.5
                repeat

            a_m "..I..want..to...inspect..more..of...that..\"tool\"..of...yours..upclose.."
            a_m "..And..maybe..."
            "(Stop! Stop! Stop!)" with vpunch
            "(I still want to \"fix\" those \"plumbing problems\"!)" with vpunch

            $ dream_aya = True
    jump dream_end



    label dream_end:
        $ renpy.end_replay()
    scene black_orb animated:
        "glitch_1_bg"
        pause 0.5
        "orb_bg"
        pause 0.5
        "glitch_2_bg"
        pause 0.5
        "orb_bg"
        pause 0.5
        repeat

    show dream_warn1
    with dissolve

    window hide

    pause

    "(What the hell is a \"Time's Up\"!?)"
    "(I want to see more of it dammit!)"

    hide dream_warn1

    show dream_warn2
    with dissolve

    window hide

    pause

    "(Game Over?)"
    "(This isn't a... {w}game?)" with vpunch
    "(Is it?)"
    pause
    "(Shit! I forgot!)" with vpunch
    "(Just 'cause I saw a naked body, I completely forgot how I came to be here in the first place!)" with vpunch
    "(Is this \"world\", a game?)"

    hide dream_warn2

    show dream_warn3
    with dissolve

    window hide

    pause

    "(Now \"Tokens\"?)"
    "(What's going on here!?)" with vpunch
    "(What's with the video game references?)"
    "(HEY OLD MAN!)" with vpunch
    "(WHERE AM I!?)" with vpunch
    "(WHERE... {w} ARRree.... {w}yoouu.....)"
    "(...)"

    hide dream_warn3

    scene black
    with fade

    show goodbye_chosen1
    with dissolve

    pause

    "(...weak..?)"

    hide goodbye_chosen1

    show goodbye_chosen2
    with dissolve

    pause

    "(...can I...return...?)"

    hide goodbye_chosen2

    stop sound fadeout 2.0

    stop music fadeout 3.0

    scene black
    with slowfade

    pause

    scene brain_after
    with slowfade

    play music "music/Easy Lemon.mp3" fadein 2.0

    if notification_songs == True:
        $ renpy.notify("Kevin MacLeod - Easy Lemon")

    "(I'm...{w} I'm back?)"
    "(That means... all of those things I saw was inside my head!?)" with vpunch
    "(What is going on with me?)"

    label after_dream:

    scene fp_17
    with dissolve

    f "Aanya! What's happening to him!?" with vpunch
    f "I thought...{w} I thought he was okay already!?" with vpunch
    a "I don't know Fiona! I thought so too!" with vpunch
    a "With the way he was awhile ago, I thought he was fine. I don't know what's happening to him right now."
    a "I'm gonna call another—"

    scene fp_18
    with dissolve

    mx "I'm alright! I'm alright! {p} It was just a... minor headache." with vpunch
    p "[mx], really? Do you want some water? Anything?"

    scene fp_19
    with dissolve

    mx "I'm fine, really."
    mx "Uhm... How long was I out?"
    a "How long were you out? {p} A minute hasn't even passed since you screamed all of a sudden."
    a "Are you sure you're okay?"
    "(A minute hasn't even passed!?)" with vpunch
    mx "No, no! I mean, I guess I'm just tired 'cause of being active after waking up from a long sleep."
    mx "It's nothing to worry about, to be honest."
    a "I think we have overstayed ourselves a bit here."
    a "It's better to leave him for now and let him rest for awhile."

    scene fp_20
    with dissolve

    a "In the meantime, I'll schedule an appointment at the MRI to see if that headache wasn't something dangerous."
    f "Let's go, Priscilla."
    p "Mama, I can stay! There's nothing important going on at school so I can skip—"
    f "Oh no you aren't young lady!" with vpunch
    f "You're already late! I'll talk to Ms. Hawkins about this."
    p "But!" with vpunch
    f "No buts!"
    p "[mx]. I'll be back later! Okay?"
    a "Rest well, [mx]."

    scene pris_1
    with dissolve

    window hide

    pause

    scene hs_16
    with dissolve

    "(What just happened to me a while ago.)"
    "(What were those visions? What's going on with this body!?)"
    "(What were the doors for? Where did they come from? The old man? The tokens!?)" with vpunch
    "(Were those my thoughts even!? She seemed {i}too{/i} real! Like, she's...)" with vpunch

    scene hs_15
    with dissolve

    mx "{i}*sigh*{/i}"
    mx "Shit."
    mx "I give up! I don't know what's going on anymore! But atleast, there's something great to look forward too."
    mx "I just... {w}I need to lie down."

    menu:
        "Rest":
            scene black with slowfade

    stop music fadeout 3.0

    show text "{size=56}A few days later...{/size}" with fade

    pause

    scene hospital_morning
    with slowfade

    play music "music/Somewhere Sunny (Ver 2).mp3" fadein 3.0

    if notification_songs == True:
        $ renpy.notify("Kevin MacLeod - Somewhere Sunny (Ver 2)")

    p "Mama! [mx]'s gonna be discharge today, right?"
    f "Yes, dear. So, have you cleaned up his room?"
    p "Of course!" with vpunch

    scene priscilla_down
    with dissolve

    f "Then can you get him upstairs? I still need to talk with Aanya regarding his discharge papers..."
    p "Yeah! No problem!"
    f "And no running in the hallways, Prii!"
    p "I know that already, Mama!"
    f "I'm just saying."
    p "Gotta go!"

    scene go_home1
    with slowfade

    mx "It's been a hell of a week being cooped up in here..."
    mx "Tests after tests, then exams after exams. Can't a guy take a break? Sheesh."
    mx "Well, atleast this body— I mean, my body's healthy!" with vpunch
    "(Man, I need to start accepting that this is me now.)"
    "(Its been a week already! Well, it doesn't help that I get nightmares of waking up to that old obese body.)"
    "(And speaking of dreams...)"

    if dream_pri:

        scene pri_dream4 with fade

        mx "What was that about? Why did entering that door gave me those images of Priscilla nude inside my head? Strange."
        mx "Priscilla, huh? I'll be living with her from now on..."
        mx "It's quite exciting..."

        scene go_home1 with fade

        "(That old man and those doors on the otherhand, they never once appeared after that even if I force myself.)"
        "(The \"tokens\" it mentioned, what was that about?)"

    elif dream_fio:

        scene fiona_dream4 with fade

        mx "What was that about? Why did entering that door gave me those images of Mrs. Fitzgerald nude inside my head? Strange."
        mx "Oh wait, she'll be angry if I called her that. Just Fiona she says and I'll be living with her from now on..."
        mx "It's quite exciting..."

        scene go_home1 with fade

        "(That old man and those doors on the otherhand, they never once appeared after that even if I force myself.)"
        "(The \"tokens\" it mentioned, what was that about?)"

    elif dream_aya:
        scene aanya_dream4 with fade

        mx "What was that about? Why did entering that door gave me those images of Dr. Aanya nude inside my head? Strange."
        mx "That was honestly hot. I wonder if I can see more of her again in the future?"
        mx "It's quite exciting..."

        scene go_home1 with fade

        "(That old man and those doors on the otherhand, they never once appeared after that even if I force myself.)"
        "(The \"tokens\" it mentioned, what was that about?)"

    "(Shit! What time is it? I better get going...)" with vpunch

    menu:
        "Grab the bag":
            scene go_home2
            with dissolve

    "(I need to wait for them at the lobby.)"
    "(And speaking of the devil...)"

    scene go_home3
    with dissolve

    "(After shaving and trimming, this guy is actually {i}much{/i} younger than I initially thought.)"
    "(Nice jawline, nice eyes. Much better looking than any guy I've seen...)"
    pause
    "(Fuck! That sounded gay.)" with vpunch
    "(But there's also another thing I wanted to try...)"
    mx "Hey! Who's that handsome guy?!" with vpunch
    mx "Hello 911! There's a handsome guy in my room..."
    mx "Oh wait... cancel that!" with vpunch
    mx "It's only me."
    "(God, I sound like a douchebag saying that...)"

    p "{size=-5}...Aha..ha..ha{/size}"
    mx "...?"

    scene ghp_1
    with dissolve

    p "Ahahahaha!" with vpunch
    mx "P-P-Priscilla!? H-How long have you been there!?!"
    p "..Ahaha.... Just before... haha... you started saying that..."
    p "I wanted to enter quietly 'cause you might've been still sleeping but.."
    p "Buhahaha!" with vpunch
    mx "Alright! Alright! Forget that ever happened!"

    scene ghp_2
    with dissolve

    p "Awwwww... that was kinda cute."
    mx "There wasn't anything remotely \"cute\" with any of that at all."
    p "Ehehehe... well, you certainly do look handsome though."
    mx "Wha? I mean... {w} shit."
    "(Fuck! I'm blushing like an idiot!)" with vpunch
    mx "O-Oh yeah? Where's Miss Fiona?"
    p "Mama's downstairs."

    scene ghp_3
    with dissolve

    p "Anyways, let's go already!"
    "(Woah my hand! She might look like a frail little girl but her strength is no joke!)" with vpunch
    mx "Okay, okay!" with vpunch

    window hide

    pause

    scene a7
    with fade

    mx "So, Priscilla..."

    scene a4
    with dissolve

    p "Hey! I told you to call me Prii!" with vpunch
    mx "Well, Prii.."

    scene b5
    with dissolve

    p "Ehehe... That's nice."
    mx "I've never managed to ask Dr. Aanya about this but..."
    mx "How old am I exactly?"

    scene b1
    with dissolve

    p "Well..."
    p "I don't know your exact age but..."

    scene c6
    with dissolve

    p "You're 4 years older than I am so, 22 or probably 23, I think?"

    scene c7
    with dissolve

    mx "Oh, I see... {w} Wait!"
    mx "That means..."
    mx "You're 18 already!? Really?" with vpunch

    scene a4
    with dissolve

    p "Hey!" with vpunch
    p "What do you mean by that!? Of course I'm 18!" with vpunch
    p "I'm a fine young lady now!" with vpunch
    mx "No, its just that..."
    p "Just what?"
    "(To be honest, you just act too young for your age, I guess?)"
    "(If she said she's even a few years younger, I wouldn't doubt it but I'll just keep these to myself.)"
    mx "Just... {w} too pretty for your age."

    scene b5
    with dissolve

    p "Really!?!" with vpunch
    mx "Yes. Really."

    scene b1
    with dissolve

    p "Thank you~"
    p "Ehehe... Your really nice."
    p "{size=-6}...I can see why Mama said she doesn't want you to regain your memories...{/size}"
    mx "Is that so?"

    scene c3
    with dissolve

    p "N-N-No! Th-That's.... {w} I-I'm sorry—"
    mx "Oh no! It's okay! It's nothing for you to worry about." with vpunch
    mx "To be honest, I don't really know much about {i}me{/i} to even care."
    mx "Just one question though and I want you to answer me honestly on this, okay?"

    scene a2
    with dissolve

    p "{i}*nods*{/i}"
    mx "Before any of {i}this{/i} happened to me, what was I like?"

    scene a3
    with dissolve

    p "Umm... that is.."
    mx "Please?"

    scene b1
    with dissolve

    p "Well, you were really difficult to talk to."
    p "Mama said that you were a \"{i}fiercely independent{/i}\" person or something like that."
    p "When Mama and the others would offer help, you..."
    mx "Yeah?"

    scene c3
    with dissolve

    p "You'd get really angry at them. You said that you don't want to be pitied and that... owing favors are for losers."
    mx "So, I was an asshole, huh?"

    scene c4
    with dissolve

    p "What? No!" with vpunch
    p "That's what the others see but..."

    scene a3
    with dissolve

    p "You were always nice to me, you'd help me no matter my problems are."

    scene a5
    with dissolve

    p "Since we were little, you've always been there for me. That's why no matter what others say that you're bad... I know your a good person."

    scene b7
    with dissolve

    "(This girl...)"
    mx "You're really a kid, you know that?"

    scene b4
    with dissolve

    p "Hey!" with vpunch
    p "I take that back! You're not nice!"
    mx "Ahahaha! I'm just joking."

    scene c6
    with dissolve

    mx "But... thank you for answering that."
    p "Ehehehe..."
    p "No problem~"

    scene c7
    with dissolve

    mx "Well then, Prii..."
    mx "Would you help me recover my memories?"

    scene ghp_end
    with dissolve

    p "Of course!" with vpunch
    p "Even if it takes me years!" with vpunch
    mx "Then, first things first, do you know what my favorite food is?"
    p "That's a tough question..."
    p "Let's see... I know that you don't like..."

    stop music fadeout 2.0

    "(I don't honestly know where my life will be heading after I walk outside that door.)"
    "(Questions are accumulating with no answers in sight.)"
    "(How did I \"reincarnate\" on this guy's body? Who is he?)"
    "(What caused all of this?)"
    "(That dream and the old man inhabiting it? Why he called me \"Chosen One\")"
    "(My guild? Quanto and the VR Prototype?)"
    "(I don't have any answers to any of those...)"

    scene black
    with slowfade

    "(And I might possibly never know for sure but...)"
    "(Today will be my first step in finding it out and the adventures that will await me in the future.)"

    jump episode2_intro


return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
