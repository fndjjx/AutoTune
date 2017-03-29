def gray2binary(gray_code):
    binary_code = []
    binary_code.append(gray_code[0])
    for i in range(1, len(gray_code)):
        binary_code.append(str(int(gray_code[i])^int(gray_code[i-1])))
    return "".join(binary_code)


if __name__ == "__main__":
    gray_code = ["0","0","1", "0"]
    print(gray2binary(gray_code))
    
