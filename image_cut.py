import random
import sys

from PIL import Image

from img_method import MethodImg


class TestImageCutting:
    def __init__(self, M, N, out_path):
        self.M = int(M)
        self.N = int(N)
        self.out_path = out_path

        img = Image.open('testimg.jpg')
        o_w, o_h = img.size
        print("orgin size")
        print(img.size)
        is_change, r_w, r_h = MethodImg.resize_check(o_w, o_h, self.M, self.N)

        if is_change:
            img = img.resize((r_w, r_h))
            o_w, o_h = img.size
            print("resize")
            print(img.size)

        grid_w = o_w / self.M
        grid_h = o_h / self.N

        random_dig = "0123456789"



        for w in range(self.M):
            for h in range(self.N):
                locate_point = (w * grid_w, h * grid_h, (w + 1) * (grid_w), (h + 1) * (grid_h))

                crop_img = img.crop(locate_point)

                fname = "{}.jpg".format(
                    "{}{}{}".format(random.choice(random_dig), random.choice(random_dig), random.choice(random_dig))
                )
                
                # if random.choice(random_dig)

                crop_img.save(fname)


if __name__ == '__main__':
    print(TestImageCutting(sys.argv[1], sys.argv[2], sys.argv[3]))
