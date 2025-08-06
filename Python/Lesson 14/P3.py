def prb_a_or_b(a,b,all_poss_outcomes):
    prob_a = len(a) /  len(all_poss_outcomes)
    prob_b = len(b) /  len(all_poss_outcomes)
    inter = a.intersection(b)
    prob_inter =  len(inter) /  len(all_poss_outcomes)
    return(prob_a + prob_b - prob_inter) 

evens = {2,4,6}
great_than_2 = {3,4,5,6}
all_poss_rolls = {1,2,3,4,5,6}
print("Probability of getting a even number or greater number than 2 : ")
print(prb_a_or_b(evens,great_than_2,all_poss_rolls))