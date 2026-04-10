from django import template

register = template.Library()

# Gradients and emojis mapped by recipe slug keywords
# Maps slug keywords → (css-class-suffix, emoji)
RECIPE_THEMES = {
    'bobotie':    ('red',    '🍲'),
    'malva':      ('orange', '🍮'),
    'pudding':    ('purple', '🍮'),
    'pap':        ('grey',   '🌽'),
    'milk-tart':  ('purple', '🥧'),
    'melktert':   ('purple', '🥧'),
    'tart':       ('purple', '🥧'),
    'vetkoek':    ('brown',  '🍞'),
    'bread':      ('brown',  '🍞'),
    'braai':      ('crimson','🍗'),
    'peri':       ('crimson','🍗'),
    'chicken':    ('crimson','🍗'),
    'koeksister': ('yellow', '🍩'),
    'umngqusho':  ('green',  '🫘'),
    'samp':       ('green',  '🫘'),
    'beef':       ('darkred','🥩'),
    'lamb':       ('darkred','🥩'),
    'cake':       ('pink',   '🎂'),
    'soup':       ('blue',   '🍜'),
    'salad':      ('green',  '🥗'),
    'pasta':      ('amber',  '🍝'),
    'rice':       ('slate',  '🍚'),
    'fish':       ('teal',   '🐟'),
    'curry':      ('orange', '🍛'),
    'stew':       ('darkred','🍲'),
}

DEFAULT_CLASSES = ['red', 'teal', 'amber', 'blue', 'purple']


@register.filter
def recipe_theme_class(slug):
    """Returns a CSS class suffix for the recipe card gradient."""
    slug_lower = slug.lower()
    for keyword, (cls, _) in RECIPE_THEMES.items():
        if keyword in slug_lower:
            return cls
    idx = sum(ord(c) for c in slug) % len(DEFAULT_CLASSES)
    return DEFAULT_CLASSES[idx]


@register.filter
def recipe_emoji(slug):
    slug_lower = slug.lower()
    for keyword, (_, emoji) in RECIPE_THEMES.items():
        if keyword in slug_lower:
            return emoji
    return '🍽️'
