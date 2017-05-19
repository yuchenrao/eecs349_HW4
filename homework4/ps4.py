import numpy as np
import math
import json

def cosine_similarity(array1, array2):
    cos_sim = 0
    cos_sim_1 = 0
    cos_sim_2 = 0
    for i in range(len(array1)):
        cos_sim = cos_sim + array1[i]*array2[i]
        cos_sim_1 = cos_sim_1 + array1[i]*array1[i]
        cos_sim_2 = cos_sim_2 + array2[i]*array2[i]
    result = cos_sim / (math.sqrt(cos_sim_1)*math.sqrt(cos_sim_2))

    return result

def question_5():

    with open('cnn_dataset.json') as data_file:
        data = json.load(data_file)

    mj1_vgg = data['vgg_rep']['mj1']
    mj2_vgg = data['vgg_rep']['mj2']
    cat_vgg = data['vgg_rep']['cat']
    mj1_pix = data['pixel_rep']['mj1']
    mj2_pix = data['pixel_rep']['mj2']
    cat_pix = data['pixel_rep']['cat']

    v_12 = cosine_similarity(mj1_vgg,mj2_vgg)
    v_1c = cosine_similarity(mj1_vgg,cat_vgg)
    v_2c = cosine_similarity(mj2_vgg,cat_vgg)
    p_12 = cosine_similarity(mj1_pix,mj2_pix)
    p_1c = cosine_similarity(mj1_pix,cat_pix)
    p_2c = cosine_similarity(mj2_pix,cat_pix)

    print v_12, v_1c, v_2c, p_12, p_1c, p_2c

def question_7():

    with open('dataset.json') as data_file:
        data = json.load(data_file)

    vgg = np.load('vgg_rep.npy')
    pixel = np.load('pixel_rep.npy')

    train = data['train']
    test = data['test']
    images = data['images']
    captions = data['captions']

    test_data_vgg = []
    test_data_pix = []
    test_name = []
    train_data_vgg = []
    train_data_pix = []
    train_name = []
    train_captions = []

    # test data
    for t in test:
        test_name.append(t)
        index = images.index(t)
        test_data_vgg.append(vgg[index])
        test_data_pix.append(pixel[index])

    # train data
    for t in train:
        train_name.append(t)
        index = images.index(t)
        train_data_vgg.append(vgg[index])
        train_data_pix.append(pixel[index])
        train_captions.append(captions[t])

    f1 = open('vgg.txt', 'w')
    f2 = open('pixel.txt', 'w')
    for i in range(len(test_name)):
        sim_vgg = []
        sim_pix = []
        for j in range(len(train_name)):
            sim_vgg.append(cosine_similarity(test_data_vgg[i], train_data_vgg[j]))
            sim_pix.append(cosine_similarity(test_data_pix[i], train_data_pix[j]))
        vgg_max_index = sim_vgg.index(max(sim_vgg))
        print vgg_max_index
        pix_max_index = sim_pix.index(max(sim_pix))
        vgg_cap = train_captions[vgg_max_index]
        pix_cap = train_captions[pix_max_index]
        vgg_train_name = train_name[vgg_max_index]
        pix_train_name = train_name[pix_max_index]
        testname = test_name[i]

        f1.write(vgg_cap + ' ' + vgg_train_name + ' ' + testname + '\n')
        f2.write(pix_cap + ' ' + pix_train_name + ' ' + testname + '\n')

    f1.close()
    f2.close()


def main():

    question_7()


if __name__ == "__main__":
    main()


