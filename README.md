# auto_curator
Automation for Elasticsearch Curator

```bash
/usr/bin/curator --config yml/curator.yml yml/delete_indices_action_INDEX.yml
/usr/bin/curator --dry-run --config yml/curator.yml yml/delete_indices_action_INDEX.yml

auto_curator.py 2>&1 | tee auto_curator.log
```
