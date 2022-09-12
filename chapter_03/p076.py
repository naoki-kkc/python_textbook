# tuple (no re-assignment)
eto_list = ('子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥')

input_val = input()

# input value to num
val_2_int = int(input_val)

# num to eto
eto_num = (val_2_int + 8) % 12

print(eto_list[eto_num])