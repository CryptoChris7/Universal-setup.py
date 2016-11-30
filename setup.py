from setuptools import setup, find_packages
import os
import re

HTTP = re.compile('^https?://.+#egg=(.+)$')


class UniversalSetupError(Exception):
    pass


def parse_dependency_info() -> dict:
    """Reads dependency info from requirements.txt"""
    packages = []
    links = []
    with open('requirements.txt') as dependencies:
        for line in map(str.strip, dependencies):
            link = HTTP.match(line)
            if link:
                packages.append(link.group(1))
                links.append(line)
            else:
                packages.append(line)
    return {'install_requires': packages, 'dependency_links': links}


def read_metadata() -> dict:
    """Finds the package to install and returns it's metadata."""
    for entry in os.scandir():
        if entry.is_dir():
            package_init = os.path.join(entry.name, '__init__.py')
            if os.path.isfile(package_init):
                break
    else:
        raise UniversalSetupError('No package found!')

    metadata = {'name': entry.name}
    name_map = {'__version__': 'version',
                '__author__': 'author',
                '__email__': 'author_email',
                '__license__': 'license'}

    with open(package_init) as init:
        first_line = next(init)
        metadata['description'] = first_line.strip('\n\'"')
        while len(name_map):
            try:
                line = next(init).strip()
            except StopIteration:
                print('Missing optional metadata:', ', '.join(name_map))
                break

            for name in name_map:
                if line.startswith(name):
                    break
            else:
                continue

            try:
                new_name = name_map.pop(name)
            except KeyError:
                raise UniversalSetupError('repeated keys in package init!')

            metadata[new_name] = line.split('=')[1].strip('\'\" ')

    metadata['packages'] = find_packages()
    metadata.update(parse_dependency_info())
    return metadata

setup(**read_metadata())
