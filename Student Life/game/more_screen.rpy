screen Time:
        image "timebaner"
        text"[calendar.output]":
             xalign 0.09
             yalign 0.035
             color "#000000"
             size 15




screen MapScreen:
    frame:
        xalign 0.5
        yalign 0.5
        xsize 500
        ysize 392
        background "map"
        for loc in Places:
            if loc.IsActive:
                button:
                    xpos loc.x
                    ypos loc.y
                    text loc.name:
                        color "#f10000"
                    action Jump("at"+stringhandling(str(loc.name)))




screen menu_top:
    hbox xalign 1.0 yalign 0:
        imagebutton idle "mapicon" action ShowTransient('MapScreen')
        imagebutton idle "phone" action Jump('moveloction')

label atnha:
    scene home
    show screen Time
    call screen menu_top
    $location = "home"
    return loction

label attruonghoc:
    scene school
    show screen Time
    call screen menu_top
    $location ="school"