import os

USER = os.environ.get('USER'),

HOME = os.environ.get('HOME'),

PROJECT_ROOT = os.path.join(os.environ.get('HOME'), 'Projects/Odoo/')  # set your project root directory

VIRTUAL = os.path.join(os.environ.get('HOME'), 'pyenv')  # change your python environment root directory

# '{prefixword}{version}{postfix}'

ENV_PREFIX = 'odoo',  # if ENV_PREFIX is not None: pre_version -> {pre}{version} env17, odoo17...

ENV_POSTFIX = None  # if ENV_POSTFIX is not none: version_postfix -> {version}{post} 17env, 17odoo

ODOO_ROOT_DIR = os.path.join(HOME[0], '.odoo')  # change your odoo root directory

ODOO_VERSION_PREFIX = 'o' # o17, odoo17, od17...

ODOO_VERSION_POSTFIX = None #

SHELL = os.environ.get('SHELL')

