def num_to_word(num):
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
        13: "thirteen",
        14: "forteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }
    # convert to string
    str_num = str(num)

    # position
    length = len(str_num)

    acc = ""
    for pos in range(length):

        base = 10 ** (length - (pos + 1))
        num_at_pos = int(str_num[pos])

        if base == 10 and num_at_pos < 2:
            that = int(str_num[pos] + str_num[pos + 1])
            acc += words.get(that)
            break
        elif base == 100 and num_at_pos > 0:
            acc += words.get(num_at_pos) + "hundred"
        elif base == 1000:
            acc += words.get(num_at_pos) + "thousand"
        else:
            that = base * num_at_pos
            acc += words.get(that)

    return acc
