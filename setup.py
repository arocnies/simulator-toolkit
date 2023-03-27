from distutils.core import setup

setup(
    name='simtoolkit',
    version='1.0',
    packages=['simtoolkit'],
    install_requires=[
        'matplotlib~=3.7.1',
        'numpy==1.23.5',
        'numpy-quaternion==2022.4.3'
    ]
)
