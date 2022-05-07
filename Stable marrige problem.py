from itertools import permutations


def stableMatching(n, menPreferences, womenPreferences):
    # Initially, all n men are unmarried
    unmarriedMen = list(range(n))
    changed_choice = list(range(n))
    for i in range(n):
        changed_choice[i] = 0
    # None of the men has a spouse yet, we denote this by the value None
    manSpouse = [None] * n
    # None of the women has a spouse yet, we denote this by the value None
    womanSpouse = [None] * n
    # Each man made 0 proposals, which means that
    # his next proposal will be to the woman number 0 in his list
    nextManChoice = [0] * n

    # While there exists at least one unmarried man:
    while unmarriedMen:
        # Pick an arbitrary unmarried man
        he = unmarriedMen[0]
        # Store his ranking in this variable for convenience
        hisPreferences = menPreferences[he][1]
        # Find a woman to propose to
        she = hisPreferences[nextManChoice[he]]
        # Store her ranking in this variable for convenience
        herPreferences = womenPreferences[she][1]
        # Find the present husband of the selected woman (it might be None)
        currentHusband = womanSpouse[she]

        # Now "he" proposes to "she".
        # Decide whether "she" accepts, and update the following fields
        # 1. manSpouse
        # 2. womanSpouse
        # 3. unmarriedMen
        # 4. nextManChoice
        if currentHusband == None:
            # No Husband case
            # "She" accepts any proposal
            womanSpouse[she] = he
            manSpouse[he] = she
            # "His" nextchoice is the next woman
            # in the hisPreferences list
            nextManChoice[he] = nextManChoice[he] + 1
            # Delete "him" from the
            # Unmarried list
            unmarriedMen.pop(0)
        else:
            # Husband exists
            # Check the preferences of the
            # current husband and that of the proposed man's
            currentIndex = herPreferences.index(currentHusband)
            hisIndex = herPreferences.index(he)
            # Accept the proposal if
            # "he" has higher preference in the herPreference list
            if currentIndex > hisIndex:
                # New stable match is found for "her"
                changed_choice[currentHusband] += 1
                womanSpouse[she] = he
                manSpouse[he] = she
                nextManChoice[he] = nextManChoice[he] + 1
                # Pop the newly wed husband
                unmarriedMen.pop(0)
                # Now the previous husband is unmarried add
                # him to the unmarried list
                unmarriedMen.insert(0, currentHusband)
            else:
                changed_choice[he] += 1
                nextManChoice[he] = nextManChoice[he] + 1

    return manSpouse, changed_choice


females_perm = list(permutations([0, 1, 2, 3]))
males_perm = list(permutations([0, 1, 2, 3]))
#
stableMatching(4, [[0, (3, 2, 1, 0)], [1, (1, 0, 2, 3)], [2, (1, 3, 2, 0)], [3, (0, 1, 3, 2)]],
               [[0, (0, 1, 2, 3)], [1, (0, 3, 2, 1)], [2, (1, 0, 2, 3)], [3, (3, 2, 0, 1)]])

solutions = 0
print(len(list(permutations([0, 1, 2, 3]))))
# Generate males permutations
for perm in permutations([0, 1, 2, 3]):
    males = [[], [], [], []]
    for i1 in range(len(females_perm)):
        males[0] = [perm[0], females_perm[i1]]
        for i2 in range(len(females_perm)):
            males[1] = [perm[1], females_perm[i2]]
            for i3 in range(len(females_perm)):
                males[2] = [perm[2], females_perm[i3]]
                for i4 in range(len(females_perm)):
                    males[3] = [perm[3], females_perm[i4]]

                    # Generate females permutations
                    for f_perm in permutations([0, 1, 2, 3]):
                        females = [[], [], [], []]
                        for j1 in range(len(males_perm)):
                            females[0] = [f_perm[0], males_perm[j1]]
                            for j2 in range(len(males_perm)):
                                females[1] = [f_perm[1], males_perm[j2]]
                                for j3 in range(len(males_perm)):
                                    females[2] = [f_perm[2], males_perm[j3]]
                                    for j4 in range(len(males_perm)):
                                        females[3] = [f_perm[3], males_perm[j4]]
                                        matching, rejects = stableMatching(4, males, females)
                                        matching2, rejects2 = stableMatching(4, females, males)
                                        if rejects[0] > 0 and rejects[1] > 0 and rejects[2] > 0 and rejects[3] > 0 and\
                                                rejects2[0] > 0 and rejects2[1] > 0 and rejects2[2] > 0 and rejects2[3] > 0:
                                            print(f"SOLUTION NO: {solutions}\nMales:")
                                            solutions += 1
                                            print(males)
                                            print("Females:")
                                            print(females)
