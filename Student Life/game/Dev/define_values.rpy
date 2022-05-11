#----------------------------------Create Map-----------------------------------
default calendar = Calendar(0,["buổi sáng", "buổi trưa", "buổi tối"],1)
init python:
    #Bản đồ
    Map_loc = [0]*3 # thay đổi theo sự mở rộng của game
    Map_loc[0] = Place(200,250,"Nhà",True)
    Map_loc[1] = Place(280,150,"Trường Học",True)
    Map_loc[2] = Place(190,200,"Ánh Dương House",True)

    #Sự kiện
    Events = [0]*3 # thay đổi theo sự mở rộng của game
    Events[0] = Event("locnha",0,1,True)
    Events[1] = Event("loctruonghoc",1,1,True)
    Events[2] = Event("loctruonghoc",0,2,False)

    #Ứng dụng điện thoại
    AppPhone = [0]*5 # thay đổi theo sự mở rộng của game
    AppPhone[0] = Place(10, 70,"appcamera",True)
    AppPhone[1] = Place(90, 70,"appmail",True)
    AppPhone[2] = Place(180, 70,"apptele",True)
    AppPhone[3] = Place(10, 130,"appimage",True)
    AppPhone[4] = Place(90,130,"appnote",True)




#--------------------------------Create Character------------------------------
#----Player----
default player_name ="..."
define Player = Player(
                        Character("[player_name]",color="#009900",image="Player"),
                        "...",
                        0,
                        "male",
                        21,
                        "Một thanh niên wibu, sau khi được truck-sama hôn đã đc remake",
                        "STL37",
                        "Student",
                        "E3.2",
                        0,
                        0,
                        0
                        )

#----Student----
define SV_AnhDuong = Student(
                            Character("Ánh Dương"),
                            "Ánh Dương",
                            0,
                            "Female",
                            21,
                            "Ánh Dương là bạn thủa nhỏ của Player, nhà sát cạnh player",
                            "SSV001",
                            "Học Sinh",
                            "E3.2"
                            )

define SV_HoangAnh = Student(
                            Character("Hoàng Anh"),
                            "Hoàng Anh",
                            0,
                            "Male",
                            21,
                            "Là người theo đuổi Ánh Dương và khá ghét Player",
                            "SSV002",
                            "Student",
                            "E3.2"
                            )

define SV_NhatTruong = Student(
                            Character("Nhật Trường"),
                            "Nhật Trường",
                            0,
                            "Male",
                            21,
                            "Bạn thân của Player, ngầu và luôn được các bạn nữ yêu thích",
                            "SSV003",
                            "Học Sinh",
                            "E3.2"
                            )

define SV_BaoTran = Student(
                            Character("Bảo Trân"),
                            "Bảo Trân",
                            0,
                            "Female",
                            21,
                            "hotgirl lớp E3.2, thường xuyên trêu trọc Player",
                            "SSV006",
                            "Học Sinh",
                            "E3.2"
                            )

define SV_ThanhBach = Student(
                                Character("Thanh Bạch"),
                                "Thanh Bạch",
                                0,
                                "Male",
                                21,
                                "Sinh viên lớp bên rất hay trêu chọc các bạn nữ lớp E3.2",
                                "SSV007",
                                "Học Sinh",
                                "E3.1"
                                )

define SV_ThanhHai = Student(
                            Character("Thanh Hải"),
                            "Thanh Hải",
                            0,
                            "Male",
                            21,
                            "Anh em với Thanh Bạch, là 1 rickid chính hiệu",
                            "SSV008",
                            "Học Sinh",
                            "E3.1"
                            )
define SV_ThuThuy = Student(
                            Character("Thu Thủy"),
                            "Thu Thủy",
                            0,
                            "Female",
                            21,
                            "Rất ghét Player",
                            "SSV009",
                            "Học Sinh",
                            "E3.1"
                            )

#----Teacher----
define GV_AVien = Teacher(
                        Character("A Viễn"),
                        "A Viễn",
                        0,
                        "Male",
                        35,
                        "Giảng viên môn nhập môn lập trình, rất có hảo cảm với Player",
                        "SGV02",
                        "Thạc Sĩ",
                        "Nhập môn lập trình"
                        )
define GV_LongVan = Teacher(
                            Character("Long Vân"),
                            "Long Vân",
                            0,
                            "Male",
                            42,
                            "Giảng viên cấu trúc dữ liệu và giải thuật, rất hài hước và thường xuyên cho kiểm tra đột xuất",
                            "SGV03",
                            "Thạc Sĩ",
                            "cấu trúc dữ liệu và giải thuật"
                            )
define GV_HaiLi = Teacher(
                        Character("Hải Lí"),
                        "Hải Lí",
                        0,
                        "Male",
                        26,
                        "Giảng viên thể dục",
                        "SGV04",
                        "Cử Nhân",
                        "Thể Dục"
                        )
define GV_BaQuan = Teacher(
                            Character("Bá Quân"),
                            "Bá Quân",
                            0,
                            "Male",
                            28,
                            "Giảng viên lập trình hướng đôi tượng",
                            "SGV05",
                            "Thạc Sĩ",
                            "Lập trình hướng đối tượng"
                            )
define GV_ThanhThao = Teacher(
                            Character("Thanh Thảo"),
                            "Thanh Thảo",
                            0,
                            "Female",
                            35,
                            "Giảng viên môn nhập môn lập trình web, có hảo cảm với Player",
                            "SGV06",
                            "Thạc Sĩ",
                            "Nhập môn lập trình web"
                            )
define GV_NgocNhu = Teacher(
                            Character("Ngọc Như"),
                            "Ngọc Như",
                            0,
                            "Female",
                            26,
                            "Giảng viên kỹ thuật lập trình python",
                            "SGV07",
                            "Giảng Viên",
                            "Nhập môn kỹ thuật lập trình python"
                            )
define HT_VanSon = Teacher(
                            Character("Văn Sơn"),
                            "Văn Sơn",
                            0,
                            "Male",
                            55,
                            "Hiệu trưởng luôn vui vẻ và có chút nghiêm khắc",
                            "SGV08",
                            "Tiến Sĩ",
                            "An Toàn Thông Tin"
                            )

#----Staff----
define NV_NgocAnh = Person(
                            Character("Ngọc Anh"),
                            "Ngọc Anh",
                            0,
                            "Female",
                            28,
                            "Ý tá của trường"
                            )
define NV_NhuQuynh = Person(
                            Character("Như Quỳnh"),
                            "Như Quỳnh",
                            0,
                            "Female",
                            35,
                            "Lao Công"
                            )
#---------Character-------------
define Daion = Character("Daion")
define Mama = Person(
                    Character("Mama"),
                    "Mama",
                    0,
                    "female",
                    42,
                    "sdsds"
                    )
