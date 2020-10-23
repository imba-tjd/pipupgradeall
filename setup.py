import setuptools
setuptools.setup(
    name='pipupgradeall',
    py_modules=['pipupgradeall'],
    entry_points={"console_scripts": ["pipupgradeall = pipupgradeall:_main"],},
)
