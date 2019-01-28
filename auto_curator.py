#!/usr/bin/env python
"""Automatically curate Elastic indices"""

import templates


def main():
    """Automatically curate Elastic indices"""
    templates.process_templates()


if __name__ == '__main__':
    main()
