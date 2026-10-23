from pathlib import Path
p = Path(__file__).resolve().parents[1]
for name in ('black-gold', 'nebula-purple', 'minimal-graphite'):
    s = (p / 'themes' / (name + '.css')).read_text(encoding='utf-8')
    assert '--ly-accent:' in s and '.cardBox' in s and '@media' in s, name
    assert '@import' not in s and 'url(' not in s, name
print('3 standalone CSS themes verified (syntax compatibility not guaranteed)')
