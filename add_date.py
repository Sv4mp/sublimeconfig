import sublime, sublime_plugin, time

class InsertDateComment(sublime_plugin.TextCommand):
    def run(self, edit):
        date = time.strftime("<%d-%m-%Y  %H:%M>")
        self.view.run_command("toggle_comment")
        self.view.run_command("insert", {
            "characters": "// Date - %s" % date
            })