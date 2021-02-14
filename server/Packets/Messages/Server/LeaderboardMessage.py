from Utils.Writer import Writer


class LeaderboardMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24403
        self.player = player

    def encode(self):
        self.writeVint(self.player.LeaderboardInfo)
        self.writeVint(0)
        if self.player.LeaderboardType == 0:
        	self.writeString()
        else:
        	self.writeString("RU")

        if self.player.LeaderboardInfo == 0:
            self.writeVint(2) # Players Count

            self.writeVint(0) # High ID
            self.writeVint(1) # Low ID

            self.writeVint(1)
            self.writeVint(99999) # Player Trophies

            self.writeVint(1)

            self.writeString("<cff3200>M<cff6500>r<cff9800> <cffcb00>V<cffff00>i<cccff00>t<c99ff00>a<c66ff00>l<c33ff00>i<c01ff00>k</c>")  # Player Name
            self.writeString("<c2aff00>O<c54ff00>b<c7fff00>j<ca9ff00>e<cd4ff00>c<cfefe00>t<cffff00> <cffd400>T<cffaa00>e<cff7f00>a<cff5500>m</c>") # Club Name

            self.writeVint(1) # Player Level
            self.writeVint(28)
            self.writeVint(0)
            self.writeVint(0)
            
            
            self.writeVint(0) # High ID
            self.writeVint(2) # Low ID

            self.writeVint(1)
            self.writeVint(99999) # Player Trophies

            self.writeVint(1)

            self.writeString("<c7f00ff>X<cff00ff>e<cff007f>o<cff0000>n</c>")  # Player Name
            self.writeString("<c2aff00>O<c54ff00>b<c7fff00>j<ca9ff00>e<cd4ff00>c<cfefe00>t<cffff00> <cffd400>T<cffaa00>e<cff7f00>a<cff5500>m</c>") # Club Name

            self.writeVint(1) # Player Level
            self.writeVint(28)
            self.writeVint(0)
            self.writeVint(0)
        elif self.player.LeaderboardInfo == 1:
            self.writeVint(2) # Players Count

            self.writeVint(0) # High ID
            self.writeVint(1) # Low ID

            self.writeVint(1)
            self.writeVint(99999) # Player Trophies

            self.writeVint(1)

            self.writeString("<cff3200>M<cff6500>r<cff9800> <cffcb00>V<cffff00>i<cccff00>t<c99ff00>a<c66ff00>l<c33ff00>i<c01ff00>k</c>")  # Player Name
            self.writeString("<c2aff00>O<c54ff00>b<c7fff00>j<ca9ff00>e<cd4ff00>c<cfefe00>t<cffff00> <cffd400>T<cffaa00>e<cff7f00>a<cff5500>m</c>") # Club Name

            self.writeVint(1) # Player Level
            self.writeVint(28)
            self.writeVint(0)
            self.writeVint(0)
            
            
            self.writeVint(0) # High ID
            self.writeVint(2) # Low ID

            self.writeVint(1)
            self.writeVint(99999) # Player Trophies

            self.writeVint(1)

            self.writeString("<c7f00ff>X<cff00ff>e<cff007f>o<cff0000>n</c>")  # Player Name
            self.writeString("<c2aff00>O<c54ff00>b<c7fff00>j<ca9ff00>e<cd4ff00>c<cfefe00>t<cffff00> <cffd400>T<cffaa00>e<cff7f00>a<cff5500>m</c>") # Club Name

            self.writeVint(1) # Player Level
            self.writeVint(28)
            self.writeVint(0)
            self.writeVint(0)
        elif self.player.LeaderboardInfo == 2:
            self.writeVint(1) # Clubs Count

            self.writeVint(0) # Club High ID
            self.writeVint(1) # Club Low ID

            self.writeVint(1)
            self.writeVint(99999) # Club Trophies
            self.writeVint(2)

            self.writeString("RetroBrawl") # Club Name
            self.writeVint(5) # Club Members Count

            self.writeVint(8) # Club Badge
            self.writeVint(5) # Club Name Color
      
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        
        self.writeString("RU")
        print("[INFO] Message LeaderboardMessage has been sent.")