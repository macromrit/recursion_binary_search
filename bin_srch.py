def recur_bin_srch(data: list,  lower_bnd: int, upper_bnd: int, item: int)->int:
    
    if upper_bnd >=lower_bnd:
        middle = (lower_bnd + upper_bnd)//2
        if item==data[middle]:
            print(middle)
        elif item<data[middle]:
            recur_bin_srch(data, lower_bnd, middle-1, item)
        else:
            recur_bin_srch(data, middle+1, upper_bnd, item)
    else:
        print('No such item found')

if __name__ == '__main__':
    pass
