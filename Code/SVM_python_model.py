import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_curve, roc_auc_score

from sklearn.svm import SVC

# source
#source_list_mode = ['mean', 'median', 'mode']
#source_list_mode = ['', '_mean', '_mode']
source_list_mode = ['', '_mean']

#source_list_num = ['preprocessed', 'k-anonymity_5', 'k-anonymity_10', 'k-anonymity_50', 'k-anonymity_100', 'k-anonymity_200',  'k-anonymity_500', 'k-anonymity_1000', 'k-anonymity_2000'] # For k-anonymity
#source_list_num = ['preprocessed', 'k-5_l-2', 'k-10_l-2', 'k-50_l-2', 'k-100_l-2', 'k-200_l-2', 'k-500_l-2', 'k-1000_l-2', 'k-2000_l-2'] # For k+L-diversity
#source_list_num = ['preprocessed', 'k-5_t-0.3', 'k-5_t-0.2', 'k-5_t-0.1', 'k-5_t-0.09'] 
#source_list_num = ['preprocessed', 'k-5_t-0.2', 'k-50_t-0.2', 'k-200_t-0.2', 'k-500_t-0.2', 'k-1000_t-0.2', 'k-2000_t-0.2']     # For k+T-closeness
source_list_num = ['preprocessed', 'k-5_t-0.1', 'k-50_t-0.1', 'k-200_t-0.1', 'k-500_t-0.1', 'k-1000_t-0.1', 'k-2000_t-0.1']                           
#source_list_num = ['preprocessed', 'k-5_t-0.09', 'k-50_t-0.09', 'k-200_t-0.09', 'k-500_t-0.09', 'k-1000_t-0.09', 'k-2000_t-0.09'] 



evaluation_totaldata = {}
evaluation_total = pd.DataFrame(evaluation_totaldata)

for m in source_list_mode:
    for k in source_list_num:

        if (m == "" and k != "preprocessed") or (m != "" and k == "preprocessed"):
           continue

        print(k + '_' + 'Generalization' + m )

        #train_source = 'dataset/k_anonymity/adult_'+ k + m + '.csv' 
        #train_source = 'dataset/k+l/adult_'+ k + m + '.csv' 
        train_source = 'dataset/k+l+t/adult_'+ k + m + '.csv' 


        test_source = 'dataset/adult_test_preprocessed.csv'

        #output_file_total = 'evaluation_k/SVM_evaluation_k2_total.csv'
        #output_file_total = 'evaluation_k_l/SVM_evaluation_kl_total.csv'
        #output_file_total = 'evaluation_k_l_t/SVM_evaluation_k=5_t_total.csv'
        #output_file_total = 'evaluation_k_l_t/SVM_evaluation_k_t=0.2_total.csv'
        output_file_total = 'evaluation_k_l_t/SVM_evaluation_k222_t=0.1_total.csv'
        #output_file_total = 'evaluation_k_l_t/SVM_evaluation_k_t=0.09_total.csv'

        # load data
        train_data = pd.read_csv(train_source, sep=r'\s*,\s*', engine='python')
        test_data = pd.read_csv(test_source, sep=r'\s*,\s*', engine='python')

        # Classify attributes into numbers and strings
        def category_attribute(dataset, list, num_list, str_list): 
            for attribute in list:
                #print(feature, type(dataset[feature][1]))
                if type(dataset[attribute][1]) == str:
                    str_list.append(attribute)
                else:
                    num_list.append(attribute)
            return num_list, str_list

        numerical_attribute_list = []
        str_attribute_list = []

        attribute_list = pd.read_csv(train_source, nrows=0)
        #print(attribute_list)
        numerical_attribute_list, str_attribute_list = category_attribute(train_data, attribute_list, numerical_attribute_list, str_attribute_list)

        # train_data normalization
        le=LabelEncoder()
        for i in str_attribute_list:
            train_data[i]=le.fit_transform(train_data[i])
        #print(train_data)

        # test_data normalization
        le=LabelEncoder()
        for i in str_attribute_list:
            test_data[i]=le.fit_transform(test_data[i])
        #print(train_data)

        # split data & label (train)
        x_train = train_data.iloc[:,0:13]
        y_train = train_data.iloc[:,13]
        # split data & label (test)
        x_test = test_data.iloc[:,0:13]
        y_test = test_data.iloc[:,13]

        #standardizing the input feature
        sc = StandardScaler()
        x_train = sc.fit_transform(x_train)
        #x_train
        x_test = sc.fit_transform(x_test)
        #x_test

        svm = SVC(C=10, gamma = 'auto',kernel='rbf',probability=True, max_iter = 200000)
        svm.fit(x_train, y_train)

        #svm.predict(x_test)
        y_pred=svm.predict(x_test)
        y_pred_new =(y_pred>0.5)
        y_pred_new

        # confusion_matrix
        cm = confusion_matrix(y_test, y_pred_new)
        print(cm)

        # Evaluation
        # Accuracy: (TP + TN) / (TP + TN + FP + FN)
        accuracy = accuracy_score(y_test, y_pred_new)
        # Precision: TP / (TP + FP)
        precision = precision_score(y_test, y_pred_new)
        # Recall: TP / (TP + FN)
        recall = recall_score(y_test, y_pred_new)
        # F1-score: (2 * Precision * Recall) / (Precision + Recall))
        F1_score = (2 * precision * recall) / (precision + recall)
        # AUC 需要原始的預測概率(y_pred)而不是二元的預測結果(y_pred_new)
        # 假設 y_pred 是模型預測的概率值
        auc = roc_auc_score(y_test, y_pred)

        #evaluation_totaldata = pd.DataFrame({"K":[ k.replace('k-anonymity_', '').replace('preprocessed', 'original') ], "Generalization_mode_":[ m.replace('_', '') ],  #For K-anonymity
        #                                    "Accuracy":[accuracy],"Precision":[precision],"Recall":[recall],"F1_score":[F1_score],"AUC":[auc]})
        evaluation_totaldata = pd.DataFrame({"K":[ k.replace('-', '=').replace('preprocessed', 'original') ], "Generalization_mode_":[ m.replace('_', '') ],           #For L-diversity & T-closeness
                                            "Accuracy":[accuracy],"Precision":[precision],"Recall":[recall],"F1_score":[F1_score],"AUC":[auc]})
        
        evaluation_total = pd.concat([evaluation_total, evaluation_totaldata], ignore_index=True)

# Write as new CSV file 
evaluation_total.to_csv(output_file_total, index=False)