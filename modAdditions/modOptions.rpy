init python:
    Gr = "{color=#0f0}"
    Red = "{color=#f00}"
    Blue = "{color=#00f}"

    HaremPath = "{color=#0f0}[Harem Path]"
    EllaPath = "{color=#0f0}[Ella Path]"

screen modWalkthroughOptions():
    tag menu
    modal True

    add "#23272a"

    vbox:
        xcenter 0.5
        ypos 50
        spacing 100

        text "Walkthrough Options" style "modTextHeader"

        text "Turn on and off character paths" style "modTextBody" xcenter 0.5

    frame:
        xcenter 0.5
        ycenter 0.5
        padding (20, 20)
        grid 1 1:
            spacing 50
            style_prefix "check"

            textbutton "Harem Path":
                action ToggleVariable("HaremPath", true_value="{color=#0f0}[Harem Path]", false_value="")

    textbutton _("Return") action Hide("modWalkthroughOptions"):
        text_font "gui/PoiretOne-Regular.ttf"
        text_color "#a11f1f"
        text_hover_color "#ffffff"
        text_size 50
        yanchor 1.0
        pos (100, 980)
