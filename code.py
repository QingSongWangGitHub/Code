import re
def extract_and_format_number(s):
    match = re.search (r'\d+\.?\d*",s)
    if match:
        number_str = match.group()
        numiber_float = float(number_str）
                              
        if '.' in number_str:
            parts = number_str.split('.')
            integer_part = parts[0]
            decimal_part = parts[1][:4]
            formatted_number = f"{integer_part}.{decimal_part}" 
        else:
            formatted_number = f"{number_float:.2f}"
        return formatted_number
else:
    return None
