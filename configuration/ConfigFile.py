import os
from configuration.Settings import SettingsBuilder


class ConfigFile(object):

    def __init__(self, configfile=None):
        self.settings = None

        if configfile is not None:
            fo = self._open_file(configfile)
            self.settings = self._file_reader(fo)

    def _open_file(self, configfile):
        if os.path.isfile(configfile):
            return open(configfile)
        return None

    def _file_reader(self, file_object):
        settings_builder = SettingsBuilder()

        try:
            for l in file_object.readlines():
                line = l.strip()
                if len(line) and line[0] not in ('#', ';'):
                    
                    prep = line.split('#', 1)[0].split(';', 1)[0].split('|', 1)

                    if len(prep) > 1:
                        varname = prep[0].strip()
                        val = prep[1].strip()

                        settings_builder.with_key_value(varname, val)
        except:
            pass
        return settings_builder.build()

    def get_settings(self):
        return self.settings
