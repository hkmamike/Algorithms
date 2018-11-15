class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        count = 0
        sentSet = set()
        
        for email in emails:
            localName = email.split("@")[0]
            domainName = email.split("@")[1]
            
            localNamePlusIndex = localName.index("+")
            localName = localName[0: localNamePlusIndex]
            localName = localName.replace(".","")
            cleanedEmail = localName + "@" + domainName

            if cleanedEmail not in sentSet:
                count += 1
                sentSet.add(cleanedEmail)
        
        return count
        