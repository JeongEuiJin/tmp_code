from PIL import Image


class MethodImg:
    @staticmethod
    def rotate90(_img_obj, _save_path):
        rotate_img = _img_obj.rotate(90, expand=True)
        rotate_img.save(_save_path)

    @staticmethod
    def img_rotate_mirring(_img_obj, _save_path):
        _trans = Image.FLIP_LEFT_RIGHT
        MethodImg._img_rotate(_img_obj, _save_path, _trans)

    @staticmethod
    def img_rotate_filp(_img_obj, _save_path):
        _trans = Image.FLIP_TOP_BOTTOM
        MethodImg._img_rotate(_img_obj, _save_path, _trans)

    @staticmethod
    def _img_rotate(_img_obj, _save_path, _trans):
        mirring_img = _img_obj.transpose(_trans)
        mirring_img.save(_save_path)

    @staticmethod
    def resize_check(ori_w, ori_h, input_m, input_n):
        re_w = ori_w
        re_h = ori_h
        do_is_resize = False
        if ori_w % input_m != 0:
            re_w = ori_w - (ori_w % input_m)
            do_is_resize = True

        if ori_h % input_n != 0:
            re_h = ori_h - (ori_h % input_n)
            do_is_resize = True


        return do_is_resize , re_w, re_h
