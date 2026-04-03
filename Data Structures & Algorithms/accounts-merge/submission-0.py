class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        par = list(range(n))
        names = []
        emails = {}

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]


        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return

            par[p1] = p2

        email_to_acc = {}
        
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_acc:
                    # If we've seen this email before, union the accounts
                    union(i, email_to_acc[email])
                else:
                    email_to_acc[email] = i
        
        # Group emails by their root parent
        email_groups = {}
        for email, acc_idx in email_to_acc.items():
            root = find(acc_idx)
            if root not in email_groups:
                email_groups[root] = set()
            email_groups[root].add(email)
        
        # Build the result
        result = []
        for root_idx, emails_set in email_groups.items():
            name = accounts[root_idx][0]
            sorted_emails = sorted(list(emails_set))
            result.append([name] + sorted_emails)
        
        return result


        
            

            
            

