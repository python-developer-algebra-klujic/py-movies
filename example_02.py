

total_str = "$28,767,189"

total_str = total_str.replace(',', '')

value = float(total_str[1 : ])
currency_symbol = total_str[0]

print(value, currency_symbol)
