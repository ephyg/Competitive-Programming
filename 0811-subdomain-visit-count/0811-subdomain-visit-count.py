class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # possible_subdomains=[]
        count_subdomain={}
        for i in range(len(cpdomains)):
            visit_number,web_domain=cpdomains[i].split()
            if(web_domain not in count_subdomain):
                count_subdomain[web_domain]=int(visit_number)
            else:
                count_subdomain[web_domain]+=int(visit_number)
            for j in range(len(web_domain)):
                if(web_domain[j]=='.'):
                    if(web_domain[j+1:] in count_subdomain):
                        count_subdomain[web_domain[j+1:]]+=int(visit_number)
                    else:
                        count_subdomain[web_domain[j+1:]]=int(visit_number)
        result=[]
        for keys ,values in count_subdomain.items():
            result.append(f"{values} {keys}")
        return result
            