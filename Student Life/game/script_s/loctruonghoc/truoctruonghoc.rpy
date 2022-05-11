label loctruonghoc:
    if Events[1].checkEvent("loctruonghoc",calendar.Session,calendar.Day):
        jump chaomung
    scene school_screen
    show screen Time
    call screen menu_top
    return



label chaomung:
    scene school_screen
    show vanson dung
    HT_VanSon.c "Ohh..."
    HT_VanSon.c "[Player.name], có phải em đó không?"
    Player.c "(Ai đó ?)"
    HT_VanSon.c "Đúng là em rồi."
    HT_VanSon.c "Em không nhận ra thầy sao ?"
    show screen Time
    call screen menu_top
    
