"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""


def numberToThaiText() -> str:
    try:
        num: int = int(input("Enter the number between 0 - 9999999: "))

        if num < 0 or num > 9999999:
            print("Please enter number in range 0 - 9999999")

            return "Please enter number in range 0 - 9999999"
    except ValueError as error:
        print(error)
        print("Please enter number in range 0 - 9999999")

        return error

    list_of_str_num: list = list(str(num))

    def digit_str_to_thai_text(digit: str) -> str:
        dict_of_digit: dict = {
            "1": "เอ็ด"
            if list_of_str_num.__len__() == 1
            else ""
            if list_of_str_num.__len__() == 2
            else "หนึ่ง",
            "2": "ยี่" if list_of_str_num.__len__() == 2 else "สอง",
            "3": "สาม",
            "4": "สี่",
            "5": "ห้า",
            "6": "หก",
            "7": "เจ็ด",
            "8": "แปด",
            "9": "เก้า",
        }

        return dict_of_digit[digit]

    list_of_digits: list = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]

    thai_text: str = ""

    while list_of_str_num.__len__() > 0:
        if list_of_str_num[0] != "0":
            thai_text += f"{digit_str_to_thai_text(list_of_str_num[0])}{list_of_digits[list_of_str_num.__len__()-1]}"

        list_of_str_num.pop(0)

    print(thai_text)
    return thai_text


if __name__ == "__main__":
    numberToThaiText()
