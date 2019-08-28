from math import log
import operator
import matplotlib.pyplot as plt
def create_data_set():
    """
    创建样本数据
    :return:
    """
    data_set = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return data_set, labels

def calc_shannon_ent(data_set):
    """
    计算信息熵
    :param data_set: 如： [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    :return:
    """
    num = len(data_set)  # n rows
    print('第一个:',num)
    # 为所有的分类类目创建字典
    label_counts = {}
    for feat_vec in data_set:
        current_label = feat_vec[-1]  # 取得最后一列数据
        if current_label not in label_counts.keys():
            label_counts[current_label] = 0
        label_counts[current_label] += 1
    # 计算香浓熵
    shannon_ent = 0.0
    for key in label_counts:
        prob = float(label_counts[key]) / num
        shannon_ent = shannon_ent - prob * log(prob, 2)
    return shannon_ent

def split_data_set(data_set, axis, value):
    """
    返回特征值等于value的子数据集，切该数据集不包含列（特征）axis
    :param data_set:  待划分的数据集
    :param axis: 特征索引
    :param value: 分类值
    :return:
    """
    ret_data_set = []
    for feat_vec in data_set:
        if feat_vec[axis] == value:
            reduce_feat_vec = feat_vec[:axis]
            reduce_feat_vec.extend(feat_vec[axis + 1:])
            ret_data_set.append(reduce_feat_vec)
    return ret_data_set

def choose_best_feature_to_split(data_set):
    """
    按照最大信息增益划分数据
    :param data_set: 样本数据，如： [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    :return:
    """
    num_feature = len(data_set[0]) - 1 # 特征个数，如：不浮出水面是否可以生存  和是否有脚蹼
    base_entropy = calc_shannon_ent(data_set) # 经验熵H(D)
    best_info_gain = 0
    best_feature_idx = -1
    for feature_idx in range(num_feature):
        feature_val_list = [number[feature_idx] for number in data_set]  # 得到某个特征下所有值（某列）
        unique_feature_val_list = set(feature_val_list)  # 获取无重复的属性特征值
        new_entropy = 0
        for feature_val in unique_feature_val_list:
            sub_data_set = split_data_set(data_set, feature_idx, feature_val)
            prob = len(sub_data_set) / float(len(data_set)) # 即p(t)
            new_entropy += prob * calc_shannon_ent(sub_data_set) #对各子集香农熵求和
        info_gain = base_entropy - new_entropy # 计算信息增益，g(D,A)=H(D)-H(D|A)
        # 最大信息增益
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature_idx = feature_idx
    return best_feature_idx

if __name__=='__main__':
    data_set,labels=create_data_set()
    print(calc_shannon_ent(data_set))