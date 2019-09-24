def num_to_word(num: int) -> str:
    words = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirdteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "fourty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand"
    }

    bases = [1000, 100, 10, 1]
    digits = {}
    acc = []

    for base in bases:
        digits[base] = num // base
        num = num % base

    for d, v in digits.items():
        if (d * v) < 100:
            acc.append(words[d * v])
        else:
            acc.append(words[v] + words[d])

    return "".join(acc)
