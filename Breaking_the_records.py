def breaking_records(gameCount, scoreList):
    if gameCount == 0:
        return [0,0];

    lowest = highest = scoreList[0];
    lowest_count = highest_count = 0;

    for score in scoreList:
        if score < lowest:
            lowest = score;
            lowest_count += 1;
        elif score > highest:
            highest_count += 1;
            highest = score;

    return highest_count, lowest_count;


gameCount = int(input('Enter the total number of game: '));
scoreList = list(map(int, input("Enter the value: ").strip().split()))[:gameCount];
print(breaking_records(gameCount, scoreList));