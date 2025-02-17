class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        companyIndex = dict()
        ind = 0
        peopleCompanies = []
        for companies in favoriteCompanies:
            compSet = set()
            for company in companies:
                if company not in companyIndex:
                    companyIndex[company] = ind
                    ind += 1

                compSet.add(companyIndex[company])

            peopleCompanies.append(compSet)

        ans = []
        for i, ownComp in enumerate(peopleCompanies):
            found = False
            for j, otherComp in enumerate(peopleCompanies):
                if i == j:
                    continue

                if not ownComp - otherComp:
                    found = True
                    break

            if not found:
                ans.append(i)

        return ans
