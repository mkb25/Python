print("Hello World !")
x = 5
y = 10
z = x + y
print("Sum:", z)
name = input("Enter your name: ") 
print(f"Hello {name} !")
print(type(name))
my_str = ["Hello", "World"]
print(",".join(my_str))
# print("Hello " + name + " !")
int_var = 10
int_var1 = 9

print(int_var/int_var1)
print(int_var//int_var1)

def caser() :
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift = 5
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet,shifted_alphabet)
    text = 'hello world'
    encrypted_text = text.translate(translation_table)
    print(encrypted_text)

caser()