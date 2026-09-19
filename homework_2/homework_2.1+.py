# Проверить правильность пароля.
# Требования к паролю:
# ● длина — 8 символов;
# ● должна быть хотя бы одна заглавная буква;
# ● должна быть хотя бы одна строчная буква;
# ● должна быть хотя бы одна цифра.

password = ""
flags = {
    'Up': False,
    'low': False,
    'number': False
}

if len(password) == 8:
    for i in password:
        if i.isalpha():
            if i.isupper():
                flags['Up'] = True
            elif i.islower():
                flags['low'] = True
        elif i.isdigit():
                flags['number'] = True
    if not (flags['Up'] and flags['low'] and flags['number']):
        print("Invalid password")
    else:
        print("Valid Password")
else:
    print("Invalid password")

