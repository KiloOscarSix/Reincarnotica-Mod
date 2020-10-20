init python:
    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1

default galleryPageNumber = 1

define sceneGalleryMenuDict = {
    "galleryMenu": [
    ["Fiona", "/images/episode 2/fiona_scenes/01_dishquest/01_dishquest_02.jpg"],
    ["Priscilla", "/images/episode 1/act 04/B6.jpg"],
    ["Other", "/images/episode 1/act 04/dr_3.jpg"],
    ],
    "Fiona": {
    1: [
    ["fiona_dream", {}, "/images/episode 1/act 04/dream sequence/fiona_dream3.jpg"],
    ["ep2_fquest_gardenfinish_peek_01", {}, "/images/episode 2/fiona_scenes/04_gardenquest/06_fionabath_07.jpg"],
    ["ep2_fquest_drunkenvisit_dress_path_lovescene", {}, "/images/episode 2/fiona_scenes/06_nightvisit/01_nightvisitroom_dress_21.jpg"],
    ["ep2_fquest_drunkenvisit_sweater_path_lovescene", {}, "/images/episode 2/fiona_scenes/06_nightvisit/01_nightvisitroom_sweater_21.jpg"],
    ],
    },
    "Priscilla": {
    1: [
    ["pri_dream", {}, "/images/episode 1/act 04/dream sequence/pri_dream3.jpg"],
    ["ep2_pquest_beachfun_changingroom_priscilla", {}, "/images/episode 2/priscilla_scenes/03_beachfun/02_beachfun_change_priscilla_04.jpg"],
    ["ep2_pquest_beachfun_play_priscilla", {}, "/images/episode 2/priscilla_scenes/03_beachfun/02_beachfun_priscillapath_06.jpg"],
    ["galleryScene1", {}, "/images/episode 2/priscilla_scenes/05_mountainadventure/04_mountainadventurecabin_19.jpg"],
    ]
    },
    "Other": {
    1: [
    ["aanya_dream", {}, "/images/episode 1/act 04/dream sequence/aanya_dream4.jpg"],
    ],
    },
    }

label galleryNameChange:
    default persistent.mc = ""
    if persistent.mc == "":
        $ persistent.mc = renpy.input("Urgh.. What's my name again?", allow=" 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length=10, default="Leon").title()
    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "#23272a"

    text "Oscar's Scene Gallery":
        style "modTextHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
                idle "/oscarAdditions/images/button.png"
                hover Transform(im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2)))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        imagebutton:
            action OpenURL("https://www.patreon.com/oscarsix/overview")
            idle Transform("/oscarAdditions/images/become_a_patron_button.png", zoom=0.7465437788)
            hover Transform(im.MatrixColor("/oscarAdditions/images/become_a_patron_button.png", im.matrix.brightness(0.2)), zoom=0.7465437788)
            xanchor 1.0

    vpgrid:
        cols 4
        xspacing 50
        yspacing 37
        pos (117, 360)

        for i in sceneGalleryMenuDict["galleryMenu"]:
            vbox:
                imagebutton:
                    action [Show("sceneCharacterMenu", galleryCharacter=i[0]), Hide("sceneGalleryMenu")]
                    idle Transform(i[1], zoom=0.2)
                    hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                text i[0]:
                    style "modTextBody"
                    xcenter 0.5

screen sceneCharacterMenu(galleryCharacter="All"):
    tag menu
    modal True
    add "#23272a"

    text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
        style "modTextHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                if galleryPageNumber == 1:
                    action Show("sceneGalleryMenu"), Hide("sceneCharacterMenu")
                else:
                    action Function(galleryDecreasePageNumber)
                idle "/oscarAdditions/images/button.png"
                hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            if galleryPageNumber != len(sceneGalleryMenuDict[galleryCharacter]):
                imagebutton:
                    action Function(galleryIncreasePageNumber)
                    idle "/oscarAdditions/images/button.png"
                    hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
                text "Next":
                    style "modTextBody"
                    xcenter 0.5
                    ycenter 0.5

    vpgrid:
        cols 4
        xspacing 50
        yspacing 100
        pos (117, 360)

        for i in sceneGalleryMenuDict[galleryCharacter][galleryPageNumber]:
            $ scopeDict = {"mc":persistent.mc}
            $ scopeDict.update(i[1])
            imagebutton:
                action Replay(i[0], scope=scopeDict, locked=False)
                idle Transform(i[2], zoom=0.2)
                hover Transform(im.MatrixColor(i[2], im.matrix.brightness(0.2)), zoom=0.2)
