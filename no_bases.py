def mul_h(a: str, b: str) -> str:
    product = ""
    carry = 0
    base_16_alpha_map = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    alpha_base_16_map = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    for idx in range(len(a) - 1, -1, -1):
        res = (
            int(alpha_base_16_map.get(a[idx], a[idx]))
            * int(alpha_base_16_map.get(b, b))
            + carry
        )
        if res >= 16:
            carry = res // 16
            res = res % 16
        else:
            carry = 0
        res = base_16_alpha_map.get(res, res)
        product = str(res) + product
    product = str(carry) + product if carry != 0 else product
    return product


def subtract_b2(minuend: str, subtrahend: str):
    longest_length = len(minuend) if len(minuend) > len(subtrahend) else len(subtrahend)
    subtrahend = subtrahend.zfill(longest_length)
    minuend = minuend.zfill(longest_length)
    complement_1 = negate(subtrahend)
    complement_2 = adder_b2(complement_1, "1")
    result = adder_b2(minuend, complement_2)
    # remove the carry overflow bit
    result = result[len(result) - longest_length :]
    return result


def negate(no: str):
    new_no = ""
    for char in no:
        new_char = "0" if char == "1" else "1"
        new_no += new_char
    return new_no


def adder_b2(augend, addend):
    longest_length = len(augend) if len(augend) > len(addend) else len(addend)
    augend = augend.zfill(longest_length)
    addend = addend.zfill(longest_length)
    result = ""
    carry = 0
    for idx in range(longest_length - 1, -1, -1):
        res = int(augend[idx]) + int(addend[idx]) + carry
        if res >= 2:
            carry = res // 2
            res = res % 2
        else:
            carry = 0
        result = str(res) + result
    result = str(carry) + result if carry != 0 else result
    return result


if __name__ == "__main__":
    print(mul_h("B", "D"))
    print(subtract_b2("01101", "00111"))
