import re

str = "The rain in spain is mainly in the plain"
nums = "Ap 10 TN 20 KA 30 are the codes"

matches1 = re.finditer(r"\bin\b", str)
matches2 = re.finditer(r"\d+", nums)

for match in matches2:
    print(match.group(), " ", "Start ==>", match.start(), "End ==> ", match.end())