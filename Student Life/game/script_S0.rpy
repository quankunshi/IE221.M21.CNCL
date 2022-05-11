label Chap0:
    #Gặp lại người thân
    show home
    show car_move
    pause 2.5
    hide car_move
    show mama happy
    Mama.c "Chào mừng trở về con trai, ta cứ ngỡ mất con sau vụ tai nạn đó chứ"
    "...."
    hide mama happy
    show mama question
    Mama.c "Mà con đã ổn chưa?"
    Mama.c "hừmmmmmm... đừng im lặng thế!!!"
    Player.c icon "Con ổn mà"
    Mama.c "(Phải làm bài test...)"
    Mama.c "Con còn nhớ tên của mình chứ??"
    menu chooseyn:

        "Tất nhiên rồi":
            jump name_choose1
        "Con không rõ lắm :(":
            jump name_choose2

    label chap0_continue:
    hide mama question
    show mama happy
    Mama.c "Đúng là con rồi!!"
    $ Mama.point_CC(1)
    Mama.c "Vào nhà thôi!"
    hide mama happy
    hide mama happy
    call locnha
    return


    label name_choose1:
        Player.c "Tất nhiên rồi... "
        Player.c "(Bỏ mẹ rồi tên mình là gì !!!)"
        "???" "(Hãy nghĩ ra cái tên đi nhóc, còn lại để ta sắp xếp!)"
        $ player_name=renpy.input("Họ và Tên:" )
        $ Player.name = player_name
        Player.c " Tất nhiên rồi con là [Player.name]"
        jump chap0_continue

    label name_choose2:
        Player.c "Con không rõ lắm... "
        Player.c "(Tên mình là gì !!!)"
        "???" "(Haizz chết tiệt..., thằng nhóc này đến cả tên mà không nhớ)"
        "???" "(Người tên là Long, Nguyễn Thanh Long. Đó là cả cái tên của người)"
        $ player_name="Nguyễn Thanh Long"
        $ Player.name = player_name
        Player.c " Tất nhiên rồi con là [Player.name]"
        jump chap0_continue
