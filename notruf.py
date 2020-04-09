from gimpfu import *
from os.path import expanduser

home = expanduser("~")


def plugin_main(image, drawable, path):
    new_image = pdb.gimp_image_duplicate(image)
    drawable = pdb.gimp_image_merge_visible_layers(new_image, CLIP_TO_IMAGE)
    drawable = pdb.gimp_item_transform_flip_simple(drawable, 1, True, 0.0)
    pdb.file_dds_save(new_image, drawable, path, path
                      , 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    pdb.gimp_image_delete(new_image)

register(
    "python-fu-plugin-notruf",
    "Als Notruf Skin exportieren",
    "Als Notruf Skin exportieren",
    "Kaktushose",
    "Kaktushose",
    "2020",
    "<Image>/Image/Exportieren als Notruf Skin...",
    "*",
    [
        (PF_STRING, "Dateipfad", "Dateipfad", home + "\\Documents\\Notruf 2 Skins")
    ],
    [],
    plugin_main)

main()
