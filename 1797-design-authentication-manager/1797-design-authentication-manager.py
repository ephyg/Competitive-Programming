class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time_to_live=timeToLive
        self.token={}

    def generate(self, tokenId: str, currentTime: int) -> None:
        if not (tokenId in self.token):
            self.token[tokenId]=currentTime
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        
        if (tokenId in self.token):
            if(self.token[tokenId]+self.time_to_live)>currentTime:
                self.token[tokenId]=currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        counter=0
        for tokenId in self.token:
            if((self.token[tokenId]+self.time_to_live)>currentTime):
                counter+=1
        return counter


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)