from dingus import Dingus, DingusTestCase

from markdown_processor import process_markdown
import markdown_processor as mod


class BaseProcessing(DingusTestCase(process_markdown)):

    def setup(self):
        super(BaseProcessing, self).setup()
        self.src_dir = Dingus('src_dir')
        self.target_dir = Dingus('target_dir')

        mod.os.listdir.return_value = ['hello_world.markdown']
        mod.os.path.splitext.return_value = ('hello_world', 'markdown')

        self.md = mod.markdown.Markdown()

    def should_check_existance_of_target_dir(self):
        assert mod.os.path.calls('exists', self.target_dir)

    def should_create_markdown_instance(self):
        assert mod.markdown.calls(
            'Markdown',
            extensions=['codehilite']
        ).once()

    def should_find_markdown_files(self):
        assert mod.os.calls('listdir', self.src_dir)

    def should_convert_files(self):

        in_file = mod.os.path.join(self.src_dir, 'hello_world.markdown')
        out_file = mod.os.path.join(self.target_dir, 'hello_world.html')
        assert self.md.calls('convertFile', in_file, out_file)


class WhenProcessingMarkdown(BaseProcessing):

    def setup(self):
        BaseProcessing.setup(self)
        mod.os.path.exists.return_value = False
        process_markdown(self.src_dir, self.target_dir)

    def should_create_target_directory(self):
        assert mod.os.calls('mkdir', self.target_dir)


class WhenProcessingMarkdownAndDirectoryExists(BaseProcessing):

    def setup(self):
        BaseProcessing.setup(self)
        mod.os.path.exists.return_value = True
        process_markdown(self.src_dir, self.target_dir)

    def should_not_create_target_directory(self):
        assert not mod.os.calls('mkdir')
