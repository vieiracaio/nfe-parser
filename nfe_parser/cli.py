import argparse, json, sys
from .parse import parse_nfe

def main():
    p = argparse.ArgumentParser()
    p.add_argument('xml')
    a = p.parse_args()
    print(json.dumps(parse_nfe(open(a.xml, encoding='utf-8').read()), ensure_ascii=False, indent=2))
if __name__ == '__main__':
    main()
