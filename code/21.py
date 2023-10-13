original_str = ('Enter original string:')
delete_str = ('Substring to delete:')
index = original_str.find(delete_str)
left_str = original_str[0:index]
right_str = original_str[index + len(delete_str):]

new_str = left_str + right_str
print('/nThe modified string is: [0]'.format(new_str))
