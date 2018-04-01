import thulac


def fenci(thu1, fullSentence):
    #   thu1 = thulac.thulac(user_dict=None, model_path=None, T2S=False, seg_only=True, filt=False, deli='_', rm_space =False)
    segement = thu1.cut(fullSentence, text=False)  # 进行一句话分词
    return segement


if __name__ == '__main__':
    print(fenci("今天天气真好呢"))
