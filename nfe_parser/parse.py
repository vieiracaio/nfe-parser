from xml.etree import ElementTree as ET
from .money import brl
NS = {"n": "http://www.portalfiscal.inf.br/nfe"}
def parse_nfe(xml: str) -> dict:
    root = ET.fromstring(xml)
    ide = root.find(".//n:ide", NS)
    emit = root.find(".//n:emit", NS)
    total = root.find(".//n:ICMSTot", NS)
    out = {
        "numero": ide.findtext("n:nNF", default="", namespaces=NS) if ide is not None else "",
        "emitente": emit.findtext("n:xNome", default="", namespaces=NS) if emit is not None else "",
        "cnpj": emit.findtext("n:CNPJ", default="", namespaces=NS) if emit is not None else "",
        "valor": str(brl(total.findtext("n:vNF", default="0", namespaces=NS) if total is not None else 0)),
    }
    return out
