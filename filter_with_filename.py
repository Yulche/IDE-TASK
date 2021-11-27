from filter import *


def main():
    image_file = Image.open("scale1200.jpg")
    block_size = 10
    gradations_count = 50
    image = np.array(image_file)
    gradation_step = 255 // gradations_count

    res = Image.fromarray(convert_image_to_mosaic(image, block_size, gradation_step))
    res.save("res_new.jpg")


if __name__ == '__main__':
    main()
