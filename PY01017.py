loop = int(input())

def maHoa(strg):
    result = []
    count = 1
    for i in range(1, len(strg)):
        if strg[i] == strg[i-1]:
            count += 1
        else:
            result.append(str(count) + strg[i-1])
            count = 1
    result.append(str(count) + strg[-1])
    return result


while loop > 0:
    input_strg = str(input())
    output_list = maHoa(input_strg)
    result_strg = ''.join(output_list)
    print(result_strg)

    loop -= 1