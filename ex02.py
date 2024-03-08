input_string = input("Informe uma string: ") 
reversed_string = ""
for char in input_string:
    reversed_string = char + reversed_string

print(f"String invertida: {reversed_string}")
