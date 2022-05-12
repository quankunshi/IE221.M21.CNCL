init python:
    import re

    def no_accent_vietnamese(s):
        """
        unidecode xóa kí tự tiếng Việt
        https://nguyenvanhieu.vn/code-xoa-dau-tieng-viet/
        =======================================================================
        input(s): no_accent_vietnamese("Nguyễn Minh Quân 19522082 Đỗ Tài 19522149")
        output: Nguyen Minh Quan 19522082 Do Tai 19522149
        """
        s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
        s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
        s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
        s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
        s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
        s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
        s = re.sub(r'[ìíịỉĩ]', 'i', s)
        s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
        s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
        s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
        s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
        s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
        s = re.sub(r'[Đ]', 'D', s)
        s = re.sub(r'[đ]', 'd', s)
        return s

    def stringhandling(str_values):
        """
        xử lý tên tiếng việt thành không dấu và bỏ khoảng cách
        =======================================================================
        input(str_values): stringhandling("Nguyễn Minh Quân 19522082 Đỗ Tài 19522149")
        output: nguyenminhquan19522082dotai19522149
        """
        str_values = no_accent_vietnamese(str_values).replace(" ","").lower()
        return str_values
