from jamo import h2j, j2hcj
from hangul_utils import join_jamos
import oodata as d
import itertools

sort = "sort"
rs = "rs"
dist = "dist"
join = "join"
jost = "join_dist"

def get_item():
    exitcode = ['e', 'ㄷ', 'e ', ' e', 'ㄷ ', ' ㄷ']
    #get_string = input("input:")
    get_string = "캬키야안눙반가와요앉아볼래여과자먹게여기앉와봐있어봐좀씨씼앉뷁"
    act = False
    test_string = list(get_string)
    print("test_string",test_string)
    test_item = Change(test_string[-1],dist).Out()
    if test_item[-1] in ['ㅆ','ㄲ']: # 마지막 단어 받침이 쌍자음일때
        test_string.append('아') # 오류 방지용, 나중에 지우기
        get_string = test_string
        act = True
    elif test_item[-1] in d.batch_from: # 마지막 단어 받침이 겹받침이면 하나짜리로 변환
        for i, ch in enumerate(d.batch_from):
            if test_item[-1] == ch:
                test_item[-1] = d.batch_to_[i]
                test_out = Change(test_item, join).Out()
                test_string[-1] = test_out
                get_string = itertools.chain(*test_string)
    if get_string in exitcode:
        exit()
    ###print(get_string) #input 검증
    return get_string, act


def main_process():
    input_item, act = get_item()
    print("input", input_item)
    trans = Translation(input_item)
    output_item = trans.out
    print("output", output_item)
    output_item = Change(output_item, join).Out()
    print("outputjoin", output_item)
    if act:
        output_item.pop(-1)
    print("result", output_item)


# Change(list, case).Out() > list를 case에 따라 변형
class Change:
    def __init__(self, item, case):
        if case in ["dist"]:
            item = itertools.chain(*item)
            item = self.distjamo(item)
        elif case in ["join"]:
            item = itertools.chain(*item)
            item = self.joinjamo(item)
        elif case in ["join_dist"]:
            item = itertools.chain(*item)
            item = self.joinjamo(item)
            item = self.distjamo(item)
        elif case in ["rs"]:
            item = self.rs(item)
        elif case in ["fs", "sort"]:
            item = self.fs(item)
        else:
            print('Change input error,', case)
            exit()
        self.out = item

    def distjamo(self, dist_list):
        return list(j2hcj(h2j(dist_list)))

    def joinjamo(self, join_list):
        return list(join_jamos(join_list))

    def rs(self, reversesort):
        return sorted(reversesort, reverse=True)

    def fs(self, forwardsort):
        return sorted(forwardsort, reverse=False)

    def Out(self):
        return self.out


# resol(list, from, to) > list 안의 모든 from을 to로 바꿈
def resol(f_input, f_case_from, f_case_to, cond=[]):
    f_out_idx = []
    f_out_val = []
    if cond: # 쌍자음 받침을 변환할 경우
        cond = [cond[i]+1 for i in range(len(cond))]
        for fi, fv in enumerate(f_input):
            if fv in f_case_from and fi-1 in cond:
                print(fv, fi-1, f_input[fi-1])
                f_out_idx.append(fi)
                f_out_val.append(fv)
    else:   # 일반적인 경우
        for fi, fv in enumerate(f_input):
            if fv in f_case_from:
                f_out_idx.append(fi)
                f_out_val.append(fv)
    if f_out_idx:
        for fi, fv in enumerate(f_out_idx):
            f_input[fv] = f_case_to
    return f_input


class Translation:
    def __init__(self, input_item):
        out = list(input_item)
        print("get_item :", out)
        out = self.ko_base(out, self.batch)
        print("batch :", out)
        out = resol(out, "와", "わ")
        out = resol(out, " ", "-")
        print("와, ' ' :", out)
        out = self.ko_base(out, self.moeum)
        print("moeum :", out)
        out = self.nbtch(out)
        print("nbatch :", out)
        out = self.ko_base(out, self.jaeum)
        print("jaeum :", out)
        out = self.hiragana(out)
        self.out = out

    def ko_base(self, fin, func):
        fin = Change(fin, dist).Out()
        fout = func(fin)
        fout = Change(fout, join).Out()
        return fout

    # 겹받침 처리이다
    def batch(self, fout):
        # 겹자음
        from_list = d.batch_from
        to_list = d.batch_to
        after_idx_list = []
        for i in range(len(from_list)):
            fout = resol(fout, from_list[i], to_list[i])
        for fi, fv in enumerate(fout):
            if fv in 'ㅇ' and fout[fi-1] in to_list:
                after_idx_list.append(fi)
        print("겹자음 끝")
        print(fout)
        # 쌍자음
        from_list = d.batch2_from
        to_list = d.batch2_to
        #batch2_cond = if(fout)
        o_idx_list = []
        for i, v in enumerate(fout):
            if v in d.all_moeum and i < int(len(fout))-1:
                o_idx_list.append(i+1)
        print('fout,"ㅇ".index',o_idx_list)
        for i in range(len(from_list)): # 이거 초성에도 적용된다 고쳐라 왜 그 생각을 또 안했니
            fout = resol(fout, from_list[i], to_list[i], o_idx_list)
        for fi, fv in enumerate(fout):
            if fv in 'ㅇ' and fout[fi-1] in to_list:
                after_idx_list.append(fi)
        print("after_idx_list", after_idx_list)
        if after_idx_list:
            cnt = 0
            for i in after_idx_list:
                del fout[i-cnt]
                cnt += 1
        fout = Change(fout, jost).Out()
        return fout

    # 그냥받침 처리이다
    def nbtch(self, fout):
        print('nbtch.fout',fout)
        from_list = d.nbtch_from
        to_list = d.nbtch_to
        temp_val = []
        temp_idx = []
        for idx, value in enumerate(fout):
            try :
                valist = Change(value, dist).Out()
                if len(valist) == 3:
                    print(valist)
                    batchim = valist[2]
                    print(batchim)
                    for i,v in enumerate(from_list):
                        if batchim == v:
                            batchim = to_list[i]
                    del valist[2]
                    print(batchim)
                    temp_idx.append(idx)
                    temp_val.append(batchim)
                    fout[idx] = Change(valist, join).Out()
            except:
                pass
        if temp_idx:
            cnt = 0
            for idx, val in enumerate(temp_idx):
                fout.insert(int(val)+cnt+1,temp_val[idx])
                cnt += 1
        fout = Change(itertools.chain(*fout),join).Out()
        return fout

    # 자음을 쓰는걸로 바꾼거다
    def jaeum(self, fout):
        from_list = d.jaeum_from
        to_list = d.jaeum_to
        for i in range(len(from_list)):
            fout = resol(fout, from_list[i], to_list[i])
        return fout

    # 기본모음 변형
    def moeum(self, fout):
        from_list = d.moeum_from
        to_list = d.moeum_to
        for i in range(len(from_list)):
            fout = resol(fout, from_list[i], to_list[i])
        from_list = d.moeum_ex_from
        to_list = d.moeum_ex_to
        for i in range(len(from_list)):
            fout = resol(fout, from_list[i], to_list[i])
        fout = Change(fout, jost).Out()
        return fout

    def hiragana(self, fout):
        from_list = d.kor
        to_list = d.jap
        for i in range(len(from_list)):
            fout = resol(fout, from_list[i], to_list[i])
        return fout

    def gatakana(self, fout):
        from_list = d.jap
        to_list = d.jak
        for i in range(len(from_list)):
            fout = resol(fout, from_list[i], to_list[i])
        return fout




if __name__ == "__main__":
    #test#
    print("===test===")
    a = [3, 2, 1, 4, 5]
    b = "안뇽"
    a = Change(a, sort).Out()
    print("fs", a)
    a = Change(a, rs).Out()
    print("rs", a)
    b = Change(b, dist).Out()
    print("dist", b)
    b = Change(b, join).Out()
    print("join", b)
    print("===test===")

    main_process()

