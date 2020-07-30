"""
Write a function called unzip that returns a tuple of two lists that result from
unzipping a zipped list 
"""

def unzip(zipped_list):
    list1 = []
    list2 = []
    for t in zipped_list:
        list1.append(t[0])
        list2.append(t[1])
    return (list1, list2)

if __name__ == "__main__":
    print(unzip([(1, 4),(2, 5),(3, 6)]))