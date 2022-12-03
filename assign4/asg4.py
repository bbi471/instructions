# Assignment 4
# Comprehensive Program
# Benjamin Bi, 201728471
# reference: https://stackoverflow.com/questions/2967194/open-in-python-does-not-create-a-file-if-it-doesnt-exist
# reference: https://mru-f22-cs1.github.io/content-curtis/pdfs/20-file-writing.pdf
# reference: https://images.zmangames.com/filer_public/81/0a/810a04df-26f8-4b01-a2de-b561719109d2/blueprints_rules.pdf

def read_building(building: str) -> list:
    """
    This function receives the file name (str) of building text file and return a list containing the dice layers of four different coloured dices
    """

    # list_of_dice_layer is a list containing the dice layers of four different coloured dices
    list_of_dice_layer = []

    # Open and append the lines of building.txt to list list_of_dice_layer
    f = open(building, "r")
    for line in f:
        list_of_dice_layer.append(line)
    f.close()

    return list_of_dice_layer

# Function score receive list_of_dice_layer and return score_list containing score information
def score(list_of_dice_layer: list) -> list:

    # list_of_dice_list is the list of the dice list
    list_of_dice_list=[]


    recycled_list = [0,2,5,10,15,20,30]
    stone_list = [0,2,3,5,8]
    
    recycled_count = 0
    recycled_score = 0
    stone_score = 0
    wood_score = 0
    glass_score = 0

    for i in range(len(list_of_dice_layer)):
        # Split each line of string into elements by "|" and append to list_of_dice_list
        element = list_of_dice_layer[i].split("|")
        list_of_dice_list.append(element)

    # Use nested for loop to check every element and get score
    for i in range(len(list_of_dice_list)):
        for j in range(len(list_of_dice_list[i])):
            if "R" in list_of_dice_list[i][j]:
                recycled_count += 1  # Count the number of "R" and score depends on how many R dice
            elif "S" in list_of_dice_list[i][j]:
                stone_score += stone_list[len(list_of_dice_list)-i] # Stone is scored by level of dices
            elif "W" in list_of_dice_list[i][j]: # Wood is scored by shared adjacent faces
                if i-1 >= 0 and list_of_dice_list[i-1][j][0] != "-":
                    wood_score += 2  
                if j-1 >= 0 and list_of_dice_list[i][j-1][0] != "-":
                    wood_score += 2
                if i+1 < len(list_of_dice_list) and list_of_dice_list[i+1][j][0] != "-":
                    wood_score += 2
                if j+1 < 3 and list_of_dice_list[i][j+1][0] != "-":
                    wood_score += 2
            elif "G" in list_of_dice_list[i][j]:
                glass_score += int(list_of_dice_list[i][j][1])  # glass is scored by the top number on dice

    recycled_score = recycled_list[recycled_count]

    total_score = recycled_score + stone_score + wood_score + glass_score
    score_list = [glass_score,recycled_score,stone_score,wood_score,total_score]
    return score_list

def result(score_list: list) -> None:
    """
    This function result receives the score_list 
    and write the information to scoring-results.txt
    """

# This is an example of score result display
# +----------+----+
# | glass    |  4 |
# | recycled |  5 |
# | stone    |  5 |
# | wood     |  6 |
# +==========+====+
# | total    | 20 |
# +----------+----+
#

    f = open("scoring-results.txt","w+") 
    
    f.write("+----------+----+\n")
    f.write(f"| glass    |  {score_list[0]} |\n")
    f.write(f"| recycled |  {score_list[1]} |\n")
    f.write(f"| stone    |  {score_list[2]} |\n")
    f.write(f"| wood     |  {score_list[3]} |\n")
    f.write(f"+==========+====+\n")
    f.write(f"| total    |  {score_list[4]} |\n")
    f.write(f"+----------+----+")
    
    f.close()
    return None

def main() -> None:
    
    # Read building text file and get a list containing the dice layers of four different coloured dices
    list_of_dice_layer = read_building("building.txt")
    
    
    print("The building structure: \n")
    # Display the information of building.txt
    f = open("building.txt", "r")
    building_display = f.read()
    print(building_display, "\n")
    f.close()

    # Call a function score and get score_list
    score_list = score(list_of_dice_layer)

    # Call function result and write the information to scoring-results.txt 
    result(score_list)

    # print the information of scoring-results.txt
    f = open("scoring-results.txt","r") 
    display_result = f.read()
    print("The score result: \n")
    print(display_result)
    f.close()

main() 
