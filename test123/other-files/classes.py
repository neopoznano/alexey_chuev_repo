class EmailProtection:
    def __init__(self, symbol):

        self.symbol = symbol

    def protect_email(self, origin_email):
        count = 0
        protected_email = ""
        for i in origin_email:
            if i != "@":
                protected_email += self.symbol
            else:
                protected_email += origin_email[count:]
                break
            count += 1
        return protected_email


class PhoneProtection:
    def __init__(self, symbol, protected_symbols_count=3):
        self.symbol = symbol
        self.protected_symbols_count = protected_symbols_count

    def protect_phone_number(self, origin_number):
        temp_number = list(origin_number[::-1])
        count = 0
        index = 0
        for i in temp_number:
            if count <= self.protected_symbols_count:
                if i == " ":
                    if temp_number[index + 1] == " ":
                        temp_number[index] = ""
                        index += 1
                        continue
                    else:
                        index += 1
                        continue
                temp_number[index] = self.symbol
            else:
                break
            count += 1
            index += 1
        return "".join(temp_number[::-1])


class SkypeProtection:

    def protect_skype(self, origin_skype):
        start_index = origin_skype.find("skype:")
        end_index = origin_skype.find("?")
        if end_index == -1:
            return origin_skype[:start_index + 6] + "xxx"
        return origin_skype[:start_index + 6] + "xxx" + origin_skype[end_index:]


x = PhoneProtection("x", 5)
print(x.protect_phone_number("8 800 555 35       35"))
y = SkypeProtection()
print(y.protect_skype("skype:alex.max"))
print(y.protect_skype("<a href=\"skype:alex.max?call\">skype</a>"))
z = EmailProtection("L")
print(z.protect_email("qwerty@gmail.com"))
