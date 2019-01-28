#!/usr/bin/env python
"""Process curator template"""
import os
from jinja2 import Environment, FileSystemLoader
import indices


def process_templates():
    """Process template"""
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template('curator.yml.j2')

    for i in indices.get_indices('indices.csv'):
        filename = os.path.join(root, 'yml', 'curator_' + i['index'] + '.yml')
        with open(filename, 'w') as temp:
            temp.write(template.render(index=i['index'], age=i['age']))


def main():
    """Process template"""
    process_templates()


if __name__ == '__main__':
    main()
