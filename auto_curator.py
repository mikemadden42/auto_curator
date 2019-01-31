#!/usr/bin/env python
"""Automatically curate Elastic indices"""

import templates


def main():
    """Automatically curate Elastic indices"""
    templates.process_templates()
    configs = templates.get_ymls()
    for config in configs:
        print('/usr/bin/curator --dry-run --config yml/curator.yml ' + 'yml/' +
              config)


if __name__ == '__main__':
    main()
