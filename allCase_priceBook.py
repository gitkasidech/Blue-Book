# coding=utf8
def main():
    type_content = ["แบบฝึกหัดโดยเฉพาะ", "ไม่เป็นแบบฝึกหัดโดยเฉพาะ"]
    type_edition = ["เก่า","ใหม่"]
    type_cover = ["ไม่สมบูรณ์","สมบูรณ์"]
    type_stain = ["เปียกน้ำ-มีคราบ ไม่เกิน 20%","เปียกน้ำ-มีคราบ 20%-50%","เปียกน้ำ-มีคราบ 50% ขึ้นไป","ไม่เปียกน้ำ"]
    type_writng = ["รอยเขียน ไม่เกิน 20%","รอยเขียน 20%-50%","รอยเขียน 50% ขึ้นไป","ไม่มีรอยเขียน"]
    type_crease = ["รอยยับ ไม่เกิน 20%","รอยยับ 20%-50%","รอยยับ 50% ขึ้นไป","ไม่มีรอยยับ"]
    type_tear = ["รอยฉีกขาด ไม่เกิน 20%","รอยฉีกขาด 20%-50%","รอยฉีกขาด 50% ขึ้นไป","ไม่มีรอยฉีกขาด"]

    start_price = 70
    content = 0
    edition = 30
    cover = 10
    stain_under20 = 10
    stain_between20to50 = 20
    stain_over50 = 40
    writing_under20 = 5 
    writing_between20to50 = 10
    writing_over50 = 20
    crease_under20 = 5 
    crease_between20to50 = 10
    crease_over50 = 20
    tear_under20 = 20
    tear_between20to50 = 30
    tear_over50 = 50
    i = 0

    for a in range(0,2):
        start_a = start_price
        format_a = content
        if a==0:
            format_a = format_a+1

        for b in range(0,2):
            start_b = start_a
            if b==0:
                start_b= start_b-edition

            for c in range(0,2):
                start_c = start_b
                if c==0:
                    start_c= start_c-cover

                for d in range(0,4):
                    start_d = start_c
                    if d==0:
                        start_d = start_d-stain_under20
                    elif d==1:
                        start_d = start_d-stain_between20to50
                    elif d==2:
                        start_d = start_d-stain_over50

                    for e in range(0,4):
                        start_e = start_d
                        writing_case1 = writing_under20
                        writing_case2 = writing_between20to50
                        writing_case3 = writing_over50
                        if format_a==1:
                            writing_case1 = writing_case1*2
                            writing_case2 = writing_case2*2
                            writing_case3 = writing_case3*2
                        if e==0:
                            start_e= start_e-writing_case1
                        elif e==1:
                            start_e= start_e-writing_case2
                        elif e==2:
                            start_e= start_e-writing_case3

                        for f in range(0,4):
                            start_f = start_e
                            if f==0:
                                start_f= start_f-crease_under20
                            elif f==1:
                                start_f= start_f-crease_between20to50
                            elif f==2:
                                start_f= start_f-crease_over50
                            
                                for g in range(0,4):
                                    start_g = start_f
                                    if g==0:
                                        start_g= start_g-tear_under20
                                    elif g==1:
                                        start_g= start_g-tear_between20to50
                                    elif g==2:
                                        start_g= start_g-tear_over50
                                    if start_g<0:
                                        start_g = 0   
                                    i=i+1
                                    print("{0}.) {1},{2},{3},{4},{5},{6},{7}\n==>ราคาที่ประเมินได้คือ {8}% ของราคาจริง"
                                    .format(i,type_content[a],type_edition[b],type_cover[c],type_stain[d],
                                    type_writng[e],type_crease[f],type_tear[g],start_g))    
main()


