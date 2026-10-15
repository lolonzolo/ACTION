from itertools import combinations

def group_score(group, preferences):
    total = 0

    for a in group:
        for b in group:
            if a != b:
                total += preferences[a][b]

    return total / len(group)


def optimize_groups(students, matrix):

    n = len(students)
    group1_size = n // 2
    all_students = set(range(n))

    best_score = float("-inf")
    best_group1 = None
    best_group2 = None
    best_score1 = None
    best_score2 = None

    for combination in combinations(range(n), group1_size):

        group1 = tuple(combination)
        group2 = tuple(sorted (all_students - set(combination)))

        #confronto lessicografico per eliminare partizioni duplicate tipo A,B,C - D,E,F e D,E,F - A,B,C
        if n % 2 == 0 and group1 > group2:
            continue

        score1 = group_score(group1, matrix) 
        score2 = group_score(group2, matrix)

        average_score = (score1 + score2) / 2

        if average_score > best_score:
            best_score = average_score

            best_group1 = group1
            best_group2 = group2

            best_score1 = score1
            best_score2 = score2

    return {
        #list comprehension per passare da indici a nomi studenti
        "group1": [students[i] for i in best_group1],
        "group2": [students[i] for i in best_group2],
        "score1": best_score1,
        "score2": best_score2,
        "average": best_score
    }







