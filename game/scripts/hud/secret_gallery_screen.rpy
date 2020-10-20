default persistent.galleryUnlocked = True

screen secret_gallery:

    modal True
    zorder 106
    add "images/hud/playbuck_bg.jpg"

    $ start = gallery_page * maxperpage
    $ end = min(start + maxperpage - 1, len(gallery_items) - 1)

    $ x = 141
    $ y = 366

    if persistent.galleryUnlocked:
        textbutton "{size=100}Unlock Gallery":
            action SetVariable("persistent.galleryUnlocked", False)
            pos(450, 100)
            text_idle_color "#23272a"
    else:
        textbutton "{size=100}Lock Gallery":
            action SetVariable("persistent.galleryUnlocked", True)
            pos(450, 100)
            text_idle_color "#23272a"

    grid maxnumx maxnumy:
        spacing -270
        xfill True
        yfill True

        for i in range(start, end + 1):

            if i%4==0:
                $ y -= 76
                $ x += 3

            $ gallery_items[i].refresh_lock()

            if gallery_items[i].is_locked and persistent.galleryUnlocked:
                add gallery_items[i].locked:
                    xpos x
                    ypos y
            else:
                imagebutton:
                    idle gallery_items[i].thumb
                    hover gallery_items[i].thumb_hover
                    action [Play ("sound", "soundfx/gallery_select.ogg"), Show("gallery_closeup", dissolve, gallery_items[i].images)]
                    xpos x
                    ypos y

        for i in range(end - start + 1, maxperpage):
            null

    if gallery_page > 0:
        imagebutton:
            focus_mask True
            idle "images/hud/playbuck_prev_idle.png"
            hover "images/hud/playbuck_prev_hover.png"
            hovered Play("sound", "soundfx/banner_hover.ogg")
            action [Play("sound", "soundfx/banner_click.ogg"), SetVariable("gallery_page", gallery_page - 1)]

    if (gallery_page + 1) * maxperpage < len(gallery_items):
        imagebutton:
            focus_mask True
            idle "images/hud/playbuck_next_idle.png"
            hover "images/hud/playbuck_next_hover.png"
            hovered Play("sound", "soundfx/banner_hover.ogg")
            action [Play("sound", "soundfx/banner_click.ogg"), SetVariable("gallery_page", gallery_page + 1)]

    imagebutton:
        focus_mask True
        idle "images/hud/playbuck_exit_idle.png"
        hover "images/hud/playbuck_exit_hover.png"
        hovered Play("sound", "soundfx/banner_hover.ogg")
        action [Play("sound", "soundfx/icon_close.ogg"), Hide("secret_gallery", transition=dissolve)]

screen gallery_closeup(images):
    zorder 106

    add images[closeup_page] at truecenter

    imagebutton:
        idle images[closeup_page]
        action [Play ("sound", "soundfx/gallery_select.ogg"), SetVariable("closeup_page", 0), Hide("gallery_closeup", dissolve)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
