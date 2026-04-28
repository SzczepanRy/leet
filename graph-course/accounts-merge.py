class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        parent = list(range(len(accounts)))


        def find(i):
            if parent[i] == i:
                return i

            parent[i] = find(parent[i])

            return parent[i]

        def union(i , j ):
            ri = find(i)
            rj = find(j)

            if ri != rj :
                parent[ri] = rj


        seen = {}

        for i , emails in enumerate(accounts):
            for email in emails[1:]:
                if email in seen:
                    union(i , seen[email])
                else:
                    seen[email] = i


        groups = {}

        for email in seen:
            owner_idx = seen[email]

            root = find(owner_idx)

            if root not in groups:
                groups[root] = []
            groups[root].append(email)

        res = []

        for root_idx in groups :
            name = accounts[root_idx][0]
            sorted_emails = sorted(groups[root_idx])

            res.append([name]+ sorted_emails )



        return res


accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
s = Solution()
s.accountsMerge(accounts)
