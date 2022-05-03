label Chap0:
    #Gặp lại người thân
    show home   
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
    Mama.c "Vào nhà thôi!"
    hide mama happy
    return