left = {
    "fond": "enamored",
    "wrath": "anger",
    "diligent": "employed",
    "outfit": "garb",
    "guide": "usher",
}


right = {"fond": "averse", "wrath": "delight", "diligent": "idle", "guide": "follow", "flow": "jam"}


def left_join(hashmap1, hashmap2):
    result = []
    values1 = list(hashmap1.values())
    values2 = list(hashmap2.values())
    keys1 = list(hashmap1.keys())
    keys2 = list(hashmap2.keys())

    for i in range(len(keys1)):
        for j in range(len(keys2)):
            print("i is: ", keys1[i])
            print("j is: ", keys2[j])
            if keys1[i] == keys2[j]:
                to_append = [keys1[i], values1[i], values2[j]]
                result.append(to_append)

        to_append = [keys1[i], values1[i], "NULL"]
        result.append(to_append)

    return result
