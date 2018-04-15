# Habrahabr.ru/post/239081
# Парсим на Python: Pyparsing для новичков

from pyparsing import Word, alphas, ZeroOrMore, Suppress, Optional
module_name = Word(alphas + '_')
full_module_name = (module_name + ZeroOrMore(Suppress('.') + module_name))('modules')
import_as = (Optional(Suppress('as') + module_name))('import_as')
parse_module = (Suppress('import') + full_module_name + import_as).setParseAction(lambda t: {'import': t.modules.asList(), 'as': t.import_as.asList()[0]})
s = 'import matplotlib.piplot as plt'
print(parse_module.parseString(s).asList())

