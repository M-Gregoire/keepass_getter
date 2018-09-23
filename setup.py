from setuptools import setup

setup(name='keepass_getter',
      version='1.0.0',
      description='Python library to retrieve passwords from CLI & Python using KeepassHTTP',
      url='https://github.com/M-Gregoire/keepass-getter',
      author='Grégoire Martinache',
      license='Apache-2.0',
      packages=['keepass_getter'],
      install_requires=['configparser', 'requests', 'cryptography'],
      include_package_data=True,
      )
