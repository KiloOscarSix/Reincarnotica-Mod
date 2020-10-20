
label ep2_pquest_burgeradventure:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene priscilla_room_morning

    show 01_burgerburgeradventurestart_idle

    $ renpy.music.stop(channel='music3', fadeout=3)

    "(Maybe I can ask Prii if I can help her with something?)"
    "(Well, I have nothing better to do right now anyways.)"
    "(Oh? It looks like she's writing something.)"

    hide all

    scene 01_burgeradventurestart_01
    with fade

    if notification_songs == True:
        $ renpy.notify("outdoors - tired")

    $ renpy.music.play("music/outdoors_tired.mp3", channel='music2', fadein=2, loop=True)

    $ story_music_ongoing = True

    p "{i}...hmmmm...{/i}"
    p "{i}...ooh! I remember we did this here..."
    p "{i}...or—no! maybe this could...{/i}"

    mx "Hey Prii!"
    mx "What're you up to there?"

    p "Hm?"

    scene 01_burgeradventurestart_02
    with dissolve

    p "[mx]!"
    p "I didn't hear you come in!"
    p "W-Wait! \nLet me be proper first!"

    scene 01_burgeradventurestart_03
    with fade

    p "There!"
    p "Sooo~ {p} What brings you to my lovely room?"

    mx "Well, I got nothing to do really. {p} So, I was just wondering if I can help you with something?"
    mx "I'm still getting used to the new surroundings after all. {p} Sitting on my ass ain't gonna help me with that."

    p "Well then! {p} You're just in time!"

    mx "Just in time... for what?"

    scene 01_burgeradventurestart_04
    with dissolve

    p "Ta-dah!" with vpunch

    mx "A... {w}notebook?"

    p "Not just a notebook! {p} But a planner!"

    mx "A planner? {p} Okay? How can I exactly help you with that?"

    p "It's not about helping me! Nuh-uh ! {p} It's for you!"

    mx "For... {w}me? Huh? \nDo you need me to write you something?"

    p "Remember what Ms. Aanya said?"

    scene 02_burgerquest_recall
    with fade

    a "You could also explore around the neighborhood with Priscilla here."
    a "Locations that you have a strong emotional bond with, might trigger something inside of you."
    a "Memories can surface from unexpected places, you know?"

    scene 01_burgeradventurestart_05
    with fade

    p "{i}\"Memories can surface from unexpected places...\"{/i}"
    p "So, I wrote all the places we've been to. \nAt least the ones I remember being with you."
    p "I don't know anything much about amnesia but..."
    p "If it were me and I lost all my memories... \nI think it'll be very lonely."

    "({i}*sigh*)"
    "(How could I have the heart to tell her the truth with that.)"
    "(Heck, {i}even I{/i} don't know much about this and I've done extensive work on the brain.)"
    "(It could even be possible that this dude might regain his memories and I might just... {w} disappear.)"
    "({i}*sigh*)"
    "(Well, there's no point in thinking too much about this.) {p} (It's a wild ride to the unknown.)"
    "(I might even learn a thing or two of who exactly this guy was.)"

    mx "I see..."

    scene 01_burgeradventurestart_06
    with dissolve

    p "Which is where you come in! {p} We'll be doing an important mission!" with vpunch
    p "I call it the {i}\"Get [mx]'s Memory Back\"{/i} mission!"

    mx "{i}\"Get [mx]'s Memory Back\"{/i} mission, eh? "
    mx "It's great and all but... {p} How exactly are we gonna pull this off?"

    p "Great question! {p} We start going somewhere we went in the past!" with vpunch

    mx "Which is..?"

    p "Err..."

    scene 01_burgeradventurestart_05
    with dissolve

    p "{i}...hmmm...{/i}"
    p "{i}...the park, no, maybe the mountains could work...{/i}"

    play sfx1 'soundfx/stomach_growl.ogg'

    $ renpy.pause(1, hard = True)

    "{i}*stomach growl*{/i}" with hpunch

    $ renpy.pause(1, hard = True)

    mx "That was..."

    scene 01_burgeradventurestart_06

    p "N-N-Nothing! \nAbsolutely nothing! Aha..haha.." with hpunch
    p "N-Now that I think about it... {p} There's this d-diner we went a lot in the past!"
    p "Just around the block from here!"
    p "I-I remember we ummm... {i}uhh...{/i} {p} Had amazing memories there! The best ones!"

    mx "Really? Because I swear—"

    scene 01_burgeradventurestart_07
    with hpunch

    p "As I said, it was indubitably, without doubt, n-nothing!"
    p "And it wasn't my s-stomach growling that's for sure!"
    p "Ahaha..ha..ha.."

    mx "{i}\"Indubitably\"{/i} indeed."

    p "S-So! {p} We definitely need to eat—I mean, visit the that local diner!"
    p "Like, right now!"

    scene 01_burgeradventurestart_08
    with dissolve

    p "As the saying goes..."
    p "{i}\"The best way to a man's memories is through his stomach!\"{/i}"

    mx "I don't remember such a saying like that—"

    p "T-There definitely was!"
    p "S-See! \nYou're memories are getting fuzzy again!"
    p "Maybe their delicious, mouth-watering burgers would make you remember!"

    mx "Aren't you just hungry—"

    p "What? I can't hear you!" with vpunch
    p "Wait for me while I change, alright?"
    p "It'll be quick!"

    scene second_floor_hallway_morning
    with fade

    play sound "soundfx/door_locked.ogg"

    "{i}*door lock*"

    pause 0.3

    "(Well...) {p} (This will be a productive day for sure...)"
    "({i}\"Get [mx]'s Memory Back\"{/i}, hm? Interesting.)"
    "(Oh well, might as well sit down and wait for her to change.)"

    scene black
    with slowfade

    show text "{size=36}{color=#A9A9A9} ( After a while... ) {/color}{/size}" at truecenter with dissolve

    pause

    scene 01_burgeradventurestart_09
    with fade

    "({i}\"It'll be quick\" she says...)"
    "(It's almost 30 minutes and all I heard is rumbling noises from her room.)"
    "(We're not exactly going to a Gala—)"

    play sound "soundfx/door_open.ogg"

    "{i}*door open*"

    pause 0.4

    scene 01_burgeradventurestart_10 with fade:
        subpixel True
        yalign 1.0
        pause 1.0
        linear 5.0 yalign 0.0

    window hide

    $ renpy.pause(2, hard = True)

    p "Sorry for taking too long."
    p "Umm, well? {p} How do I look?"

    mx "Uh, y-you look..."
    mx "Amaz—tiful! I mean—" with hpunch
    mx "Amazingly beautiful!"
    "(Whew! It's supposed to be Amazing but I changed it to Beautiful midway.)"
    "(What's wrong with me?)"

    p "Pfft! Ahahaha!" with hpunch
    p "You don't have to be so nervous, [mx]."

    mx "Well, you did certainly took your time."

    p "Ehehe~ \nThere were just too many choices to choose..."
    p "So, I just settled for this one as its comfy."
    p "Well then, let's head out, shall we?"

    $ burgerjoint_unlock = True
    $ pquest_burgeradventure = False
    $ pquest_burgeradventure_burgerjoint_start = True
    $ story_ongoing_priscilla = True
    $ map_time_skip = False

    scene second_floor_hallway_morning
    with fade

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump second_floor_hallway

label ep2_pquest_burgeradventure_burgerjoint:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    $ pquest_burgeradventure_burgerjoint_start = False
    $ pquest_burgeradventure_burgerjoint_finish = True

    scene burgerjoint_morning
    with fade

    pause 0.3

    scene 02_burgerjoint_02
    with fade

    p "[mx]! \nLook! We're here!"
    p "This is the diner I'm talking about! The {i}Americana{/i}."

    mx "Quite a charming joint."

    scene 02_burgerjoint_01
    with dissolve

    p "It's been a while since I came back here."
    p "I wonder how's Miss Anna doing these days?"

    mx "Anna?"

    scene 02_burgerjoint_02
    with dissolve

    p "Miss Annamae! {p} She owns this diner!"
    p "Let's go meet her!"

    scene 02_burgerjoint_03
    with fade

    ana "{i}*sigh*{/i}"
    ana "Ugh! {p} If this place doesn't get any more walk-in customers I'll—"
    ana "Dangnabit! I'd buy those ol' mannequins on sale and have them spiffied up an' display em' here!"
    ana "It's getting gloomy with 'em empty seats this early in the mornin'."
    ana "Don't they want to experience an ol' American classic!?"
    ana "{i}*sigh*{/i}"

    $ renpy.music.stop(channel='music2', fadeout=2)

    play sound "soundfx/storebelljingle.ogg"

    "{i}*jingle*"

    $ renpy.pause(1, hard = True)

    ana "Hmm? {p} Walk-ins!?"

    scene 02_burgerjoint_04
    with dissolve

    if notification_songs == True:
        $ renpy.notify("domo - &nbsp;")

    $ renpy.music.play("music/domo_nbsp.mp3", channel='music2', fadein=1, loop=True)

    ana "H-Howdy folks! {p} Welcome to the—"
    ana "Well, well, well... {p} Look what the cat dragged in!"
    ana "If it ain't a pretty little peach fuzz!"

    scene 02_burgerjoint_05
    with dissolve

    ana "Lil' Miss Priscilla Fitzgerald!"

    p "Ms. Anna! {p} I missed you!"
    p "And I'm not a little peach fuzz, okay?"

    ana "Ahahaha! {p} I'm just glad to see a familiar face, Prii."
    ana "Look around! \nYou know, I barely get walk-in customers these days."
    ana "Most customers order through them delivery apps. {p} All I get to see are them unfriendly couriers who just wants to grab the food and leave!"
    ana "Speaking of which, why haven't I seen you these past few weeks?"
    ana "You were always here everyday—"

    p "A-A-Aha..haha..!\n Y-You don't have to mention {i}any of that{/i} really!"

    mx "Everyday, huh?"

    ana "Oh?"

    scene 02_burgerjoint_06
    with dissolve

    ana "My, my, my..."
    ana "Who do we have here, Prii?"

    p "Oh! This is [mx]. \nHe's... a friend of mine."
    p "And \"everyday\" is a r-relative term, [mx]."

    mx "Riiiight. {p} Well, hello there Ma'am."

    ana "{i}\"Ma'am\"?{/i} {p} I'm just a little bit older than Prii here."
    ana "Anna works fine, hotshot. {p} A friend of our little Priscilla here is always welcome!"

    scene 02_burgerjoint_05
    with dissolve

    p "You see, a couple of months ago he had a bad accident that sent him to the hospital."
    p "He lives alone in this city so no one could take care of him, really."
    p "His landlord was a total meanie too! {p} He kicked him out while he was in the hospital!"

    scene 02_burgerjoint_07
    with dissolve

    mx "Which is why I'm freeloading with them right now."
    mx "They're really great people."

    scene 02_burgerjoint_06
    with dissolve

    ana "That's so?"
    ana "You've been through hell, kid."

    p "See? He's nice if you get to know him."

    mx "Hey! What's that supposed to mean?"

    p "Ehehe~"

    scene 02_burgerjoint_05
    with dissolve

    ana "Bless your lovely hearts, dear."
    ana "You and your Mama."
    ana "Now..."

    scene 02_burgerjoint_08
    with dissolve

    ana "{i}Is that the only reason, Prii?{/i}"

    p "{i}W-Why are you whispering, Ms. Anna? {p} And what do you mean by {i}\"The only reason\"{/i}?"

    ana "{i}Well, he looks fine as a field of corn in a hot summer's day, ain't he?{/i}"
    ana "{i}And I overhear a lot. \n This place ain't exactly that big, ya'know?{/i}"
    ana "{i}You and your lot aren't exactly quiet as a churchmouse when you talk ova' here.{/i}"

    p "{i}W-What exactly do you mean by that?{/i}"

    ana "{i}Well... I was wondering why his name sounded so familiar then I remembered you talking about him multiple times.{/i}"
    ana "{i}And you become red as a peach every time you mention him.{/i}"
    ana "{i}He's the rumored Prince Charming, ain't he?{/i}"

    scene 02_burgerjoint_09
    with vpunch

    p "W-W-WHAT!?" with hpunch
    p "N-NO! [mx] is just...just a..."
    p "We're just friends, alright?"

    ana "Oh-ho!"
    ana "{i}Hit that nail on its head, didn't I?{/i}"
    ana "{i}I'll keep it a secret between us.{/i}"

    scene 02_burgerjoint_10
    with dissolve

    p "N-Noooooo~"
    p "Ms. Annnnaaaaaaaaaaa!"

    ana "{i}Work your charm, Prii!{/i}"
    ana "{i}I'll be cheering for ya'.{/i}"

    scene 02_burgerjoint_11
    with vpunch

    p "HMPH!"
    p "I-I'm not talking anymore!"

    ana "Ahahaha! \nThis is why you're so cute, Prii!"
    ana "You're so easy to tease!"

    p "HMPH!"

    ana "Aww! She's angry at me right now."
    ana "Well then, loverboy. \nWhat'll it be?"

    mx "M-Me?"
    mx "Uh, how about, uhh, a burger? {p} Umm, orange juice would be fine too, I guess?"

    ana "Just a burger and juice, huh? {p} Well, Prii? The usual is it then?"

    p "HMPH!" with hpunch

    ana "I'll take that as a yes."
    ana "Alright! \nWhy don't you two get comfortable while I tell Bobby your orders."

    mx "Yeah, thanks."

    scene black
    with fade

    scene 02_burgerjoint_13
    with fade

    mx "What was that all about?"
    mx "You were whispering with each other?"

    p "Err..."

    scene 02_burgerjoint_12
    with dissolve

    p "Um, uh, i-i-it's not something important for you to worry about!"
    p "Miss Anna was just teasing me again."
    p "Ehe..he..he..\n {i}*gulp*{/i}"

    mx "Uh, okay."
    mx "It seems you get along with her?"

    scene 02_burgerjoint_13
    with dissolve

    p "Yeah! She's very nice and funny but... {p}She teases me a lot!"
    p "You know, she's actually the new manager of this place.{p}Along with Mr. Bobby at the back, her older brother."
    p "He was suppose to inherit this place but he loves being a cook more than being a manager."

    scene 02_burgerjoint_12
    with dissolve

    p "She actually started just over a year and a half ago and the changes to the menu were amazing!"
    p "Especially the dessert selection!"
    p "She's the old Missus's youngest daughter."

    mx "The {i}\"old Missus\"{/i}?"

    p "The old owner of this place.{p}She ran this diner for quite a long time too!"
    p "She was a lovely woman. {p} She would always add a bit of extra fries on my order."

    scene 02_burgerjoint_15
    with dissolve

    p "You actually met her, y'know?"

    mx "I did?"

    p "Yeah! She scolded you for stealing my fries and making me cry."
    p "Which is always a very bad thing to do!"

    mx "Uh, I'll keep that in mind."
    mx "So, what happened to her?"

    scene 02_burgerjoint_14
    with dissolve

    p "Well, she was nearing retirement."
    p "She threw out the biggest party here and all of the food was free!"
    p "That's also when I met Miss Anna."
    p "She was introduced as the next owner of this joint and Mr. Bobby being the cook."

    scene 02_burgerjoint_16
    with dissolve

    p "Now that I think about it..."
    p "That was also the first time she teased me."
    p "I remember she said that I had to pay for the food I ate when it was free!"
    p "I got scared and cried! {p} I got angry at her and swore to never talk to her."
    p "I wonder how she made me talk to her again..?"

    ana "Well, it was... \n{i}\"Have you ever ate a Parfait before?\"{/i}"
    ana "{i}\"It's the greatest thing ever made.\"{/i} {p} And the rest was history."

    scene 02_burgerjoint_17
    with dissolve

    p "M-Ms. Anna~"

    ana "Well, I discovered that Prii here is easily pacified with food."
    ana "Keep that in mind, [mx]."
    ana "Anyways, here's your order. \nThank you for waiting."

    mx "W-Whoa..."
    mx "That's... {p} ...our order?"

    ana "Well, most of it is Prii's anyway."

    mx "This is {i}\"the usual\"{/i}?"
    mx "And you were her {i}\"everyday\"{/i} too..."

    p "I-I'm not pacified with anything, alright!"
    p "A-As I said, \"everyday\" is a r-relative term!"

    ana "Yeah, the only relative of the 24/7 store around the corner."
    ana "Anyways, why don't I leave you two lovebirds here to enjoy the food together?"
    ana "Remember what I said Prii, work your charm!"

    p "Ms. Anna! \nYou're teasing me a lot!"

    ana "Ahahaha! \nI'm gettin' mah fix since you didn't came back for so long!"
    ana "Well to apologize, I also threw in a bit of extra fries and rings for you, Prii."

    p ".{w=0.2}.{w=0.2}.{w=0.2} T-Thank you."

    scene black
    with fade

    play sound "soundfx/dishes_01.ogg"

    scene 02_burgerjoint_18
    with fade

    p "Wow~"
    p "It's been too long since I've last ordered this..."

    mx "It seems an awful lot, hm?"

    scene 02_burgerjoint_20
    with dissolve

    p "Ehehehe... {p} Don't look at me like that..."
    p "I-I'm still a growing girl, y'know?"

    mx "Uh-huh..."
    mx "What's all of these anyway?"

    scene 02_burgerjoint_22
    with dissolve

    p "Well..."
    p "Where should I start first..."
    p "Ah!"

    scene 02_burgerjoint_18
    with dissolve

    p "The burger! \nThe best seller in this diner!"
    p "This is their Americana Classic with extra pickles and tomatoes just for me!"
    p "It adds a bit more sweetness and punch to them!"
    p "And they ground their beef every morning with secret spices! \nA signature taste!"

    scene 02_burgerjoint_19
    with dissolve

    p "As for the side dish, a mix of fries and onion rings with a garlic mayo dip."
    p "My go-to beverage is their Vanilla Ice Cream Soda!"
    p "As for the dessert..."

    scene 02_burgerjoint_24
    with dissolve

    p "That gets a bit tricky!"
    p "Before, it was just the healthy scoop of ice cream but after Ms. Anna revamped the menu.."

    scene 02_burgerjoint_23
    with dissolve

    p "First, the Banana Split Sundae!"
    p "An amazing concoction of three different ice cream flavors between a split banana!"
    p "I heard the creator won some prestigious award or something for this!"

    scene 02_burgerjoint_19
    with dissolve

    p "However!"
    p "It is rivaled by another one in the menu!"
    p "The Parfait!"

    scene 02_burgerjoint_22
    with dissolve

    p "This one goes up rather than flat unlike the Banana Split!"
    p "It builds upon the flavors underneath that—"

    mx "...?"

    scene 02_burgerjoint_21
    with dissolve

    p "S-Sorry..."
    p "I didn't mean to bore you..."
    p "I just get excited by their food that I go off like that."

    mx "What? I didn't mind really. {p} Honestly, I actually found all of that fascinating."
    mx "It made me regret just ordering a burger and juice."
    mx "You showed a side I never knew."

    scene 02_burgerjoint_19
    with dissolve

    p "Ehehe..."

    mx "Anyways, hearing all that just made me hungrier."
    mx "Let's dig in before it gets cold."

    scene 02_burgerjoint_18
    with dissolve

    p "Yeah!"
    p "Maybe I'll try a bit of the fries or maybe the burger first..."

    scene black
    with slowfade

    show text "{size=36}{color=#A9A9A9} ( After a while... ) {/color}{/size}" at truecenter with dissolve

    play sound "soundfx/finished_eating.ogg"

    pause

    scene 02_burgerjoint_25
    with fade

    p "Ugh..."
    p "That was amazing..."
    p "Especially the fries! Mr. Bobby outdid himself..."

    mx "Y-Yeah.. {p} That was really something."

    "(Wow! I never even thought you could possibly devour food like that.)"
    "(Mental note: Prii really loves food.)"

    mx "It seems that solved your hunger problem."

    scene 02_burgerjoint_26
    with dissolve

    p "Y-Yeah."
    p "T-This was supposed to be a mission to help you recover your memories but I..."

    mx "Nah, that's okay! {p} We still have a lot of time after this."
    mx "I think I learned a lot about you from this experience alone.{p}It was worth the trip."

    p "N-Next time! \nI'll definitely... do... something..."

    mx "How about we leave this joint?"

    p "Good...{i}*burp*{/i} idea!"

    scene black
    with fade

    scene 02_burgerjoint_27
    with fade

    mx "Hey Anna!"
    mx "Thanks for the food, we'll be going now."

    p "Ms. Annamae, you're Parfaits and Sundaes were great as usual!"
    p "Tell Mr. Bobby his food were amazing!"

    ana "Anything for you, Prii!{p}Hear that Bobby? Prii likes your food!"
    ana "Anyways, be sure you two lovebirds comeback, alright?"

    p "Ms. Anna!" with vpunch

    play sound "soundfx/storebelljingle.ogg"

    scene burgerjoint_afternoon
    with slowfade

    mx "That was a nice experience."
    mx "How about we head home."

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    $ time += 1

    jump burgerjoint

label ep2_pquest_burgeradventure_finish:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button
    hide screen map_button

    scene 02_burgerjoint_28
    with fade

    p "I'll go rest for now. \nThe food coma is starting to set in."
    p "Thanks for going along with my food trip..."
    p "The {i}\"Get [mx]'s Memory Back\"{/i} first mission is a failure but we'll succeed eventually!"

    mx "Right. Well, I'll be waiting. {p} Go rest for now."

    p "Bye~"

    $ renpy.music.stop(channel='music2', fadeout=2)

    if notification_songs == True:
        $ renpy.notify("XNimVn - Sunny Day")

    $ story_music_ongoing = False

    scene ground_floor_afternoon
    with fade

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    $ pquest_burgeradventure_burgerjoint_finish = False
    $ pquest_burgeradventure_complete = True
    $ story_ongoing_priscilla = False
    $ map_time_skip = True

    jump ground_floor_hallway


label ep2_pquest_parkquest:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    $ pquest_parkquest = False
    $ pquest_parkquest_start = True

    $ renpy.music.stop(channel='music3', fadeout=1)

    if notification_songs == True:
        $ renpy.notify("outdoors - tired")

    $ renpy.music.play("music/outdoors_tired.mp3", channel='music2', fadein=1, loop=True)

    $ story_music_ongoing = True

    scene 01_parkqueststart_01
    with fade

    p "{i}...dum..doo..doo..dii..dun...{/i}"
    p "{i}...writing another plan...{/i}"

    mx "It looks like you're up to something, Prii?"
    mx "Another {i}\"food journey\"{/i} like last time?"

    scene 01_parkqueststart_02
    with dissolve

    p "[mx]!"
    p "A-And no! {p} It's not another {i}\"food journey\"{/i}, okay?"
    p "That was a...{w}a practice run, sort of?"
    p "B-But this time it's different!"

    mx "Oh? Go on."

    scene 01_parkqueststart_03
    with dissolve

    p "Well, you know..."
    p "{i}...how I got carried away a little bit last time...{/i}"

    mx "Hm? What was that?"

    p "N-Nothing!"
    p "What I meant to say is..."

    scene 01_parkqueststart_04
    with dissolve

    p "This is my new and improved {i}\"Get [mx]'s Memory Back\"{/i} mission! {p} Number 2!"
    p "Now based on a very proper and very scientific process!"

    mx "{i}\"A very proper and very scientific process?\"{/i}, is it?"

    p "Yup! Very scientific! {p}On that note, our next destination is the city park!"

    mx "The park near the city hall?"

    p "Yeah, that park!"

    scene 01_parkqueststart_03
    with dissolve

    p "I thought long and hard about the places you might have strong emotional bonds with..."
    p "Then I suddenly had an idea! {p} An epi.. phany or something like that!"

    mx "Sounds scientific already."

    p "It is! You know when we played with each other when we were kids, right? {p} What if we recreate those memories together!"

    scene 01_parkqueststart_04
    with dissolve

    p "We might be able to make you remember something!"

    mx "That's... {p} ...actually quite possible."

    "(If I was actually amnesiac but then again...)"

    p "I know right! I thought about the last time we—"
    p "Wait! {p} Let me get up first..."

    scene 01_parkqueststart_06
    with fade

    p "Now! Where were we... Oh yeah!"
    p "Remember when I told you about the time the old Missus scolded you back in diner?"

    mx "Yeah?"

    scene 01_parkqueststart_07
    with dissolve

    p "Well, that started this idea! \nBut we didn't really went there enough in the past...."
    p "So, it might be hard to remember anything deep. {p} But maybe if we go somewhere where we played a lot as kids..."

    mx "Like the park?"

    scene 01_parkqueststart_08
    with dissolve

    p "Uh-huh! \nYou might be able to remember more!"
    p "And also... {p} I wanted to go there to remember something too."

    mx "About what?"

    p "If I knew, I wouldn't need to remember it, y'know?"

    mx "O-Oh, ahaha..ha.. {p} Point taken."

    scene 01_parkqueststart_07
    with dissolve

    p "Well, it's been bugging me for the past few days too..."
    p "It's something that was very important but I couldn't point my finger on it..."
    p "There's this feeling that if I remember it, you might remember something too."
    p "Atleast that's how I think it'll happen..?"

    scene 01_parkqueststart_05
    with dissolve

    p "But overall, it's a totally an amazing plan, right?"

    mx "So, in summary..."
    mx "You want us to go to the park to recreate our old memories."
    mx "But also, that by chance, you might remember this missing memory of yours too?"
    mx "All in the chance that I might remember something in all of this?"

    scene 01_parkqueststart_06
    with dissolve

    p "Correct! {p} Whaddaya think?"

    mx "Well, it looks good in paper and all..."
    mx "But how is this {i}\"scientific\"?"
    mx "This is more like a..."

    scene 01_parkqueststart_05
    with dissolve

    p "A science experiment!"

    mx "Well, I was thinking along the lines of... \n{i}\"Whacking a pinata and seeing what comes out of it.\"{/i}."
    mx "But {i}\"science experiment\"{/i} works too, I guess? \nIn a non-scientific way..."

    p "And you'll be the... umm... y'know the science helper... {p} The cute furry thing. What was it called again?"

    mx "The guinea pig?"

    scene 01_parkqueststart_08
    with dissolve

    p "A very cute and very big guinea pig!"

    mx "They aren't exactly helpers and more like...{w} a victim."

    p "A victim of fun! \nSo, on we go!"

    mx "{i}*sigh*{/i} {p} Alright, let's just get this over with."

    p "Yay~ {p} Now then Mr. Guinea Piggy..."

    scene 01_parkqueststart_09
    with dissolve

    mx "M-Mr. Guinea Piggy?"

    p "Now off you go and wait! {p} {i}\"Get [mx]'s Memory Back: Mission 2\"{/i} starts now!"
    p "Get comfy by the stairs while I'll go get dressed!"

    scene second_floor_hallway_afternoon
    with slowfade

    play sound "soundfx/door_locked.ogg"

    "{i}*door lock*"

    pause

    "(Great... just like last time.) {p} (Get comfy by the stairs, huh?)"
    "(No point in complaining.) {p} (Guess I'll just wait for her again.)"

    scene black
    with slowfade

    show text "{size=36}{color=#A9A9A9} ( A few minutes later... ) {/color}{/size}" at truecenter with dissolve

    pause

    scene 01_burgeradventurestart_09
    with fade

    "(The city park, huh?)"
    "(I remember going there when I was young... the old body of mine.)"
    "(But work and following my father's footsteps made me isolated all of these years.)"
    "(I wonder what it looks now?)"

    mx "Hm?"

    play sound "soundfx/door_open.ogg"

    "{i}*door open*"

    scene 01_parkqueststart_10 with dissolve:
        subpixel True
        yalign 1.0
        pause 1.0
        linear 5.0 yalign 0.0

    window hide

    $ renpy.pause(3, hard = True)

    mx "Oh, I remember that outfit."
    mx "Isn't that what you wore when you visited me?"

    p "Yeah! The weather said it'll be a bit chilly today."
    p "Well then, how about we do some science stuff, hm?"

    mx "Oh boy."

    p "Ehehe~"

    scene second_floor_hallway_afternoon
    with fade

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    $ park_unlock = True
    $ story_ongoing_priscilla = True
    $ pquest_parkquest = False
    $ pquest_parkquest_start = True
    $ map_time_skip = False

    jump second_floor_hallway

label ep2_pquest_parkquest_park_enter:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    $ pquest_parkquest_start = False
    $ pquest_parkquest_swingstart_01 = True

    $ renpy.music.stop(channel='music2', fadeout=4)

    if notification_songs == True:
        $ renpy.notify("biosphere - let's be lazy together")

    $ renpy.music.play("music/biosphere-let's be lazy together.mp3", channel='music1', fadein=3, loop=True)

    scene 02_parkquestplay_01
    with fade

    p "Yay! We're finally here!"
    p "It looks so peaceful!"
    p "A perfect weather for doing science stuff!"

    mx "So, this is the experimental lab, huh?"

    scene 02_parkquestplay_02
    with dissolve

    p "It's been so long since I've stepped back here again!"

    mx "Really? {p} Not even once?"

    p "Only kids hang around here, [mx]!"
    p "And y'know..."

    scene 02_parkquestplay_03
    with dissolve

    p "The occasional lovey-dovey couples here and there..."

    mx "Oh, {i}those{/i} people."

    scene 02_parkquestplay_05
    with dissolve

    p "Anyways, our first order of business!"
    p "{i}\"Get [mx]'s Memory Back\"{/i} {p} El Numero Dos!"
    p "That's Spanish for Number 2, by the way."

    mx "Because in {i}\"Numero Uno\"{/i}, we just ended up eating—"

    scene 02_parkquestplay_03
    with dissolve

    p "Ehehe..hehe... \nY-You don't have to talk about that..."
    p "Experiments build upon failures, y'know?"

    mx "Alright then. \nSo, how exactly are we gonna do this?"
    mx "Do we just do something and hope for the best?"

    scene 02_parkquestplay_08
    with dissolve

    p "Well, based on my little research..."
    p "Our little neurons still carry our old memories and they're still sleeping there."
    p "So it needs to be woken up by special alarm clocks called, uhh, a stimuli!"

    scene 02_parkquestplay_06
    with dissolve

    p "Which are unique on their own! Some needs pictures or music or even just by doing stuff to activate!"

    mx "Amazingly explained... {p} Did you learn all of this on your own?"

    p "Well, yes and no... {p} I asked Ms. Aanya to explain it to me like I'm five—I mean, like an adult!"
    p "Because, y'know! \nI'm an adult like that!"

    scene 02_parkquestplay_09
    with dissolve

    p "Anyways! It means that our brain needs to be stimulated if we want to remember something!"

    mx "Stimulated with what?"

    p "With fun and games!" with vpunch

    mx "Really? \nShe said that?"

    scene 02_parkquestplay_03
    with dissolve

    p "Well, not exactly but she said doing something physically and mentally stimulating might work..."
    p "Soooo~"

    scene 02_parkquestplay_06
    with dissolve

    p "I thought we could play at the swing sets! {p} It's something physical, right?"

    mx "The swings? {p} Aren't we a little too old for that?"

    scene 02_parkquestplay_07
    with dissolve

    p "Hmph!" with hpunch
    p "F-For your information! \nThis is for the sake of science, [mx]!"
    p "A-And I'm never too old for anything especially the swings!"
    p "Grrr!"

    mx "Alright, alright! \nCalm down!"
    mx "The swings it is."

    scene 02_parkquestplay_06
    with dissolve

    p "Then let's go—"

    mx "Wait! What about the {i}\"mental stimulation\"{/i} part? {p}Isn't that important too? \nLike a lot? Because the memories are in the brain?" with hpunch
    mx "Are we gonna play some puzzles or chess here?"

    scene 02_parkquestplay_07
    with dissolve

    p "Puzzles? Chess? {p} They're boring!"
    p "We can do the {i}\"mental stuff\"{/i} later~ {p} It's too exhausting too think about it!"

    scene 02_parkquestplay_04
    with dissolve

    p "We should go to the swings and play first! {p} It's much more fun to do that!"
    p "That's what we're here about anyways! \nFun and games!"

    mx "Why do I get the feeling that someone's here just to play around? {p} And that Mission {i}\"Numero Tres\"{/i} is just around the corner?"

    scene 02_parkquestplay_03
    with dissolve

    p "Ehe..he..he... {p} Err, m-maybe you just lack the f-feeling of fun!"
    mx "Feeling of fun—"

    scene 02_parkquestplay_10

    p "Anyways! \nLet's go play while the sun's out!" with vpunch
    p "The playground is over there!"

    scene park_afternoon_entrance
    with fade

    mx "Well, to the playground it is."

    "(As if I've had a choice to begin with.) {p} (I think it's over there beyond the fountain.)"

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump park_fountain_afternoon

label ep2_pquest_parkquest_park_playground_intro:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button
    hide screen map_button

    scene park_afternoon_playground
    with fade

    p "The playground!"
    p "There's the swings to the right."
    p "Let's go near it."

    $ pquest_parkquest_swingstart_01 = False
    $ pquest_parkquest_swingstart_02 = True

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump park_playground_afternoon

label ep2_pquest_parkquest_park_playground:

    $ pquest_parkquest_swingstart_02 = False

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene 03_parkquestswing_01
    with fade

    p "..."

    mx "You okay, Prii? \n You got quiet all of a sudden?"

    p "Y-Yeah, it's just... {p} I feel the nostalgia coming back to me."
    p "This seat was the one I used the most. \nIt looks like it's been fixed and repainted."
    p "Let me grab this and..."

    scene 03_parkquestswing_02
    with dissolve

    p "There!"
    p "Ehehehe~ {p} I'm starting to remember the fun I had here!"
    p "Every time after school's out and early weekend mornings! {p} We'd be here all day!"
    p "Oh! How about you, [mx]? {p} Anything comes to mind?"

    mx "It's hard to say really... {p} Actually, it isn't. I don't remember anything."

    p "That's alright!"

    scene 03_parkquestswing_03
    with dissolve

    p "It means we still have the rest of the day to make you remember!"
    p "So, hang in there!"

    mx "Don't worry about it. \nI'm not exactly in a hurry."
    mx "So, do I ride another swing too or—"

    p "Wait! Umm..."
    p "Uh, p-pushing me is also a physical activity too, y'know?"

    mx "Really..?"
    mx "Why do I get another uneasy feeling that you don't want me to seat... {p}Because you want me push you all day?"

    p "{i}...why do you always get it right..."

    mx "Hmm?"

    scene 03_parkquestswing_04
    with dissolve

    p "I-I mean, it's an ongoing s-scientific process! {p} Sacrifices has to be made!" with vpunch
    p "We will never know if it works if you just complain! \nSo hurry~"

    mx "Yes, yes. I understand Princess Priscilla. {p} Does your grace want this peasant to start pushing you?"

    p "Ooh! Princess Priscilla! I like the sound of that! {p} Yeah! You can push me now, Mr. Peasant!"
    p "{i}Push me! {w} Push me! {w} Push me!"

    mx "Here goes!"

    play sound "soundfx/swing_push.ogg"

    scene 03_parkquestswing_05
    with dissolve

    p "{i}Wheeeeee~" with hpunch
    p "Ahahaha!"
    p "This is so much fun!"

    scene 03_parkquestswing_04

    mx "{i}*Oof!*" with hpunch

    "(Guh! M-My knees!)"
    "(I should've realized that swing still has a momentum even if I hold the chains.)"

    p "That was amazing!"
    p "Come on! Push me again!"

    mx "{i}*Hyaa!*{/i}"

    play sound "soundfx/swing_push.ogg"

    scene 03_parkquestswing_05
    with hpunch

    p "Yaaaaay~"
    p "Ahahaha!"
    p "Almost there!"

    scene 03_parkquestswing_04
    with hpunch

    mx "{i}*Huff*{/i} {w} {i}*Huff*{/i}"

    "(I think the pain's starting to intensify.)"
    "(I should rest a bit...)"

    p "Come on! One more push!"
    p "You're not tired yet, are you?"

    mx "I'm just breathing... {i}deeply."

    p "Or maybe you're getting older?"

    mx "Old, huh? {p} Okay, here's an old man push then!"

    p "W-Wait I'm not in position—"

    play sound "soundfx/swing_push.ogg"

    scene 03_parkquestswing_06

    p "Waaaaaah!" with hpunch
    p "[mx]! You meanie!"

    "(Oh shit!)"
    mx "P-Prii!"

    scene 03_parkquestswing_07
    with vpunch

    play sound "soundfx/falling_thud.ogg"

    p "O-Owwie!"
    p "H-Hot!"

    mx "Prii, are you all right?"
    mx "I-I'm sorry about that."

    p "Grrr!"

    scene 03_parkquestswing_08
    with dissolve

    p "HMPH!" with hpunch
    p "{i}Meanie! {w} Meanie! {w} Meanie!"

    mx "Er, sorry... that was my fault."

    p "T-That hurt!"

    mx "W-What can I do to make it up to you?"

    scene 03_parkquestswing_09
    with dissolve

    p "HMPH!" with hpunch
    p "I'm not talking! Meanie Peasant! Meanie Piggy!"

    "(Ah shit! What can I do? She's really angry.)"

    scene 03_parkquestswing_flashback
    with fade

    ana "{i}Well, I discovered that Prii here is easily pacified with food."
    ana "{i}Keep that in mind, [mx]."

    "(Wait!) {p} (Oh yeah! She likes food!)"

    scene 03_parkquestswing_09
    with dissolve

    "(I think I saw an ice cream shop over there!)"

    mx "Um, how about I make it up to you by... {p} Buying you some ice cream?"

    scene 03_parkquestswing_10
    with dissolve

    p "Ice... cream?"
    p "Like Strawberry ice cream o-or Bubblegum or Vanilla and..and..."

    mx "Uh.. yeah? All of that?"

    scene 03_parkquestswing_09
    with dissolve

    p "W-Well, if you insist!"
    p "W-We're still in the middle of our experiment but if you want to eat ice cream then..."

    mx "Uh, sure! It's my apology for pushing you too much."

    scene 03_parkquestswing_11
    with dissolve

    p "Really! {p} Let's go then!"
    p "You already said you're gonna treat me with ice cream, right!?"

    mx "O-Of course! \nI'm not gonna break that promise any time soon!"

    p "Yay! Ice cream!"

    scene park_afternoon_playground
    with fade

    "(Well, that actually worked.)"
    "(As for the ice cream truck...) {p} (I think it was in the food area?)"

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    $ pquest_parkquest_icecreamstart_01 = True

    jump park_playground_afternoon

label ep2_pquest_parkquest_icecream_intro:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    $ pquest_parkquest_icecreamstart_01 = False
    $ pquest_parkquest_icecreamstart = True

    scene park_afternoon_foodarea
    with fade

    show 02_parkquest_icecream_idle

    p "There's the truck!"
    p "Let's go buy some ice cream!"

    jump park_foodarea_triggers

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

label ep2_pquest_parkquest_icecream:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    $ pquest_parkquest_icecreamstart = False
    $ pquest_parkquest_icecreamstart_fountain = True

    scene 04_parkquesticecream_01
    with fade

    $ renpy.music.stop(channel='music1', fadeout=3)

    unk "{i}...it's slow day today..."
    unk "{i}...maybe I'll play that game Kaleb always wanted me to..."

    mx "Excuse me?"
    mx "I'd like to order something."

    unk "Hmm?"

    scene 04_parkquesticecream_02
    with dissolve

    if notification_songs == True:
        $ renpy.notify("neeks - under cherry blossom trees")

    $ renpy.music.play("music/neeks_under cherry blossom trees.mp3", channel='music2', fadein=3, loop=True)

    unk "Oh, {i}denibenya{/i}! I mean, customers! \nWhat can I—wait ah minute, ah!"
    unk "Boy, ya look very familiar."
    unk "Did ya borrow money from me?"

    mx "I... did? N-No! I mean, not that I can remember..."

    p "Oh! It's Mr. Negasi!"
    p "Remember us? We played here as kids!"

    ice "Red hair... {w}Oh!"

    scene 04_parkquesticecream_03
    with dissolve

    ice "Well, look who it is, ah!"
    ice "It's the crybaby and this must be..."
    ice "The bully {i}ganeni{/i}, eh!"
    ice "All grown up! Especially ya, young miss, like a beautiful {i}qwara{/i}!"

    p "What's a \"qwara\", Mr. Negasi?"

    ice "A big beautiful tree that blooms with red flowers in my old country, ya know?"

    p "Ooh! You heard it, [mx]? \nI'm a beautiful flower tree!"
    p "Ehehe~"

    mx "Then what's a {i}\"bully ganeni\"{/i}? \nIs that a tree too?"

    ice "Oh no! \n{i}\"Ganeni\"{/i} means demon!"
    ice "Bad kids would always run away from ya because ya beat them up!"
    ice "The demon of bullies here, ah! \nAhahaha!"

    mx "O-Oh, uh, I see."

    "(This kid had that kind of history, huh?)"

    p "[mx], you're a {i}Ganeni{/i} Piggy now! Ehehe!"

    mx "{i}*sigh*{/i} {p} Great, Prii's making puns now."

    ice "Anyways! What did ya two need, ah?"

    mx "Well, we would like to order some ice cream sundae."

    ice "Is that all? \nWhy didn't ya say so!"
    ice "How about this, because ya gave me great big smile, ah! {p}I'll give this to ya two for free, ah!"

    p "Really, Mr. Negasi?"

    scene 04_parkquesticecream_04
    with dissolve

    ice "Of course! Only once an' no more after, eh? \nI still need money, ya know?"
    ice "Now, Mr. {i}Ganeni{/i}, what flavor do ya want eh?"
    ice "Ya can look at the chart, ah?"

    mx "Um, uh, its..."

    p "Take a pick, [mx]! {p} {i}Hurry! {w} Hurry! {w} Hurry!"

    mx "H-Huh? O-Okay! {p} Uhh, umm, vanilla!"

    ice "Vanilla it is. {p} For the young lady..."

    p "I want, umm, vanilla too—No! Strawberry! {p} Stop! Umm, Blueberry! Err... maybe Chocolate?"

    mx "What? I thought you already had a flavor picked? {p} That's why you were rushing me."

    p "Y-You picked too fast before I could decide!"

    mx "Because you said to hurry it up! {p} I panicked and chose vanilla."

    p "Errr... {w} Ah-ha! {p} That's right!"

    mx "What is?"

    p "T-This is what we now call a {i}\"mental stimulation\"{/i} thingy!"
    p "For that, you're the one who's going to choose what flavor I get!"
    p "I'll judge your choice after eating the ice cream! {p} Challenge start!"

    mx "R-Right now?"

    ice "So, what kind of flavor, boy?"

    mx "Umm..."

    menu:
        mod "Choice of icecream doesn't seem to affect later game options."
        "Chocolate seems like the safest choice.":


            mx "Chocolate please."

            $ pquest_parkquest_icecream_chocolate = True

            scene 04_parkquesticecream_04
            with dissolve

            ice "Chocolate it is for the beautiful young lady, ah!"

            pause 0.4

            jump ep2_pquest_parkquest_icecream_choco
        "I chose Vanilla so it should be fine too, right?":


            mx "Vanilla please."

            $ pquest_parkquest_icecream_vanilla = True

            scene 04_parkquesticecream_04
            with dissolve

            ice "Vanilla it is for the beautiful young lady, ah!."

            pause 0.4

            jump ep2_pquest_parkquest_icecream_vanilla
        "No one hates Strawberry, right?":


            mx "Strawberry please."

            $ pquest_parkquest_icecream_strawberry = True

            scene 04_parkquesticecream_04
            with dissolve

            ice "Strawberry it is for the beautiful young lady, ah!"

            pause 0.4

            jump ep2_pquest_parkquest_icecream_strawberry
        "Bubblegum seems like a weird flavor. Maybe she'll like it?":


            mx "Bubblegum please."

            $ pquest_parkquest_icecream_bubblegum = True

            scene 04_parkquesticecream_04
            with dissolve

            ice "Bubblegum it is for the beautiful young lady, ah!"

            pause 0.4

            jump ep2_pquest_parkquest_icecream_bubblegum


label ep2_pquest_parkquest_icecream_vanilla:

    scene 04_parkquesticecream_05_vn
    with dissolve

    ice "Thanks for waiting! {p} Two vanilla ice cream sundae for the boy and girl!"

    mx "Thanks!"

    ice "Anytime, kids! Be sure to tell your friends about me, ah!"

    p "Goodbye, Mr. Negasi!"
    p "Thank you for the free ice cream!"

    scene 04_parkquesticecream_06_vn
    with fade

    p "Vanilla!"
    p "That's a pretty good choice!"

    mx "So, do I pass the test now?"

    p "Not yet!"

    scene 04_parkquesticecream_07_vn
    with dissolve

    p "You know, Vanilla gets made fun of as being boring and plain."
    p "But it's actually one of the most complex flavors, y'know? {p} And it isn't overbearing and full of itself."
    p "It's a shy flavor. \nVanilla is vanilla!"

    mx "Oh! That's really interesting. {p} Probably why I chose it too, I guess?"

    p "See! Ehehe~"
    p "Let's dig in!"

    scene 04_parkquesticecream_08_vn
    with dissolve

    p "{i}*shlurp* {w} *shlurp*{/i}"
    p "Eech helishus! {i}(It's delicious!){/i} {p} Waneela ish eely wheey! {i}(Vanilla is really great!){/i}"

    mx "Maybe you should slow down a bit first?"

    scene 04_parkquesticecream_09_vn
    with dissolve

    p "Eh? Wy? {i}(Eh? Why?)"
    p "Ah wan hoo eeh maa ahk kheem! \n{i}(I want to eat my ice cream!)"

    mx "Maybe we should sit down somewhere first?"
    mx "My knees are killing me."

    scene 04_parkquesticecream_10_vn
    with dissolve

    p "Hrmm?"
    p "Okay..."
    p "I really {i}really{/i} want to eat my ice cream, y'know..."

    mx "Yeah, I know."

    p "Well, if that's the case..."

    scene 04_parkquesticecream_11_vn
    with dissolve

    p "Maybe we can sit at the fountain over there!"
    p "I love the feeling of the water splashing!"

    mx "The fountain?"
    mx "Alright, let's go there."

    scene park_afternoon_foodarea
    with fade

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump park_foodarea_afternoon

label ep2_pquest_parkquest_icecream_bubblegum:

    scene 04_parkquesticecream_05_bb
    with dissolve

    ice "Thanks for waiting! {p} A vanilla ice cream sundae for the boy..."
    ice "And bubblegum ice cream sundae for the young lady!"

    mx "Thanks!"

    ice "Anytime, kids! Be sure to tell your friends about me, ah!"

    p "Goodbye, Mr. Negasi!"
    p "Thank you for the free ice cream!"

    scene 04_parkquesticecream_06_bb
    with fade

    p "Bubblegum!"
    p "That's a pretty colorful choice!"

    mx "So, do I pass the test now?"

    p "Not yet!"

    scene 04_parkquesticecream_07_bb
    with dissolve

    p "You know, Bubblegum is actually made through a combination of strawberry-banana-fruit flavors!"
    p "It's a very {i}punchy{/i} flavor, y'know? {p} It isn't shy and it assaults your taste buds in the right way!"
    p "It's a very fun flavor, isn't it?"

    mx "I guess so? Speaking of {i}\"punchy\"{/i}... {p} It certainly reminds me of a certain someone who wanted to punch me after waking up from a coma."

    p "Ehe..he..he~"

    scene 04_parkquesticecream_08_bb
    with dissolve

    p "{i}*shlurp* {w} *shlurp*{/i}"
    p "Eech helishus! {i}(It's delicious!){/i} {p} Bubba-umm ish eely wheey! {i}(Bubblegum is really great!){/i}"

    mx "Maybe you should slow down a bit first?"

    scene 04_parkquesticecream_09_bb
    with dissolve

    p "Eh? Wy? {i}(Eh? Why?)"
    p "Ah wan hoo eeh maa ahk kheem! \n{i}(I want to eat my ice cream!)"

    mx "Maybe we should sit down somewhere first?"
    mx "My knees are killing me."

    scene 04_parkquesticecream_10_bb
    with dissolve

    p "Hrmm?"
    p "Okay..."
    p "I really {i}really{/i} want to eat my ice cream, y'know..."

    mx "Yeah, I know."

    p "Well, if that's the case..."

    scene 04_parkquesticecream_11_bb
    with dissolve

    p "Maybe we can sit at the fountain over there!"
    p "I love the feeling of the water splashing!"

    mx "The fountain?"
    mx "Alright, let's go there."

    scene park_afternoon_foodarea
    with fade

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump park_foodarea_afternoon

label ep2_pquest_parkquest_icecream_strawberry:

    scene 04_parkquesticecream_05_sb
    with dissolve

    ice "Thanks for waiting! {p} A vanilla ice cream sundae for the boy..."
    ice "And strawberry ice cream sundae for the young lady!"

    mx "Thanks!"

    ice "Anytime, kids! Be sure to tell your friends about me, ah!"

    p "Goodbye, Mr. Negasi!"
    p "Thank you for the free ice cream!"

    scene 04_parkquesticecream_06_sb
    with fade

    p "Strawberry!"
    p "That's a pretty sweet choice!"

    mx "So, do I pass the test now?"

    p "Not yet!"

    scene 04_parkquesticecream_07_sb
    with dissolve

    p "You know, Strawberries aren't technically berries? {p} The fruit is the ovary of a flowering plant which houses the seed inside it."
    p "But in strawberries, the \"seeds\" on the skin are the actual ovaries! {p} Which holds a seed inside each of it!"
    p "So, the strawberry is actually an overgrown stem! {p} Which means, we're technically eating a vegetable ice cream!"
    p "Which is, in a way, healthy! Teehee~"

    mx "... {p} Riiiiggght."
    mx "I'm actually amazed, not because of the strawberry fact but the extensive knowledge you have about food related things."
    mx "Also, I'm pretty sure ice cream is only, like, 10%% strawberry flavoring and 90%% cream."

    p "Technicalities schmecalities~"
    p "Let's eat! Ehehe~"

    scene 04_parkquesticecream_08_sb
    with dissolve

    p "{i}*shlurp* {w} *shlurp*{/i}"
    p "Eech helishus! {i}(It's delicious!){/i} {p} Shobewy ish eely wheey! {i}(Strawberry is really great!){/i}"

    mx "Maybe you should slow down a bit first?"

    scene 04_parkquesticecream_09_sb
    with dissolve

    p "Eh? Wy? {i}(Eh? Why?)"
    p "Ah wan hoo eeh maa ahk kheem! \n{i}(I want to eat my ice cream!)"

    mx "Maybe we should sit down somewhere first?"
    mx "My knees are killing me."

    scene 04_parkquesticecream_10_sb
    with dissolve

    p "Hrmm?"
    p "Okay..."
    p "I really {i}really{/i} want to eat my ice cream, y'know..."

    mx "Yeah, I know."

    p "Well, if that's the case..."

    scene 04_parkquesticecream_11_sb
    with dissolve

    p "Maybe we can sit at the fountain over there!"
    p "I love the feeling of the water splashing!"

    mx "The fountain?"
    mx "Alright, let's go there."

    scene park_afternoon_foodarea
    with fade

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump park_foodarea_afternoon

label ep2_pquest_parkquest_icecream_choco:

    scene 04_parkquesticecream_05_ch
    with dissolve

    ice "Thanks for waiting! {p} A vanilla ice cream sundae for the boy..."
    ice "And chocolate ice cream sundae for the young lady!"

    mx "Thanks!"

    ice "Anytime, kids! Be sure to tell your friends about me, ah!"

    p "Goodbye, Mr. Negasi!"
    p "Thank you for the free ice cream!"

    scene 04_parkquesticecream_06_ch
    with fade

    p "Chocolate!"
    p "That's a pretty good choice!"

    mx "So, do I pass the test now?"

    p "Not yet!"

    scene 04_parkquesticecream_07_ch
    with dissolve

    p "You know, Chocolate was the very first ice cream flavor? Even before Vanilla!"
    p "And the guy who first tasted even exclaimed... {p} {i}\"In all my time, I have never made a discovery so fine. This is not a taste, it’s an emotion\""
    p "Chocolate is the flavor of happiness!"

    mx "That's a really fascinating history for a flavor which I thought was very basic."
    mx "You can't judge ice cream by its flavor, eh?"

    p "Ehehe~"

    scene 04_parkquesticecream_08_ch
    with dissolve

    p "{i}*shlurp* {w} *shlurp*{/i}"
    p "Eech helishus! {i}(It's delicious!){/i} {p} Lokolet ish eely wheey! {i}(Chocolate is really great!){/i}"

    mx "Maybe you should slow down a bit first?"

    scene 04_parkquesticecream_09_ch
    with dissolve

    p "Eh? Wy? {i}(Eh? Why?)"
    p "Ah wan hoo eeh maa ahk kheem! \n{i}(I want to eat my ice cream!)"

    mx "Maybe we should sit down somewhere first?"
    mx "My knees are killing me."

    scene 04_parkquesticecream_10_ch
    with dissolve

    p "Hrmm?"
    p "Okay..."
    p "I really {i}really{/i} want to eat my ice cream, y'know..."

    mx "Yeah, I know."

    p "Well, if that's the case..."

    scene 04_parkquesticecream_11_ch
    with dissolve

    p "Maybe we can sit at the fountain over there!"
    p "I love the feeling of the water splashing!"

    mx "The fountain?"
    mx "Alright, let's go there."

    scene park_afternoon_foodarea
    with fade

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump park_foodarea_afternoon

label ep2_pquest_parkquest_finishing_up:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button
    hide screen map_button

    $ pquest_parkquest_icecreamstart_fountain = False

    play sound "soundfx/fountain.ogg" loop

    if pquest_parkquest_icecream_vanilla == True:

        scene 04_parkquesticecream_12_vn
        with fade

        p "This is nice, isn't it?"

        mx "Yeah. \nIt's refreshing here, a bit calming too."

        p "It's the water splashing and the sound it makes that does it!"

        mx "I kinda see that now."

        p "So, how do you feel about our day so far?"

        mx "Honestly? {w} I'm actually having fun. {p} I thought {i}\"recreating memories\"{/i} would be much more complicated than this."

        p "Well, why would it be? {p} All we did in the past is play and eat ice cream here!"
        p "We were just kids after all."

        mx "... {w} You know, you're right Prii. {p} Maybe I was thinking too much into this, huh?"

        p "That's why I'm the one making the plans and you're the guinea pig!"

        mx "Ahahaha! Aren't you the cutest little runt?"

        p "Bleh~"

        mx "So, how's it with that thing you wanted to remember?"

        scene 04_parkquesticecream_13_vn
        with dissolve

        p "Well... {w} I think I'm getting the gist of it? {p} But nothing solid as of yet."
        p "I think talking with Mr. Negasi helped a lot to clear some of it! {p} More importantly, how about you though?"

        scene 04_parkquesticecream_14_vn
        with dissolve

        p "This is {i}\"Get [mx]'s Memory Back\"{/i} mission after all..."

        mx "Still no dice. {p} Just... nothing"

        "(If I actually did remember something, that'll be a really scary thing.)"

        p "Oh..."

        mx "Cheer up! \n It's not like I'm gonna turn back to my old self in a snap."
        mx "Speaking of which, I was wondering how I was before all of this happened?"
        mx "From the small bits I noticed, I think I was more of a douchebag?"

        scene 04_parkquesticecream_13_vn
        with dissolve

        p "What!? No you weren't! You were just... {p} Well, you were really difficult."
        p "When I heard you moved back to the city... {p} I tried asking around."
        p "I learned that you were enrolled in the same university I'm attending."

        mx "Wait. I'm still attending school? {p} Am I still enrolled?"

        p "Yeah, silly!"
        p "We're still in {i}spring break{/i} so you have a bit of time to talk with them about your \"situation\"."
        p "I also heard of rumors that you weren't exactly the cooperative kind..."

        "(Ugh! This kid is still in school!?)"
        "(I should try going there and solving the problem after the break is over.)"
        "(His problem is gonna be my problem too.)"

        mx "I'm starting to think I was not that great of a person to be around with?"

        scene 04_parkquesticecream_14_vn
        with dissolve

        p "W-Well, uhh, I admit you were hard to talk to when I finally talked with you..."
        p "It seems you've changed completely. {p} You were really stubborn about accepting help from us."
        p "B-But you're here now, right? \nThat's progress too?"

        mx "Yeah but it took me losing my memories to even accept it. {p} Now, I'm kinda afraid of what'll happen if I remember all of it."

        scene 04_parkquesticecream_13_vn
        with dissolve

        p "You're such a downer, [mx]! \nYou've been given another chance of life!"
        p "And remembering your memories isn't that bad... \nEspecially the promise we made..."

        mx "The promise—"

        "{i}*drip* {w=0.2} *drip*{/i}"

        p "Hm..?"

        scene 04_parkquesticecream_15_vn

        p "M-My ice cream's starting to melt!" with vpunch
        p "Nooo! It's dripping!"
        p "{i}*slurp*! {w} *slurp!* {w} *slurp!*"
        p "Hyoo shood esh owrs shoo! \n{i}(You should eat yours too!){/i}"

        mx "Oh crap!"

        jump ep2_pquest_parkquest_finishing_end

    if pquest_parkquest_icecream_chocolate == True:

        scene 04_parkquesticecream_12_ch
        with fade

        p "This is nice, isn't it?"

        mx "Yeah. \nIt's refreshing here, a bit calming too."

        p "It's the water splashing and the sound it makes that does it!"

        mx "I kinda see that now."

        p "So, how do you feel about our day so far?"

        mx "Honestly? {w} I'm actually having fun. {p} I thought {i}\"recreating memories\"{/i} would be much more complicated than this."

        p "Well, why would it be? {p} All we did in the past is play and eat ice cream here!"
        p "We were just kids after all."

        mx "... {w} You know, you're right Prii. {p} Maybe I was thinking too much into this, huh?"

        p "That's why I'm the one making the plans and you're the guinea pig!"

        mx "Ahahaha! Aren't you the cutest little runt?"

        p "Bleh~"

        mx "So, how's it with that thing you wanted to remember?"

        scene 04_parkquesticecream_13_ch
        with dissolve

        p "Well... {w} I think I'm getting the gist of it? {p} But nothing solid as of yet."
        p "I think talking with Mr. Negasi helped a lot to clear some of it! {p} More importantly, how about you though?"

        scene 04_parkquesticecream_14_ch
        with dissolve

        p "This is {i}\"Get [mx]'s Memory Back\"{/i} mission after all..."

        mx "Still no dice. {p} Just... nothing"

        "(If I actually did remember something, that'll be a really scary thing.)"

        p "Oh..."

        mx "Cheer up! \n It's not like I'm gonna turn back to my old self in a snap."
        mx "Speaking of which, I was wondering how I was before all of this happened?"
        mx "From the small bits I noticed, I think I was more of a douchebag?"

        scene 04_parkquesticecream_13_ch
        with dissolve

        p "What!? No you weren't! You were just... {p} Well, you were really difficult."
        p "When I heard you moved back to the city... {p} I tried asking around."
        p "I learned that you were enrolled in the same university I'm attending."

        mx "Wait. I'm still attending school? {p} Am I still enrolled?"

        p "Yeah, silly!"
        p "We're still in {i}spring break{/i} so you have a bit of time to talk with them about your \"situation\"."
        p "I also heard of rumors that you weren't exactly the cooperative kind..."

        "(Ugh! This kid is still in school!?)"
        "(I should try going there and solving the problem after the break is over.)"
        "(His problem is gonna be my problem too.)"

        mx "I'm starting to think I was not that great of a person to be around with?"

        scene 04_parkquesticecream_14_ch
        with dissolve

        p "W-Well, uhh, I admit you were hard to talk to when I finally talked with you..."
        p "It seems you've changed completely. {p} You were really stubborn about accepting help from us."
        p "B-But you're here now, right? \nThat's progress too?"

        mx "Yeah but it took me losing my memories to even accept it. {p} Now, I'm kinda afraid of what'll happen if I remember all of it."

        scene 04_parkquesticecream_13_ch
        with dissolve

        p "You're such a downer, [mx]! \nYou've been given another chance of life!"
        p "And remembering your memories isn't that bad... \nEspecially the promise we made..."

        mx "The promise—"

        "{i}*drip* {w=0.2} *drip*{/i}"

        p "Hm..?"

        scene 04_parkquesticecream_15_ch

        p "M-My ice cream's starting to melt!" with vpunch
        p "Nooo! It's dripping!"
        p "{i}*slurp*! {w} *slurp!* {w} *slurp!*"
        p "Hyoo shood esh owrs shoo! \n{i}(You should eat yours too!){/i}"

        mx "Oh crap!"

        jump ep2_pquest_parkquest_finishing_end

    if pquest_parkquest_icecream_strawberry == True:

        scene 04_parkquesticecream_12_sb
        with fade

        p "This is nice, isn't it?"

        mx "Yeah. \nIt's refreshing here, a bit calming too."

        p "It's the water splashing and the sound it makes that does it!"

        mx "I kinda see that now."

        p "So, how do you feel about our day so far?"

        mx "Honestly? {w} I'm actually having fun. {p} I thought {i}\"recreating memories\"{/i} would be much more complicated than this."

        p "Well, why would it be? {p} All we did in the past is play and eat ice cream here!"
        p "We were just kids after all."

        mx "... {w} You know, you're right Prii. {p} Maybe I was thinking too much into this, huh?"

        p "That's why I'm the one making the plans and you're the guinea pig!"

        mx "Ahahaha! Aren't you the cutest little runt?"

        p "Bleh~"

        mx "So, how's it with that thing you wanted to remember?"

        scene 04_parkquesticecream_13_sb
        with dissolve

        p "Well... {w} I think I'm getting the gist of it? {p} But nothing solid as of yet."
        p "I think talking with Mr. Negasi helped a lot to clear some of it! {p} More importantly, how about you though?"

        scene 04_parkquesticecream_14_sb
        with dissolve

        p "This is {i}\"Get [mx]'s Memory Back\"{/i} mission after all..."

        mx "Still no dice. {p} Just... nothing"

        "(If I actually did remember something, that'll be a really scary thing.)"

        p "Oh..."

        mx "Cheer up! \n It's not like I'm gonna turn back to my old self in a snap."
        mx "Speaking of which, I was wondering how I was before all of this happened?"
        mx "From the small bits I noticed, I think I was more of a douchebag?"

        scene 04_parkquesticecream_13_sb
        with dissolve

        p "What!? No you weren't! You were just... {p} Well, you were really difficult."
        p "When I heard you moved back to the city... {p} I tried asking around."
        p "I learned that you were enrolled in the same university I'm attending."

        mx "Wait. I'm still attending school? {p} Am I still enrolled?"

        p "Yeah, silly!"
        p "We're still in {i}spring break{/i} so you have a bit of time to talk with them about your \"situation\"."
        p "I also heard of rumors that you weren't exactly the cooperative kind..."

        "(Ugh! This kid is still in school!?)"
        "(I should try going there and solving the problem after the break is over.)"
        "(His problem is gonna be my problem too.)"

        mx "I'm starting to think I was not that great of a person to be around with?"

        scene 04_parkquesticecream_14_sb
        with dissolve

        p "W-Well, uhh, I admit you were hard to talk to when I finally talked with you..."
        p "It seems you've changed completely. {p} You were really stubborn about accepting help from us."
        p "B-But you're here now, right? \nThat's progress too?"

        mx "Yeah but it took me losing my memories to even accept it. {p} Now, I'm kinda afraid of what'll happen if I remember all of it."

        scene 04_parkquesticecream_13_sb
        with dissolve

        p "You're such a downer, [mx]! \nYou've been given another chance of life!"
        p "And remembering your memories isn't that bad... \nEspecially the promise we made..."

        mx "The promise—"

        "{i}*drip* {w=0.2} *drip*{/i}"

        p "Hm..?"

        scene 04_parkquesticecream_15_sb

        p "M-My ice cream's starting to melt!" with vpunch
        p "Nooo! It's dripping!"
        p "{i}*slurp*! {w} *slurp!* {w} *slurp!*"
        p "Hyoo shood esh owrs shoo! \n{i}(You should eat yours too!){/i}"

        mx "Oh crap!"

        jump ep2_pquest_parkquest_finishing_end

    if pquest_parkquest_icecream_bubblegum == True:

        scene 04_parkquesticecream_12_bb
        with fade

        p "This is nice, isn't it?"

        mx "Yeah. \nIt's refreshing here, a bit calming too."

        p "It's the water splashing and the sound it makes that does it!"

        mx "I kinda see that now."

        p "So, how do you feel about our day so far?"

        mx "Honestly? {w} I'm actually having fun. {p} I thought {i}\"recreating memories\"{/i} would be much more complicated than this."

        p "Well, why would it be? {p} All we did in the past is play and eat ice cream here!"
        p "We were just kids after all."

        mx "... {w} You know, you're right Prii. {p} Maybe I was thinking too much into this, huh?"

        p "That's why I'm the one making the plans and you're the guinea pig!"

        mx "Ahahaha! Aren't you the cutest little runt?"

        p "Bleh~"

        mx "So, how's it with that thing you wanted to remember?"

        scene 04_parkquesticecream_13_bb
        with dissolve

        p "Well... {w} I think I'm getting the gist of it? {p} But nothing solid as of yet."
        p "I think talking with Mr. Negasi helped a lot to clear some of it! {p} More importantly, how about you though?"

        scene 04_parkquesticecream_14_bb
        with dissolve

        p "This is {i}\"Get [mx]'s Memory Back\"{/i} mission after all..."

        mx "Still no dice. {p} Just... nothing"

        "(If I actually did remember something, that'll be a really scary thing.)"

        p "Oh..."

        mx "Cheer up! \n It's not like I'm gonna turn back to my old self in a snap."
        mx "Speaking of which, I was wondering how I was before all of this happened?"
        mx "From the small bits I noticed, I think I was more of a douchebag?"

        scene 04_parkquesticecream_13_bb
        with dissolve

        p "What!? No you weren't! You were just... {p} Well, you were really difficult."
        p "When I heard you moved back to the city... {p} I tried asking around."
        p "I learned that you were enrolled in the same university I'm attending."

        mx "Wait. I'm still attending school? {p} Am I still enrolled?"

        p "Yeah, silly!"
        p "We're still in {i}spring break{/i} so you have a bit of time to talk with them about your \"situation\"."
        p "I also heard of rumors that you weren't exactly the cooperative kind..."

        "(Ugh! This kid is still in school!?)"
        "(I should try going there and solving the problem after the break is over.)"
        "(His problem is gonna be my problem too.)"

        mx "I'm starting to think I was not that great of a person to be around with?"

        scene 04_parkquesticecream_14_bb
        with dissolve

        p "W-Well, uhh, I admit you were hard to talk to when I finally talked with you..."
        p "It seems you've changed completely. {p} You were really stubborn about accepting help from us."
        p "B-But you're here now, right? \nThat's progress too?"

        mx "Yeah but it took me losing my memories to even accept it. {p} Now, I'm kinda afraid of what'll happen if I remember all of it."

        scene 04_parkquesticecream_13_bb
        with dissolve

        p "You're such a downer, [mx]! \nYou've been given another chance of life!"
        p "And remembering your memories isn't that bad... \nEspecially the promise we made..."

        mx "The promise—"

        "{i}*drip* {w=0.2} *drip*{/i}"

        p "Hm..?"

        scene 04_parkquesticecream_15_bb

        p "M-My ice cream's starting to melt!" with vpunch
        p "Nooo! It's dripping!"
        p "{i}*slurp*! {w} *slurp!* {w} *slurp!*"
        p "Hyoo shood esh owrs shoo! \n{i}(You should eat yours too!){/i}"

        mx "Oh crap!"

        jump ep2_pquest_parkquest_finishing_end

label ep2_pquest_parkquest_finishing_end:

    scene 04_parkquesticecream_16
    with slowfade

    p "{i}*shlurp* {w} *shlurp*{/i}"

    mx "Wow! It never ceases to amaze me you can make food disappear like that since we went to the diner."
    mx "You have a particular set of skill, Prii."

    p "Eh?"

    scene 04_parkquesticecream_17
    with dissolve

    p "B-Because it was melting! I told you I should've finished it back then!"
    p "We ended up talking for a while which started to melt..."
    p "Y-You were the one who started it! "

    mx "Alright, alright! {p} Now that I think about it..."
    mx "You could also add a bit of fiber and vegetables to your diet."

    scene 04_parkquesticecream_18
    with dissolve

    p "Veggies? {p} Ugh! I hate eating them! {i}Sensei{/i} always tells me to do do that too!"

    mx "Sensei?"

    p "My Karate sensei! \nI said I did Karate, y'know!"

    mx "Exactly! It's part of a healthy diet for building muscles!"
    mx "Especially for burning a large amount of fat!"

    "(Err, that's quite hypocritical of me when I didn't do anything to lose a single digit of fat in my old life.)"
    "(I think this buffed body is rubbing off on my consciousness too.)"

    p "Did you...{w}did you call me fat?"

    mx "What..?"

    scene 04_parkquesticecream_19

    p "HMPH!" with hpunch
    p "First, you pushed me off the swings really hard! {p} Then you told me to eat veggies and now..."
    p "You're calling me fat!"

    mx "N-No! Uh.. well... {p} Some of it are true but the last one is quite stretching it a bit..."

    p "HMPH!" with hpunch

    scene 04_parkquesticecream_20
    with fade

    $ renpy.music.stop(channel='music2', fadeout=5)

    mx "P-Prii, hold on!"

    p "{i}\"Get [mx]'s Memory Back: Numero Dos\"{/i} is canceled because [mx] is an {i}El Doodoo head!"

    mx "{i}\"El Doodoo head?\""

    p "That's Spanish for you're a Doodoo head!"

    mx "W-What? \nI mean, \"El\" isn't exactly gonna—"

    p "HMPH! \nStill a meanie!"
    p "I'm leaving!"

    mx "W-Wait! Prii!"

    stop sound fadeout 3.0

    $ story_music_ongoing = False

    $ time = 3
    $ pquest_parkquest_finish = True

    scene park_evening_entrance
    with fade

    "(She won't talk to me after what happened.)"
    "({i}*sigh*{/i}) {p} (It's getting late, we better go back home.)"

    if notification_songs == True:
        $ renpy.notify("BROCKBEATS - september")

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button
    show screen map_button

    jump citypark

label ep2_pquest_parkquest_finish:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button
    hide screen map_button

    scene 04_parkquesticecream_21
    with fade

    mx "Well, here we are at last..."

    p "Hmph! {p} Meanie! {w} Meanie!"

    mx "Look, I'm sorry about what happened."
    mx "I'll do you a favor next time, alright?"

    scene 04_parkquesticecream_22
    with dissolve

    p "Hmmm... {p} ...really?"

    mx "Yeah. Trust me."

    p "Hnnnng...."
    p "Even if I want to go somewhere dark and scary at night?"

    mx "Umm, isn't that dangerous..?"

    p "...."

    mx "Yes. That too."

    scene 04_parkquesticecream_23
    with dissolve

    p "Fine. That'll do! {p} I'm not angry anymore!"
    p "But if you call me names again I'll never talk to you..."

    mx "Yes, yes. \nI learned my lesson."

    p "Ehehe~ {p} Well, despite what you did, I still enjoyed the trip to the park."
    p "I'm gonna go clean up myself now."

    $ pquest_parkquest_finish = False
    $ pquest_parkquest_complete = True
    $ story_ongoing_priscilla = False
    $ map_time_skip = True

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    scene ground_floor_evening
    with fade

    jump ground_floor_hallway



label ep2_pquest_beachfun:

    $ pquest_beachfun = False
    $ pquest_beachfun_clothchange = True
    $ story_ongoing_priscilla = True
    $ map_time_skip = False

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button
    hide screen map_button

    scene kitchen_morning

    show 03_beachfun_idle

    $ renpy.music.stop(channel='music3', fadeout=3)

    "(What's Prii doing here this early in the morning?)"
    "(I better check what's up.)"

    mx "Mornin' Prii!"

    scene 01_beachfun_01
    with dissolve

    if notification_songs == True:
        $ renpy.notify("BROCKBEATS - frills & flowers")

    $ renpy.music.play("music/BROCKBEATS-frills & flowers.mp3", channel='music2', fadein=2, loop=True)

    $ story_music_ongoing = True

    mx "What's that big hat you're holding there?"

    p "Good morning. {p} This old thing? It's my old sun hat I found in the bathroom a few minutes ago."

    mx "A sun hat?"

    p "Well, if you didn't notice already... I'm a redhead. {p} Mr. Sun and I aren't really the bestest of friends."

    mx "Ah, I see."

    p "I've bought this a long time ago and haven't used it lately... {p} I just didn't had the time to go to the beach."

    mx "The beach, huh? {p} So, is that the next stop for {i}\"Get My Memory Back\"{/i}?"
    mx "I don't know if I have any \"beach\" clothes in my closet..."

    p "Next mission? {p} Oh no! I wasn't planning to go to the bea—"

    scene 01_beachfun_02
    with dissolve

    p "Wait a minute!"
    p "A mission on the beach..?"

    mx "Oh? So, it wasn't part of the plan? {p} Then we can just stay here—"

    p "Why didn't I think of that!" with hpunch
    p "{i}\"Get [mx] Memory Back: Number 3\"{/i} is still ongoing, y'know! {p} We now have a reason to go there!"

    mx "We do?"

    scene 01_beachfun_03
    with dissolve

    p "We still have to make you recover your memories, [mx]!"
    p "And I can finally wear this sun hat after all this time! Ooh! With my sun dress too!"

    mx "Okaaaay.... \nI see, this is the other kind of \"mission\"."
    mx "Operation: {i}\"Prii uses a vulnerable amnesiac man to play around and act as her servant\"."

    p "Hey! You're not being grateful for this, Mr. Guinea Piggy! {p} Where's your scientific spirit!"

    mx "I forgot this was also a {i}\"science experiment\"{/i}. {p} Whatever exactly that means in this scenario..."

    scene 01_beachfun_04
    with dissolve

    p "We still need to prepare a lot of things! {p} The sunscreen! The parasol! The list goes on!"
    p "Oh yeah! {p} We could also ask Mama to join us!"

    mx "Are you sure she'll join us with such short notice?"

    p "Of course she will! {p} She could also drive us there!"
    p "She's been itching to go to the beach for quite some time too!"
    p "The more the merrier as they say!"

    scene 01_beachfun_05
    with dissolve

    p "So, you better hurry it up and change!"

    mx "What kind of clothes?"

    p "A tank top and shorts would do fine! {p} You could even borrow one of my bikinis too! Ehehe~"

    mx "Tank top and shorts it is!"

    p "Alright! That settles it! {p} We're going to the beach!"

    scene kitchen_morning
    with fade

    p "Mama! We're going to the beach today with [mx]!"

    f "Today? Like this very morning? {p} Sure! I'll go get ready in a few minutes!"

    "(Well, that took no time at all.) {p} (I should better go change at my room too.)"

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump kitchen

label ep2_pquest_beachfun_leaving:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button
    hide screen map_button

    $ pquest_beachfun_leaving = False
    $ pquest_beachfun_start = True
    $ pquest_beachfun_start_car = True

    scene 01_beachfun_07
    with dissolve

    p "Well, look who decided to be fashionably late?"

    "(Huh? I was the one actually late? That's surprising.) {p} (Well, you could never underestimate both of these girl's thirst for adventure.)"

    mx "Well, as they say, better late than not be fashionable!"

    p "Ehehe~ that's such a cheesy line, [mx]!"

    mx "Sorry for roping you with our antics, Fiona."

    f "It's alright, dear. \nI'm quite experienced with Prii's sudden burst of... excitement."
    f "Also, I'd be lying if I wasn't thrilled with the notion of going to the beach."

    mx "I see. I was just shocked how fast you two have got all of your things prepared already."

    p "Us Fitzgeralds are always ready for adventure, [mx]!"

    f "Both of us rarely go to the beach these days unless for special occasions."
    f "So, we've prepared a \"emergency beach essentials\" in case someone invites us to the beach."

    p "It's like doomsday rations except for the beach! {p} The struggles of us redheads, y'know!"

    mx "Quite, uh, a very interesting scenario."

    scene 01_beachfun_08
    with dissolve

    f "We could talk all day but we really should start to get going. {p} The sun won't wait for us."

    p "Oh, you've brought sunscreen right, [mx]?"

    mx "Should I? {p} I don't think I have any."

    f "Of course, dear! {p} You'll be red as an apple if you don't apply any."
    f "But don't worry, I always bring one with me here."
    f "Now, shall we go?"

    scene ground_floor_morning
    with fade

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump ground_floor_hallway

label ep2_pquest_beachfun_leaving_car:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button
    hide screen map_button

    scene neighborhood_morning
    with fade

    f "Wait a minute here, you two."
    f "I'll go get the the car."

    scene black
    with fade

    $ renpy.music.stop(channel='music2', fadeout=7)

    f "Now, let's go to the beach alright?"
    p "Ready!"

    $ beach_unlock = True
    $ pquest_beachfun_start_car = False

    jump ep2_pquest_beachfun_start

label ep2_pquest_beachfun_start:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button
    hide screen map_button

    $ time = 2

    scene 01_beachfun_09
    with fade

    pause

    p "It's the beach!"

    if notification_songs == True:
        $ renpy.notify("J Bliz - paradise.mp3")

    $ renpy.music.play("music/jbliz_paradise.mp3", channel='music1', fadein=2, loop=True)

    p "Look [mx]! \nBoats!"

    mx "To be precise, those are sailboats. {p} Emphasized by their sails which they use to move."

    p "You know, for someone who lost their memories, you sure do know a lot of boring stuff."

    mx "Just saying."

    p "Whatever! They're floaty mcfloats with curtains!"

    f "Okay, let me look for a parking spot over there."

    scene black
    with fade

    pause 0.5

    scene 01_beachfun_10
    with fade

    p "Yay~ {p} We're here!"

    f "Sorry for making you carry my stuff, dear."

    mx "Don't be. \nIt's embarrassing for me to not even offer help."

    p "Yeah, don't worry about him, Mama! {p} Look, how tough he is!"

    "{i}*punch!*" with hpunch

    mx "Ow! That hurt, Prii!"

    p "Ehehe~ Sorry! \n But see, he's tough as a sack of potato!"

    scene 01_beachfun_11
    with dissolve

    f "Ah, {i}Puesta de Sol{/i} beach..."
    f "I already feel my stress lifting from looking at it."

    p "Oh, it's so blue!"
    p "Mama, how about we play together at the beach later?"

    f "I'm sorry, Prii. {p} I want to relax by the seaside and enjoy the breeze."
    f "Too much exposure is bad for our skin."

    p "Eeh? That's boring adult stuff! {p} It's the beach! Swimming is a must!"

    f "What about you, [mx]? {p} What do you plan to do?"

    mx "I'll wait and see."

    "(Prii already forgot her reason for coming here.)"
    "(Well, that {i}\"reason\"{/i} is more of an excuse to hangout really.)"

    p "Too much talk! \nLet's go down already!"

    scene beach_afternoon_promenade
    with fade

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump beach

label ep2_pquest_beachfun_tochangingcabins:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button
    hide screen map_button

    $ pquest_beachfun_start = False

    scene beach_afternoon_seaside
    with fade

    pause 0.3

    p "Here I come—"

    f "Slow down, young lady! {p} You're still wearing your dress."

    p "O-Oh, right."

    scene 01_beachfun_13
    with dissolve

    p "But the beach looks really nice isn't it?"

    f "Yeah, I know but you shouldn't dive straight in. "
    f "Don't you remember what happened years ago? Do you want to be called {i}\"tomato-face\"{/i} again?"

    p "N-Nooo~"

    f "Precisely! {p} Anyways, it looks like there are only a handful of people here."

    p "Oh! Which means we can have the beach to ourselves!"
    p "I can swim as much as possible!"

    f "On that note..."

    scene 01_beachfun_12
    with dissolve

    f "[mx], sorry but we're gonna leave you here for a while."
    f "We'll go ahead to the changing cabins and switch to our swimsuits."

    p "And no peeking!"

    mx "W-What? {p} I didn't even have any plans to begin with!"

    scene 01_beachfun_14
    with dissolve

    f "Ahahaha! Don't tease him like that, Prii."
    f "[mx]'s still a growing young man, right?"

    mx "{i}...*cough*..."

    p "You can just guard our things here then, [mx]."

    f "Oh, maybe you can check the Cafe over there a bit."

    p "But our stuff is priority alright?"

    mx "Okay, okay! \nBetter hurry and change."

    scene beach_afternoon_seaside
    with fade

    mx "Well, I didn't have plan to peek before but after however..."
    mx "Should I?"

    menu:
        "A \"little\" peek won't hurt.":

            $ pquest_beachfun_beachchange = True
            $ pquest_beachfun_beachchange_fin = False

            "(The carnal desires win.)"
            "(I think the changing cabins were to the left of here?)"

            scene beach_afternoon_seaside
            with fade

            show screen calendar_time
            show screen calendar_week
            show screen inventory_button

            jump beach_seaside_triggers
        "A stroll around the beach sounds nice.":


            "(Maybe I'll walk around the beach and feel the breeze...)"
            "(Now, maybe I could find one of those small crabs loitering here...)"

            scene black
            with slowfade

            show text "{size=36}{color=#A9A9A9} ( A few minutes later... ) {/color}{/size}" at truecenter with dissolve

            pause

            jump ep2_pquest_beachfun_play

label ep2_pquest_beachfun_changingcabinspeek:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene beach_afternoon_cabins
    with fade

    pause 0.3

    mx "(So, which cabin among these is Prii and Fiona changing?)"
    mx "(Hm, maybe I should go around the back check it one by one?)"

    scene 02_beachfun_change_peeking
    with fade

    "(Hmm...) {p} (Found them!)"
    "(Looks like both of them are just starting to change.)"
    "(Unfortunately, they're both on the opposite sides.)"
    "(I could only see one of them at a time.) {p} (Which one should I check out?)"

    menu:
        "Fiona.":

            $ pquest_beachfun_beachchange = False

            jump ep2_pquest_beachfun_changingroom_fiona
        "Priscilla.":


            $ pquest_beachfun_beachchange = False

            jump ep2_pquest_beachfun_changingroom_priscilla

label ep2_pquest_beachfun_changingroom_fiona:

    scene 02_beachfun_change_fiona_01
    with fade

    "(Jackpot! Just in time.)"
    "(I should stay quiet unless I want to be found out.)"

    f "How long has it been I've been back here?"
    f "Almost 8 years, I think?"

    scene 02_beachfun_change_fiona_02
    with dissolve

    f "I've been busy with my job."
    f "It's great to be able to relax for awhile, I guess."

    scene 02_beachfun_change_fiona_03
    with dissolve

    f "Hmm? \nWhere did I put that swim wear on?"
    f "Let's see..."

    scene 02_beachfun_change_fiona_04
    with dissolve

    f ".{w}.{w}."
    f "Here it is! {p} I hope it fits! I didn't bring any backup."
    f "But it's worth it!"

    scene black
    with fade

    pause

    scene 02_beachfun_change_fiona_05
    with fade

    f "This is an exact replica of Adelaide's bathing suit from her debut movie from the 60s!"
    f "That scene where in Fabio approaches her and puts sunblock on her back on the beach is..."
    f "Ehehe~ I always wanted to feel like a movie star!"
    f "Maybe I could ask [mx] to do that scene too—"
    f "Oh no! I should hurry back! {p}I hope [mx] didn't wait for too long!"

    scene 02_beachfun_change_peeking
    with fade

    mx "She's done! {p} I think Priscilla is starting to get out too."
    mx "Putting sunblock on Fiona's back, huh?"
    mx "I should hurry back too..."

    $ pquest_beachfun_beachchange_fin = True

    scene black
    with fade

    scene beach_afternoon_cabins
    with fade

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump beach_cabins_triggers

label ep2_pquest_beachfun_changingroom_priscilla:

    scene 02_beachfun_change_priscilla_01
    with fade

    p "Uwaa~"
    p "It's so bright in here!"

    scene 02_beachfun_change_priscilla_02
    with dissolve

    p "I also need to change fast..."
    p "Just a couple minutes in and I'm sweating this much."
    p "I want to hurry and go for a swim already!"

    scene 02_beachfun_change_priscilla_03
    with dissolve

    p "{i}*phew*"
    p "Now, where did I put my swimsuit again?"
    p "Uhh.. {p} I hope I didn't forget it."
    p ".{w}.{w}."

    scene 02_beachfun_change_priscilla_04
    with dissolve

    p "Found it!"
    p "Let me put this on..."
    p "I'm glad I bought this with Hyuna when we were shopping together!"
    p "I can finally wear it!"

    scene black
    with fade

    scene 02_beachfun_change_priscilla_05
    with fade

    p "There! {p} It looks cute especially the little cover!"
    p "I hope [mx] likes it! {p}I wonder if he'll join with me at the beach?"
    p "I should hurry! I don't want him to wait too long."

    scene 02_beachfun_change_peeking
    with fade

    mx "She's done! {p} I think Fiona is starting to get out too."
    mx "Swimming with Prii, huh?"
    mx "I should hurry back too..."
    $ renpy.end_replay()
    $ pquest_beachfun_beachchange_fin = True

    scene black
    with fade

    pause

    scene beach_afternoon_cabins
    with fade

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump beach_cabins_triggers

label ep2_pquest_beachfun_play:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene 02_beachfun_changefin_01
    with fade

    p "Mama, isn't that swimsuit the one in that old movie you love? {p}Isn't that a bit outdated?"

    f "Outdated? Oh Prii, that's why you're still a child.{p}This is what's called a \"timeless classic\"."

    p "H-Hey! I'm just saying you could, y'know... {p}Wear more modern stuff."

    f "Well, if you want me to wear more of that then I'll start cooking more veggie based foods?"
    f "How about I serve a delicious salad for breakfa—"

    p "Noooooo! {p}I-I take it back! That swimsuit looks amazing!" with vpunch
    p "You don't have to change anything!"

    f "{i}*smirk*"

    mx "Oh, looks like you two are ready?"

    scene 02_beachfun_changefin_02
    with dissolve

    p "[mx]!"
    f "[mx], dear."

    p "We were looking for you! \nWhere'd you go?"

    mx "Uh, I was strolling around the beach..."
    mx "I was looking for, umm, some crabs?"

    p "Crabs? Did you find one?"

    mx "W-Well, not really, no."

    f "Oh? Then have you visited the Cafe over there?"
    f "I heard they're finally serving alcoholic drinks come evening."

    mx "A Cafe serving alcohol, huh?"

    p "Hey! Enough talking! Let's go to the beach already!" with vpunch

    scene 02_beachfun_changefin_01
    with dissolve

    p "Mama, are you still gonna stay here? {p}You don't want to join me for a swim?"

    f "I'm fine staying on the shore, dear.{p}Enjoying the sea breeze and the sound of the wind is enough."

    p "Ehh, sounds boring. {p}Well, I'll go for a swim first!"

    scene 02_beachfun_changefin_02
    with dissolve

    p "You should join me too, [mx]!"
    p "I want to find starfishes!"

    f "I should also set up the parasol and towel over there."
    f "Come join me too [mx] if you have time..."

    scene black
    with fade

    scene beach_afternoon_seaside
    with fade

    "(Looks like both of them has their own things to do...)"
    "(Now, who should I join?)"

    menu:
        "Hang out with Fiona on the Beach.":


            $ pquest_beachfun_beachchange_fin = False

            scene black
            with fade

            jump ep2_pquest_beachfun_play_fiona
        "Hang out with Priscilla in the Sea.":


            $ pquest_beachfun_hangout_prii = True
            $ pquest_beachfun_beachchange_fin = False

            scene black
            with fade

            jump ep2_pquest_beachfun_play_priscilla

label ep2_pquest_beachfun_play_fiona:

    scene 02_beachfun_fionapath_01
    with fade

    f "{i}...hum...dum...hum..."
    f "It's so peaceful and beautiful out here."
    f "I should take more breaks like this every once in a while..."

    scene 02_beachfun_fionapath_02
    with dissolve

    f "{i}*sigh*{/i}{p}The client this time is such a bitch."
    f "Too much this and that. {p}{i}\"Oh, I wanted lace! This is too tight! Scrap that, I like this color more!\"{/i}"
    f "Argh! I don't want to even think about her! {p} {i}*breathe in* {w} *breathe out*"

    mx "If you breathe in that hard, you'd suck out the surrounding sand."

    scene 02_beachfun_fionapath_03
    with dissolve

    f "[mx]?"
    f "I was just, uh, \"meditating\" away my frustrations."
    f "What brought you to this part of town, hm?"
    f "I thought you'd be swimming with Prii right now?"

    mx "Well, Prii ran off and swam far away before I could approach her."
    mx "I thought I could get some of that \"meditation\" for myself too."

    f "Oh? Ehehe~"

    scene 02_beachfun_fionapath_04
    with dissolve

    f "You're welcome to enjoy the scenery here with me, if you like?"
    f "A good view like this is to be enjoyed with good company, y'know?"

    mx "Well, don't mind if I do?"
    mx "But isn't it a waste of swimwear if you don't atleast take a dip?"

    f "Well..."

    scene 02_beachfun_fionapath_05
    with dissolve

    f "You only get to be young once and the Sun isn't helping with that."
    f "Women get conscious of that, y'know?{p}Prii's enjoying her youth right now."
    f "I'm kinda jealous of it too...{p}That's why this sunblock here is—Hm?"
    f "Um, [mx] c-can you help me out a bit?"

    mx "Sure? What is it?"

    f "Can you get that sunblock over there first?"

    scene 02_beachfun_fionapath_06
    with fade

    mx "What do you want me to do with this?"

    f "Um, well, could you help me with applying that on my back?"

    mx "Are you... sure?"
    mx "I mean, I could get Prii—"

    f "N-No! U-Uh, I mean...{p}She'll just get angry with you if interrupt her fun." with vpunch

    mx "Oh, I see..."

    scene 02_beachfun_fionapath_07
    with dissolve

    mx "Well, where should I start first?"
    mx "Should I start on the shoulders or on the bottom?"

    f "Just start from the shoulders and down my back."

    mx "Then excuse me... \nI'm inexperienced with this after all."

    f "Oh, you've never touched another woman like this before?"

    scene 02_beachfun_fionapath_08
    with dissolve

    mx "W-What? N-Not that I remember... {p}I'm amnesiac, y'know?"
    mx "I don't even know if I did or did not do \"it\" with someone before..."

    f "Oh? So you're technically still a virgin?"

    mx "H-Hey! I've probably had a woman or two—"

    f "At applying sunblock.{p}What did you think I was implying, hm?"

    mx "N-Nothing! \nI was, um, uhh, also meant, uh, a-applying sunblock too!"

    scene 02_beachfun_fionapath_09
    with dissolve

    f "Oh no! How could I forget? {p}I'm such a ditz..."

    mx "W-What are you doing, Fiona?"

    f "Well, isn't it silly of me to have my top on if you're gonna apply sunblock?"
    f "How would you apply it on my entire body?"

    mx "You n-never said anything about your body?"

    scene 02_beachfun_fionapath_10
    with dissolve

    f "Oh? I didn't? Well, I just did now. Ehehe~"
    f "So, apply it on every nook and cranny alright?"

    mx "Uh, {i}*gulp*{/i}"

    f "[mx]... You're not getting embarassed, are you?"
    f "It's just you applying a little sunblock, isn't it?"
    f "Unless you're thinking some other {i}naughty{/i} thoughts? Ehe~"

    mx "I-I'm not!"

    scene 02_beachfun_fionapath_11
    with dissolve

    mx "From the shoulders down to just the base of your back, r-right?"

    f "My, my! Why are your hands shaking that much? {p}Slow down a bit, will you?"

    mx "I-Isn't it better for me to do this quickly?"

    f "Well, if you want to do it much quicker then I'll—"

    scene 02_beachfun_fionapath_12

    f "Help you with that?"

    mx "F-Fiona!" with hpunch

    f "My waist gets hit more of those nasty UV rays, y'know?"
    f "You don't want me to getting sunburnt now, would you?"

    mx "B-But isn't this a bit.. too risque?"

    f "Risque? I think it's still not enough coverage?"

    scene 02_beachfun_fionapath_13
    with dissolve

    f "Here! You could get a \"handful\" of coverage if you apply more here." with vpunch

    mx "{i}*gulp*{/i} {p}This is bad if I'm seen like this especially by Prii!"
    mx "It doesn't look like I'm just applying sunblock?"

    f "Oh, look at around us.{p}There isn't a soul in sight."
    f "You're just... {w}applying some... {w}sunblock innocently..."

    mx "{i}*gulp*{/i}" with vpunch
    mx "Uh, umm..."

    p "[mx]! Help! M-My, my..." with vpunch

    scene 02_beachfun_fionapath_14
    with dissolve

    f "Was that Prii?"

    mx "Oh no! M-Maybe she got caught up with something?"
    mx "I-I-I s-should go, Fiona."

    f "Well, alright.{p}You've done more than enough."

    scene 02_beachfun_fionapath_15
    with fade

    f "Phooey! {p}I wanted to tease him more!" with vpunch
    f "He acted like Fabio did at the movie too! \nFlustered and embarassed!"
    f "{i}Teehee~"
    f "Hm? It's starting to get late.{p}Maybe a trip to that cafe, would be nice?"

    scene black
    with fade

    pause

    scene 02_beachfun_fionapath_16
    with fade

    p "Hnngguuo~"
    p "This is my fault for playing too much."
    p "I should've not went diving that far to see Mr. Starfish..."

    mx "Prii! {p}Are you alright?"
    mx "I heard you screaming?"

    scene 02_beachfun_fionapath_17
    with dissolve

    p "[mx]!"

    mx "What happened?"

    p "W-Well, you see I saw a big blue starfish near some corals so I decided to take a look a bit closer..."
    p "It was very pretty! But it was hiding in some corner so I went closer and found a family of them!"
    p "But then I realize it was getting darker so I came back up b-but my bra got hooked on some corals and then..."
    p "I-It was already too late!"

    mx "{i}Whew!{/i} I thought you got hurt by something.{p}I'm glad that you're safe."
    "(Well, atleast I got to escape Fiona.)"
    "(I know I'm a pervert and all but that was too much exhibition even for me.)"
    mx "It seems we had quite... an adventure today, huh?"

    p "Y-Yeah... {p}But what do I do now? My top's gone."

    mx "You still have your clothes you wore this morning right?"

    scene 02_beachfun_pathfin_f_01
    with fade

    $ renpy.music.stop(channel='music1', fadeout=6)
    $ renpy.music.stop(channel='nature', fadeout=1)

    $ renpy.music.play('soundfx/ambience_pm_beach.ogg', channel='nature', loop=True, fadeout=0.4, fadein=0.4, tight=None, if_changed=True)

    p "Uh-huh! I left my sundress around the changing cabins."

    mx "Then let's go there!"

    scene beach_evening_seaside
    with fade

    if notification_songs == True:
        $ renpy.notify("Desired - Secret Senshi")

    $ renpy.music.play("music/desired_secret_senshi.mp3", channel='music2', fadein=7, loop=True)

    $ pquest_beachfun_beachchange_tankon = True
    $ pquest_beachfun_priichange = True
    $ time = 3

    jump beach_seaside_triggers

label ep2_pquest_beachfun_play_priscilla:

    scene 02_beachfun_priscillapath_01
    with fade

    p "[mx]!"
    p "You're late again! {p}I was about to swim and search for some starfish!"
    p "You want to join me?"

    mx "Uh, I... I can't swim. {p}It seems I forgot that part too?"
    "(Well, in reality, I haven't swam since I was a little kid.)"
    "(I don't even know how to float anymore let alone swim.)"

    p "Awww..."

    scene 02_beachfun_priscillapath_02
    with dissolve

    p "Hm? If that's the case... {p}What should we do?"

    mx "Looks like Fiona's having a time of her day relaxing over there?"
    mx "Maybe we could do the same?"

    p "Nuh-uh! That's boring! We're at the beach after all! {p}We're surrounded by the sea!"

    mx "Then what?"

    p "Well, how about something like..."

    scene 02_beachfun_priscillapath_03

    play sound "soundfx/splash.ogg"

    "{i}*splash*" with hpunch

    p "This!"
    p "Ahahaha!"

    mx "H-Hey! {p}That's cheating! I wasn't ready!"

    p "No way, slowpoke!"
    play sound "soundfx/splash.ogg"
    p "{i}Hiya! Take this! Anotha' one!"
    p "Ehehehe~"

    scene 02_beachfun_priscillapath_04
    with dissolve

    mx "Slowpoke? Me?{p}Alright then!"

    play sound "soundfx/splash.ogg"

    "{i}*splash*" with hpunch

    p "H-Hey! I-I wasn't ready!"

    mx "Who's the slowpoke now, huh?"

    p "Still you!"

    play sound "soundfx/splash.ogg"

    "{i}*splash*" with hpunch

    p "Ahahaha~"

    mx "Well, here's a big one for you then!"

    p "W-W-Wha—"

    play sound "soundfx/splash.ogg"

    scene 02_beachfun_priscillapath_05
    with vpunch

    mx "Prii!"

    p "Ah! [mx]! You meanie~"

    play sound "soundfx/splash_heavy.ogg"

    scene black
    with fade

    scene 02_beachfun_priscillapath_06
    with fade

    p "O-Owie..."
    p "Hmph! [mx]! You didn't had to be that aggressive!{p}We're just playing you big bully!"

    mx "I'm sorry I—"
    mx "Uh... {i}oh{/i}."

    p "Hm? What're you going silent for..?"
    p "Down?"

    scene 02_beachfun_priscillapath_07
    with dissolve

    p "..."

    pause

    p "{b}EEEEEEEEEEEEKKK!!{/b}" with vpunch
    p "{i}W-W-W-W-Where's my bikini top!?{/i}"

    scene 02_beachfun_priscillapath_08
    with dissolve

    p "Huhu~{i}*sniff*{/i}!"
    p "Not again! {p}Where did it go?"
    p "How could I go back to—Wait!"

    scene 02_beachfun_priscillapath_09
    with dissolve

    p "[mx]!"

    mx "H-Huh?"

    p "This is all your fault and-and..."
    p "Y-Y-You saw them, didn't you!?" with vpunch

    mx "I, uh, umm... {p}T-The circumstance dicatates that I didn't intend—"

    p "{i}Pervert! Deviant! Lecher!" with vpunch

    mx "H-Hey! It was an a-accident! {p}I didn't m-mean to see it!"

    p "{b}HMPH!{/b}" with vpunch
    p "Argh! J-Just quickly turn around!"

    scene 02_beachfun_priscillapath_10
    with dissolve

    mx "Here? Happy now?"

    p "If you peek, I'll punch you hard!"
    p "I did Karate, y'know!"

    mx "I'm not going to, alright?"

    p "You're also forbidden thinking indecent thoughts!"

    mx "Wha? {p} I mean, uh, sure! Okay!"
    mx "No perverted thoughts here!"

    p "Luckily, my Sunhat didn't get lost too!"

    scene 02_beachfun_priscillapath_11
    with dissolve

    mx "Woah!" with vpunch

    p "I-I said don't turn around!"
    p "You're my cover! I don't want to get seen by others!"

    scene 02_beachfun_priscillapath_12
    with dissolve

    mx "P-Prii! Your—"

    p "If I don't stick close to you, other people might take a peek!"
    p "You have take responsibility!"

    mx "I do! But...{p}Do you have to stick close to me like this?"

    p "W-Well, I really don't want to but the Sun's hot!"
    p "A-And..."

    mx "And?"

    p "{i}...my nipples are sensitive to heat..."

    mx "E-Excuse me?"

    p "H-Hey! Don't turn!"

    scene 02_beachfun_priscillapath_14
    with dissolve

    p "Just...{w}Just continue moving forward!"
    p "I forgot to take Mama's sunblock and I'll be red as a tomato if I don't get cover!"

    mx "You know, I can feel your... y'know?"

    p "H-Hey! I said no indecent thoughts!"

    mx "I-I'm just saying!"

    scene 02_beachfun_priscillapath_13
    with dissolve

    p "Well, if it's you then..."

    mx "Then... what?"

    p "Ehehe~{p}Nothing!"

    scene 02_beachfun_pathfin_p_01
    with fade

    $ renpy.music.stop(channel='music1', fadeout=6)
    $ renpy.music.stop(channel='nature', fadeout=1)

    $ renpy.music.play('soundfx/ambience_pm_beach.ogg', channel='nature', loop=True, fadeout=0.4, fadein=0.4, tight=None, if_changed=True)

    mx "So, are you gonna be topless the rest of the evening?"

    p "N-No, silly! Let's go back to the changing cabins."
    p "My Sun dress is still there."

    mx "To the Changing Cabins, it is."
    $ renpy.end_replay()
    scene beach_evening_seaside
    with fade

    if notification_songs == True:
        $ renpy.notify("Desired - Secret Senshi")

    $ renpy.music.play("music/desired_secret_senshi.mp3", channel='music2', fadein=7, loop=True)

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    $ pquest_beachfun_priichange = True
    $ time = 3

    jump beach_seaside_triggers

label ep2_pquest_beachfun_play_priichange:

    if pquest_beachfun_beachchange_tankon == True:

        hide screen calendar_time
        hide screen calendar_week
        hide screen inventory_button

        $ pquest_beachfun_priichange = False

        scene beach_evening_cabins
        with fade

        p "Here it is!"
        p "I'll change so wait for me here, [mx]!"

        scene black
        with fade

        pause 0.2

        scene 02_beachfun_pathfin_f_02
        with dissolve

        mx "{i}*yawn*"
        mx "It's getting dark."
        mx "Well, atleast the sunset's quite beautiful."

        play sound "soundfx/door_open.ogg"

        "{i}*door open*"

        scene 02_beachfun_pathfin_f_03
        with dissolve

        p "Ugh..."
        p "I wanted to wear my swimsuit more..."
        p "It was so cute too. {p} {i}*sniff*{/i}"

        mx "You could always buy a new one."

        p "I guess.... \nMaybe I'll buy a new one when Hyuna comes back."

        mx "Hyuna?"

        p "Yeah! You should meet her!{p}She's still on vacation with her family."
        p "She's my bestie from Uni!"

        scene 02_beachfun_pathfin_f_04
        with dissolve

        mx "I see. {p} Well, why don't we go back to Fiona?"
        mx "She's probably bored waiting for us."

        p "Uh-huh! Mama's probably bored waiting for us. Ehe~"

        $ pquest_beachfun_priichange_fin = True
        $ pquest_beachfun_priichange_after = True

        scene beach_evening_cabins
        with fade

        show screen calendar_time
        show screen calendar_week
        show screen inventory_button

        jump beach_cabins_triggers
    else:


        hide screen calendar_time
        hide screen calendar_week
        hide screen inventory_button

        $ pquest_beachfun_priichange = False

        scene beach_evening_cabins
        with fade

        p "Here it is!"
        p "I'll change so wait for me here, [mx]!"

        scene black
        with fade

        pause 0.2

        scene 02_beachfun_pathfin_p_02
        with dissolve

        mx "{i}*yawn*"
        mx "It's getting dark."
        mx "Well, atleast the sunset's quite beautiful."

        play sound "soundfx/door_open.ogg"

        "{i}*door open*"

        scene 02_beachfun_pathfin_p_03
        with dissolve

        p "Ugh..."
        p "I wanted to wear my swimsuit more..."
        p "It was so cute too. {p} {i}*sniff*{/i}"

        mx "You could always buy a new one."

        p "I guess.... \nMaybe I'll buy a new one when Hyuna comes back."

        mx "Hyuna?"

        p "Yeah! You should meet her!{p}She's still on vacation with her family."
        p "She's my bestie from Uni!"

        scene 02_beachfun_pathfin_p_04
        with dissolve

        mx "I see. {p} Well, why don't we go back to Fiona?"
        mx "She's probably bored waiting for us."

        p "Uh-huh! Mama's probably bored waiting for us. Ehe~"

        $ pquest_beachfun_priichange_fin = True
        $ pquest_beachfun_priichange_after = True

        scene beach_evening_cabins
        with fade

        show screen calendar_time
        show screen calendar_week
        show screen inventory_button

        jump beach_cabins_triggers

label ep2_pquest_beachfun_play_priichange_after:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    $ pquest_beachfun_priichange_after = False

    scene beach_evening_seaside
    with fade

    p "Hrm? I don't see Mama anywhere?"
    p "Did she go somewhere?"

    mx "Maybe she's at the cafe near here?"

    p "The Cafe! {p} Let's check there!"

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump beach_seaside_triggers

label ep2_pquest_beachfun_bar:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene beach_evening_cafe
    with fade

    p "Oh, I see her!"
    p "Mama!"

    scene 03_beachfun_cafe_01
    with fade

    f "Prii!"
    f "Both of you took your time, huh? {p} Do I need to know something? Hmm!"

    p "Mama!"
    p "Hmph!" with vpunch

    f "Ahahaha! I'm just teasing you."
    f "I saw what happened earlier. {p} The case of the disappearing bra, huh?"
    f "Well, it's hard not to notice with how loud you were."

    p "Er..ehehe... {p} {i}*gulp*"
    p "L-Let's not talk about that..."

    f "Ahahaha! \nAlright, alright."
    f "Since both of you were late... \nI took the liberty and ordered drinks for us."

    scene 03_beachfun_cafe_02
    with fade

    f "I know Prii likes lemon juice so I already ordered that for her but..."
    f "I'm not really familiar with your taste, [mx]."
    f "I just requested a glass of beer if that's alright with you?"

    menu:
        "Just the right kind of poison for this evening.":

            p "Poison? Mama's not trying to kill you."
            p "If you don't want to drink—"

            mx "N-No, that's not what it means.{p}It's just an old fashioned term for any alcoholic drink."

            p "Huh? Is that so?{p}What a weird way of calling it."

            mx "Well, the way they made alcohol back then could definitely poison you."

            p "Hm, then more reason to stick with my lemon juice."

            f "Ehehe~\nAnyways..."

            jump ep2_pquest_beachfun_bar_cont
        "Well, alcohol is alcohol.":


            mx "Well, I don't mind any drink as long as there's alcohol in it."

            p "That sounds like what an alcoholic would say, [mx]?"
            p "I bet you'd drink rubbing alcohol too?"

            mx "W-What? No! You can't physically ingest rubbing alcohol, Prii."
            mx "What I mean is that whether it be a beer or a glass of wine, it's fine, y'know?"

            f "I couldn't agree more. {p}Although, I prefer the sweetness of wine."
            f "It goes down smoothly with a sweet aftertaste."

            p "Ugh! You're starting to become like Mama, [mx]! Boring!"

            mx "Maybe because we're adults, Prii?"

            p "H-Hey! What do you mean by that?"

            mx "N-Nothing!"

            f "Ehehe~\nAnyways..."

            jump ep2_pquest_beachfun_bar_cont

label ep2_pquest_beachfun_bar_cont:

    scene 03_beachfun_cafe_03
    with dissolve

    f "I was wondering for a while now why you two wanted to go to the beach today?"

    p "Oh! That's because we are on a mission to make [mx] remember his memories!"

    f "Ooh! A mission, huh? {p}But all you did was just play around today?"

    p "Ah...haha..er, y-yeah! \nT-That's part of the, uh, mission too!"

    scene 03_beachfun_cafe_04
    with dissolve

    p "R-Right, [mx]?"

    mx "{i}*cough*{w}*cough*"
    mx "Y-Yeah! I-It's definitely, absolutely, part of the mission!"

    p "Y-You see, Ms. Aanya told us to, um, stimulate our thoughts to remember the memories trapped within!"

    f "Oh, Aanya said that?{p}You too, Prii?"

    mx "Well, Prii just wants to laze and play aroun—"

    scene 03_beachfun_cafe_05

    mx "M-My foot!" with vpunch

    p "W-What [mx] meant to say is that us doing these activities would stimulates his neurons thereby triggering his old memories to the surface..."
    p "E-Ehehe..he..he.. {p} Atleast that's what I've been told. {i}*sluuuuuurp*"

    f "Amazing! \nYou're outdoing yourself with this Prii."
    f "I'm proud you're taking the extra mile for [mx]..."

    p "I know right!"

    f "But...{p}What happens after this?"

    p "Um, what do you mean by {i}\"what happens after\"?"

    f "Well, you know him personally more than I do, y'know?"
    f "What if [mx] becomes the same as before if he remembers his memory?"

    p "T-That's, umm, err..."

    scene 03_beachfun_cafe_04
    with dissolve

    p "[mx] will still be [mx] like always, right?"
    p "H-He'll remember our promise and he'll be like he always is."

    mx "Uh, haha..ha..."

    "(Maybe I've let this \"pretend mission\" get in my head for quite some time.)"
    "(Even though Prii doesn't look like she's taking this seriously...)"
    "(She really wants me to remember my—No, this guy's memories.)"
    "(Maybe I need to be frank with her?)"

    f "Prii, we shouldn't force [mx] like this—"

    scene 03_beachfun_cafe_07
    with vpunch

    mx "{i}*glug*{w} *glug*{w} *glug*"

    scene 03_beachfun_cafe_04
    with vpunch

    mx "{i}Haaaaaaaaah!"
    mx "{i}*hic!*"

    p "[mx]! \nW-What was that?"

    mx "I-I just felt drinking all of it at once."
    mx "I know it's just been a short time since I've survived the accident so..."
    mx "I'm just celebrating the fact that I'm still breathing."

    p "[mx]..."

    f "Ahahaha! {p} Well said [mx]!" with hpunch
    f "Let's just celebrate that [mx] is still alive."

    p "Yeah..."

    scene 03_beachfun_cafe_06
    with dissolve

    p "For [mx] breathing again! {p}{i}*sluuurp*"

    f "For you, [mx]!"

    mx "Well, to the both of you too for helping me!"

    p "Ehehe~"

    f "Well, I think we should finish up and start packing up our stuff."
    f "We don't want to get caught up in traffic."

    scene black
    with fade

    pause 0.2

    scene beach_evening_cafe
    with fade

    f "This was a really fun day. \nSadly, all good things have to end."
    f "Let's get back to the promenade."

    $ pquest_beachfun_priichange_fin = False
    $ pquest_beachfun_bar_fin = True

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump beach_cafe_triggers

label ep2_pquest_beachfun_sunset:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    $ pquest_beachfun_bar_fin = False
    $ pquest_beachfun_finish = True

    scene 04_beachfun_fin_01
    with fade

    f "Why don't you two stay here while I get the car?"
    f "Looks like people are rushing to get out of here too..."

    p "Okay~"

    mx "We will."

    f "Keep a watch on Prii, [mx]."

    p "H-Hey! I'm not a kid! \nI can do fine on my own too!"

    scene 04_beachfun_fin_02
    with fade

    p "Mama coddles me too much... {p}That said, uh, this was a fun day, wasn't it?"
    p "E-Even despite the, um, my d-disappearing top."
    p "Also {i}\"Get [mx]'s Memory Back: Number 3\"{/i} was another failure?"

    mx "Well, to be honest, I wasn't expecting much of that in the first place."
    mx "I didn't even care. \nI just wanted to have fun today, really."

    p "Eh..ehehe~ I see. \nSpeaking of fun..."

    scene 04_beachfun_fin_03
    with dissolve

    if pquest_beachfun_hangout_prii == True:

        p "I'm glad I got to play with you at the sea today! {p} You should've seen your face when I splashed you!"

        mx "Well, you also should've seen your face when you fell and lost your bra—"

        p "[mx]! \nL-L-Let's not talk about that~" with vpunch
        p "{i}...not to mention, your eyes were staring at it too much—"

        mx "I-I'm sorry! That was my bad! {p} How about we move on, huh?"

        p "Ehehe~"

        jump ep2_pquest_beachfun_sunset_cont
    else:


        p "You missed out swimming with me, y'know?{p}Seeing those starfishes were really amazing!"
        p "They were so cute I wanted to touch them but that stupid rock..."
        p "It's a shame where my bikini top disappeared, it was my favorite too!"
        p "How about you though? \nI saw you hanging out with Mama?"

        mx "Well, I just helped her apply sunblock... {p} That was pretty much it."

        p "That's it? Boring! {p} You should've played with me!"

        mx "Boring... indeed."

        p "Ehehe~"

        jump ep2_pquest_beachfun_sunset_cont

label ep2_pquest_beachfun_sunset_cont:

    scene 04_beachfun_fin_04
    with dissolve

    p "I'm really happy you're here with us enjoying all of this, y'know?"
    p "If I asked you in the past, you'd probably shut me down..."

    mx "..."

    p "..[mx]?"

    mx "Hey Prii... {w} you still remember what Fiona said awhile ago regarding what happens after if my old memories comes back?"

    p "Um, yeah? You'll still be you, right?"
    p "You'll just regain all of your memories and we'll go back to the way we are, like, right now?"

    mx "What if, y'know, I don't? {p} What if I just suddenly forget everything since I woke up from the hospital."
    mx "Forget what happened at the diner, the park, and maybe this moment right here?"

    scene 04_beachfun_fin_05
    with dissolve

    p "What... {w=0.3} what do you mean?"

    mx "I remember waking up at the hospital confused and afraid... {p} Having no clue on what exactly happened to me."
    mx "As if, I was put into another man's body. {p} As if an impostor playing someone I don't know..."
    mx "Then you and Fiona came through that door... {p} Our first introduction was strange but both of you made me feel like a family."
    mx "A family who's been with you for a long time..."

    p "[mx]... I—"

    mx "Hahaha! {p} Forget it! I was just being dramatic about this."
    mx "Sunsets just makes me quite a sentimentalist, y'know? {p} Brings out the inner Shakespeare in me."

    play sound "soundfx/carhorn.ogg"

    "{i}*beep*"

    pause 0.3

    f "[mx]! Prii!"

    mx "Fiona?"

    scene 04_beachfun_fin_06
    with dissolve

    f "It's getting dark already! {p} Hurry up, both of you!"

    mx "Coming! {p} Hey Prii! We should go!"

    p "... {p} {i}...what [mx] said..."
    p "{i}...is this all worth it? {p} ...I want to spend everyday like this with him..."
    p "{i}...[mx]..."

    scene black
    with fade

    jump city_map

label ep2_pquest_beachfun_finish:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button
    hide screen map_button

    $ pquest_beachfun_finish = False
    $ pquest_beachfun_complete = True

    scene 04_beachfun_fin_end
    with fade

    f "Wooh. That was an exciting day, wasn't it?"
    f "I hope we could go back again in the future?"
    f "I should really change out of my swimsuit."

    p "{i}*yawn*"
    p "I'm... going to my room first. {p} I need to think about something..."

    f "Well, we're gonna take a rest, [mx]."
    f "Don't stay up too late, alright?"

    $ renpy.music.stop(channel='music2', fadeout=2)

    scene ground_floor_evening
    with fade

    if notification_songs == True:
        $ renpy.notify("BROCKBEATS - september")

    $ story_music_ongoing = False

    $ story_ongoing_priscilla = False
    $ map_time_skip = True

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump ground_floor_hallway


label ep2_pquest_nightrendezvous:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    $ pquest_nightrendezvous = False
    $ pquest_nightrendezvous_start = True

    scene living_room_evening
    show 04_nightrendezvous_idle

    $ renpy.music.stop(channel='music3', fadeout=2)

    "(Hm? It's quite late. Why is Prii still here?)"

    hide all

    scene 01_nightparkstart_01
    with fade

    if notification_songs == True:
        $ renpy.notify("prima - june gloom.")

    $ renpy.music.play("music/prima-june gloom.mp3", channel='music2', fadein=2, loop=True)

    $ story_music_ongoing = True

    p "{i}...I mean but what if he..."

    mx "Yo! Evenin' Prii. {p} Isn't it a little bit late writing plans?"

    p "W-W-Wha!?"

    scene 01_nightparkstart_02
    with dissolve

    p "Oh... it's only you, [mx]."
    p "Don't scare me like that."

    mx "I was just checking why you're here this late at night."

    scene 01_nightparkstart_03
    with dissolve

    p "W-Well, I was just doing a bit of, um, uh, c-cleaning?"

    mx "Cleaning? {p} Did you spill ketchup on it or something?"

    scene 01_nightparkstart_02
    with dissolve

    p "Ketchup? \n I'm a clean eater, you meanie..."

    mx "Just guessin'..."

    scene 01_nightparkstart_03
    with dissolve

    p "Well, this is, um... {p} It's nothing important really..."
    p "And I'm not gonna be spilling ketchup on this, y'know?"

    mx "If you say so."

    scene 01_nightparkstart_04
    with dissolve

    p "A-Anyways! {p} Are you free tonight?"

    mx "I'm almost always free. {p} It's not like I have a job or something really—"

    p "Great!" with vpunch

    mx "Uh... why do you ask?"

    scene 01_nightparkstart_05
    with dissolve

    p "Well, you still remember what you promised me the other day, right?"
    p "Y'know, the one you'll accompany me somewhere during night time."

    mx "Ah, O-Oh. {p} Like right now? Isn't it a bit dangerous?"

    scene 01_nightparkstart_04
    with dissolve

    p "That's why I'm asking you! \n You're not backing out of that promise, are you?"

    mx "N-No! I mean, it's cold and dark... {p} Creatures of the night lurks between the bushes, y'know?"
    mx "Is it necessary to go out at this time? \nIt's probably safer when the sun's out."

    p "Uh-huh! Very necessary! Ehe~"

    "(Err... that {i}\"Ehe~\"{/i} smells like trouble.)"

    mx "{i}*sigh*{/i} {p} Fine! I already died once anyway..."

    scene 01_nightparkstart_06

    p "Yay~" with hpunch
    p "Not the dying part but you coming with me part!"

    mx "Okay! {p} Where exactly are we going?"
    mx "I hope it isn't a cemetery or some sketchy area like {i}\"Malmart\"{/i}"
    mx "That place gives me the heebie jeebies."

    p "Nope! {p} Just the city park!"

    mx "Oh no, it's much worse. {p} What if we encounter one of those... {w} {i}\"crossfitters\"{/i} running—"

    p "[mx]!" with vpunch

    mx "Kidding! I'm kidding! {p} Before we go, aren't you gonna change first?"

    p "Nooope~ {p} I always wanted to wear my sweater nighties outside!"

    mx "Alright..."

    p "Let's go out then!"

    scene living_room_evening
    with fade

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump living_room

label ep2_pquest_nightrendezvous_start:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    $ pquest_nightrendezvous_start = False
    $ pquest_nightrendezvous_start_park = True

    scene 01_nightparkstart_07
    with fade

    p "{i}*sniff*{/i} {w} {i}*sniff*{/i}"
    p "{i}ACHOOO!" with hpunch
    p "{i}Brrrrr!{/i} \nIt's so cold!"

    mx "Wanna take my offer on that dress change? \nIt isn't too late."

    p "Nooo~ {p} I want to be in my nighties!"

    mx "You're choice. {p} I can't believe we're doing this."

    p "We'll be fine! {p} If someone were to see those muscles, they'll be running away!"
    p "You still remember where the city park is, do you?"

    mx "I may be amnesiac but I'm not an idiot, y'know?"
    mx "Center of the city with a big fountain."

    p "Just checking! Ehe~"

    $ renpy.music.stop(channel='music2', fadeout=2)

    scene black
    with fade

    scene neighborhood_evening
    with fade

    $ park_unlock = True
    $ time = 4

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button
    show screen map_button

    jump neighborhood

label ep2_pquest_nightrendezvous_start_park:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button
    hide screen map_button

    $ pquest_nightrendezvous_start_park = False
    $ pquest_nightrendezvous_finish = True

    scene 01_nightparkstart_08
    with fade

    if notification_songs == True:
        $ renpy.notify("biosphere - soliloquy in a planetarium.")

    $ renpy.music.play("music/biosphere-soliloquy in a planetarium.mp3", channel='music2', fadein=2, loop=True)

    p "Wow!"
    p "It's really pretty here!"

    mx "It kinda is, huh?"

    p "How many people do you think are there inside each one of those windows, hm?"

    mx "Probably not that much."
    mx "Maybe just one or two that decided that it would be nice to have all the lights on."

    "(Well, that's what I did when I worked at the old company.) {p} (Out of boredom and mostly just to waste company money.)"

    mx "So, what exactly did you want to do here?"

    p "Well..."

    scene 01_nightparkstart_08_1
    with fade

    p "How about we sit over there? {p} The park lit by the skyscraper's glow is really something!"

    mx "Yeah, sitting at the dark, just the two of us, with low visibility, and surrounded by eerie quietness..."
    mx "Is really quite... {w=0.4} something. \n I guess?"

    p "[mx]! You're a moodie patootie!"
    p "It's gonna be amazing! Let's go!"

    scene 01_nightparkstart_09
    with fade

    p "See? The city feels alive, doesn't it?"
    p "The trees rustling as the wind passes, the slow rumbles of the distant cars..."
    p "It's as if a painting came to life, hm? {p} It's a rare sight to behold in this day of haste, y'know?"

    mx "..."
    mx "Who are you and where'd you hide the real Priscilla?"

    scene 01_nightparkstart_11
    with dissolve

    p "[mx]! {p} You meanie!"

    mx "Well, you just surprised me with all of that sentimental poetic stuff."
    mx "What's gotten you into that mood?"

    p "It's... a lot of things, I guess?"
    p "Well, it's just me being me. Never mind any of that."

    scene 01_nightparkstart_10
    with dissolve

    p "Do you still remember the other day when we went here? {p} I told you about the memory I wanted to remember?"

    mx "Oh yeah. I almost forgot about that."

    p "Well, I finally remembered what it was... {p} I even felt so dumb to have even forgotten it."
    p "It was such an important moment too..."

    mx "What was it?"

    scene 01_nightparkstart_11
    with dissolve

    p "After Mr. Negasi told us said the story on why he called you the... umm... what was it again?"

    mx "The {i}\"Bully Ganeni\"{/i}, the demon of this park's bullies."

    p "Right! I think it was at that time when this happened. {p} The memory, I mean."

    scene 01_nightparkstart_12
    with dissolve

    p "It was just right over there!"
    p "We decided to meet up here days after we made the promise!"

    "(That promise thing again?)"

    p "You said that we'll meet up here at 8AM or something and I arrived but you were late!"

    scene 01_nightparkstart_13
    with dissolve

    p "So, to kill time, I wanted to play at swings but then..."
    p "..."

    $ renpy.music.stop(channel='music2', fadeout=1)

    mx "...?"
    mx "(Prii?)"

    play sound "soundfx/glitch.ogg" loop

    show nightpark_glitch with vpunch

    pause 0.3

    if fquest_nightdrinking_glitch == False:

        "(GGGAAAAHHHHH!)" with vpunch
        "(W-What... the hell... is this?)"
        "(UUURRRRKKKKK!)" with vpunch
        "(M-My head... feels like... its...)"

        scene black
        with slowfade

        pause 0.4

        stop sound

        jump ep2_pquest_nightrendezvous_flashback
    else:


        "(UUUGGGHHHHH!)" with vpunch
        "(Another... memory... glitch..?)"
        "(UUURRRRKKKKK!)" with vpunch
        "(Fiona... and Prii... too?)"
        "(That... sinking... feeling again...)"

        scene black
        with slowfade

        pause 0.4

        stop sound

        jump ep2_pquest_nightrendezvous_flashback

label ep2_pquest_nightrendezvous_flashback:

    unk "What're you doing in our turf, squirt?"
    unk "Yeah! What he said! Squirt!"
    unk "I-I-I'm not a s-squirt!"
    unk "M-My name's Priscilla!"

    scene 02_nightparkflashback_01
    with fade

    if notification_songs == True:
        $ renpy.notify("BROCKBEATS - flashback")

    $ renpy.music.play("music/BROCKBEATS_flashback.mp3", channel='music2', fadein=1, loop=True)

    p "A-And this is a public park! \nI-I can play here too!"

    b1 "No. You. Can't!"
    b1 "Third graders aren't allowed here!"

    b2 "{i}*snort*"
    b2 "Yeah! He's right!"
    b2 "We don't like girls here!"

    scene 02_nightparkflashback_02
    with dissolve

    b1 "This playground is for Fifth graders only, tomato hair!"
    b2 "Yeah! Tomato hair!"
    b2 "No girls allowed!"

    scene 02_nightparkflashback_03
    with dissolve

    p "I-I'm not a tomato hair!"
    p "M-Mama said m-my hair's p-pretty..."
    p "{i}*sniff*"

    scene 02_nightparkflashback_04
    with dissolve

    b1 "Eww! Look at that! \nShe's gonna cry!"

    scene 02_nightparkflashback_05
    with dissolve

    b2 "Yeah! Yeah!"
    b2 "A Cry Baby! \nAhahaha!"

    scene 02_nightparkflashback_06
    with dissolve

    unk "Ugh! I'm late— {p} Wait. Is that Prii?"
    unk "Who are those kids?"

    p "I-I'm not g-g-gonna c-cry—{i}*sniff*{/i}!"
    p "UWAAAAH!" with vpunch

    scene 02_nightparkflashback_07
    with dissolve

    b1 "Hahaha! She's crying!"
    b2 "Yeah! Tomato hair's crying!"

    p "{i}*sniff!* *sniff!* \n G-Guuhh..."

    unk "Hey tweedle-stick and tweedle-fat!"
    unk "Why don't you pick on someone your own size?"

    scene 02_nightparkflashback_08
    with dissolve

    b1 "HAAAAAAAAH!?"
    b1 "Who the hell are you!?"
    b2 "YEAH! Who called me fat, huh!? \nI-I'm just big boned!"
    b2 "You want to take a beating!"

    scene 02_nightparkflashback_09
    with dissolve

    mx "The only ones who's gonna take a beating are you two."

    p "A-AH!"
    p "[mx]!" with vpunch

    b1 "[mx]? \nSounds like a loser name."
    b2 "Yeah! A loser's name!"
    b1 "Come here and I'll kick your ass—"

    scene 02_nightparkflashback_10

    play sound "soundfx/punch.ogg"

    "{i}*KAPOW*" with hpunch

    b1 "....ssss \n Ugghh..."

    p "W-Whaa..."

    b2 "K-Kingsley!"

    mx "Always go for the first strike! \nThat's what sensei told me!"
    mx "Wait! I think it was there's no first strike in Karate? {p} Well, whatever."

    scene 02_nightparkflashback_11
    with dissolve

    b2 "You murderer! {w}{i}Killer!{/i}{p}{b}C-Criminal!" with hpunch

    mx "Calm down. He's just unconscious. \nThat wasn't even a strong kick."
    mx "Well, I still need to kick your ass though."

    b2 "D-D-Don't come closer! \nI-I-I have the power of anime within me!" with vpunch
    b2 "I've s-s-seen A LOT of Kung Fu movies too!"

    scene 02_nightparkflashback_12
    with dissolve

    b2 "Y-You don't know w-what will happen to you if you c-come near m-m-me!"

    mx "Oh really? \nI also have the power of anime in me too."
    mx "And it doesn't like bullies!"

    b2 "Y-You're asking for it!"
    b2 "{b}{i}I-I HAVE THE POWER OF GOD AND ANIME ON MY SIDE!{/i}{/b}"

    mx "Come on, dude. That's just lame—"

    play sound "soundfx/spit.ogg"

    b2 "{i}*Ptooey!*{/i}"

    scene black
    with vpunch

    mx "YUCK!"
    mx "EUUGGGGHHH! \nWhat the hell was that?"
    mx "Not cool!"

    p "[mx]!"

    scene 02_nightparkflashback_13
    with dissolve

    b2 "RUUUUUNNNNNN!" with vpunch
    b2 "Kingsley! Let's scram!"
    b1 "Ugh... guu... why is... the earth... ugh... moving..?"
    b2 "I had to use the holy spit! \n That kid's power is beyond mine!"

    mx "HEY NOT SO FAST!"

    b2 "RRRRRUUUUUUNNNN!!!!" with vpunch

    mx "Ugh. They're gone."
    mx "Hey Prii, you alri—"

    scene 02_nightparkflashback_14

    mx "Oof!" with hpunch

    p "[mx]!"
    p "You saved me!"

    mx "W-W-Woah there! {p} I almost fell!"

    scene 02_nightparkflashback_15
    with fade

    p "I-I was so scared!"
    p "I wanted to play on the swings b-but they blocked me a-a-and, and..."

    mx "Well, they're gone now."

    scene 02_nightparkflashback_16
    with fade

    mx "Didn't I tell you we'll meet up near the ice cream van?"

    p "But the swings looked really fun though..."
    p "A-And you were late too!"

    mx "{i}*sigh*{/i} {p} You should've just waited for me then."

    scene 02_nightparkflashback_17
    with dissolve

    p "W-Well, if you hadn't come, I c-could've deal with them too, y'know!"
    p "I'd be {i}\"Boom! Bam! POW!\""

    mx "Then what was that about you being scared earlier, hm?"

    p "T-That was some o-other thing!"

    mx "Riiiiight..."
    mx "You could barely punch a ladybug."

    scene 02_nightparkflashback_18
    with dissolve

    p "HMPH! {p} Ladybugs are {i}very{/i} cute and nice!" with vpunch
    p "I won't punch them! {p} That's a very bad thing to do!"

    mx "Alright, alright! \nNo punching the ladybugs."

    p "But I c-could throw a mean punch like you too!"

    mx "Sure you do, Prii."

    scene 02_nightparkflashback_19
    with dissolve

    p "Grrr~"
    p "I'm really strong you know! \nLook at this!"
    play sound "soundfx/punch.ogg"
    p "Hiyaa!" with vpunch

    mx "{w=0.2}.{w=0.2}.{w=0.2}."

    scene 02_nightparkflashback_20
    with dissolve

    mx "That was, uh, a {i}really{/i} great punch, kiddo."

    p "Nnnguuoo~"
    p "I-I'll practice one day! You'll see!"

    mx "Yeah, we'll see."

    p "Hnnggg~"

    mx "So, how about that ice cream, huh?"

    p "{w=0.2}.{w=0.2}.{w=0.2}."

    mx "Well?"

    p "...okay. \nI'm still angry with you and..."

    $ renpy.music.stop(channel='music2', fadeout=3)

    scene 02_nightparkflashback_21
    with dissolve

    if pquest_parkquest_icecream_chocolate == True:

        p "I-I want a Chocolate one, alright?"

        mx "Chocolate it is."
        mx "Did you know, Chocolate was the first ice cream flavor?"

        p "Really?"

        mx "Yeah, the story goes..."

        scene black
        with fade

        jump ep2_pquest_nightrendezvous_leaving

    if pquest_parkquest_icecream_strawberry == True:

        p "I-I want a Strawberry one, alright?"

        mx "Strawberry it is."
        mx "Did you know, Strawberry isn't actually a berry?"

        p "Really?"

        mx "You see, berries are..."

        scene black
        with fade

        jump ep2_pquest_nightrendezvous_leaving

    if pquest_parkquest_icecream_vanilla == True:

        p "I-I want a Vanilla one, alright?"

        mx "Vanilla it is."
        mx "You know, Vanilla is also my favorite."

        p "Why?"

        mx "Well, first of all..."

        scene black
        with fade

        jump ep2_pquest_nightrendezvous_leaving

    if pquest_parkquest_icecream_bubblegum == True:

        p "I-I want a Bubblegum one, alright?"

        mx "Bubblegum it is."
        mx "You know, to make Bubblegum, they need to mix three flavors."

        p "Three?"

        mx "Yup! It's..."

        scene black
        with fade

        jump ep2_pquest_nightrendezvous_leaving

label ep2_pquest_nightrendezvous_leaving:

    scene black

    "(W-Was that...?)"
    "(Prii's...?)"
    "(Ugh...)"

    scene 03_nightparkend_01
    with fade

    if notification_songs == True:
        $ renpy.notify("biosphere - soliloquy in a planetarium.")

    $ renpy.music.play("music/biosphere-soliloquy in a planetarium.mp3", channel='music2', fadein=4, loop=True)

    p "[mx]..."
    p "[mx]? Are you okay?"

    if fquest_nightdrinking_glitch == False:

        $ pquest_nightrendezvous_glitch = True

        "(Did I... {w} What did happen just now?)"
        "(Whose memories was those? Mine or Prii's?)"
        "(Ugh.)"

        mx "U-Uh? W-What is it?"

        p "Well, you were quite silent for a minute there. {p} I'm just checking if you're okay?"

        mx "O-Oh."

        "(The scene I saw was more than a minute.)"

        mx "I think... I remembered something."

        p "Y-You did?"

        jump ep2_pquest_nightrendezvous_leaving_cont
    else:


        mx "Um, uh, y-yeah."

        "(Were those Prii's memories?)"
        "(I thought Fiona was the only one this was happening.)"
        "(It seems to be triggered by strong emotions.)"

        mx "I just remembered some things."

        p "Y-You do?"

        $ pquest_nightrendezvous_glitch = True

        jump ep2_pquest_nightrendezvous_leaving_cont

label ep2_pquest_nightrendezvous_leaving_cont:

    scene 03_nightparkend_02
    with dissolve

    mx "Yeah..."
    mx "I remember a fat kid and skinny kid bullying... you? {p} And I kicked one of them?"
    mx "We also ate ice cream and funnily enough, told you info about the flavor."

    p "Aha..ha..ha... \n{i}*gulp*"
    p "Y-You actually remembered? {p} D-D-Do you remember... {w=0.3}everything now?"

    mx "Not really. {p} Just that one."

    p "O-Oh, haha..ha... {i}*phew*{/i}{p}I mean, t-that's unfortunate..."

    "(Hm? What was that sigh about?)"

    scene 03_nightparkend_03
    with dissolve

    p "But it looks like our {i}\"Get [mx]'s Memory Back\"{/i} mission is finally paying off, huh?"
    p "Maybe tomorrow you'll start remembering all of it?"

    mx "I highly doubt it'll be that fast."

    p "Probably but you never know."
    p "{i}...this could be our last time too..."

    mx "Hm?"

    p "N-Nothing! {p} We should probably go back as it's getting late."

    scene 03_nightparkend_04
    with fade

    p "Thanks for coming along with me here."

    mx "Well, I didn't exactly had a choice, did I?"

    p "Ehehe~ But you remembered something, right? \nThat's a good sign."

    mx "I guess so. \nDo you know what happened to those two kids?"

    p "Hmmmm... No idea! {p} That wasn't the only time you beat them though."
    p "You were the Bully Demon after all! You had multiple run-ins with them after that."

    mx "O-Oh yeah.\n I forgot I was called that too."
    mx "Well, I think we should hurry back. \n I saw something ran behind you."

    p "W-What! W-Where..!? {p}..." with hpunch
    p "[mx]! You Bully Demon!"

    scene black
    with fade

    scene park_latenight_entrance
    with fade

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button
    show screen map_button

    jump citypark

label ep2_pquest_nightrendezvous_finish:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button
    hide screen map_button

    scene 03_nightparkend_05
    with fade

    p "What was that about you big meanie?"

    mx "Well, I thought I'd add a bit of excitement to our night?"

    p "Hmph! \nThat wasn't exciting at all!"

    mx "It was for me."

    p "A-Anyways, thanks again for going with me."

    mx "Yeah, about that. \nI was just wondering why you wanted to remember that memory in the first place?"

    p "Hm? Probably because the way you saved me was the coolest thing ever."

    mx "Really? Well, how about now? \nAm I still cool?"

    p "Secret! Tehee~ {p} Goodnight, [mx]."

    mx "Hey! No fair!"

    $ renpy.music.stop(channel='music2', fadeout=2)

    scene black with fade

    scene ground_floor_evening
    with fade

    if notification_songs == True:
        $ renpy.notify("BROCKBEATS - september")

    $ story_music_ongoing = False

    $ pquest_nightrendezvous_finish = False
    $ pquest_nightrendezvous_complete = True
    $ map_time_skip = True

    jump ground_floor_hallway


label ep2_pquest_mountainadventure:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    $ pquest_mountainadventure = False
    $ pquest_mountainadventure_start = True
    $ pquest_mountainadventure_start_1 = True

    scene priscilla_room_afternoon
    show 05_mountainadventure_idle

    $ renpy.music.stop(channel='music3', fadeout=3)

    mx "Prii? Where is she?"
    mx "I thought she'll be here coming up with another plan?"
    mx "Isn't that her planner?"

    hide all

    scene 01_mountainadventurestart_01
    with fade

    "(Huh? I thought she'll be carrying this with her.)"
    "(I'm curious on where we'll be going today.)"

    scene 01_mountainadventurestart_02
    with dissolve

    mx "So these were the plans..."
    "(Plans to do in the diner, then the park, the beach, and...)"
    "(Hm? Why are these last few entries crossed out?) {p} (Did she make a mistake?)"
    "(...)"
    "(Oh? There's something here at the end.) {p} ({i}\"The last entry\"?{/i})"

    $ renpy.music.play("music/dvdkm-lonely.mp3", channel='music2', fadein=1, loop=True)

    $ story_music_ongoing = True

    scene black
    with fade

    scene 01_mountainflashback_01
    with fade

    if notification_songs == True:
        $ renpy.notify("dvdkm - lonely.")

    p "After spending time with [mx] after these past few days. {p} I've never been happier!"
    p "I really wanted him to recover his memories and remember our promise together at the lake."
    p "But what he said at the beach bothered me about his memories, that the \"him\" now will just..."
    p "Go away. {p} Like last time."

    scene 01_mountainflashback_02
    with fade

    p "At first, I genuinely wanted him to recover his old self. {p} As it was the right thing to do!"
    p "Because I don't want to lose my memories too! \nMemories of Mama, my friends, and him."
    p "But I also remember that after the accident with his parents, he changed. {p} He became... distant to us. {w} To me."

    scene 01_mountainflashback_03
    with fade

    p "I know I'm selfish for doing this but I'll delay this as long as I can..."
    p "I also know it's cruel of me to stop him from remembering when he... {w} he started recovering our old memories."
    p "There's already a fear inside of me that if he finally remembers it all, I would say goodbye again..."
    p "A second final goodbye. {p}It hurts me so much to even think about it."
    p "I hope he never leaves me again but if he does... {p} I'll cherish the time we had in this planner."

    scene black
    with fade

    p "So, this is probably my last entry on this notebook."
    p "Sincerely, Priscilla."

    scene 01_mountainadventurestart_02
    with fade

    mx "Prii..."

    "(I thought playing the character of an amnesiac would just be a breeze.)"
    "(Because it'll cause nobody harm, right?) {p} (Who would be hurt by an amnesiac man?)"
    "(I was wrong.) {p} (Priscilla, Fiona, and who knows. This guy was important to them.)"
    "(And I'm just pretending to be him at the end of the day...)"

    play sound "soundfx/door_open.ogg"

    p "Yeah! I'll just go get my stuff here!"

    scene 01_mountainadventurestart_03
    with dissolve

    p "[mx]?"
    p "What are you doing here? You should've—"

    mx "P-Prii?"

    scene 01_mountainadventurestart_04
    with dissolve

    p "Is that my... n-notebook? \nIt's open..."
    p "Y-Y-You've read it!?" with vpunch

    mx "Um, uh, about the last entry..."

    scene 01_mountainadventurestart_05
    with dissolve

    p "T-T-That wasn't meant to be for you! \nI-It was—"
    p "No! I-I mean, it's—"
    p "{i}*sniff* {w=.3} *sniff*"

    mx "Prii, you don't need to—"

    scene 01_mountainadventurestart_06

    p "I'm sorry!" with vpunch
    p "I'm such a horrible person!"

    mx "Wait!"

    play sound "soundfx/door_close.ogg"

    scene priscilla_room_afternoon
    with fade

    mx "Shit! I need to follow her!"

    $ story_ongoing_priscilla = True

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump priscilla_room

label ep2_pquest_mountainadventure_start_1:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene second_floor_hallway_afternoon
    with fade

    f "P-Prii!?" with hpunch
    f "Why are you running so fast?"
    f "Prii!"

    "(Downstairs!)"

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump second_floor_hallway

label ep2_pquest_mountainadventure_start:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene 01_mountainadventurestart_07
    with fade

    f "What's going on with that girl?"
    f "Did she forget something else too?"

    mx "Fiona!"

    f "[mx]?"

    scene 01_mountainadventurestart_08
    with dissolve

    f "What was that about?"
    f "She said she was getting her notebook upstairs but then ran outside immediately."

    mx "Well, its, umm, uh, a very complicated matter."
    mx "Do you have any idea where she would go to?"

    f "I don't, sadly."

    $ renpy.music.stop(channel='music2', fadeout=1)

    mx "Oh, okay I should go—"

    scene 01_mountainadventurestart_10
    with dissolve

    play sound "soundfx/glitch.ogg" loop

    show mountain_start_glitch with vpunch

    pause 0.3

    "(URGH!)"
    "(This... again..?)"
    "(It's... Prii's... memories...)"

    stop sound fadeout 6.0

    jump ep2_pquest_mountainadventure_flashback_01

label ep2_pquest_mountainadventure_flashback_01:

    scene black
    with fade

    pause 0.5

    unk "Fiona, we understand your pain..."
    f "Why would he lie to us like that..."
    f "I'm too young to be a single mom to Prii..."

    scene flashback_mountainadventure_01
    with fade

    if notification_songs == True:
        $ renpy.notify("BROCKBEATS - flashback")

    $ renpy.music.play("music/BROCKBEATS_flashback.mp3", channel='music2', fadein=1, loop=True)

    p "{i}*sniff* {w} *sniff*"
    p "Papa..."

    scene flashback_mountainadventure_02
    with fade

    p "{i}*sniff*"
    p "Why... why would he leave me..."
    p "And Mama too."

    f "It's already been a few months now but the pain is still..."
    unk "I understand, dear."
    unk "[mx], can you take care of Prii while we adults talk?"

    p "{i}*sniff*"

    play sound "soundfx/door_open.ogg"

    pause 0.5

    scene flashback_mountainadventure_03
    with fade

    mx "Hey Prii."

    p "{i}*sniff*{/i} {p} [mx]..."

    mx "You okay, buddy?"

    p "..."

    mx "Uh, aha..ha.. I see."

    scene flashback_mountainadventure_04
    with dissolve

    p "[mx], I-If... I just did good with my homework..."
    p "Would Papa come back..?"
    p "{i}*sniff*"

    mx "Oh...umm...err..."
    mx "I'm sorry, Prii. \nI don't know about adult stuff."

    scene flashback_mountainadventure_03
    with dissolve

    p "I... {p} I already know."
    p "I know he wouldn't come back."
    p "Papa said so when he left... {i}*Guhk!*"

    mx "Hey, hey, hey! \nThen how about this..."

    scene flashback_mountainadventure_04
    with dissolve

    mx "Our moms would probably talk for hours by the looks of it."
    mx "Maybe we can go somewhere you always wanted to go, huh?"

    p "Somewhere to go..?"

    mx "Yeah! You want to go to the park again?"

    p "Park..? \nNo.."

    mx "Then where?"

    scene flashback_mountainadventure_05
    with dissolve

    p "T-That..."

    mx "A bus..?"

    p "Uh-huh."

    mx "I mean, sure, we can ride one to the park. \nI got my bus pass here."

    p "N-No... Not that. \n{i}*sniff*..."
    p "Mountains... {p} I want to go there."

    mx "Mt. Mudder, huh?"

    p "Uh-huh."

    mx "Err, I mean, it takes about an hour..."

    scene flashback_mountainadventure_04
    with dissolve

    p "{i}*sniff*"
    p "Hnnggg..."

    mx "{i}*sigh*{/i} {p}Fine, fine. We'll go."

    $ renpy.music.stop(channel='music2', fadeout=2)

    scene black
    with fade

    mx "Come on. {p}Let's go there while it's still noon."

    p "Yeah..."

    play sound "soundfx/map_move.ogg"

    pause 0.6

    jump ep2_pquest_mountainadventure_start_cont

label ep2_pquest_mountainadventure_start_cont:

    scene 01_mountainadventurestart_10
    with fade

    "(G-Guhhh...) {p} (I'm... I'm back.)"
    "(It seemed the memory was cut short.)"

    f "[mx]? You okay?"

    scene 01_mountainadventurestart_11
    with fade

    if notification_songs == True:
        $ renpy.notify("dvdkm - her.")

    $ renpy.music.play("music/dvdkm-her.mp3", channel='music2', fadein=1, loop=True)

    f "You got silent for a moment there."

    mx "Y-Yeah. {p} I was just thinking of places where Prii would go."
    mx "I recall she wanted to go to the mountains."

    f "The mountains?"

    scene 01_mountainadventurestart_09
    with dissolve

    mx "Yeah, Mt. Mudder."
    mx "She, uh, wanted to get, umm, some flowers, I guess?"

    f "Oh? She does? {p} Isn't it a bit too late for that?"
    f "It'll be evening when she gets there. \nShe should've went this morning."
    f "And I heard there'll be a storm coming this night."

    mx "A storm? {p} I'll take her back before that happens!"

    scene 01_mountainadventurestart_08
    with dissolve

    f "If you say so..."

    mx "Don't worry. {p}Even if it does, I'll be there to protect her."

    f "Against a storm? \n{i}*chuckle*"
    f "Alright, I trust you [mx]. {p}Take care, alright?"
    f "And don't take too long with those flowers too, okay?"

    mx "I will."

    scene 01_mountainadventurestart_09
    with dissolve

    f "Good luck."

    $ mountain_unlock = True
    $ map_time_skip = False
    $ pquest_mountainadventure_start = False
    $ pquest_mountainadventure_entrance = True

    scene ground_floor_afternoon
    with fade

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump ground_floor_hallway

label ep2_pquest_mountainadventure_entrance:

    $ time = 3
    $ pquest_mountainadventure_entrance = False

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button
    hide screen map_button

    scene mountaintrail_evening_entrance
    with fade

    pause 0.5

    scene 02_mountainadventureentrance_01
    with fade

    $ renpy.music.stop(channel='music2', fadeout=1)

    mx "ARGH!" with hpunch
    "(I-It's coming!)"

    play sound "soundfx/glitch.ogg" loop

    show mountain_entrance_glitch

    pause 0.5

    "(S-She's... definitely... here...!)"
    "(And.... t-this... one's... s-s-stronger....)"

    scene black
    with fade

    hide all

    stop sound

    pause

    jump ep2_pquest_mountainadventure_flashback_02

label ep2_pquest_mountainadventure_flashback_02:

    scene flashback_mountainadventure_06
    with fade

    if notification_songs == True:
        $ renpy.notify("BROCKBEATS - flashback")

    $ renpy.music.play('soundfx/ambience_am_mountain.ogg', channel='nature', loop=True, fadeout=0.4, fadein=0.4, tight=None, if_changed=True)

    $ renpy.music.play("music/BROCKBEATS_flashback.mp3", channel='music2', fadein=3, loop=True)

    p "Wow!"
    p "Look! A cabin!"
    p "And over there! \nA river and a bridge!"

    mx "{i}*huff!* {w} *huff!*"
    mx "Y-Yeah..."
    mx "{i}*huff!*"

    p "[mx]?"

    scene flashback_mountainadventure_07
    with dissolve

    p "Are you okay?"

    mx "Well, it isn't exactly easy carrying you up the mountains, is it?"

    p "Oh, er, ehehe~ \nSorry."
    p "I didn't know that it'll be this far from the bus stop."
    p "B-But atleast we're here!"

    mx "Y-Yeah. {p}Then do you want to go somewhere here?"

    p "Yeah! I want to go near the lake!"

    mx "Lake? At the center? \nThat's a bit long way to go... again."

    scene flashback_mountainadventure_08
    with dissolve

    mx "Can't we just stay here and rest?"
    mx "My body's still aching."

    p "Ehehe... sure!\nHm, oh! How about we hangover there at the bridge."

    mx "The bridge, huh?"

    unk "Well, well,well. {p} Who do we have here?"

    scene flashback_mountainadventure_09
    with dissolve

    unk "A couple of truant children no doubt!"
    unk "Unsupervised ones at that! \nUnbelievable!"

    scene flashback_mountainadventure_10
    with dissolve

    mx "Uhh.."
    mx "H-H-Hello... umm.. Officer...uh...sir?"

    unk "That's Cadet Ranger Roger Rogers, young man!" with hpunch

    mx "Y-YES! \nCadet Ranger..uh.. Roger... Rogers?" with hpunch

    rr "Now to my question!"
    rr "Why are you and the young miss here in Mt. Mudder!"
    rr "The home of the Phaak-Ur tribe!"
    rr "Without adult supervision!"

    scene flashback_mountainadventure_11
    with dissolve

    mx "Umm.. for.. uh.. independent r-research?"
    mx "Yes! Research for my..uh...boy scout... merit badge... mission?"
    p "{i}...you didn't tell me you were in the boy scouts..."

    rr "Boy scout mission, huh?"

    scene flashback_mountainadventure_12
    with dissolve

    rr "You mean to tell me that {i}YOU{/i}."
    rr "Without the iconic {i}Khaki uniform{/i} on!"
    rr "Without your {i}Merit Badge sash{/i} on!"
    rr "And without your trusty {i}Tools of Survival{/i}!"
    rr "Is to undertake Mt. Mudder, holy site of the Phaak-Urs! {p} Alone!?"
    rr "For what reason?"

    scene flashback_mountainadventure_11
    with dissolve

    mx "Uhh... {w}s-self-improvement?"

    scene flashback_mountainadventure_12
    with dissolve

    rr "..."
    rr "{i}Self-improvement...?"
    rr "..."

    scene flashback_mountainadventure_13

    rr "{b}I LIKE IT!{/b}" with vpunch
    rr "Spoken like a true man of mountains!"
    rr "I'm starting to see my young self in you, young scout!"
    rr "Tell me! {p}What's your name, lad!"

    scene flashback_mountainadventure_10
    with dissolve

    mx "U-Uh...umm...[mx], sir."
    rr "[mx]? A good name! \nI see it all now!" with vpunch
    mx "E-Excuse me?"

    scene flashback_mountainadventure_12
    with dissolve

    rr "The lack of uniform? {p} It's to prove scout spirit isn't tied to clothing but to the soul!"
    rr "The lack of merit sash? {p} An item to only worship physical awards and not one's help to empower society!"
    rr "Tools of survival? {p} The sweat from our palms is enough!"

    scene flashback_mountainadventure_13
    with dissolve

    rr "That's what a true scout is, isn't it!?" with vpunch
    rr "This ranger is awed at your spirit!"
    rr "It brings a tear to my eye that I, too, must strive harder!"

    scene flashback_mountainadventure_11
    with dissolve

    mx "{i}C-C-Correct!{/i} \nA-Ahahaha!"

    p "{i}...[mx]! You thought all of that! Amazing..."

    mx "Eh.. aha... haha.. y-yeah!"
    mx "{i}*gulp*"

    scene flashback_mountainadventure_13
    with dissolve

    rr "Mt. Mudder claims you as his own, young [mx]!"
    rr "As a representative of the {i}Phaak-Urs{/i}, I give you my blessing!"
    rr "Enter the mountains and come out as a man!"

    scene flashback_mountainadventure_14
    with dissolve

    rr "{b}Onward to your destiny, my boy!{/b}" with hpunch

    mx "Uhh.. y-yeah! Onward!"

    p "{i}...[mx], he's weird..."
    mx "{i}...Shh...I know..."

    unk "Roger, you want to go to the BBQ party this—"

    rr "No time for parties, Warden!"
    rr "Call the others and we will train like we've never trained before!"

    unk "W-What's gotten into you?"

    rr "SELF-IMPROVEMENT!" with vpunch

    mx "{i}...Let's go..."

    scene flashback_mountainadventure_15
    with fade

    play sound "soundfx/lakeshore.ogg"

    p "Look! Look!"
    p "I saw a fish!"

    mx "So this river comes from the lake, huh?"

    p "Uh-huh! You can see the lake where it comes from too!"

    mx "Yeah and it looks like a very long walk too."

    scene flashback_mountainadventure_17
    with dissolve

    p "Papa said we he'll bring me to this place, y'know?"
    p "And we'll visit the lake together but I guess not..."

    mx "O-Oh. \nSorry, I didn't know that."

    scene flashback_mountainadventure_16
    with dissolve

    p "Well, atleast I got you with me to see this!"
    p "I like how Mr. Sun makes the water sparkle like that."

    mx "Then you want to go further to see the lake?"

    p "Are your legs alright now?"

    $ renpy.music.stop(channel='nature', fadeout=2)

    $ renpy.music.stop(channel='music2', fadeout=2)

    mx "Of course! \nI'm a boy, y'know!"

    scene flashback_mountainadventure_17
    with dissolve

    stop sound fadeout 1.0

    p "The pretty lake..."

    scene black
    with fade

    p "Alright! Let's go..."

    scene 02_mountainadventureentrance_01
    with fade

    mx "Argh..."
    mx "It's... It's over."

    jump ep2_pquest_mountainadventure_entrance_cont

label ep2_pquest_mountainadventure_entrance_cont:

    $ pquest_mountainadventure_entrance_glitch_fin = True
    $ pquest_mountainadventure_ranger = True

    scene mountaintrail_evening_entrance

    show 05_mountainadventure_ranger_idle
    with fade

    "(I need to find Prii before night arrives.)"
    "(Hm? Who's that near the bridge?)"

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button
    hide screen map_button

    jump mountaintrail

label ep2_pquest_mountainadventure_rangertalk:

    $ pquest_mountainadventure_ranger = False
    $ pquest_mountainadventure_rangertalk = True

    hide all

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button
    hide screen map_button

    scene 02_mountainadventureentrance_02
    with fade

    mx "Um, excuse me?"
    mx "Have you seen a young lady come through here?"

    unk "Hrmm?"

    scene 02_mountainadventureentrance_03
    with dissolve

    if notification_songs == True:
        $ renpy.notify("Jack CC - dream of me")

    $ renpy.music.play("music/jackcc-dream of me.mp3", channel='music2', fadein=3, loop=True)

    unk "..."

    mx "Y-Yeah?"

    unk "Let me get this straight. {p}You're looking for a woman?"

    mx "R-Right."

    unk "Beyond this forest where no people are around?"

    mx "I guess... so?"

    unk "At this time of day where most criminals would do nefarious things in the dark?"

    mx "Uh.. umm.. by that you mean \"this evening\" then, uh, y-yes?"

    unk "I see... {w=0.3} I see..."

    scene 02_mountainadventureentrance_04
    with dissolve

    play sound "soundfx/rangertalk.ogg"

    "{i}*Psshhhkk!*"

    unk "Attention all rangers! {p}Apprehending a possible sexual pervert near my vicinity—"

    mx "WHAT!?" with vpunch
    mx "No, no, no, no!"
    mx "She's a friend of mine! {p} She must've went here—No! She's definitely here!"

    unk "Went missing, eh?"

    scene 02_mountainadventureentrance_05
    with dissolve

    unk "Tell me! {p}How could I trust a word from you, stranger?"
    unk "First off, what's your name?"

    mx "[mx], sir."

    unk "[mx], huh? \nSounds familiar... {w=0.3}suspiciously so."
    unk "Is your name on any wanted list?"
    unk "Haaaahhh!? \nMr. Criminal!" with hpunch

    mx "N-NO! \nWhy would a criminal even talk to law enforcement?"

    unk "Something like a criminal would say, hm? {p}But you do have a point there."

    scene 02_mountainadventureentrance_06
    with dissolve

    unk "Well, name's Roger Rogers! {p} WARDEN Ranger Roger Rogers!" with vpunch

    rr "Warden of this beautiful blessed mountain of the Mudder Phaak-Ur!"
    rr "Reknowned site of the Phaak-Ur tribe of old!"
    rr "The same tribe that flows in this vein of mine!"

    mx "C-Cool."

    scene 02_mountainadventureentrance_05
    with dissolve

    rr "Now, Mr. [mx]..."
    rr "Civilians aren't allowed after hours unless you have a permit or a credential."
    rr "And permits are only given just days before one goes here. {p}So, which is it?"

    "(Well, I certainly don't have a permit but I could say I have credentials.)"

    mx "Uh, c-credentials?"

    rr "Credentials, eh? {p}What kinda credentials are we talking about?"

    mx "Well, I was a..."

    menu mountain_ask01:
        "A decorated Eagle Scout! T-Top in my class!":


            scene 02_mountainadventureentrance_06
            with dissolve

            rr "You, one of the Eagle scouts?"
            rr "The highest achievement that a scout can achieve in his lifetime with a 4%% success rate?"
            rr "And decorated one at that?"

            mx "Err.. yes, I've w-worked hard for it!"

            rr "..."

            jump ep2_pquest_mountainadventure_rangertalk_cont1
        "Umm... an exceptional mountain climber? Climbed lots of mountains before.":


            scene 02_mountainadventureentrance_06
            with dissolve

            rr "You, a mountain climber?"

            mx "Y-Yeah! {p}Climbed the highest mountains!"

            scene 02_mountainadventureentrance_03
            with dissolve

            rr "Well then, Mr. Mountain Climber. \nI don't know much about your profession but..."
            rr "I expect that a lot of preparation is required. \nUnless you call that shirt and jeans you're wearing your mountain climbing gear."
            rr "Especially so climbing one in complete darkness."

            mx "{i}*gulp*{/i}" with vpunch

            rr "I'm starting to get suspicious that you're one of those criminal—"

            mx "D-Did I say I'm a mountain climber? \nWhat I meant to say was that I'm..."

            jump mountain_ask01
        "A-A journalist! That's right! I did stories about the excellence of... park rangers before!":


            rr "Oh! A journalist! {p} I'm familiar with a lot of publications!"
            rr "Especially those that detail the adventures of our Park Rangers!"

            scene 02_mountainadventureentrance_06
            with dissolve

            rr "Which one is it?"

            mx "The...umm... The Finest... Rangers?"

            rr "The Finest Rangers? {p}The magazine showcasing the hottest female rangers in all of the 50 states?"
            rr "I knew it! {p}You were here to spy on our cadets aren't you!" with hpunch

            scene 02_mountainadventureentrance_04
            with dissolve

            play sound "soundfx/rangertalk.ogg"

            "{i}*Psshhhkk!*"

            rr "Attention all rangers! A sleazy journalist from—"

            mx "N-N-No, no, no! Wait! \nYou must've misheard me! I ain't a journalist but a..."

            jump mountain_ask01

label ep2_pquest_mountainadventure_rangertalk_cont1:

    scene 02_mountainadventureentrance_07
    with dissolve

    rr "Why didn't you say so!" with vpunch
    rr "An Eagle scout is enough of a credential for you to venture this mountain! But..."

    scene 02_mountainadventureentrance_06
    with dissolve

    rr "I still find your lack of attire and essentials problematic, scout."
    rr "As you know, we still need to adhere to protocol!"
    rr "The suits in Capitol will grill me if you don't explain why."

    "(I extremely doubt they'll do that with bureaucracy and all.)"

    rr "Like, for example, where's your uniform?"

    mx "Um, I don't have it cause..."

    menu mountain_ask02:
        "Uh, it doesn't fit me anymore.":


            rr "Then you should've refitted it at the tailors!"
            rr "An Eagle scout is an example who leads!"

            scene 02_mountainadventureentrance_04
            with dissolve

            rr "Heck, I just refitted this uniform of mine for the 100th time!"

            mx "T-That's a lot of refitting..."

            rr "Damn straight, you're right! {p}A Park Ranger's uniform is our armor against the perilous nature!" with vpunch
            rr "You'll never know when the scouts need your help saving the wild!"

            mx "They... do that?"

            scene 02_mountainadventureentrance_06
            with dissolve

            rr "Shame! \nYou're a disgrace to the Eagle scouts!" with hpunch
            rr "I oughta call the Scout master—"

            mx "A-Ah! N-No! It seemed you have taken my questions l-literally!"
            mx "I don't have my uniform on is because..."

            jump mountain_ask02
        "It's at the laundry shop for cleaning.":


            scene 02_mountainadventureentrance_07
            with dissolve

            rr "That's admirable! {p}Our uniform must always be speckled clean!"
            rr "A dirty uniform reflects your spirit!"

            mx "O-Of course!"

            scene 02_mountainadventureentrance_05
            with dissolve

            rr "Still, I have to decline that request! {p}No uniform, no entry!"

            mx "W-Wait! The thing is, is that..."

            jump mountain_ask02
        "An Eagle scout isn't just his uniform but it's also his soul! My soul is the uniform!":


            scene 02_mountainadventureentrance_03
            with dissolve

            rr "{i}...isn't tied to his uniform but to his soul..."
            rr "Hmmm... {p}That's a deep philosophical thought."
            rr "It reminds me of certain time in my past when I was just a cadet here."
            rr "Getting my ranger certification..."

            scene 02_mountainadventureentrance_07
            with dissolve

            rr "That's an acceptable answer!" with hpunch

            mx "Uh, t-that's great!"
            jump ep2_pquest_mountainadventure_rangertalk_cont2

label ep2_pquest_mountainadventure_rangertalk_cont2:

    scene 02_mountainadventureentrance_06
    with dissolve

    rr "However! You're \"Lack of Uniform\" excuse isn't enough still!"
    rr "Do you even have your merit sash? {p}That's a sign for a worthy scout!"

    mx "About that..."

    menu mountain_ask03:
        "It's an item to only worship the material awards and not one's actions to the betterment of society!":


            scene 02_mountainadventureentrance_05
            with dissolve

            rr "{i}...I see...I see..."
            rr "I didn't really understand what that meant but it {i}SPOKE{/i} to my soul!"
            rr "I recall the hard days of training I did that even other rangers mocked me!"
            rr "Hmm... I like it."

            mx "Umm, does that mean I could go now?"

            jump ep2_pquest_mountainadventure_rangertalk_cont3
        "Isn't it weird to just wear the sash everywhere?":


            scene 02_mountainadventureentrance_05
            with dissolve

            rr "{i}Weird?{/i} WEIRD!?" with vpunch
            rr "How dare you! {i}How dare you, boy!{/i}"
            rr "The others tell me I'm \"weird\" too because I wear my trusty top of the line Ranger Glasses when I shower and even when I sleep."
            rr "Well, to HELL to that! {p}These glasses are the symbol, no, the spirit of a true ranger!"

            scene 02_mountainadventureentrance_04
            with dissolve

            play sound "soundfx/rangertalk.ogg"

            "{i}*Psshhhkk!*"
            rr "Attention! \nSomeone just committed the biggest crime out here!" with vpunch
            rr "The victim, me!\nAttacking my sense of style—"

            mx "N-No! Wait! \nI dare say, that those glasses looked mighty fine on you!"
            mx "What I meant when I didn't have it was..."

            jump mountain_ask03
        "Um, isn't it because its dangerous to wear a bunch of pins going up a mountain?":


            scene 02_mountainadventureentrance_06
            with dissolve

            rr "{i}Dangerous?{/i}"
            rr "{b}Nonesense!{/b}" with vpunch
            rr "You know what's dangerous? {p}A brown bear! That's what!"
            rr "And you know what'll protect you from them? {p}That's right! Your merit sash!"
            rr "They'll think {i}\"Oh, this man is an honorable member of society!\"."
            rr "They'll also think \"{i}Those big pins are very scary, better not eat him.{/i}\". {p}Boom! The merit sash has just saved your life!"

            mx "I, uh, didn't thought of that before..."

            "(Because it's just plain stupid and ridiculous.)"

            scene 02_mountainadventureentrance_05
            with dissolve

            rr "Or more likely, you're not an Eagle scout and pretending to be one!"

            mx "N-No! It's actually because of..."

            jump mountain_ask03

label ep2_pquest_mountainadventure_rangertalk_cont3:

    scene 02_mountainadventureentrance_06
    with dissolve

    rr "Not yet!" with vpunch

    mx "O-Okay! {p}I just like to find my friend while the Sun's still out."

    rr "This is my last question and the most important too!"
    rr "If you're finding this \"young lady\" then you should've been prepared!"
    rr "What if she fell? Drowned? CONSTIPATED!?"

    mx "Constipated?"

    scene 02_mountainadventureentrance_03
    with dissolve

    rr "The most dangerous state a person in the wild could be! {p}There was a man here who took a dump and was found dead later!"

    mx "R-Really? \nYou can get killed by constipation like that?"

    rr "Constipation? What, no!\nA windswept branch hit him hard in his head."
    rr "Tsk, tsk! \nLots of people have been victim to constipation's vulnerability!"

    mx "..."

    rr "And you don't have any {i}Tool of Survival{/i} to counter such scenario! {p}Why is that?"

    mx "Err..."

    menu mountain_ask04:
        "What exact tools of survival do I need? A hammer?":


            scene 02_mountainadventureentrance_05
            with dissolve

            rr "A hammer? {p}That's it? It's called \"Tools\" with an S! It's plural!"
            rr "What exactly are you gonna hammer away, hm? \nTiny rocks?"
            rr "You don't have nails to board up something!"
            rr "I'm afraid even with your credentials that you aren't sufficient to undertake the mountain!"

            mx "W-Wait!" with hpunch

            scene 02_mountainadventureentrance_03
            with dissolve

            mx "I was just joking! {p}Why I don't have my tools is because..."

            jump mountain_ask04
        "We were born with hands, sir! The sweat of our palms is enough to reckon' with Mother Nature!":


            scene 02_mountainadventureentrance_03
            with dissolve

            rr "{i}...the sweat of our palms is enough to reckon' with Mother Nature..."
            rr "{i}...Mhm...yes...yes..."

            scene 02_mountainadventureentrance_07
            with dissolve

            rr "{b}STUPENDOUS!{/b} {p}I couldn't have said it better myself!" with vpunch
            rr "As if I've spoken those words before!"
            rr "You know, young Eagle scout... \nYou remind me of a younger, determined me!"

            mx "T-Thanks?"

            jump ep2_pquest_mountainadventure_rangertalk_fin
        "Er, I have a pen here. Does that count?":


            scene 02_mountainadventureentrance_06
            with dissolve

            rr "A pen? {i}PEN!?{/i}{p}Are you gonna write a letter of apology to a brown bear?" with vpunch
            rr "Most ridiculous thing I've ever heard today!{p}That and the guy who wanted to dig underground for cheese..."
            rr "I'm afraid even with your credentials that you aren't sufficient to undertake the mountain!"

            mx "W-Wait!" with hpunch

            scene 02_mountainadventureentrance_03
            with dissolve

            mx "I was just joking! {p}Why I don't have my tools is because..."

            jump mountain_ask04

label ep2_pquest_mountainadventure_rangertalk_fin:

    scene 02_mountainadventureentrance_03
    with dissolve

    rr "Tell me, [mx]..."
    rr "What does those answers mean to you?"
    rr "The essence, the mana of those words you've spoken?"

    mx "Uh, umm, it's all for...{p}S-Self-improvement?"

    rr "{b}SELF-IMPROVEMENT!?" with hpunch

    mx "Y-Yes! \nT-That what I-I s-said, didn't I..?"

    rr "..."
    rr "It's been years since I, too, have uttered those words..."

    scene 02_mountainadventureentrance_08
    with dissolve

    rr "Over yonder, through that forest. {p}There was a report earlier of someone who ran through here."
    rr "I was about to check it out just before you arrived."

    scene 02_mountainadventureentrance_09
    with dissolve

    rr "Rescue her, my boy. {p}Your spirit and valor is much greater than mine."
    rr "Self-improvement, eh? {p}I think the young ones here could learn a lesson or two about that."

    scene 02_mountainadventureentrance_04
    with dissolve

    play sound "soundfx/rangertalk.ogg"

    "{i}*Psshhhkk!*"
    rr "Attention all rangers! Tomorrow morning! We will undergo a hellish training to forge our bodies and spirit!" with hpunch
    rr "All for the sake of self-improvement!"

    play sound "soundfx/rangertalk.ogg"

    "{i}*Psshhhkk!*"
    unk "W-Warden, d-don't we have to prepare for the flower festival?"

    rr "Fuck the flower festival! {p}Better yet! We should show our bodies freshly forged from nature's trials!"
    rr "That'll be the highlight of the event!"

    unk "W-What? \nWarden, that doesn't make sense—"

    scene 02_mountainadventureentrance_07
    with dissolve

    rr "Good luck out there, Eagle scout!"
    rr "I need to do some lapses after that much needed motivation!"
    rr "{i}Raaah!{/i}" with vpunch

    mx "T-Thanks, uh, Warden."

    scene mountaintrail_evening_entrance
    with fade

    mx "{i}*Phew!*"
    "(That was some luck.) {p}(That memory of Prii's earlier helped me with that dude.)"
    "(From Cadet to Warden, huh?) {p}(Well, let's find Prii already!)"

    $ mountainforest_unlock = True
    $ pquest_mountainadventure_ranger = False
    $ pquest_mountainadventure_rangertalk = True

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump mountaintrail

label ep2_pquest_mountainadventure_forest:

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button
    hide screen map_button

    scene mountaintrail_evening_forest
    with fade

    $ renpy.music.stop(channel='music2', fadeout=1)

    pause 0.3

    play sound "soundfx/glitch.ogg" loop

    scene 03_mountainadventuresearch_01

    pause 0.3

    show mountain_forest_glitch

    mx "GUUHHHHKKK!" with vpunch
    "(T-T-That... assault... just now..!)"
    "(It...struck...my...mind...brutally...)"
    "(She's...just...ahead...)"
    "(Let's...finish....this.....memory.....)"

    scene black
    with fade

    pause 0.5

    $ renpy.music.stop(channel='nature', fadeout=2)

    stop sound

    jump ep2_pquest_mountainadventure_flashback_03

label ep2_pquest_mountainadventure_flashback_03:

    scene flashback_mountainadventure_18
    with fade

    if notification_songs == True:
        $ renpy.notify("biosphere - cozy cove")

    $ renpy.music.play("music/biosphere-cozy cove.mp3", channel='music2', fadein=3, loop=True)

    $ renpy.music.play('soundfx/ambience_am_mountain.ogg', channel='nature', loop=True, fadeout=0.4, fadein=0.4, tight=None, if_changed=True)

    p "Woah!"
    p "[mx]! [mx]! Look!"
    p "A red birdie—Oh, a pretty blue birdie passed by too!"

    mx "Prii... there's a lot of birds here, y'know?"
    mx "We're in the mountains after all."

    p "I-I know that! It's just..."
    p "This is my first time here!"

    mx "{i}*sigh*"
    mx "I'm sorry. \nI'm just tired and all."

    p "Ehe~ \nI know!"

    mx "Hm? I think I see the fields already."

    scene black
    with fade

    p "Wow!"

    scene flashback_mountainadventure_19
    with fade

    p "Flowers! Lots and lots of them!"
    p "They're so small and cute and—."

    mx "Uh, yeah. \nSure are."
    mx "They look all the same to me though."

    scene flashback_mountainadventure_20
    with dissolve

    p "I wonder what they're called?"

    mx "Flowers, I guess?"

    p "Hmph! Not that! {p}You know what I mean! Like Roses or Tulips!"

    mx "Well, let's just call them Prii's flowers."

    p "REALLY? \nThen let's pick—"

    scene flashback_mountainadventure_21
    with dissolve

    p "H-HOT!" with hpunch
    p "Nguuoo... \nI didn't put on my sunblock."

    mx "Yeah! Let's get out of this heat then."
    mx "Uh, should we go back to the forest? \nThere's a lot of tree to cover us there."

    p "Hm!?"

    scene flashback_mountainadventure_22
    with dissolve

    p "Ooh! That's the lake! Look!" with vpunch
    p "We're already here, I guess?"
    p "We can get cover from the tree over there!"

    mx "Let's hurry before you burn up!"

    p "[mx]!"

    scene black
    with fade

    play sound "soundfx/lakeshore.ogg" loop

    pause 0.2

    scene flashback_mountainadventure_23
    with fade

    pause 0.5

    mx "Ah! Nice! We could relax here for a while!"

    p "Ehe~ \nYup!"
    p "Thanks a lot. [mx]."

    mx "Don't think about it! \nI just wanted to go somewhere without Mom."

    p "Yeah. \nI never noticed how beautiful this place is..."
    p "I saw a frog jump! Then I saw a Mr. and Mrs. Squirrel by the trees! \nThe flowers too—Oh, it's called Prii's Flowers now, I guess?"

    mx "Well, I saw a cool looking Beetle too!"
    mx "I wanted to capture it but it ran away!"

    p "Those are scary, [mx]! {p}But we saw a lot of things today..."
    p "Do you... {p}Do you think Papa wanted me to see all of this too, [mx]?"

    mx "I... guess, so?"
    mx "He's your Papa after all."

    p "Really? B-But..."

    mx "Hm? What is it, Prii?"

    scene flashback_mountainadventure_24
    with dissolve

    p "If... {w}If he did then why did he leave me and Mama? {p}Even though he promised to visit and call me..."
    p "{i}*sniff*{/i}"

    mx "Adult stuff is complicated."

    p "Yeah... {p}Do you think he'll ever come back?"
    p "And be a family again?"

    scene flashback_mountainadventure_25
    with dissolve

    mx "I... don't know. {p}Maybe you could ask Santa?"
    mx "Nah, its too long till Christmas."
    mx "But he still promised to visit and call you again, right?"
    mx "I heard that he's in, uh, S-South America?"

    scene flashback_mountainadventure_24
    with dissolve

    p "Uh-huh. {p}I asked Mrs. Howell how long would it take by bus."
    p "She said it'll be too long. \nEven longer than our bedtime."
    p "{i}*sniff*{/i}"
    p "I heard Mama crying every night and I'm sad that I..."
    p "I couldn't help her..."
    p "{i}*sniff*{/i}"

    mx "Hey, hey, hey!"

    scene flashback_mountainadventure_26
    with dissolve

    mx "We went here to not make you sad, right?"

    p "B-But..."

    mx "No \"Buts\", okay? {p}You still got me!"

    p "Y-You..?"

    mx "Sure! We play all the time! \nI'll never leave you!"

    p "Really!?"
    p "Something like... {w}an older brother?"

    mx "Uh... sort of? {p}Well, we're not related though."

    p "That's fine! Ehehe~"

    scene flashback_mountainadventure_27
    with dissolve

    mx "W-What're you grabbing my hand for?"

    p "Let's make a pinky promise then!"

    mx "Pinky promise? \nFor that?"

    p "Uh-huh! {p}You... You don't want to?"

    mx "I mean, isn't this enough?"

    p "N-No! A promise is—"

    unk "{i}Mi Amore!{/i} \nThis looks like a beautiful spot, no?"
    unk "It is, darling!"
    unk "Why don't we rest for while, hm?"

    scene flashback_mountainadventure_28
    with dissolve

    mx "H-Huh? Who're those?\nThey speak weird?"

    p "Ooh! Foreigners!"
    p "Let's look!"

    mx "W-Wait!"

    scene flashback_mountainadventure_29
    with dissolve

    p "L-Look!"
    p "I've seen this in movies! {p}They're duh..dey..ting? {i}Dheyting{/i}?"

    mx "Dating? Like boyfriend and girlfriend?"

    p "Uh-huh! \nI think they're gonna kiss like from the movies!"

    mx "KISS—"

    p "{i}...Shhhhh! Don't shout!..{/i}"

    mx "{i}...Mrhsshppp—Fine!...{/i}"

    scene flashback_mountainadventure_30
    with dissolve

    fom "This forest's beauty remind me of you, {i}bella."

    fow "Oh, Alejandro! \nYou never fail to make me fall in love with you again and again."

    fom "And I never will."

    fow "Alejandro..."

    scene flashback_mountainadventure_29
    with dissolve

    mx "Ew! Lovey-dovey stuff!"

    p "Shh! They might hear us!"
    p "A-And.. they're not \"{i}Ew{/i}\", okay?"
    p "L-Love is very c-cute."

    mx "Whatever."

    fom "Have you heard the tale of this lago?"

    fow "A tale about this lake?"

    fom "Si."

    scene flashback_mountainadventure_30
    with dissolve

    fom "It's said that once upon a time, a girl from the Phaak-Ur tribe met a young man here, a {i}colonista."
    fom "Despite the differences in their way of life, the two fell madly in love like they've never fallen before."
    fom "They would always meet here, in this very {i}lago{/i}."
    fom "As the {i}colonistas{/i} work in the daylight...\nThe Phaak-Urs roam in the night."
    fom "They always met here in the dusk and proclaimed their love for each other."
    fom "But that was soon to end..."

    scene flashback_mountainadventure_31
    with dissolve

    fow "W-Why!? \nW-What happened next?"

    fom "Like {i}El Dia{/i} and {i}La Noche{/i}, the Sun and Moon. {p}This mountain cannot contain two cultures that conflicts with each other."
    fom "One worships nature as its {i}Madre{/i} and the other exploits it for gain. {p}It simply came to {i}La batalla final{/i}..."
    fom "At the dawn of that battle..."

    fow "Y-Yeah!?"

    scene flashback_mountainadventure_29
    with dissolve

    fom "So, they met for the last time..."
    fom "Like they always do, as the Sun was about to touch the horizon..."
    fom "{i}El Nino{/i}, the boy, saw her condition, she was pale and out of breath..."

    fow "{i}*gasp*{/i}"
    p "{i}*gasp*{/i}"

    fow "Oh no!"

    fom "Her tribe found out of the affair and as a {i}consecuencia{/i}..."
    fom "She was forced to consume {i}veneno{/i}, poison, to preserve her {i}familia's{/i} honor."
    fom "A Phaak-Ur tradition. \n{i}Una tradicion brutal...{/i}"

    fow "{i}*sniff*{/i}"
    p "{i}*sniff*{/i}"
    mx "... {w}{i}*sniff*{/i}"

    scene flashback_mountainadventure_31
    with dissolve

    fom "With her remaining life left, she forced herself here, in this {i}El lago{/i} to wait for the boy."
    fom "{i}El Nino{/i} wanted to be close to her despite her reluctance and just wanted to stay by her side..."
    fom "And when the Sun touched the horizon, so did both of their lips."
    fom "The girl wept as she knew the poison on her lips would kill the boy too..."
    fom "But {i}El nino{/i} just smiled and said..."

    fow "..."
    p "..."
    mx "...{i}What did he said!?{/i}..."
    p "...{i}Shhh!{/i}.."

    scene flashback_mountainadventure_30
    with dissolve

    fom "A life without you is a life not worth living."
    fom "With that, {i}El Nino{/i} and {i}La Nina{/i}, a boy from another land and a daughter from the Phaak-Ur, died embracing each other..."
    fom "Lips locked to each other, smiling."
    fom "The Phaak-Ur chieftain and {i}El Capitan{/i} of the {i}Colonistas{/i} saw their corpses and stopped the war."
    fom "The legend continues to this day that if you make a promise here in this very lake..."
    fom "Under the setting Sun's light and kiss one another..."
    fom "The souls of the two that lie here, in {i}Monte Muddera{/i}, will wake up and fulfill that promise..."
    fom "Even beyond death."

    fow "R-Really?"

    fom "That's why, {i}Mi Amor{/i}, under the watchful eye of this {i}Monte{/i}..."

    scene flashback_mountainadventure_32
    with dissolve

    fow "!!!"

    fom "I will always love you."

    fow "Alejandro!"

    scene flashback_mountainadventure_34
    with dissolve

    p "O-O-O-Oh m-my!"
    p "T-T-They kissed, [mx]!" with vpunch
    p "It was so lovely!"

    mx "Yech! Eugh! \nEww! Ugh!" with vpunch
    mx "Disgusting!"

    fow "Alejandro, let's head back to the hotel, shall we?"
    fom "Say no more... {p}That smile can only mean one thing..."

    scene black
    with fade

    scene flashback_mountainadventure_33
    with fade

    mx "Man, that was long! {p}I-I got bored l-listening—{i}*sniff!*"
    mx "A-Anyways, I thought that weird guy would continue talking for a long time."
    mx "I... I didn't even—{i}*sniff*{/i}—cry! {p}Prii, let's better go back to—"

    p "W-Wait!" with hpunch

    mx "Hm? It's getting dark already..."

    scene flashback_mountainadventure_35
    with hpunch

    mx "Woah!"
    mx "Why'd you pulled me like that?"

    p "I-I said wait!"

    mx "O-Okay! \nWe can stay more if you like to!"

    p "N-No! Not that! {p}It's about the promise I said earlier."

    mx "Oh yeah? The pinky promise. {p}Let's do it right here."

    p "N-No, well, I..."
    p "I-I want to do what t-those couple did..."
    p "T-T-The... k-kiss..."

    mx "W-What!? \nEw! That's gross!"

    p "Hngg—{i}*sniff*{/i}"

    scene flashback_mountainadventure_36

    p "U-UWAAAAHH!" with vpunch
    p "Y-You're so mean! {p}I-I'm going to be all alone!"
    p "{i}*hic!* {w} *hic!*"

    mx "W-What!? \nM-Maybe, uh, s-some other time?"

    p "{i}*G-Guh!* \n*sniff*"

    mx "{i}*sigh*{/i} {p} You're killing me, Prii."
    mx "Fine, fine! {p}I'll do the stupid kiss, alright?"

    p "{i}*sniff*{/i} \nR-Really?"

    mx "Yeah... \nLet's just make it quick before I changed my mind."

    p "W-Well, {i}*sniff*{/i}, f-first let's go at that bench too..."

    mx "Where those couple kissed? \nErr... okay. Let's go."

    p "Mhm!"

    scene black
    with fade

    pause 0.5

    stop sound

    scene flashback_mountainadventure_37
    with fade

    mx "Ugh. We're really gonna do it, huh?"

    p "Y-Yeah... \nYou heard them, right?"
    p "They say that if we make a promise here... {p}The spirits will fulfill it."
    p "I-I wonder if we'll actually see them."

    mx "You know, the pinky promise would be more than enough?"
    mx "We really don't need to do this."

    scene flashback_mountainadventure_38
    with dissolve

    p "N-NO!" with vpunch
    p "Nope! Nuh-uh! \nWe're gonna do it or I'll cry again! Hmph!"

    mx "Alright! Sheesh."
    mx "Then let's do it already?"

    p "T-This is my f-f-first kiss! {p}S-So, it's important for me to prepare!"

    scene flashback_mountainadventure_39
    with dissolve

    p "S-So they p-posed like this a-and..."
    p "Then I-I'll hold your face like t-this—"

    mx "Your hands are shaking."

    p "I-I know! \nI just want to be ready!"
    p "{i}*breathing in!* {p} *breathing out!*"
    p "Okay!"
    p "First, you say your promise to me."

    mx "Uh, what kind of promise exactly? {p}I actually haven't asked you that."

    p "W-Well, p-promise you'll stay by my side f-forever!"

    mx "Forever? Isn't that too long—"

    p "Hnngg! {i}*sniff*{/i}"

    mx "Alright!"

    scene flashback_mountainadventure_40
    with dissolve

    mx "Hey, uh, Mt. Mudder and the spirits..."
    mx "I, the super duper strong [mx]..."

    p "[mx]!" with vpunch

    mx "I'm kidding!"
    mx "I promise Prii that I'll stay with her..."

    p "{i}Uh-huh?"

    mx "..."
    mx "Forever. {p}Happy now?"

    p "Yeah! Ehe~ {p}I also promise to do that too with [mx]."

    p "T-Then...{i}*gulp*{/i}"

    scene flashback_mountainadventure_41
    with fade

    "..."
    "{i}*chuu*{/i}"
    "..."

    pause 0.5

    scene black
    with fade

    mx "Ugh! You got spit on my face!"

    p "N-No! I-I did not!"
    p "That was yours!"

    mx "What? No..."

    $ renpy.music.stop(channel='music2', fadeout=2)

    $ renpy.music.stop(channel='nature', fadeout=2)

    jump ep2_pquest_mountainadventure_forestcont

label ep2_pquest_mountainadventure_forestcont:

    $ pquest_mountainadventure_rangertalk = False
    $ pquest_mountainadventure_flashbackend = True

    scene 03_mountainadventuresearch_01
    with fade

    $ renpy.music.play('soundfx/ambience_pm_mountain.ogg', channel='nature', loop=True, fadeout=0.4, fadein=0.4, tight=None, if_changed=True)

    mx "Urgh. \nMy...head."
    "(So, that was Prii's history with this guy, huh?)"
    "(I never thought it'd be this deep.)"
    "(I guess that's more than enough reason for her to take care of me at the hospital.)"
    "(A promise that even fulfills itself beyond death.)"
    "(...) {p}(That's quite eerie to even think about judging by what happened to me.)"
    "(Or maybe... I'm fulfilling it still?)"
    mx "{i}*sigh*{/i}"
    mx "I need to go and get her."

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    scene mountaintrail_evening_forest
    with fade

    jump mountaintrail_forest_triggers

label ep2_pquest_mountainadventure_encounter:

    $ pquest_mountainadventure_flashbackend = False
    $ pquest_mountainadventure_storm = True

    hide screen calendar_time
    hide screen calendar_week
    hide screen inventory_button

    scene 03_mountainadventuresearch_02
    with fade

    "(There she is.)"
    "(Hm? This area..?)"
    "(It seems this area was where the promise was sealed?)"
    "(I understand now why she's scared for me to leave if I \"remembered\" my past.)"
    "(Well, I really should talk with her and resolve this.)"

    scene 03_mountainadventuresearch_03
    with fade

    p "{i}*sniff* {p} *sniff*"
    p "Hnggg... {i}*sniff*{/i}"
    p "{i}...h-how will I show my face to him again... {p}...it's my fault..."

    mx "Ahem!" with hpunch
    mx "It's getting late, miss. \nThe park visitation is almost over."

    p "I-I-I'm sorry, M-Mr. Ranger!"
    p "I-I know its...{i}*sniff*{/i} late but can I h-have more t-time?"

    scene 03_mountainadventuresearch_04
    with dissolve

    p "I-I can get down on my own so c-can I stay for a—"
    p "...while?"
    p "[mx]..?"

    if notification_songs == True:
        $ renpy.notify("sweetbn_ - i held you so close i forgot the world")

    $ renpy.music.play("music/sweetbn-i held you so close i forgot the world.mp3", channel='music2', loop=True)

    mx "Hey Prii. {p}It looks like you've cried your eyes out?"

    p "I..."

    scene 03_mountainadventuresearch_05
    with dissolve

    p "I didn't mean to hurt with you with all of that!"
    p "I-I really want your memories to return! \nI do! I-It's just that...."

    scene 03_mountainadventuresearch_06
    with dissolve

    p "I want to spend more time with you!"
    p "I-I know losing your memories is bad but I..."
    p "I don't know what will happen if you remember your memories.."
    p "You might become distant again like..."
    p "Like last time..."

    mx "Prii, its—"

    scene 03_mountainadventuresearch_07
    with dissolve

    p "B-But I swear I didn't mean anything bad! {p}I j-just..." with vpunch
    p "W-We can restart the m-missions again!"
    p "Y-Y-Yeah! I-I-I can write another planner..."
    p "Y-You can go alone...without me..."

    scene 03_mountainadventuresearch_08
    with dissolve

    p "I just eat and get grumpy and-and..."
    p "{i}*sniff*"
    p "And I know I'm very selfish... {p}Just please..."
    p "Please don't hate me."

    mx "Pft! {p}You're too much of a drama queen, aren't you?"

    p "W-Wha?"

    scene 03_mountainadventuresearch_09

    p "H-Hey! S-Stop it!" with vpunch

    mx "Yeah, sure! You can eat a lot! {p} Get grumpy and be distracted by lots of things."
    mx "And yes... \nYou can be very {i}very{/i} selfish..."
    mx "Running off alone and making me chase you. {p}Cutting me off before I could say anything."

    p "I-I'm sorry but s-stop patting me!"

    mx "But even with all of those... \nI never hated you, not even once."
    mx "You see, it's a policy of mine not to hate kids."
    mx "Especially those who are still kids in the head like you? Haha..."

    p "H-Hey! \nI-I'm not a kid!"

    scene 03_mountainadventuresearch_10
    with dissolve

    p "Hmph!"
    p "Ehe~"

    mx "Are you okay now?"

    p "Y-Yeah. {p}I'm sorry for putting you through all this."
    p "How did you even find me here, anyways?"

    mx "Well... I remembered a story."

    p "Story?"

    mx "Yeah, about a little redheaded girl making a promise to a snotty kid. {p}Heck, on this very spot too!"
    mx "That he'll be with that tomato-haired girl... forever. {p}It seems the spirits did fulfill their promise."

    p "!!!"

    scene 03_mountainadventuresearch_11

    mx "{i}Ooof!{/i}" with hpunch

    p "Y-Y-YOU REMEMBERED!?"
    p "Y-You also remember the foreign couple here? \nA-And the story about the Phaak-Ur girl and the colonist boy?"
    p "D-Do you remember everything now? \nW-What about—"

    mx "Okay, okay, okay! {p}Catch your breath first." with hpunch
    mx "Not everything yet. {p}Just that part of my memory."

    p "What do you mean?"

    mx "Let's sit down first."

    scene black
    with fade

    scene 03_mountainadventuresearch_12
    with fade

    p "I see."
    p "So, you remember when we traveled here. \nJust the two of us?"

    mx "Pretty much. \nThat's what lead me here."

    p "T-Then you remember Mr. Ranger—I mean, he's Mr. Warden now."

    mx "Yeah, I just met him earlier when I came through here."
    mx "Looks like he's still the same naive—um, foolhardy guy back then."

    scene 03_mountainadventuresearch_13
    with dissolve

    $ renpy.music.stop(channel='nature', fadeout=2)

    p "Well, at least a piece of you is back."
    p "S-So, I'm wondering... {p} Y-You aren't planning to l-leave now, are you?"

    mx "I don't. \nI don't even know where I'll go?"
    mx "Wait. \nYou aren't kicking me out, are you?"

    p "N-No! I w-wouldn't do that!" with vpunch
    p "You could stay a bit longer?"

    mx "Just a bit?"

    p "N-No! Y-You can stay lots! {p}E-Even... {i}forever{/i}."

    mx "What was that?"

    p "N-Nothing!" with hpunch
    p "Anyways, we should go back home. {p}I want to say sorry to Mama too for running like that."

    $ renpy.music.stop(channel='music2', fadeout=2)

    mx "Sure. Hm, now that I think about it. {p}She was warning me about something earlier—"

    jump ep2_pquest_mountainadventure_stormclouds

label ep2_pquest_mountainadventure_stormclouds:

    scene 05_mountainadventurestorm_1
    with dissolve

    pause 0.2

    play sound "soundfx/thunder.ogg"

    scene 05_mountainadventurestorm_2
    with flash

    pause 0.8

    scene 05_mountainadventurestorm_1
    with dissolve

    pause

    scene 03_mountainadventuresearch_14
    with fade

    $ renpy.music.play("soundfx/stormwinds.ogg", channel='sfx3', fadein=0.4, loop=True)

    p "A s-storm? \nOh no!"

    mx "That's right! {p}She warned me a storm is coming this evening!"
    mx "Shit! We're too late! {p}It's a long way back to the outpost!"
    mx "I hope we can make it in time—"

    scene 03_mountainadventuresearch_15

    mx "Woah!" with hpunch

    p "[mx], I know a way where we can take shelter!"
    p "I remember seeing an old cabin near here! {p}It was supposedly the old outpost back in the day!"

    mx "Really? \nIs it safe?"

    p "Well, it's infinitely better than getting drenched here in the middle of the woods!"

    mx "Point taken."

    scene mountaintrail_storm_cabin
    with fade

    p "It's over there!"

    mx "I see, let's check it out."

    jump mountaintrail_oldcabin_storm

label ep2_pquest_mountainadventure_cabin_start:

    scene 03_mountainadventuresearch_16
    with dissolve

    mx "Looks like we're gonna be here for a while."
    mx "The storm's getting nearer."

    play sound "soundfx/door_creak_stuck.ogg"

    "{i}*creak*"

    p "Hm? [mx], the door seems to be stuck. {p}It's not budging at all."
    p "Can you help me with this?"

    mx "Hm? \nOh yeah."

    scene black
    with fade

    mx "The hinges are pretty rusted alright. {p}Thankfully, it's not locked."
    mx "A push or two would loosen this up."

    p "Ooh! A push let me help! {p}One, two..."

    play sound "soundfx/door_thud.ogg"

    p "Three! {p}O-Owiiiie..." with vpunch

    mx "You alright?"

    p "I-I'm fine! Atleast it worked!"

    mx "Yeah, it's definitely loose now. {p}Let's check out our \"forest villa\", eh?"

    play sound "soundfx/door_creak_open.ogg"

    "{i}*creak*"

    scene 03_mountainadventuresearch_17
    with dissolve

    p "{i}*cough* {w} *cough*{/i} {p} Ugh. It's so dusty in here!"

    mx "Tell me about it. {p}The smell isn't making it welcoming either."

    p "Err... m-maybe there's a much better cabin out there?"
    p "I think we still have time to look for another—"

    scene 03_mountainadventuresearch_18

    play sound "soundfx/thunder2.ogg"

    "{i}*Roar!*" with vpunch

    scene 03_mountainadventuresearch_19
    with dissolve

    $ renpy.music.play("soundfx/rain_heavy.ogg", channel='sfx2', fadein=0.7, loop=True)

    p "Eeeeeeekk!!!"
    p "[mx]!"

    mx "You were saying?"

    p "Hnnggg..."

    mx "Well, so much for looking for that other cabin, eh? {p}Looks like we have no other choice."
    mx "It's home sweet home."

    scene 03_mapcabin_00
    with fade

    $ renpy.music.stop(channel='sfx3', fadeout=2)

    $ renpy.music.stop(channel='sfx2', fadeout=2)

    $ renpy.music.play("soundfx/cabin_storm.ogg", channel='nature', fadein=2, loop=True)

    p "{i}Brrrrr!"
    p "I didn't know that it'll get very cold in here."
    p "I should've worn a sweater!"

    mx "Well, let's search for something we can light up."
    mx "It's too dark in here."

    jump mountaintrail_oldcabin_storm_inside

label ep2_pquest_mountainadventure_cabin_cont:

    hide screen inventory_button

    scene 04_mountainadventurecabin_01
    with fade

    play sound "soundfx/lamp_start.ogg"

    p "[mx]! This gas lamp still has some juice left."

    mx "Good find, Prii!"
    mx "But judging by this storm, it'll get much colder."
    mx "I better find something to start a fire enough for the both of us."

    p "Okay, I'll just warm up here for a minute."

    jump mountaintrail_oldcabin_storm_lantern

label ep2_pquest_mountainadventure_cabin_priscillalantern:

    hide screen inventory_button

    scene 04_mountainadventurecabin_02
    with fade

    if pquest_mountainadventure_cabin_firewoodplaced == False:

        p "Yes, [mx]? \nI thought you were searching for materials to start a fire?"
        p "I think I saw some firewood over there. {p}Oh! You also need a fire starter!"
        p "Maybe you should check around the fireplace? {p} The previous owners must've left something."

        scene 03_mapcabin_01
        with fade

        jump mountaintrail_oldcabin_storm_lantern
    else:


        p "Oh, you've already set the firewood? {p}Great! But you still need something to light it!"
        p "The ember in this lantern could be helpful but it's openings are all rusted."
        p "I read somewhere that striking piece of steel unto a flint could start a fire."
        p "Maybe there's something here like that you could use?"

        scene 03_mapcabin_01
        with fade

        jump mountaintrail_oldcabin_storm_lantern

label ep2_pquest_mountainadventure_cabin_firewoodplaced:

    hide screen inventory_button

    $ pquest_mountainadventure_cabin_firewoodplaced = True

    scene black
    with fade

    play sound "soundfx/firewood_place.ogg"

    "{i}*clink* {w=0.3} *clank* {w=0.3} *clonk*"

    scene 03_mapcabin_fplace01
    with fade

    if oldcabinflint in inventory.items:

        mx "There! That should do it!"
        mx "I just need to use the flint with me to start a fire."

        $ inventory.drop(oldcabinwood)

        show screen inventory_button

        jump mountaintrail_oldcabin_storm_fireplace_fin
    else:


        mx "There! That should do it!"
        mx "But I still need something to start the fire."
        mx "Hmm, where can I find one here?"

        $ inventory.drop(oldcabinwood)

        show screen inventory_button

        jump mountaintrail_oldcabin_storm_fireplace_fin

label ep2_pquest_mountainadventure_cabin_finish:

    hide screen inventory_button

    $ inventory.drop(oldcabinflint)

    scene black
    with fade

    play sound "soundfx/flint_start.ogg"

    "{i}*chkk* {w=0.3} *chkk*"

    scene 03_mapcabin_fplace02
    with fade

    $ renpy.music.play("soundfx/fireplace.ogg", channel='sfx3', fadein=1, loop=True)

    mx "Yes! I'm the Firelord, baby!"

    p "Wow! You actually did it, [mx]!"
    p "Now, could the \"Firelord\" scooch over?"

    mx "Ughh..."

    mx "Ehe~"

    jump ep2_pquest_mountainadventure_cabin_storycont

label ep2_pquest_mountainadventure_cabin_storycont:

    if notification_songs == True:
        $ renpy.notify("mittens - christmas sweaters.")

    $ renpy.music.play("music/mittens-christmas sweaters.mp3", channel='music2', fadein=7, loop=True)

    scene 04_mountainadventurecabin_03
    with fade

    mx "Well, that solves our cold problem. {p}Next is, well, just waiting out this storm."

    p "Hm, this cabin is starting to grow on me. {p}It's quite cozy too!"
    p "I'm surprised there isn't much more dust in here."

    mx "Looks this place was well-sealed and insulated. {p}Most of the dust were on the door."
    mx "I wish this storm would be over and done already.{p}I already broke my deal with Fiona to get you home before the storm hits."
    mx "{i}*sigh*"

    p "Mama... {p}She must be worried sick about us."

    scene 04_mountainadventurecabin_06
    with dissolve

    p "If I just talked this out with you then we wouldn't be in this situation."
    p "We could've been home right now. {p}It's my fault and my selfishness that brought us here."
    p "Sorry...{i}*sniff*"

    mx "Well, it could be worse, y'know? {p}And honestly, I understand you needed some time to think."
    mx "Even if the choices that led us here were a little bit selfish."

    scene 04_mountainadventurecabin_05
    with dissolve

    p "This was a little bit selfish?"

    mx "Just a {i}little{/i} bit."

    p "{i}*smirk*"

    mx "Look at the big picture! {p}We don't exactly often get to experience being stuck in an abandoned cabin..."
    mx "In the middle of the woods... {p} While a storm rages outside in complete darkness."
    mx "I think this is more exciting if we just had stayed at home."

    p "[mx]... Ehehe~ {p}Thanks for cheering me up."

    scene 04_mountainadventurecabin_04
    with dissolve

    p ".{w=0.3}.{w=0.3}.{p}Can I be a bit honest to you..?"
    p "After Papa left, I only had Mama and you in my life. {p}I was afraid that both of you will leave me."
    p "Especially you. {p}You were the only boy in my life I trusted after he left..."
    p "I always had anxiety that you're gonna leave too...{p}But that promise always gave me relief."

    mx "The promise, huh? {p}I remember you asking me that when I was still in the hospital."
    mx "Now that I remember it, it was kinda a cheesy scene, wasn't it?"

    scene 04_mountainadventurecabin_05
    with dissolve

    p "Hmph!" with vpunch
    p "I-It was cute! {p}Even if it's a little childish, I held that promise dear in my heart all these years."
    p "Even when you really left...{p}I believed we would've met again like right now."

    mx "What a powerful promise indeed..."

    p "I actually did more research about that story, y'know? {p}The Phaak-Ur girl and the boy colonist..."
    p "There was actually more to that story."

    mx "What was it—Wait! Let me guess?{p}They didn't kiss and the promise wasn't real?"

    p "On the contrary, it was all real albeit... {i}heavily{/i} edited. {p}They weren't a pair of kids but a man and woman."

    scene 04_mountainadventurecabin_04
    with dissolve

    p "You see, the couple didn't die that night. {p}They escaped and the war went through."
    p "The accounts of the conflict were quite... gruesome. {p}It lasted for months until something big happened on both sides."
    p "A revolution. The men and his supporters overthrew the Governor-General and the girl killed the Matriarch of her tribe."
    p "Both becoming the leaders..."

    mx "Matriarch?"

    scene 04_mountainadventurecabin_05
    with dissolve

    p "Surprising, isn't it? {p}It turns out that the Phaak-Ur tribe is ruled by a woman shaman and the girl was a candidate."
    p "Their illicit affair angered the Matriarch where she sent people after her but managed to escape."
    p "On the other side, the Governor-General had a reputation of being tyrannical and was hated that even his death."
    p "Both of their deaths ascended the Man and Woman to the respective positions they've overthrown."
    p "The marriage of the new Governor-General and the Phaak-Ur Matriarch would grant this everlasting peace between the two."
    p "But before this union could be achieved... {p}The Phaak-Urs were still against it unless a ritual is to be performed."

    mx "I assume this is where the promise comes in."

    p "Uh-huh! The Phaak-Ur's Ritual of the Kissing Death. {p}If the new couple survives, the Phaak-Urs must follow the new Matriarch's orders without question."

    mx "Kissing... Death..? \nThat's quite an eery name."

    p "It is. \nThe ritual goes like this..."

    scene 04_mountainadventurecabin_04
    with dissolve

    p "Both of them must place these two herbs on their tongues.{p}The herb themselves doesn't do any harm but if mixed together..."
    p "It creates a potent poison that could kill you in a couple of hours.{p}But it's also quite easily detoxified by having a higher bodyheat alone."

    mx "Oh, if that's the case, shouldn't a campfire or something be enough."

    scene 04_mountainadventurecabin_05
    with dissolve

    p "It's a ritual, silly!{p}They're not gonna let her pass easily."

    mx "Figures."

    p "The Phaak-Ur wanted them to do it in a cold, stormy night like this.\nSo that there's a high chance for the poison to kill them."
    p "I think they were expecting for their survival as a miracle."

    mx "So, how did they survive?"

    scene 04_mountainadventurecabin_04
    with dissolve

    p "E-Ehe..he..he... \nUh, umm, that is..."

    mx "Yeah..?"

    p "{i}...they had... s-sex..."

    mx "Sex? {w}Oh...{w} OH!{w} {i}OOOOOH!{/i} {p}{i}\"Higher bodyheat\"{/i}, gotcha!"

    scene 04_mountainadventurecabin_05
    with dissolve

    p "A-And they survived enough for the poison to be rendered ineffective and the rest was history... sort of?"
    p "If you've noticed by now, the whole ritual was also, um, {i}\"toned down\"{/i} for the history books."

    mx "More like censored brutally. {p}Honestly, that was a great story, Prii."

    p "Ehe~ {p}See, I did my homework!"

    mx "But doesn't that mean our \"promise\" wasn't real then?"

    scene 04_mountainadventurecabin_07

    p "Y-Yes! It d-does! {p}W-We kissed already, didn't we?" with hpunch

    mx "W-Well, y-yeah? \nI'm just putting out my observations."
    mx "The promise was based on a sketchy interpretation, y'know?"
    mx "Like, if you wanted a hamburger but the recipe you heard said that two pieces of bread and a slice of cheese is an authentic \"hamburger\" then..."
    mx "It's still not a hamburger, it was basically a sandwich. {p}Maybe that's why I left? Haha—"

    p "O-Oh! So, you're saying it's still incomplete?" with vpunch
    label galleryScene1:
    scene 04_mountainadventurecabin_08
    with dissolve

    mx "Y-Yeah..?{p}What're you planning?"

    p "Well, you said it yourself! {p}The promise is still incomplete!"
    p "That means that we just have to finish it, right?"

    mx "Finish... it? \nHow are we gonna do that?"

    p "With this—"

    scene 04_mountainadventurecabin_09

    mx "{i}Oof!" with vpunch

    p "Ehehe~"

    mx "Priscilla Fitzgerald. {p}What are you... {w=0.4} planning?"

    p "Finishing what we started!"

    mx "You know they took poison, right?{p}Are we gonna do the same?"

    p "Well, this is more like the abridged version of that. {p}It may not be 100%% but 90%% is more than enough."

    scene 04_mountainadventurecabin_10
    with dissolve

    p "But to be honest, I'm doing this because I want to."
    p "We're not the same boy and girl like before..."
    p "We've grown up now. {p}I grew up."

    scene 04_mountainadventurecabin_13
    with dissolve

    p "I know that believing in legends and stuff like this makes me look silly but..."
    p "If there's a chance in the world to not lose you again like I did before..."
    p "Then I'll do every legend and Phaak-Ur rituals there are just not see you again like that time in the hospital."
    p "Powerless and helpless to do anything to wake you up...{p}The only thing I can do is to be there for you..."

    mx "Prii..."

    scene 04_mountainadventurecabin_12
    with fade

    "{i}*chuu*"

    scene 04_mountainadventurecabin_14
    with dissolve

    p "Ehe~"
    p "That was the second time we kissed."

    mx "Ah, Y-Yeah."
    mx "Are you sure about doing this?"

    scene 04_mountainadventurecabin_11
    with dissolve

    p "I've never been more sure in my life."

    scene 04_mountainadventurecabin_15
    with dissolve

    p "Well, um... e-excuse me..."
    p "I've never done this before, so..."

    mx "{i}*gulp*"

    scene 04_mountainadventurecabin_16
    with dissolve

    p "I know you've already seen them at the beach but..."
    p "Guys like this stuff, right?"

    mx "W-W...Wow. \nI guess, we do?"

    p "Umm...c-can you not look at it that intensely?{p}You're making me embarrassed."

    mx "I can't exactly look anywhere else, can I?\nWith you on top, giving me a front view."

    p "Ehehe~"
    p "!!!{p}W-What's that poking..." with vpunch

    scene 04_mountainadventurecabin_17
    with dissolve

    p "Hm? {p}I-Is that your..?"
    p "{i}...p-penis..?"

    mx "I-I can't help it!"

    p "O-Oh... {i}*smirk*"
    p "Lemme take a look!"

    mx "W-Wait—"

    scene black with fade

    play sound "soundfx/zipper.ogg"

    "{i}*ziiip!*"

    scene 04_mountainadventurecabin_18
    with fade

    p "W-Wow... it really gets big like this, huh?"
    p "I've seen one on the Quantumnet but...{p}It looks different in person."
    p "D-Does it hurt?"

    mx "Uh, depends what you mean by \"hurt\"?"
    mx "Either way, it's uncomfortable."

    p "It's... throbbing..."
    p "It looks so..."

    scene 04_mountainadventurecabin_19

    pause 1.0

    mx "G-Guh!" with hpunch

    p "{i}*lick*{w}*lick*"
    p "{i}...its..salty..."

    mx "F-Fuck! P-Prii...{i}*Guh!{/i} {p}W-What're you doing?" with vpunch

    p "I-I just want you.. to be comfortable?"
    p "They say... guys like this, right?"

    p "{i}*lick*{w}*lick*"

    mx "Argh!" with vpunch

    p "I wonder if..?"

    scene 04_mountainadventurecabin_20

    mx "{b}FUCK!" with hpunch

    p "{i}*shlurp*"
    p "Ishh shhoo higgssh... \n(It's so big...)"

    p "{i}*shlurp*{w}*shlurp*"

    mx "G-GUH!" with vpunch
    mx "P-Prii! I-I-I can't hold on any longer.."

    scene 04_mountainadventurecabin_20_1
    with flash

    pause 0.3

    scene 04_mountainadventurecabin_20_1
    with flash

    mx "{i}AAAAAAAARRRRRGGGGHH!!" with hpunch

    pause

    mx "{i}Haaa... {w}haaa..."

    p "MMHHHMMPHH!"

    scene 04_mountainadventurecabin_21
    with dissolve

    p "MMHHHMMPHH—" with vpunch
    p "{i}*gulp!*" with vpunch

    mx "Are you okay..?"

    scene 04_mountainadventurecabin_22
    with dissolve

    p "{i}*cough*" with vpunch
    p "{i}*cough*" with vpunch
    p "Bleh... {p}S-So bitter..."

    mx "You... didn't need to swallow it?"

    p "I didn't... need to? \nB-But I read that guys like that if we s-swallow it?"

    mx "Some do but more importantly..."

    p "Y-Yeah? {w}Hm?\nW-W-What are you—"

    scene black

    play sound "soundfx/chair_slide.ogg"

    p "[mx]!" with vpunch

    scene 04_mountainadventurecabin_24
    with fade

    p "Ah..haha..ha..."
    p "W-W-Why are you looking at me like t-that, [mx]?"

    mx "What do you think I'll do, hm?"

    p "Uh, umm, y-you'd be nice to me, hehe..he?"

    mx "After you pull my zipper down with such force and started blowing me vigorously?"

    scene 04_mountainadventurecabin_23
    with dissolve

    p "Y-Y-You don't h-have to word it like that?"
    p "I-I just got carried away by the mood and... aha..ha..ha..\n{i}*gulp!*"

    mx "You see, Prii. {p}I'm a gentleman."
    mx "And gentlemen return favors given to them."

    scene 04_mountainadventurecabin_24
    with dissolve

    p "R-Return favors?{p}W-What do you mean?"

    mx "Like this!"

    p "Hm!?"

    scene black with fade

    p "{i}Eeeeeek!"

    play sound "soundfx/zipper.ogg"

    "{i}*ziiip!*"

    $ renpy.music.stop(channel='nature', fadeout=14)

    scene 04_mountainadventurecabin_25
    with fade

    pause

    mx "Wow..."

    p "{i}*whimper*{/i}."
    p "D-D-Don't look at it... {p}I-It's embarrassing!"

    mx "What's there to be embarassed about?"
    mx "Yours is much cuter."

    p "[mx]! \nU-Using cute is—"

    scene 04_mountainadventurecabin_26

    p "{i}HNNNNGGGG!" with vpunch

    pause

    p "[mx]! You big meanie!{p}T-That's dirty! Don't just—"

    mx "{i}*lick*"

    p "{i}MMMHHHHHMMMPPPHH!" with vpunch

    mx "I can't help it.{p}You're pussy taste sweet, Prii.."

    scene 04_mountainadventurecabin_27
    with dissolve

    mx "Y-Y-You... big... dummy.... meanie... pervert!"

    mx "{i}*lick* {w} *lick*"

    p "{i}HIIIIIYYYYAAAA!" with vpunch

    p "{i}Hnnnggg—N-Nooo!!{p}S-Slow down! S-Something's c-c-com—"

    scene 04_mountainadventurecabin_27
    with flash

    pause 0.3

    scene 04_mountainadventurecabin_27
    with flash

    p "—ING!!" with vpunch

    pause

    p "{i}Haaaa.... {w}Haaaa...{w} Haaaa..."
    p "T-That... {w}was... {w}amazing..."

    scene black
    with fade

    scene 04_mountainadventurecabin_28
    with fade

    p "Y-You... big... meanie..."
    p "I-I said slow down..."

    mx "Well, I got carried away by the mood, too."

    p "Ehehe~"

    mx "I'm still not done yet."

    scene black
    with fade

    play sound "soundfx/chair_slide.ogg"

    scene 04_mountainadventurecabin_30
    with fade

    mx "What're you smiling about?"

    p "I'm just...{p}So happy right now."
    p "My hearts beating crazy—Hm?"
    p "Y-You're...um, {i}thing{/i} is h-hard again..."

    mx "Well, I can't help it looking at you."
    mx "Come here..."

    scene 04_mountainadventurecabin_29
    with dissolve

    p "[mx]..."
    p "{i}Ahn! {w}Ah!"

    mx "Prii..."

    p "{i}Mhm! {w}Haah..."
    p "W-Wait a minute..."

    scene 04_mountainadventurecabin_31
    with dissolve

    mx "Uh, yeah?"
    mx "What is it?"

    p "Ehe~"
    p "I just want to look at your face before...{p}We do {i}it{/i}, y'know?"

    scene 04_mountainadventurecabin_32
    with dissolve

    p "This is my first time after all and..."
    p "I'm so glad it's you. {p}Even if we're somewhere strange..."

    mx "Well, it makes for an interesting story."
    mx "I mean who had their first time in a dusty old cabin on top of a rickety table?"
    mx "It already sounds really romantic, doesn't it?"

    scene 04_mountainadventurecabin_33
    with dissolve

    p "[mx]! \nI-I'm serious you meanie!" with vpunch

    mx "Ahahaha! I'm sorry, Prii!{p}I just find your serious face right now so cute."
    mx "It just makes me want to tease you more."

    p "HMPH!" with vpunch
    p "Meanie! {w}Dummy!"

    mx "Ahahaha!{p}So, are you ready?"

    scene 04_mountainadventurecabin_34
    with dissolve

    p "W-Well, um, they say it hurts..."
    p "But..."

    scene 04_mountainadventurecabin_35
    with dissolve

    p "If it's you..."
    p "I-I can take it."

    mx "Err.. if you say something like that I..."
    mx "I won't be able to stop my—"

    unk "..."

    mx "..?"

    scene 04_mountainadventurecabin_36
    with dissolve

    mx "Wait! {p}Did you hear that..?"

    p "Hm?{p}.{w=0.3}.{w=0.3}.{w=0.3}"
    p "I... {w=0.5}I heard it! {p}It looks like the storm has also stopped!" with vpunch

    unk "{i}...[mx]..."
    unk "{i}...cilla..."

    p "That's...{w} Mama!"

    mx "Fiona?"

    $ renpy.music.stop(channel='sfx3', fadeout=3)

    $ renpy.music.stop(channel='music2', fadeout=3)
    $ renpy.end_replay()
    scene black
    with fade

    jump ep2_pquest_mountainadventure_cabin_finale

label ep2_pquest_mountainadventure_cabin_finale:

    $ renpy.music.play('soundfx/ambience_pm_mountain.ogg', channel='nature', loop=True, fadein=1)

    scene 05_mountainadventureafter_01
    with fade

    f "Priscilla!" with hpunch
    f "[mx]!" with hpunch
    f "Can you hear me!?"
    f "Where are those two? {p} Hng! I should've just joined [mx] when he went after Prii..."

    rr "Don't worry, Ma'am!"
    rr "You've got the best Park Ranger in this mountain—{p}Heck, even the entire world!"

    scene 05_mountainadventureafter_02
    with dissolve

    if notification_songs == True:
        $ renpy.notify("Jack CC - dream of me")

    $ renpy.music.play("music/jackcc-dream of me.mp3", channel='music2', fadein=2, loop=True)

    rr "I've got the blood of the Phaak-Urs running in this veins of mine!"
    rr "My people have hunted in these woods at night for years!"

    play sound "soundfx/sniff.ogg"

    "{i}*SNIIIFFFF!*" with vpunch

    rr "I could practically smell their odor in the air!"

    play sound "soundfx/sniff.ogg"

    "{i}*SNIIIFFFF!*" with vpunch

    rr "Hmm... yeah, yeah.{p} It kinda smells like burning wood even."

    scene 05_mountainadventureafter_03
    with dissolve

    f "Um, uhh... t-that seems helpful."
    f "M-Maybe we could ask the other rangers for help?"
    f "It's past midnight already... {p}I'm scared for their safety especially after the storm..."

    rr "You just need to have faith on that young Eagle scout, Ma'am!{p}That young man is equivalent to five—No, ten Rangers!"
    rr "Or maybe... a half of me!"

    f "[mx]? An Eagle scout?"

    p "Mama!" with vpunch

    f "Huh?"

    scene 05_mountainadventureafter_04
    with fade

    p "Mama! I'm here!" with vpunch
    p "I can see them over there!"

    mx "She really is here.{p}It looks like she's with the Warden."

    p "[mx]! \nWe're saved!"

    mx "Err... y-yeah.\nThe Mountains must be in our favor, huh?"

    "(I was so close!)"
    "({i}*sigh*)"

    f "Prii!" with vpunch

    scene 05_mountainadventureafter_05
    with hpunch

    p "Mama!"
    p "I'm sorry I made you worry!"
    p "If I just didn't run I..."

    f "It's alright, Prii.{p}It's alright!"
    f "I'm just glad you're safe!"

    scene 05_mountainadventureafter_06
    with dissolve

    f "Why did you want to even get flowers this late even..?"
    f "Thankfully, [mx] was here to help you."

    p "F-Flowers..?{p}A-Ah! Y-Yeah! F-Flowers!"
    p "I-I lost them when we were looking for shelter."

    scene 05_mountainadventureafter_07
    with dissolve

    rr "{i}*sniff!*" with vpunch
    rr "Don't you love a beautiful scene of a reunion between mother and daughter?"

    mx "Y-Yeah..."

    rr "I'm surprised you found the old Outpost!"
    rr "I was supposed to get a search team for you but after our talk at the Outpost...{p}It would be insulting to you if I conducted one!"
    rr "I never doubted your ability to survive in a middle of a storm!{p}Heck, I bet you could even survive a month without any help at all!"

    mx "Uhhh... you should, um, still send help.{p}Just in case, y'know?"

    rr "Ahahaha! \nThat's a very funny joke!" with vpunch

    mx "H-Haha..ha..\n{i}...i-it wasn't one..."

    rr "This lady was insistent in finding you so I just had to accompany her here!"

    f "[mx]..."

    scene 05_mountainadventureafter_08
    with dissolve

    mx "Sorry, I broke my word to bring Prii back before night came, Fiona."

    f "Don't be! \nYou said you'll protect her, right?"
    f "That's all that matters."

    p "Yeah...{p}It's my fault for... uh... picking flowers here, right?"

    mx "Flowers..?"
    mx "Y-Y-Yeah! Right!{p}I said we're here for Prii's flowers..." with vpunch

    f "Hm?"
    f "Uh, both of you came here to get flowers... {w=0.4}right?{p}Or did something happen that I should know?"

    mx "Y-YES!" with vpunch
    p "U-UH-HUH!{p}N-Nothing happened! Y-Yes! Definitely nothing, um, n-naughty happened!" with vpunch

    f "Um, okay..? \nIf both of you say so."

    play sound "soundfx/thunder2.ogg"

    scene 05_mountainadventureafter_09
    with dissolve

    rr "Hmm... {p}We should hurry back."
    rr "It seems the storm's passing is momentary."

    scene 05_mountainadventureafter_10
    with dissolve

    rr "Come on, Civilians!" with hpunch
    rr "We better move! {p}The storm won't wait for us!"

    f "Is that so?"

    scene 05_mountainadventureafter_11
    with dissolve

    p "..."

    mx "..."
    mx "Err.."

    p "Y-Yeah..."
    p "Umm... \nAbout what happened in the cabin..."

    scene 05_mountainadventureafter_12
    with dissolve

    p "I was ready for my first time to happen there, y'know?"
    p "I'd be lying if I wasn't curious to see where it goes..."

    mx "Well, you're not the only one feeling like that.{p}It seems we can't do the ritual without the storm, huh?"

    p "Well..."

    scene 05_mountainadventureafter_13
    with dissolve

    p "Storms come and go, y'know? {p}One will happen definitely someday..."
    p "Maybe somewhere that's not in an abandoned cabin in the middle of the woods..."
    p "Maybe even somewhere like...{w=0.5} my room?{p}We just need to wait, right?"

    mx "Oh? What're you suggesting, Prii?"

    p "N-Nothing!"

    mx "A second time?"

    f "I'm not suggesting anything!{p}Ehehe~"

    scene 05_mountainadventureafter_14
    with dissolve

    p "But I still did a \"first time\" here tonight."
    p "Let's keep what happened inside that cabin our little {i}secret{/i}, alright?"
    p "Ehe~"

    f "Prii? [mx]? \nWe better go."

    scene 05_mountainadventureafter_end
    with fade

    p "Coming Mama~"

    mx "{i}*sigh*{/i}"

    f "What did you two talk about over there?"

    p "Just stuff from the cabin and how [mx] started a fire with a flint and stone."

    f "Really?"

    p "Yeah, first he got some wood and..."

    mx "..."

    "(This was...{w}an interesting night.)"
    "(What a roller coaster ride.){p}(More importantly, this ability to view the memories of someone.)"
    "(I need to understand what happened that night when I got \"reincarnated\".)"
    "(I think that old apartment of mine and Quanto can answer this questions.)"

    $ renpy.music.stop(channel='nature', fadeout=2)
    $ renpy.music.stop(channel='music2', fadeout=2)

    $ weekday += 1
    $ time = 1
    $ pquest_mountainadventure_finish = True
    $ map_time_skip = True
    $ story_ongoing_priscilla = False
    $ story_music_ongoing = False
    $ pquest_mountainadventure_complete = True

    scene black
    with fade

    pause

    scene mc_room_morning
    with fade

    show screen end_screen_priscilla

    pause

    mx "Well, that trip to the forest was a night to remember."
    mx "I better get ready."

    if notification_songs == True:
        $ renpy.notify("XNimVn - Sunny Day")

    $ story_music_ongoing = False

    show screen calendar_time
    show screen calendar_week
    show screen inventory_button

    jump mc_room
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
