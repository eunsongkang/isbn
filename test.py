# this is a script to test isbn numbers

isbn_false = '9781234567890'
isbn_true = '9783161484100'

isbn_true_trunc = isbn_true[0:12]

d_1_t = int(isbn_true[0])*1
d_2_t = int(isbn_true[1])*3
d_3_t = int(isbn_true[2])*1
d_4_t = int(isbn_true[3])*3
d_5_t = int(isbn_true[4])*1
d_6_t = int(isbn_true[5])*3
d_7_t = int(isbn_true[6])*1
d_8_t = int(isbn_true[7])*3
d_9_t = int(isbn_true[8])*1
d_10_t = int(isbn_true[9])*3
d_11_t = int(isbn_true[10])*1
d_12_t = int(isbn_true[11])*3

sum_digits_true = d_1_t + d_2_t + d_3_t + d_4_t + d_5_t + d_6_t + d_7_t + d_8_t + d_9_t + d_10_t + d_11_t + d_12_t
print(sum_digits_true)

checksum_true = 10 - sum_digits_true % 10

if checksum_true == 10:
    checksum_true = 0
    print(checksum_true)
else:
    print(checksum_true)

if checksum_true == int(isbn_true[12]):
    print("Checksum matches")
else:
    print("Checksum does not match")


isbn_false_trunc = isbn_false[0:12]

d_1_f = int(isbn_false[0])*1
d_2_f = int(isbn_false[1])*3
d_3_f = int(isbn_false[2])*1
d_4_f = int(isbn_false[3])*3
d_5_f = int(isbn_false[4])*1
d_6_f = int(isbn_false[5])*3
d_7_f = int(isbn_false[6])*1
d_8_f = int(isbn_false[7])*3
d_9_f = int(isbn_false[8])*1
d_10_f = int(isbn_false[9])*3
d_11_f = int(isbn_false[10])*1
d_12_f = int(isbn_false[11])*3

sum_digits_false = d_1_f + d_2_f + d_3_f + d_4_f + d_5_f + d_6_f + d_7_f + d_8_f + d_9_f + d_10_f + d_11_f + d_12_f
print(sum_digits_false)
checksum_false = 10 - sum_digits_false % 10

if checksum_false == 10:
    checksum_false = 0
    print(checksum_false)
else:
    print(checksum_false)

if checksum_false == int(isbn_false[12]):
    print("Checksum matches")
else:
    print("Checksum does not match")

#
# test = 'superfragalisticexpedeladocious'
#
# for digit in map(int, isbn_true_trunc):
#     print(digit)
