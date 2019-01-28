#!/usr/bin/env python
"""Process curator template"""
import os
from jinja2 import Environment, FileSystemLoader


def process_template():
    """Process template"""
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template('curator.yml.j2')

    filename = os.path.join(root, 'yml', 'curator.yml')
    with open(filename, 'w') as temp:
        temp.write(template.render(index='filebeat'))


if __name__ == '__main__':
    process_template()
