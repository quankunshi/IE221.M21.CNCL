screen Time:
        image "timebaner"
        text"[calendar.output]":
             xalign 0.09
             yalign 0.035
             color "#000000"
             size 15



screen MapScreen:
    frame:
        xsize 700
        ysize 500
        xalign 0.6
        yalign 0.4
        background "map_screen"
        for loc in Map_loc:
            if loc.IsActive:
                button:
                    xpos loc.x
                    ypos loc.y
                    text loc.name:
                        color "#f10000"
                    action Jump("loc"+stringhandling(str(loc.name)))




screen menu_top:
    hbox xalign 1.0 yalign 0:
        imagebutton idle "mapicon" action ShowTransient('MapScreen')
        imagebutton idle "phone" action ShowTransient('Phone')
