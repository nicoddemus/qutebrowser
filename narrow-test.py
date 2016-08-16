files = [
'tests/end2end/test_dummy.py',

# 'tests/unit/test_app.py',
# 'tests/unit/misc/test_autoupdate.py',
# 'tests/unit/misc/test_checkpyver.py',
# 'tests/unit/misc/test_cmdhistory.py',
# 'tests/unit/misc/test_crashdialog.py',
# 'tests/unit/misc/test_earlyinit.py',
# 'tests/unit/misc/test_editor.py',
# 'tests/unit/misc/test_guiprocess.py',
# 'tests/unit/misc/test_ipc.py',
# 'tests/unit/misc/test_keyhints.py',
# 'tests/unit/misc/test_lineparser.py',
# 'tests/unit/misc/test_miscwidgets.py',
# 'tests/unit/misc/test_msgbox.py',
# 'tests/unit/misc/test_pastebin.py',
# 'tests/unit/misc/test_readline.py',
# 'tests/unit/misc/test_sessions.py',




'tests/unit/misc/test_split.py',
'tests/unit/misc/test_split_hypothesis.py',
'tests/unit/utils/test_debug.py',
#'tests/unit/utils/test_error.py', CONFIRMED
'tests/unit/utils/test_javascript.py',
#'tests/unit/utils/test_jinja.py',  CONFIRMED
'tests/unit/utils/test_log.py',
'tests/unit/utils/test_qtutils.py',
'tests/unit/utils/test_standarddir.py',
#'tests/unit/utils/test_typing.py',  CONFIRMED
'tests/unit/utils/test_urlutils.py',
'tests/unit/utils/test_utils.py',
'tests/unit/utils/test_version.py',





# 'tests/unit/utils/usertypes/test_downloadtarget.py',
# 'tests/unit/utils/usertypes/test_enum.py',
# 'tests/unit/utils/usertypes/test_neighborlist.py',
# 'tests/unit/utils/usertypes/test_question.py',
# 'tests/unit/utils/usertypes/test_timer.py',
]

import pytest

pytest.main(files + ['--color=no'])
