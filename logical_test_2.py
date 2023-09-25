"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""


def number_to_roman() -> str:
    try:
        num: int = int(input("Enter number between 1 - 1000: "))

        if num < 1 or num > 1000:
            print("Please enter number in range 1 - 1000")

            return "Please enter number in range 1 - 1000"
    except ValueError as error:
        print(error)
        print("Please enter number in range 1 - 1000")

        return error

    roman: str = ""

    dict_of_roman: dict = {
        "1": "I",
        "4": "IV",
        "5": "V",
        "9": "IX",
        "10": "X",
        "40": "XL",
        "50": "L",
        "90": "XC",
        "100": "C",
        "400": "CD",
        "500": "D",
        "900": "CM",
        "1000": "M",
    }

    if num == 1000:
        roman += "M"
    else:
        if num >= 500:
            while num > 499:
                roman += dict_of_roman["900"] if num > 899 else dict_of_roman["500"]
                num -= 900 if num > 899 else 500
        if num >= 100:
            while num > 99:
                roman += dict_of_roman["400"] if num > 399 else dict_of_roman["100"]
                num -= 400 if num > 399 else 100
        if num >= 50:
            while num > 49:
                roman += dict_of_roman["90"] if num > 89 else dict_of_roman["50"]
                num -= 90 if num > 89 else 50
        if num >= 10:
            while num > 9:
                roman += dict_of_roman["40"] if num > 39 else dict_of_roman["10"]
                num -= 40 if num > 39 else 10
        if num > 4:
            roman += dict_of_roman["9"] if num > 8 else dict_of_roman["5"]
            num -= 9 if num > 8 else 5
        else:
            while num > 0:
                roman += dict_of_roman["4"] if num > 3 else dict_of_roman["1"]
                num -= 4 if num > 3 else 1

    print(roman)

    return roman


if __name__ == "__main__":
    number_to_roman()
