class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        mySet ={
        1: "I",
        2: "II",
        3: "III",
        4:"IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10:"X",
        20:"XX",
        30:"XXX",
        40:"XL",
        50:"L",
        60:"LX",
        70:"LXX",
        80:"LXXX",
        90:"XC",
        100:"C",
        200:"CC",
        300:"CCC",
        400:"CD",
        500:"D",
        600:"DC",
        700:"DCC",
        800:"DCCC",
        900:"CM",
        1000:"M",
        2000:"MM",
        3000:"MMM"
        }

        x = 1
        s = ""
        while num > 0:
            r = num%10
            num = num //10
            if(r == 0 ):
                x=x*10
                continue
            s = mySet[r*x] +s
            #print( r*x)
            x=x*10
      #  print(s)
        return s
s = Solution()

s.intToRoman(100)
