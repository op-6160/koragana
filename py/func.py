from jamo import h2j, j2hcj
from hangul_utils import join_jamos
import data

def get_item():
    get_string = input("input:")
    ###print(get_string) #input 검증
    return get_string


class Translation:
    def __init__(self, input_string):
        self.val = input_string
        self.cnt = 0
        self.kor = data.kor
        self.jap = data.jap
        self.ja = data.jaeum
        self.ja_ex = data.jaeum_ex
        self.mo = data.moeum
        self.yo = data.jap_yo
        self.x = self.trans(self.val)
        self.x = self.special(self.x)
        self.x = self.join(self.x)

    # 요음(ㅑㅠㅛ) 처리
    def dis(self, dis_input):
        dis_list_ = list(j2hcj(h2j(dis_input)))
        ja_list = self.ja
        yo_list = self.yo
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
        ###print('dis_list', dis_list_)
        return dis_list_

    # 받침 처리
    def syll(self, syll_input):
        ###print('syll_input',syll_input)
        syll_list = list(j2hcj(h2j(syll_input)))
        mo_list = self.mo
        ja_list = self.ja_ex
        ###print('syll_list',syll_list)
        for sy_idx, sy_val in enumerate(syll_list):
            ###print('sy_val1',sy_val)
            ###print('syll_list[sy_idx-2]',syll_list[sy_idx-2],sy_idx)
            #if sy_idx < len(syll_list)-1 and syll_list[sy_idx-2] not in ja_list and syll_list[sy_idx+1] not in mo_list:
                #if sy_idx != 2
                    #pass

            if syll_list[sy_idx-1] in mo_list and sy_idx != 0 and sy_idx != 1:
                if sy_val == 'ㅇ' or sy_val == 'ㄴ':
                    syll_list[sy_idx] = 'ん'
                elif sy_val == 'ㄱ' or sy_val == 'ㅂ' or sy_val == 'ㅅ':
                    syll_list[sy_idx] = 'っ'
            ###print('sy_val2', sy_val)
        ###print('syll_list_out', syll_list)
        return syll_list

    ### 받침을 먼저 처리하도록 해야됨 ###
    # 특수문자(요음,받침) 처리
    def special(self, special_input):
        value = self.syll(special_input)
        value = join_jamos(value)
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
        i_idx = 0
        for i_val in out:
            # 조사 판별
            if i_val == 'ㅇ' or 'ㅎ' and i_idx < len(out) - 1:
                self.anl_2(i_idx, out)
            i_idx += 1

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

    # 일반문자 번역
    def trans(self,trans_input):
        i = self.anl(trans_input)
        #self.cnt_list = list(range(len(i))) # 특별문자 처리(def specaial)를 위한 index list
        #self.cnt_list.remove(int(len(self.cnt_list))-1) # 마지막 공백 index 제거
        cnt = self.kor
        jap = self.jap
        ###print('transinput', i)  #
        for a_idx, a_val in enumerate(i):
            hiragana = 0
            for b in cnt:
                if a_val == b:
                    i[a_idx] = jap[hiragana]
                    #self.cnt_list.remove(a_idx) # 특별문자 index list에서 처리된 index 제거
                    self.cnt += 1
                hiragana += 1
            a_idx += 1
        ###print('trans end',i)
        return i

    def join(self,x):
        output = ''.join(x)
        ###print('joinend',output)
        return output

    # 이음동의어 ex) 씨=시=쉬 ㅓ=ㅗ ㅡ=ㅜ 이딴거
    def sam(self):
        pass

    # 특문 이건 근데 굳이 필요한가 싶음
    def sym(self):
        pass

    # 예외처리
    def exc(self):
        pass

    # 쫌만 수정하면 가타카나도 될듯
    def gata(self):
        pass

if __name__ == "__main__":
    #input_ = '츤데레가루아이리'#for test
    input_ = get_item()
    print('input :', input_)
    translation = Translation(input_)
    output = translation.x
    print('result:', output)
