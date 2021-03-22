booksan = ['채치수', '서태웅', '강백호', '정대만', '송태섭']
neungnam = ['윤대협', '변덕규', '기타등등']
player = '윤대협'

# 인덴션을 지켜라
if player in booksan:
    print("북산입니다.")
else:
    print("북산이 아닙니다")


# 아무것도 하지않는 pass 예약어
if '정대만' in booksan:
    pass

# and, or, not, in

# elif 사용
if player in booksan:
    print("북산입니다.")
elif player in neungnam:
    print("능남입니다.")
else:
    print("무소속")
