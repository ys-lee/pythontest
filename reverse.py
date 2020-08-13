
def reverse(input):
    # corner case
    if not input: return {}

    key = output = list(input.keys())[0]
    input = input[key]

    while type(input) is dict:
        key = list(input.keys())[0]
        output = {key: output}
        input = input[key]
    
    return {input: output}
