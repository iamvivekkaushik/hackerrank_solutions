# https://www.hackerrank.com/challenges/one-month-preparation-kit-climbing-the-leaderboard/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-month-week-three


def binary_search(search_item, sorted_list):
    half = len(sorted_list) // 2
    if half > len(sorted_list) - 1:
        return None
    
    if sorted_list[half] == search_item:
        return half
    elif sorted_list[half] > search_item:
        value = binary_search(search_item, sorted_list[half + 1:])
        if value is None:
            value = 0
        else:
            value += 1
        return half + value
    else:
        value = binary_search(search_item, sorted_list[:half])
        if value is None:
            return -1
        else:
            return value


#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    rankedMap = {str(ranked[0]): 1}
    
    for i in range(1, len(ranked)):
        previous_rank = rankedMap[str(ranked[i-1])]
        
        if ranked[i-1] != ranked[i]:
            rankedMap[str(ranked[i])] = previous_rank + 1
    
    final_list = []
    for i in player:
        if str(i) in rankedMap:
            final_list.append(rankedMap[str(i)])
        else:
            if ranked[0] < i:
                final_list.append(1)
                continue
            
            pos = binary_search(i, ranked)
            final_list.append(rankedMap[str(ranked[pos])] + 1)

    
    return final_list

if __name__ == '__main__':
    ranked = [100, 90, 90, 80, 75, 60]

    player = [50, 65, 77, 90, 102]

    result = climbingLeaderboard(ranked, player)

    for i in result:
        print(i)

# Expected Output
# 6
# 5
# 4
# 2
# 1
