# Written by Jack Franklin (www.jackfranklin.co.uk)

# Thanks to Eric Martel for his Stack Overflow search plugin - which this is based heavily off: https://github.com/ericmartel/Sublime-Text-2-Stackoverflow-Plugin


# available commands
#   mdn_search_selection
#   mdn_search_from_input


import sublime
import sublime_plugin

import subprocess
import webbrowser


def SearchFor(text):
    url = 'https://developer.mozilla.org/en-US/search?q=' + text.replace(' ', '%20')
    webbrowser.open_new_tab(url)


class MdnSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                text = self.view.word(selection)

            text = self.view.substr(selection)
            SearchFor(text)


class MdnSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Search the MDN for', '',
            self.on_done, self.on_change, self.on_cancel)

    def on_done(self, input):
        SearchFor(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass
