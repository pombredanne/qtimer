import alembic.config as config
import configparser
from os import path

from qtimer.strings import strings


class Section(object):
	pass


class Config(config.Config):
	def __init__(self, configPath):
		super(Config, self).__init__(configPath)

		if not path.exists(configPath):
			raise RuntimeError(strings['no_config'])

		parser = configparser.ConfigParser()
		with open(configPath) as configFile:
			parser.readfp(configFile)

		isLoggerSection = lambda section: not (section.startswith('logger')
			or section.startswith('handler') or section.startswith('formatter'))

		sections = filter(isLoggerSection, parser.sections())
		for section in sections:
			setattr(self, section, Section())
			mySection = getattr(self, section)
			for option in parser.options(section):
				attr_name = option.replace('.', '_')
				value = parser.get(section, option)
				setattr(mySection, attr_name, value)
