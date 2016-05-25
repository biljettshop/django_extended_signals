from setuptools import setup

tests_require = [
    'django',
    'mock',
]

setup(
    name='django_extended_signals',
    version='1.0.0',
    url='https://github.com/biljettshop/django_extended_signals/',
    description=(
        'Provides extended signals to Django'
    ),
    author='Thomas Lundqvist',
    author_email='thomas@biljettshop.se',
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
    },
    #test_suite='.runtests.runtests',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    packages=[
        'extended_signals',
    ],
    install_requires=[
        'six>=1.6.1',
        'Django>=1.8',
    ]
)
