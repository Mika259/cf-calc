# ambil dan guna library time
from time import sleep as wait

# boleh baca sudah saya permudahkan
# salah ubah habis semua

# fungsi kira dengan formula fahrenheit ke celcius
def f_c(fahrenheit):
    celcius = (fahrenheit-32)/1.8;
    return celcius;

# fungsi kira dengan formula celcius ke fahrenheit
def c_f(celcius):
    fahrenheit = celcius * 1.8 + 32;
    return fahrenheit;

# buat teks hiasan
def process(text):
    print("==[%s]=="%text)

# buat garisan penutup output
def endline(bil):
    print("="*bil)

# disini looping, minta input selagi boleh(tak error)
while True:
    try:
        choose = input("C°>F°(1) or F°>C°(2) or Exit(e) or Info(i)\nChoose :")

        # kalau pilih 1
        if choose == '1':
            process("Calculate")
            celcius = float(input("C° :"));wait(1.3)
            print("C° > F°: {:.2f}".format(c_f(celcius)))
            endline(15)

        # kalau pilih 2
        elif choose == '2':
            process("Calculate")
            fahrenheit = float(input("F° :"));wait(1.3)
            print("F° > C°:",round(f_c(fahrenheit)))
            endline(15)

        # kalau pilih i
        elif choose == 'i':
            print("\nTool dibuat oleh Daniel Hakim :)\n")

        # kalau pilih e
        elif choose == "e":
            exit("Thanks for using me :)")

        # lain-lain
        else:
            print(f"command :'{choose}' is not valid!")
    except Exception as e:
        print(e)
