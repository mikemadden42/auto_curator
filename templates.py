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
    template = env.get_template('delete_indices_action.yml.j2')

    if not os.path.exists('yml'):
        os.makedirs('yml')

    for i in indices.get_indices('indices.csv'):
        filename = os.path.join(root, 'yml',
                                'delete_indices_action_' + i['index'] + '.yml')
        with open(filename, 'w') as temp:
            temp.write(
                template.render(
                    index_prefix=i['index'], older_than_days=i['age']))


def get_ymls():
    """Process template"""
    root = os.path.dirname(os.path.abspath(__file__))
    yml_dir = os.path.join(root, 'yml')
    return os.listdir(yml_dir)


def main():
    """Process template"""
    process_templates()


if __name__ == '__main__':
    main()
