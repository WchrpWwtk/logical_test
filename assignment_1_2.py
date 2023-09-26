# เขียนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน Array ด้วยภาษา python เช่น [1,2,1,3,5,6,4] ลำดับที่มีค่ามากที่สุด คือ
# index = 5 โดยไม่ให้ใช้ฟังก์ชั่นที่มีอยู่แล้ว ให้ใช้แค่ลูปกับการเช็คเงื่อนไข


def find_index_of_max_number(nums: list) -> int:
    result: dict = {"num": nums[0], "index": 0}

    for i in range(1, len(nums)):
        if nums[i] > result["num"]:
            result = {"num": nums[i], "index": i}

    return result["index"]


if __name__ == "__main__":
    print(find_index_of_max_number([1, 2, 1, 3, 6, 5, 4]))
