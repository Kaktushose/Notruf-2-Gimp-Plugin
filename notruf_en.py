# -*- coding: utf-8 -*-

from gimpfu import *

options = ["tex", "mtl", "nrm"]

def plugin_main(image, drawable, name, option, path):
    if not name:
        gimp.message("Please specify a name!")
        return
        
    if not path:
        gimp.message("Please specify a directory!")
        return

    path = path + "\\" + name + "_" + options[option] + ".dds"

    new_image = pdb.gimp_image_duplicate(image)
    drawable = pdb.gimp_image_merge_visible_layers(new_image, CLIP_TO_IMAGE)
    drawable = pdb.gimp_item_transform_flip_simple(drawable, 1, True, 0.0)

    try:
        pdb.file_dds_save(new_image, drawable, path, path
                            , 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        pdb.gimp_image_delete(new_image)
    except WindowsError as e:
        gimp.message(str(e))
    except RuntimeError as e:
        print(str(e))

    gimp.message("Successfully saved file at " + str(path))


register(
    "Notruf-Gimp-Plugin",
    "Export As Emergency Call 112 Skin",
    "Export As Emergency Call 112 Skin",
    "Kaktushose", "Kaktushose", "2020",
    "<Image>/File/Export/Export As Emergency Call 112 Skin",
    "*",
    [
        (PF_STRING, "name", "File Name", ""),
        (PF_OPTION, "type", "Skin Type", 0, options),
        (PF_DIRNAME, "directory", "Directory", "")
    ],
    [],
    plugin_main)

main()
