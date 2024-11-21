# Privacy Preserving methods based on “k-anonymity”, “l-Diversity” and “t-Closeness” algorithm

This project aims to implement and compare three widely used privacy-preserving techniques: k-Anonymity, l-Diversity, and t-Closeness. These methods are essential for protecting personal information during data sharing and analysis.

## About the Project
In today's digital age, data privacy protection has become increasingly important. With the widespread adoption of data sharing and big data analytics, maintaining data utility while safeguarding personal privacy presents a significant challenge. This project explores and compares three commonly used privacy-preserving techniques: k-Anonymity, l-Diversity, and t-Closeness, to address this challenge.
These methods are widely applied in data privacy protection to prevent the disclosure of personal information. The project provides theoretical background, implementation details, and performance evaluation of these techniques on various datasets. This helps users choose the most suitable privacy protection strategy. Through this research, we aim to promote safer data management practices and enhance public awareness of data privacy protection.

## Method / Paper References

- **k-Anonymity**: K. LeFevre, D. J. DeWitt, and R. Ramakrishnan, "Mondrian Multidimensional k-Anonymity," in Proceedings of the 22nd International Conference on Data Engineering (ICDE), 2006. [[Paper]](https://personal.utdallas.edu/~mxk055100/courses/privacy08f_files/MultiDim.pdf)

- **l-Diversity**: A. Machanavajjhala, J. Gehrke, D. Kifer, and M. Venkitasubramaniam, "l-Diversity: Privacy Beyond k-Anonymity," in Proceedings of the 22nd International Conference on Data Engineering (ICDE), IEEE, 2006. [[Paper]](https://personal.utdallas.edu/~muratk/courses/privacy08f_files/ldiversity.pdf)

- **t-Closeness**: Ninghui Li, Tiancheng Li, and Suresh Venkatasubramaniam, "t-Closeness: Privacy Beyond k-Anonymity and l-Diversity," in Proceedings of the 23rd International Conference on Data Engineering (ICDE), IEEE, 2007. [[Paper]](https://www.cs.purdue.edu/homes/ninghui/papers/t_closeness_icde07.pdf)


### Steps
1.Data Preprocessing

Begin with preprocessing the dataset. This involves removing unnecessary columns and handling missing data by eliminating incomplete entries. Ensure the data is clean and consistent for further analysis and processing.

2.Privacy Preservation Techniques

Apply the following privacy preservation techniques to the preprocessed data:

- k-Anonymity: Implement k-anonymity to protect personal information by making each record indistinguishable from at least k-1 other records.
- k-Anonymity + l-Diversity: Enhance privacy by adding l-diversity to k-anonymity, ensuring that sensitive attributes have a diverse range of values.
- k-Anonymity + l-Diversity + t-Closeness: Further improve privacy by incorporating t-closeness, which maintains the distribution of sensitive attributes within a certain threshold.

3.Machine Learning Model Training and Evaluation

Train and evaluate the data using Multi-Layer Perceptron (MLP) and Support Vector Machine (SVM). This step aims to assess the impact of different privacy preservation techniques on model performance and compare the accuracy and efficiency of the models.



## Contact
Ding Yu Xiang - [dyx2000803a@gmail.com](Gmail:dyx2000803a@gmail.com)

Project Link: [https://github.com/dyuxiang/](https://github.com/dyuxiang/Privacy-Preserving)
