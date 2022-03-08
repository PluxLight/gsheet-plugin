"""
====================================
 :mod:`your.demo.helloworld`
====================================
.. moduleauthor:: Your Name <user@modify.me>
.. note::

Description
===========
Your Demo plugin module sample
"""
# Authors
# ===========
#
# * Your Name
#
# Change Log
# --------
#
#  * [2019/03/08]
#     - add icon
#  * [2018/10/28]
#     - starting

################################################################################
import sys
from alabs.common.util.vvargs import ModuleContext, func_log, \
    ArgsError, ArgsExit, get_icon_path
from your.demo.gsheet import google_sheet


################################################################################
@func_log
def g_sheet(mcxt, argspec):
    """
    plugin job function
    :param mcxt: module context
    :param argspec: argument spec
    :return: True
    """
    mcxt.logger.info('>>>starting...')

    google_sheet.main(argspec.url, argspec.sheet_range, argspec.json_file,
                      argspec.sheet_name)

    mcxt.logger.info('>>>end...')
    return 0


################################################################################
def _main(*args):
    """
    Build user argument and options and call plugin job function
    :param args: user arguments
    :return: return value from plugin job function
    """
    with ModuleContext(
        owner='jeon',
        group='demo',
        version='1.2',
        platform=['windows', 'darwin', 'linux'],
        output_type='text',
        display_name='Google Spreadsheet',
        icon_path=get_icon_path(__file__),
        description='Google Spreadsheets Read Only',
    ) as mcxt:
        # ##################################### for app dependent parameters
        mcxt.add_argument('url',
                          display_name='URL',
                          help='google spreadsheets url')
        mcxt.add_argument('sheet_name',
                          display_name='Sheet Name',
                          help='if first sheet, please empty the compartment')
        mcxt.add_argument('sheet_range',
                          display_name='Range',
                          help='sheet range. ex) A2:E')
        mcxt.add_argument('json_file',
                          display_name='JSON File',
                          input_method='fileread',
                          help='credentials.json location')
        argspec = mcxt.parse_args(args)
        return g_sheet(mcxt, argspec)


################################################################################
def main(*args):
    try:
        return _main(*args)
    except ArgsError as err:
        sys.stderr.write('Error: %s\nPlease -h to print help\n' % str(err))
    except ArgsExit as _:
        pass
