import os.path

from markdown_processor import process_markdown

class WhenRunningProcessor(object):

    @classmethod
    def setup_class(cls):
        cls.src_dir = 'src_example'
        cls.target_dir = 'target_dir'

        process_markdown(cls.src_dir, cls.target_dir)

    def should_have_html_hello_world(self):
        file_path = os.path.join(self.target_dir, 'hello_world.html')
        content = open(file_path, 'r').read()
        assert '<p>Hello World!</p>' in content

