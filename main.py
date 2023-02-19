
import time
def espresso_chain(distances,profits, k):
    dp = [0]*len(distances)
    dp[0] = profits[0]
    for i in range(1,len(distances)):
            for j in range(0, i):
                if distances[i] - distances[j] > k:
                    curr_max = dp[j] + profits[i]
                else:
                    curr_max = dp[j]
                if curr_max> dp[i]: dp[i] = curr_max
            ##if dp[i]< profits[i]: dp[i] = profits[i]
    return dp[len(distances)-1]

def lake_ontario(food_stops, M):
    max_dist = [0 for element in range((len(food_stops)+1))]
    max_dist[0] = M

    for index,i in enumerate(food_stops):
       for j in range(0,index+1):
            if max_dist[j] >= i:
                max_dist[j+1] = max(max_dist[j+1],i + M)

    for i in range(len(max_dist)-1):
        if max_dist[i] >= food_stops[len(food_stops)-1]:
            return i
    return -1

def greedy_Lake_Ontario(food_stops, M ):
    hunger_meter = M
    num_stops = 0
    distance_list = [0]
    for i in food_stops:
        distance_list.append(i)
    j = 0

    for i in range(0, len(distance_list) - 1):
        if hunger_meter >= distance_list[i + 1] - distance_list[j]:
            hunger_meter = M - (distance_list[i] - distance_list[j])
        else:
            hunger_meter = M
            num_stops += 1
            j = i
            if hunger_meter < distance_list[i + 1] - distance_list[i]:
                return -1
    return num_stops






def usta_gril(customers):
    ## greedy algorithm, shortest first
    return 1

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Game = input("Do you want to test Espresso Chain (1) or Lake ontario (2): ")
    if Game == "1":
        input_str1 = input("Enter your list of distances as a list of integers separated by spaces: ")
        distances = [int(x) for x in input_str1.split()]
        input_str2= input("Enter your list of profits as a list of integers separated by spaces: ")
        profits = [int(x) for x in input_str2.split()]
        k = int(input("Enter your value for K"))
        start_time = time.time() * 1000
        print("Max Profit:" + str(espresso_chain(distances, profits, k)))
        end_time = time.time() * 1000

    elif Game == "2":
        input_str1 = input("Enter your list of food stops as a list of integers separated by spaces: ")
        food_stops = [int(x) for x in input_str1.split()]
        M = int(input("Enter your value for M"))
        start_time = time.time() * 1000
        print( "Fewest stops:" + str(greedy_Lake_Ontario(food_stops, M)))
        end_time = time.time() * 1000
    else:
        print("Please enter a valid imput")
    print("Runtime: {:.3f} Milliseconds".format(end_time - start_time))
