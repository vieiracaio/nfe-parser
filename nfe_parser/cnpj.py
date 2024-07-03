def only_digits(s: str) -> str:
    return ''.join(c for c in s if c.isdigit())

def format_cnpj(s: str) -> str:
    d = only_digits(s).zfill(14)
    return f'{d[:2]}.{d[2:5]}.{d[5:8]}/{d[8:12]}-{d[12:]}'
