import setuptools

# PRODUCTION setup.py: name, version, install_requires, packages only
setuptools.setup(
    name='django-bulk_delete',
    version='1.0.1',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)