import setuptools
setuptools.setup(
    name='PipUpgradeall',
    py_modules=['pipupgradeall'],
    entry_points={"console_scripts": ["pipupgradeall = pipupgradeall:main"],},
)
