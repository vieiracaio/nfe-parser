from decimal import Decimal, ROUND_HALF_UP

def brl(n) -> Decimal:
    return Decimal(str(n)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
