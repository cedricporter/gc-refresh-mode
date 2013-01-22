#!/usr/bin/env python
#
#
# Reload Chrome on port 9222
# Code forked and modified by Strzelewicz Alexandre, Stupid ET
#
# Thanks to :
# http://pypi.python.org/pypi/chrome_remote_shell/ (out of date)
# http://www.emacswiki.org/emacs/SaveAndReloadBrowser
# http://pypi.python.org/pypi/remote-webkit-debug
#
# You may install dependency by `pip install remote_webkit_debug`

import remote_webkit_debug


def main():
    sh = remote_webkit_debug.ChromeShell()
    json_tabs = sh.get_tabs()
    tab = sh.pick_tab(json_tabs[0])
    tab.send_command("Page.reload")
    print 'sent reload command to Chromium'


if __name__ == '__main__':
    main()
