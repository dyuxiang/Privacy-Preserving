# Privacy-Preserving Methods: k-Anonymity, l-Diversity, and t-Closeness

This project explores and compares three widely-used privacy-preserving techniques: **k-Anonymity**, **l-Diversity**, and **t-Closeness**. These methods play a crucial role in protecting personal information during data sharing and analysis.



## About the Project

In today's digital age, protecting data privacy has become more critical than ever. With the growing reliance on data sharing and big data analytics, maintaining the balance between data utility and privacy poses significant challenges.

This project delves into three prominent privacy-preserving techniques to address these challenges:

- **k-Anonymity**
- **l-Diversity**
- **t-Closeness**

By implementing and comparing these methods, the project aims to:

1. **Safeguard Personal Information**: Prevent the disclosure of sensitive data while maintaining data usability.
2. **Provide Implementation Insights**: Offer theoretical background, practical implementation, and performance evaluation.
3. **Guide Privacy Strategy Selection**: Help users choose the most suitable privacy-preserving method for their needs.

Through this research, we aim to promote safer data management practices and enhance public awareness of data privacy protection.



## Methodology

### 1. Data Preprocessing

Before applying privacy-preserving techniques, the dataset undergoes preprocessing:

- **Remove Unnecessary Columns**: Exclude irrelevant features.
- **Handle Missing Data**: Eliminate incomplete entries or impute missing values.
- **Clean and Normalize**: Ensure the data is consistent for further analysis.

### 2. Privacy Preservation Techniques

The following methods are implemented on the preprocessed data:

#### **k-Anonymity**
- Makes each record indistinguishable from at least **k-1 other records** in the dataset.
- Protects individuals by reducing the granularity of data.

#### **k-Anonymity + l-Diversity**
- Extends k-anonymity by ensuring that **sensitive attributes** have at least **l diverse values** within each anonymized group.
- Protects against homogeneity attacks and background knowledge attacks.

#### **k-Anonymity + l-Diversity + t-Closeness**
- Further improves privacy by ensuring the **distribution of sensitive attributes** within each anonymized group is close to their distribution in the entire dataset.
- Mitigates skewness and similarity attacks.

### 3. Machine Learning Model Training and Evaluation

To evaluate the impact of these privacy techniques on data utility:

- **Models Used**: Multi-Layer Perceptron (MLP) and Support Vector Machine (SVM).
- **Evaluation Metrics**: Accuracy, efficiency, and performance are compared across datasets with different privacy-preserving techniques applied.



## Paper References

### **k-Anonymity**
- K. LeFevre, D. J. DeWitt, and R. Ramakrishnan, "Mondrian Multidimensional k-Anonymity," in *Proceedings of the 22nd International Conference on Data Engineering (ICDE)*, 2006.  
  [Read the paper](https://personal.utdallas.edu/~mxk055100/courses/privacy08f_files/MultiDim.pdf)

### **l-Diversity**
- A. Machanavajjhala, J. Gehrke, D. Kifer, and M. Venkitasubramaniam, "l-Diversity: Privacy Beyond k-Anonymity," in *Proceedings of the 22nd International Conference on Data Engineering (ICDE)*, IEEE, 2006.  
  [Read the paper](https://personal.utdallas.edu/~muratk/courses/privacy08f_files/ldiversity.pdf)

### **t-Closeness**
- Ninghui Li, Tiancheng Li, and Suresh Venkatasubramaniam, "t-Closeness: Privacy Beyond k-Anonymity and l-Diversity," in *Proceedings of the 23rd International Conference on Data Engineering (ICDE)*, IEEE, 2007.  
  [Read the paper](https://www.cs.purdue.edu/homes/ninghui/papers/t_closeness_icde07.pdf)



## Steps to Reproduce

1. **Preprocess the Data**: Clean the dataset and handle missing values.
2. **Apply Privacy Techniques**: Implement k-Anonymity, l-Diversity, and t-Closeness in sequence.
3. **Train Machine Learning Models**:
   - Use MLP and SVM to evaluate data utility after applying privacy-preserving techniques.
4. **Compare Results**: Analyze the trade-offs between privacy protection and model performance.

---

## Contact

For any questions or feedback, feel free to reach out:

- **Name**: Ding Yu Xiang  
- **Email**: [dyx2000803a@gmail.com](mailto:dyx2000803a@gmail.com)  
- **GitHub**: [dyuxiang](https://github.com/dyuxiang/Privacy-Preserving)

---

## Project Link

[Explore the Repository](https://github.com/dyuxiang/Privacy-Preserving)
