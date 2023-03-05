text = "#1 of udi di data > primary di > code: Provided value '08907097112790' do not pass check-digit validation. For GS1 key '0890709711279' last validation digit should be '6', but is '0'"

udi = "08907097112790"
size = len(udi)
lis = text.split("should be ")[1][1:2]
print(lis)
new_udi = udi[:-1]+lis
print(new_udi)