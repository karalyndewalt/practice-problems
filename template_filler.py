template = '{{customerAge}} {{ customerName}} {{   customerName   }} '

context = {
    "customerName": 'abq',
    "customerAge": '12'
}
#

# render(template, context)

# output should be: 12 abq abq
# cases:
# replace double bracketed keys with use passed vaule
# Could be unbalabnced brackets or single >> are strings and should be passed unchanged
    # {customerAge} => {customerAge} or { customerAge  => { customerAge

# if key not in context {{name}} => ""

# Steps
# make output var (probably list that will be joined on return)
# iterate over string,
# if two consecutive chars are {{ : place on Stack
#     continue to push onto the stack untill you find }}
#         once closing bracket found, clean string and check if it's in the context
#         and replace (or find end of string )
# for all other characters iterate until I find {{
#     append slice to output


def replace_keys(temp, context):
    """Return string with {{key}} from temp replaced with context keys value"""


    output = []

    stack = []
    temp_size = len(temp)

    idx = 0

    while idx <= (temp_size - 1):

        char = temp[idx]

        if idx + 1 > (temp_size - 1):

            next_char = None

        else:
            next_char = temp[idx+1]

        if char == '{' and next_char == '{':
            stack.append('{{')
            idx += 2

        elif char == '}' and next_char == '}':
            stack.append('}}')
#             check for stack value in our context
            temp_key = "".join(stack[1:-1])
            temp_key = temp_key.strip()
            replace_val = context.get(temp_key, '')
            output.append(replace_val)
            idx += 2
            stack = []

        elif len(stack) == 0:
            output.append(char)
            idx += 1

        else:
            stack.append(char)
            idx += 1

    return "".join(output)


print(replace_keys(template, context))
