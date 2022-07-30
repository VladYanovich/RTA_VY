import re
import sys

MODULE_REGEX = r'[_a-zA-Z][_a-zA-Z0-9]+$'

if __name__ == "__main__":
    module_name = '{{ cookiecutter.repo_name }}'
    if not re.match(MODULE_REGEX, module_name):
        print('ERROR: %s is not a valid Python modeule name' % module_name)
        sys.exit(1)

sys.exit(0)