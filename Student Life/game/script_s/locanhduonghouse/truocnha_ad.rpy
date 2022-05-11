label locanhduonghouse:
    if calendar.Session == 0:
        scene anhduonghouse_screen
    elif calendar.Session == 1:
        scene anhduonghouse_midday_screen
    elif calendar.Session == 2:
        scene anhduonghouse_lastday_screen
    call screen menu_top
    
