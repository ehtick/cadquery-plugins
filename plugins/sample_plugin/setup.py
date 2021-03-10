from setuptools import setup

# Change these variables to set the information for your plugin
version = '1.0.0' # Please update this version number when updating the plugin
plugin_name = 'sample_plugin' # The name of your plugin
description = 'What does your plugin do?'
long_description = 'Extended explanation of your plugin'
author = 'Your name'
author_email = 'optional, you can put GitHub user name instead'
packages = [] # List of packages that will be installed with this plugin
install_requires = [] # Any dependencies that pip also needs to install to make this plugin work


setup(
    name=plugin_name,
    version=version,
    url='https://github.com/CadQuery/cadquery-plugins',
    license='Apache Public License 2.0',
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    packages=packages,
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    test_suite='tests',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Topic :: Scientific/Engineering'
    ]
)