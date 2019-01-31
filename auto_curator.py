#!/usr/bin/env python
"""Automatically curate Elastic indices"""

import templates


def curate_indices():
    """Automatically curate indices"""
    configs = templates.get_ymls()
    for config in configs:
        print('/usr/bin/curator --dry-run --config yml/curator.yml ' + 'yml/' +
              config)


def main():
    """Automatically curate Elastic indices"""
    templates.process_templates()
    curate_indices()


if __name__ == '__main__':
    main()
