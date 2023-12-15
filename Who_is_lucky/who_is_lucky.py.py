# The toggle function to toggle the input
def toggle(num):
    '''
    This function will toggle the input that is if there is zero then it will become one and vise versa
    input ---> num:str
    output---> res:str
    '''
    num = ['1' if num[i] == '0' else '0' for i in range(len(num))]
    res = ""
    for i in num:
        res += i
    return res

# Function for playing the game


def play_game(array, rahul, rupesh, k):
    '''
    This function will apply all the rules for playing the game and then decide the result of the game.
    input --->array:list[int]
              rahul:list[str]
              rupesh:list[str]
              k:int
    output--->str
    '''
    turn = 0  # 0 for rahul and 1 for rupesh
    rahul_sum = 0
    rupesh_sum = 0
    while (len(array)):
        if turn == 0:  # turn of rahul
            # getting the index of the maximum element
            x = array.index(max(array))
            l = x - k
            r = x + k
            if l < 0:  # checking the boundry conditions
                l = 0
            if r > len(array):  # checking the boundry condition
                r = len(array)
            removed = array[l:r+1]
            array = array[:l]+array[r+1:]
            rahul_sum += sum(removed)
            turn = 1
        if (len(array)):
            if turn == 1:  # turn of rupesh
                x = array.index(max(array))
                l = x - k
                r = x + k
                if l < 0:
                    l = 0
                if r > len(array):
                    r = len(array)
                removed = array[l:r+1]
                array = array[:l]+array[r+1:]
                rupesh_sum += sum(removed)
                turn = 0
    # toggle as per the rule of the game
    if turn == 1:  # rahul is winner.
        rahul[0] = toggle(rahul[0])
    else:
        rupesh[0] = toggle(rupesh[0])

    if rahul_sum > rupesh_sum:
        rahul[1] = toggle(rahul[1])
    elif rupesh_sum > rahul_sum:
        rupesh[1] = toggle(rupesh[1])
    else:
        rahul[1] = toggle(rahul[1])
        rupesh[1] = toggle(rupesh[1])

    # Deciding who is going to win the game
    if int(rahul[0], 2) ^ int(rahul[1], 2) > int(rupesh[0], 2) ^ int(rupesh[1], 2):
        return "Rahul"
    elif int(rahul[0], 2) ^ int(rahul[1], 2) < int(rupesh[0], 2) ^ int(rupesh[1], 2):
        return "Rupesh"
    else:
        return "Both"


# Main code
# Taking all the input from the user
l = input()
array = l.split(" ")
rahul_value = input()
rahul = rahul_value.split(" ")
rupesh_value = input()
rupesh = rupesh_value.split(" ")
k = input()
k = int(k)
array = [int(i) for i in array]
# Playing the game
result = play_game(array, rahul, rupesh, k)
# Getting the result
print(f"The winner of the Game is {result}")
