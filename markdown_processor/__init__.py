import os

import markdown


def process_markdown(src_dir, target_dir):
    "Converts files from :param src_dir: to html in the :param target_dir:"
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    md = markdown.Markdown(extensions=['codehilite'])

    for file in os.listdir(src_dir):
        name, ext = os.path.splitext(file)

        in_file = os.path.join(src_dir, file)
        out_file = os.path.join(target_dir, name + '.html')
        md.convertFile(in_file, out_file)
