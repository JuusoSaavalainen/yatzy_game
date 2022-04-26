class Checkrules:
    def __init__(self):
        pass

    def possibility_all(self, pos_list, num_list):
        for i in range(0, 6):
            pos_list[i] = True
        pos_list[12] = True
        max_num = 0
        counter = [num_list.count(i + 1) for i in range(6)]
        consec_sum = (min(num_list) + max(num_list)) * (max(num_list) - min(num_list) + 1) / 2

        for i in range(1, 7):
            if num_list.count(i + 1) > max_num:
                max_num = num_list.count(i + 1)

        if max_num >= 3:
            pos_list[6] = True
            if max_num >= 4:
                pos_list[7] = True
                if max_num >= 5:
                    pos_list[11] = True

        if max_num < 3:
            pos_list[6] = False
            pos_list[7] = False
            pos_list[8] = False
            pos_list[11] = False

        elif max_num == 3:
            pos_list[7] = False
            pos_list[11] = False

        if len(set(num_list)) == len(num_list):
            if 1 in num_list and consec_sum == sum(num_list):
                pos_list[9] = True
            if 6 in num_list and consec_sum == sum(num_list):
                pos_list[10] = True
        if 2 in counter and 3 in counter:
            pos_list[8] = True
        return pos_list

    def points(self, score, pointer):
        if pointer == 12:
            return sum(score)

        if pointer == 11:
            return 50

        if pointer == 10:
            return 20

        if pointer == 9:
            return 15

        if pointer == 8:
            return 25

        if pointer == 7:
            return max(set(score), key=score.count)*4

        if pointer == 6:
            return max(set(score), key=score.count)*3

        if pointer == 5 and pointer+1 in score:
            return (6) * (score.count(6))

        if pointer == 4 and pointer+1 in score:
            return (5) * (score.count(5))

        if pointer == 3 and pointer+1 in score:
            return (4) * (score.count(4))

        if pointer == 2 and pointer+1 in score:
            return (3) * (score.count(3))

        if pointer == 1 and pointer+1 in score:
            return (2) * (score.count(2))

        if pointer == 0 and pointer+1 in score:
            return (1) * (score.count(1))

        else:
            return 0
            