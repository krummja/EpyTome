from setuptools import setup, find_packages

setup(
    name='EpyTome',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    packages=['epytome'],
    install_requires=[
        'Click',
        'python-docx'
        ],
    entry_points='''
        [console scripts]

    '''
    )
