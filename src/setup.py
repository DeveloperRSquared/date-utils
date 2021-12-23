from pathlib import Path
from typing import List

from setuptools import find_packages  # type: ignore[import]
from setuptools import setup

from datetime_helpers import __version__

setup_directory = Path(__file__).absolute().parent


def parse_requirements(requirements_file: str) -> List[str]:
    if not Path(requirements_file).is_file():
        raise Exception(f'Invalid file: {requirements_file!r} passed to parse_requirements. File does not exist.')
    requirements: List[str] = []
    with open(file=requirements_file, mode='r', encoding='utf-8') as reqs_file:
        for requirement in reqs_file.read().splitlines():
            if requirement and not requirement.startswith('--'):
                requirements.append(requirement)
    return requirements


with open(file=str(setup_directory.parent / 'README.md'), mode='r', encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='datetime-helpers',
    version=__version__,
    description="Util for working with date and datetime objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/DeveloperRSquared/datetime-helpers/',
    packages=find_packages(exclude=['tests*']),
    license='MIT LICENSE',
    python_requires='>=3.7',
    install_requires=parse_requirements(requirements_file=str(Path(setup_directory) / 'requirements.txt')),
    tests_require=parse_requirements(requirements_file=str(Path(setup_directory) / 'requirements.dev.txt')),
    package_data={
        'datetime_helpers': [
            'py.typed',
        ]
    },
    test_suite='tests',
    include_package_data=True,
    extras_require={},
    keywords=['date', 'datetime', 'api', 'web', 'rest', 'python'],
    classifiers=[
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Typing :: Typed',
    ],
    project_urls={
        'Documentation': 'https://github.com/DeveloperRSquared/datetime-helpers#datetime-helpers',
        'Funding': 'https://www.paypal.com/paypalme/rikhilrai',
        'Repository': 'https://github.com/DeveloperRSquared/datetime-helpers/',
        'Source': 'https://github.com/DeveloperRSquared/datetime-helpers/',
        'Tracker': 'https://github.com/DeveloperRSquared/datetime-helpers/issues',
    },
)