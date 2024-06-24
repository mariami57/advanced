def positive_vs_negative(*args):
    positives_sum = 0
    negatives_sum = 0
    for l in args:
        for num in l:
            if num > 0:
                positives_sum += num
            else:
                negatives_sum += num
    print(negatives_sum)
    print(positives_sum)
    if abs(negatives_sum) < positives_sum:
        return "The positives are stronger than the negatives"
    elif abs(negatives_sum) > positives_sum:
        return "The negatives are stronger than the positives"


numbers = [int(x) for x in input().split()]
print(positive_vs_negative(numbers))

