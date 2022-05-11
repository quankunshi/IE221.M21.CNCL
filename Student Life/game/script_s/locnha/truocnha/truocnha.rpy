label locnha:
    if calendar.Session == 0:
        scene home_screen
    elif calendar.Session == 1:
        scene home_midday_screen
    elif calendar.Session == 2:
        scene home_lastday_screen
    show screen Time
    call screen menu_top
    return location_x
