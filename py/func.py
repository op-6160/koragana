from jamo import h2j, j2hcj
from hangul_utils import join_jamos
import data as d

is_not_test = True


def get_item():
    exitcode = ['e', 'ㄷ', 'e ', ' e', 'ㄷ ', ' ㄷ']
    get_string = input("input:")
    if get_string in exitcode:
        exit()
    ###print(get_string) #input 검증
    return get_string


def distjamo(dist_list):
    disted = list(j2hcj(h2j(dist_list)))
    return disted


def joinjamo(join_list):
    joined = list(join_jamos(join_list))
    return joined


def rs(reversesort):
    return reversesort.sort(reverse=True)


class Translation:
    def __init__(self, input_string):
        self.val = input_string
        #self.cnt = 0

        self.x = self.anl(self.val)
        #print('end anl',self.x)
        self.x = self.anl_3(self.x)
        #self.x = self.zz(self.x)
        #print('end zz', self.x)
        self.x = self.trans(self.x)
        self.x = self.zz(self.x)
        #print('end trans', self.x)
        self.x = self.special(self.x)
        #print('end special', self.x)
        self.x = self.join(self.x)
        #print('end class', self.x)

    # 요음(ㅑㅠㅛ) 처리
    def dis(self, dis_input):
        dis_list_ = distjamo(dis_input)
        ja_list = d.jaeum
        yo_list = d.jap_yo
        for j_idx, j_val in enumerate(dis_list_):
            for ja_idx, ja_val in enumerate(ja_list):
                if ja_val == j_val:
                    dis_list_[j_idx] = yo_list[ja_idx]
            if j_val == 'ㅑ':
                dis_list_[j_idx] = 'ゃ'
            elif j_val == 'ㅠ':
                dis_list_[j_idx] = 'ゅ'
            elif j_val == 'ㅛ':
                dis_list_[j_idx] = 'ょ'
        ###print('dis_input', dis_input)
        ###print('dis_output', dis_list_)
        return dis_list_

    # 받침 처리
    def syll(self, syll_input):
        syll_list = distjamo(syll_input)
        mo_list = d.moeum
        ja_list = d.jaeum_ex
        batchim = d.batchim_h # if () else d.batchim_g
        spe_syll_list = list(d.is_im_sads)
        temp_idx_list=[]
        temp_syll_list=[]
        temp_idx = 0
        temp_syll =0
        ###print('syll_input',syll_input)
        ###print('syll_list',syll_list)
        for sy_idx, sy_val in enumerate(syll_list):
            ###print('sy_val1',sy_val)
            ###print('syll_list[sy_idx-2]',syll_list[sy_idx-2],sy_idx)

            if sy_idx<int(len(syll_list)-1) and syll_list[sy_idx - 1] in mo_list and sy_idx != 0 and syll_list[sy_idx+1] not in mo_list\
                    or sy_idx == int(len(syll_list)-1) and syll_list[sy_idx - 1] in mo_list:
                if sy_val in d.baatn:
                    syll_list[sy_idx] = batchim[0] # ん
                elif sy_val in d.baats:
                    syll_list[sy_idx] = batchim[1] # っ
                elif sy_val in 'ㅁ':
                    syll_list[sy_idx] = batchim[2] # む
                elif sy_val in 'ㄹ':
                    syll_list[sy_idx] = batchim[3] # る
                elif sy_val in spe_syll_list:
                    pass
                    syll_list[sy_idx], temp_idx, temp_syll = self.spesyll(sy_val)
                    temp_idx_list.append(temp_idx)
                    temp_syll_list.append(temp_syll_list)
        if temp_syll_list:
            pass
            for i,v in enumerate(temp_idx_list):
                syll_list.insert(i, temp_syll_list[v])

        ###print('sy_val2', sy_val)
        ###print('syll_list_out', syll_list)
        return syll_list

    def spesyll(self, spsin):
        ins = spsin
        ses = ins
        sesidx = 1
        return ins, ses, sesidx

    ### 받침을 먼저 처리하도록 해야됨 ###
    # 특수문자(요음,받침) 처리
    def special(self, special_input):
        value = self.syll(special_input)
        value = joinjamo(value)
        ###print('join_jamos',value)
        value = self.trans(value)
        value = self.dis(value)
        ###print('return special', value)
        return value
        pass

    # 전처리
    def anl(self,anl_input):
        string = anl_input
        ###print('anlinput', string) ##
        out = list(string)
        ###print('anl_2 in', out) ##
        for i_idx, i_val in enumerate(out):
            # 조사 판별
            if i_val == 'ㅇ' or 'ㅎ' and i_idx < len(out) - 1:
                self.anl_2(i_idx, out)

        ###print('anl_2 out', out) ##
        return out

    #전처리 2 ㅇㅗ ,ㅇㅘ, ㅎㅏ 이딴거 변환
    def anl_2(self, idx, out):
        if out[idx+1] == 'ㅗ':
            out[idx] = 'ㅗ'
            del out[idx+1]

        elif out[idx+1] == 'ㅘ':
            out[idx] = 'ㅘ'
            del out[idx + 1]

        elif out[idx + 1] == 'ㅏ':
            out[idx] = 'ㅏ'
            del out[idx + 1]

    #자음처리
    def anl_3(self, anl_in):
        ilist = distjamo(anl_in)
        ilist = self.sam(ilist)
        tempidx = []
        for lidx, lval in enumerate(ilist):
            if lval in d.sajs :#and lidx < int(len(ilist))-1:
                if lidx == int(len(ilist))-1 or ilist[lidx+1] in d.moeum:
                    if   lval in d.saj_1: ilist[lidx] = 'ㅅ'
                    elif lval in d.saj_2: ilist[lidx] = 'ㅍ'
                    elif lval in d.saj_3: ilist[lidx] = 'ㅊ'
                    elif lval in d.saj_4: ilist[lidx] = 'ㅋ'
                # 쌍받침 처리 일단 쌍시옷만
                # 뒤 자음이 ㅇ인 받침 ㅆ은 종성ㅅ이랑 초성ㅅ으로 분리 근데 개복잡하네 진짜
                if lidx != int(len(ilist)) - 1 and lval == d.saj_1 and ilist[lidx-1] in d.moeum and ilist[lidx+1] == 'ㅇ':
                    tempidx.append(lidx)
                if ilist[lidx-1] in d.moeum and lval == d.saj_1:
                    ilist[lidx] = 'ㅅ'
            elif lidx == int(len(ilist))-1:
                if   lval in d.saj_1: ilist[lidx] = 'ㅅ'
                elif lval in d.saj_2: ilist[lidx] = 'ㅍ'
                elif lval in d.saj_3: ilist[lidx] = 'ㅊ'
                elif lval in d.saj_4: ilist[lidx] = 'ㅋ'
        if tempidx:
            if len(tempidx) > 1:
                rs(tempidx)
                print(tempidx)
            for idd, iv in enumerate(tempidx):
                ilist[iv] = 'ㅅ'
                tempidx[idd] += 1
        if tempidx :
            for idd in tempidx:
                ilist.insert(idd,'ㅅ')
        #ilist = self.sam(ilist)
        out_anl_3 = joinjamo(ilist)
        return out_anl_3

    # 이음동의어 ex) ㅊ ㅉ 씨=시=쉬 ㅓ=ㅗ ㅡ=ㅜ 이딴거 받침 제외하고 처리해야 될 듯
    def sam(self, ilist):
        tempval = []
        tempidx = []
        for ili, ilv in enumerate(ilist):
            ###print('test', ilv, ilist[ili - 1])
            if ilv in d.sams:
                if ilv in d.sam_1: ilist[ili] = 'ㅗ'
                elif ilv in d.sam_2: ilist[ili] = 'ㅛ'
                elif ilv in d.sam_3: ilist[ili] = 'ㅔ'
                #elif ilv in d.sam_4: ilist[ili] = 'ㅣ'
                elif ilv in d.sam_5: ilist[ili] = 'ㅡ'
            elif ilv in d.is_fu:
                if ilv in d.fu_1: #ㅗㅔ 'ㅙ', 'ㅚ'
                    ilist[ili] = 'ㅗ'
                    tempidx.append(ili)
                    tempval.append(d.fu_hina[3])
                elif ilv in d.fu_2:#ㅜㅔ 'ㅞ'
                    ilist[ili] = 'ㅡ'
                    tempidx.append(ili)
                    tempval.append(d.fu_hina[3])
                elif ilv in d.fu_3:#ㅜㅓ 'ㅝ'
                    ilist[ili] = 'ㅡ'
                    tempidx.append(ili)
                    tempval.append(d.fu_hina[4])
                elif ilv in d.fu_4:#ㅡㅣ 'ㅟ', 'ㅢ'
                    ilist[ili] = 'ㅡ'
                    tempidx.append(ili)
                    tempval.append(d.fu_hina[1])
            if ilv in 'ㅘ' and ilist[ili-1] != 'ㅇ':
                ilist[ili] = 'ㅗ'
                tempidx.append(ili)
                tempval.append(d.fu_hina[0])
        if tempval:
            ###print(tempidx)
            ###print(tempval)
            t = 1
            for i,v in enumerate(tempidx):
                ilist.insert(v+t,tempval[i])
                t += 1
        return ilist
        pass

    def ssang(self,tempidx, ):
        
        pass

    # 일반문자 번역
    def trans(self, trans_input):
        #i = self.anl(trans_input)
        #self.cnt_list = list(range(len(i))) # 특별문자 처리(def specaial)를 위한 index list
        #self.cnt_list.remove(int(len(self.cnt_list))-1) # 마지막 공백 index 제거
        i = list(trans_input)
        cnt = d.kor
        jap = d.jap
        ###print('transinput', i)  #
        for a_idx, a_val in enumerate(i):
            hiragana = 0
            for b in cnt:
                if a_val == b:
                    i[a_idx] = jap[hiragana]
                    #self.cnt_list.remove(a_idx) # 특별문자 index list에서 처리된 index 제거
                    #self.cnt += 1
                hiragana += 1
            a_idx += 1
        ###print('trans end',i)
        return i

    def join(self,x):
        output = ''.join(x)
        ###print('joinend',output)
        return output

    # ㅋㅋ 처리
    def zz(self,zzinput):
        ###print('zzinput',zzinput)
        wow1 = d.wow1
        wow2 = d.wow2
        for idx, val in enumerate(zzinput):
            if val in wow1:
                for wowidx, wowval in enumerate(wow1):
                    if val == wowval:
                        zzinput[idx] = wow2[wowidx]
                        break
        if len(zzinput) > 2 and zzinput[-1] == 'w' and zzinput[-2] != 'w':
            zzinput[-1] = '笑'
        ###print('zzoutput', zzinput)
        return zzinput

    # 특문 이건 근데 굳이 필요한가 싶음
    def sym(self):
        pass

    # 예외처리
    def exc(self):
        pass

    # 쫌만 수정하면 가타카나도 될듯
    def gata(self):
        pass


# 오지랖
def old_word(oooo):
    is_p = False
    new_output = oooo
    old = list(d.old_)
    outoldlist = []
    for o in oooo:
        if o in old:
            for i, v in enumerate(old):
                if o in old:
                    outoldlist.append(v)
                    del old[i]

    print('result:', oooo)
    if outoldlist:
        print(' '.join(outoldlist), '는 현재 잘 쓰이지 않는 문자입니다')
        is_op = input("자주 사용되는 문자로 변환 할까요? y or ㅇ :")
        op_ = ['y', 'ㅇ', 'Y', 'y ', 'ㅇ ', 'Y ',' y', ' ㅇ', ' Y',' y ', ' ㅇ ', ' Y ']
        if is_op in op_:
            is_p = True
            new_output = old_process(oooo)
    return new_output, is_p


def old_process(in_old_list):
    ols = list(in_old_list)
    old = list(d.old_)
    new = list(d.new_)
    for oi, ov in enumerate(ols):
        for i, v in enumerate(old):
            if ov == v:
                ols[oi] = new[i]
    ols = ''.join(ols)
    return ols


def main_process():
    input_ = get_item()
    is_p = True
    #print('input :', input_)
    translation = Translation(input_)
    output = translation.x
    output, is_p = old_word(output)
    if is_p:
        print('result:', output)
    if is_not_test: # 컴파일시 비활성화
        main_process()

if __name__ == "__main__":
    #input_ = '츤데레가루아이리'#for test
    '''
    input_ = get_item()
    if input_ == "exit":
        exit()
    print('input :', input_)
    translation = Translation(input_)
    output = translation.x
    print('result:', output)
    old_word(output)
    print(' ')
    '''
    print("input e => exit")
    #is_not_test = False # 배포시 비활성화

    main_process()

    # 왤케코드가 길어?