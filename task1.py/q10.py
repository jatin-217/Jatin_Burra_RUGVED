def is_valid_credit_card(number: str) -> bool:
    number =number.replace(" ","").replace("-","")
    if not number.isdigit():
        return False
    total =0
    reverse_digits =number[::-1]
    for i, digit in enumerate(reverse_digits):
        n=int(digit)
        if i%2==1:
            n*=2
            if n>9:
                n-=9
        total+=n
    return total % 10 == 0
