#!/bin/bash

for i in yml/*.yml; do
	/usr/bin/curator --dry-run --config yml/curator.yml $i
	#/usr/bin/curator --config yml/curator.yml $i
done
