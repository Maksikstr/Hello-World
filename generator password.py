import random
digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
chars = ""
count_pasw = int(input("Колличество паролей для генерации??:"))
pasw_len = int(input("Длинна одного пароля??:"))
ent_num = input("Включать ли цифры 0123456789 ? y/n:")
ent_up_bukv = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ ? y/n:")
ent_low_bukv = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz ? y/n:")
ent_simv = input("Включать ли символы !#$%&*+-=?@^_ ? y/n:")
del_simv = input("Исключать ли неоднозначные символы il1Lo0O ? y/n:")
if ent_num == "y":
    chars = chars + digits
if ent_up_bukv == "y":
    chars = chars + uppercase_letters
if ent_low_bukv == "y":
    chars = chars + lowercase_letters
if ent_simv == "y":
    chars = chars + punctuation
if del_simv == "y":
    for i in chars:
        if i in "il1Lo0O":
            chars = chars.replace(i, "")


def generate_password(pasw_len, chars):
    password = ""
    for _ in range(pasw_len):
        password += random.choice(chars)
    return password


for _ in range(count_pasw):
    print(generate_password(pasw_len, chars))

