screen Phonescreen:
    frame:
        xsize 600
        ysize 500
        xalign 0.9
        yalign 0.5
        background "phone screen"
        for loc in AppPhone:
            if loc.IsActive:
                button:
                    xpos loc.x
                    ypos loc.y
                    image loc.name
                    action Jump(stringhandling(str(loc.name)))

screen Updatelaterscreen:
    frame:
        xsize 500
        ysize 250
        xalign 0.5
        yalign 0.4
        image "updatelaterscreen"
        imagebutton idle "backbutton":
            xalign 0.5
            yalign 0.98
            action Rollback()






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
        imagebutton idle "backbutton":
            xalign 0.5
            yalign 0.98
            action Rollback()



screen menu_top:
    image "timebaner"
    text"[calendar.output]":
         xalign 0.09
         yalign 0.035
         color "#000000"
         size 15
    hbox xalign 1.0 yalign 0:
        imagebutton idle "mapicon" action ShowTransient('MapScreen')
        imagebutton idle "phone" action ShowTransient('Phonescreen')
