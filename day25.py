text = open('inputtxt/day25input.txt').read().splitlines()

def snafu_to_decimal(s):
    if s:
        *remaining_string, last_character = s
        return snafu_to_decimal(remaining_string) * 5 + '=-012'.find(last_character)-2
    else:
        return 0

def decimal_to_snafu(s):
    if s:
        remaining_string, last_character = divmod(s + 2, 5)
        return decimal_to_snafu(remaining_string) + '=-012'[last_character]
    else:
        return ''
total = 0
for line in text:
    total += snafu_to_decimal(line)
print(decimal_to_snafu(total))


