"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

# input = 128
# output = "CXXVIII"


def number_to_roman() -> str:
    try:
        num: int = int(input("Enter number between 1 - 999: "))

        if num < 1 or num > 999:
            return "Please enter number in range 1 - 999"
    except ValueError as error:
        print(error)
        print("Please enter number in range 1 - 999")

        return error

    print(num)

    return ""


if __name__ == "__main__":
    number_to_roman()
