# textbutton _("Mod Options") action Show("modOptions")

# if title == "Save":
#     text "{color=#fff}Save Name:{/color}":
#         xalign 0
#         yalign -0.005
#     input:
#         xalign 0
#         yalign 0.05
#         value VariableInputValue("save_name")

screen main_menu():
    tag menu

    add gui.main_menu_background

    imagemap:
        ground "main_menu_bg"
        idle "buttons_idle"
        hover "buttons_hover"
        hotspot ( 82, 80, 290, 193):
            hovered Play("sound", "soundfx/main_hover1.ogg")
            action [Play ("sound", "soundfx/main_click.ogg"), Start()]
        hotspot ( 94, 272, 282, 184):
            hovered Play("sound", "soundfx/main_hover2.ogg")
            action [Play ("sound", "soundfx/main_click.ogg"), ShowMenu("load")]
        hotspot ( 84, 456, 276, 180):
            hovered Play("sound", "soundfx/main_hover3.ogg")
            action [Play ("sound", "soundfx/main_click.ogg"), ShowMenu("credits")]
        hotspot ( 106, 636, 273, 178):
            hovered Play("sound", "soundfx/main_hover4.ogg")
            action [Play ("sound", "soundfx/main_click.ogg"), ShowMenu("preferences")]
        hotspot ( 94, 814, 276, 181):
            hovered Play("sound", "soundfx/main_hover5.ogg")
            action [Play ("sound", "soundfx/main_click.ogg"), Quit(confirm=True)]

    textbutton _("{size=75}Oscars Gallery") action [ui.callsinnewcontext("galleryNameChange"), Show("sceneGalleryMenu")] pos(400, 100) text_idle_color "#23272a"


screen preferences():
    tag menu

    imagemap:
        ground "gui/options_screen.jpg"
        bar:
            value Preference("music volume")
            at Position (xpos= 740, ypos = 531, xmaximum = 411, ymaximum = 26)
            style "mail_slider"
        bar:
            value Preference("sound volume")
            at Position (xpos= 740, ypos = 596, xmaximum = 411, ymaximum = 26)
            style "mail_slider"
        bar:
            value Preference("text speed")
            at Position (xpos= 740, ypos = 660, xmaximum = 411, ymaximum = 26)
            style "mail_slider"

        imagebutton:
            focus_mask True
            idle "gui/options/gui_opt_full_idle.png"
            hover "gui/options/gui_opt_full_hover.png"
            hovered Play("sound", "soundfx/switch_hover.ogg")
            action [Play("sound", "soundfx/switch_toggle.ogg"), Preference("display", "fullscreen")]

        imagebutton:
            focus_mask True
            idle "gui/options/gui_opt_windowed_idle.png"
            hover "gui/options/gui_opt_windowed_hover.png"
            hovered Play("sound", "soundfx/switch_hover.ogg")
            action [Play("sound", "soundfx/switch_toggle.ogg"), Preference("display", "window")]

        if preferences.fullscreen:
            add "gui/options/gui_opt_full_hover.png"
        else:
            add "gui/options/gui_opt_windowed_hover.png"

        imagebutton:
            focus_mask True
            idle "gui/options/gui_opt_sound_off_idle.png"
            hover "gui/options/gui_opt_sound_off_hover.png"
            hovered Play("sound", "soundfx/switch_hover.ogg")
            action [Play("sound", "soundfx/switch_toggle.ogg"), SetVariable("notification_songs", False)]

        imagebutton:
            focus_mask True
            idle "gui/options/gui_opt_sound_on_idle.png"
            hover "gui/options/gui_opt_sound_on_hover.png"
            hovered Play("sound", "soundfx/switch_hover.ogg")
            action [Play("sound", "soundfx/switch_toggle.ogg"), SetVariable("notification_songs", True)]

        if notification_songs == True:
            add "gui/options/gui_opt_sound_on_hover.png"
        else:
            add "gui/options/gui_opt_sound_off_hover.png"

        imagebutton:
            focus_mask True
            idle "gui/options/gui_opt_skip_unseen_idle.png"
            hover "gui/options/gui_opt_skip_unseen_hover.png"
            hovered Play("sound", "soundfx/switch_hover.ogg")
            action [Play("sound", "soundfx/switch_toggle.ogg"), Preference("skip", "toggle")]

        imagebutton:
            focus_mask True
            idle "gui/options/gui_opt_skip_choices_idle.png"
            hover "gui/options/gui_opt_skip_choices_hover.png"
            hovered Play("sound", "soundfx/switch_hover.ogg")
            action [Play("sound", "soundfx/switch_toggle.ogg"), Preference("after choices", "toggle")]

        if preferences.skip_unseen == True:
            add "gui/options/gui_opt_skip_unseen_toggle_on.png"

        if preferences.skip_after_choices == True:
            add "gui/options/gui_opt_skip_choices_toggle_on.png"

        imagebutton:
            focus_mask True
            idle "gui/return_button_idle.png"
            hover "gui/return_button_hover.png"
            hovered Play("sound", "soundfx/navigation_hover.ogg")
            action [Play("sound", "soundfx/navigation_click.ogg"), Return()]

    if _in_replay:
        textbutton _("{size=75}End Replay") action EndReplay(confirm=False) xcenter 0.5 ypos 300 text_idle_color "#23272a"


init 1 screen save():
    tag menu
    imagemap:
        ground "images/gui/save_screen.jpg"
        alpha False
        hotspot (124, 294, 427, 235):
            action [FileSave(1), Play("sound", "soundfx/sfx_save_overwrite.ogg")]
            use thumbnail(number=1)
        hotspot (744, 294, 432, 235):
            action [Play("sound", "soundfx/sfx_save_overwrite.ogg"), FileSave(2)]
            use thumbnail(number=2)
        hotspot (1367, 294, 426, 235):
            action [Play("sound", "soundfx/sfx_save_overwrite.ogg"), FileSave(3)]
            use thumbnail(number=3)
        hotspot (124, 708, 427, 235):
            action [Play("sound", "soundfx/sfx_save_overwrite.ogg"), FileSave(4)]
            use thumbnail(number=4)
        hotspot (744, 708, 432, 235):
            action [Play("sound", "soundfx/sfx_save_overwrite.ogg"), FileSave(5)]
            use thumbnail(number=5)
        hotspot (1367, 708, 426, 235):
            action [Play("sound", "soundfx/sfx_save_overwrite.ogg"), FileSave(6)]
            use thumbnail(number=6)

    imagebutton:
        focus_mask True
        idle "images/gui/save/save_idle_1.png"
        hover "images/gui/save/save_hover_1.png"
        hovered Play("sound", "soundfx/banner_hover.ogg")
        action [Play("sound", "soundfx/banner_click.ogg"), FilePage(1)]
    imagebutton:
        focus_mask True
        idle "images/gui/save/save_idle_2.png"
        hover "images/gui/save/save_hover_2.png"
        hovered Play("sound", "soundfx/banner_hover.ogg")
        action [Play("sound", "soundfx/banner_click.ogg"), FilePage(2)]
    imagebutton:
        focus_mask True
        idle "images/gui/save/save_idle_3.png"
        hover "images/gui/save/save_hover_3.png"
        hovered Play("sound", "soundfx/banner_hover.ogg")
        action [Play("sound", "soundfx/banner_click.ogg"), FilePage(3)]
    imagebutton:
        focus_mask True
        idle "images/gui/save/save_idle_4.png"
        hover "images/gui/save/save_hover_4.png"
        hovered Play("sound", "soundfx/banner_hover.ogg")
        action [Play("sound", "soundfx/banner_click.ogg"), FilePage(4)]
    imagebutton:
        focus_mask True
        idle "images/gui/save/save_idle_5.png"
        hover "images/gui/save/save_hover_5.png"
        hovered Play("sound", "soundfx/banner_hover.ogg")
        action [Play("sound", "soundfx/banner_click.ogg"), FilePage(5)]
    imagebutton:
        focus_mask True
        idle "images/gui/save/save_idle_6.png"
        hover "images/gui/save/save_hover_6.png"
        hovered Play("sound", "soundfx/banner_hover.ogg")
        action [Play("sound", "soundfx/banner_click.ogg"), FilePage(6)]
    imagebutton:
        focus_mask True
        idle "images/gui/save/save_idle_7.png"
        hover "images/gui/save/save_hover_7.png"
        hovered Play("sound", "soundfx/banner_hover.ogg")
        action [Play("sound", "soundfx/banner_click.ogg"), FilePage(7)]
    imagebutton:
        focus_mask True
        idle "images/gui/save/save_idle_8.png"
        hover "images/gui/save/save_hover_8.png"
        hovered Play("sound", "soundfx/banner_hover.ogg")
        action [Play("sound", "soundfx/banner_click.ogg"), FilePage(8)]
    imagebutton:
        focus_mask True
        idle "images/gui/save/save_idle_9.png"
        hover "images/gui/save/save_hover_9.png"
        hovered Play("sound", "soundfx/banner_hover.ogg")
        action [Play("sound", "soundfx/banner_click.ogg"), FilePage(9)]
    imagebutton:
        focus_mask True
        idle "images/gui/save/back_idle.png"
        hover "images/gui/save/back_hover.png"
        hovered Play("sound", "soundfx/banner_hover.ogg")
        action [Play("sound", "soundfx/banner_click.ogg"), Return()]
    imagebutton:
        focus_mask True
        idle "images/gui/save/navigation_idle.png"
        hover "images/gui/save/navigation_hover.png"
        hovered Play("sound", "soundfx/banner_hover.ogg")
        action [Play("sound", "soundfx/banner_click.ogg"), ShowMenu("navigation")]
    imagebutton:
        focus_mask True
        idle "images/gui/save/to_load_idle.png"
        hover "images/gui/save/to_load_hover.png"
        hovered Play("sound", "soundfx/banner_hover.ogg")
        action [Play("sound", "soundfx/banner_click.ogg"), ShowMenu("load")]

    text "{size=50}{color=#23272a}Save Name:":
        pos(100, 200)
    input:
        pos(360, 210)
        value VariableInputValue("save_name")

style input:
    xalign 0
    xmaximum gui.dialogue_width
    color "#23272a"
