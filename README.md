# Privacy-Preserving Methods: k-Anonymity, l-Diversity, and t-Closeness

This project explores and compares three widely-used privacy-preserving techniques: **k-Anonymity**, **l-Diversity**, and **t-Closeness**. These methods play a crucial role in protecting personal information during data sharing and analysis.

### 📖 About the Project

This project explores and compares three widely-used privacy-preserving techniques: **k-Anonymity**, **l-Diversity**, and **t-Closeness**. These methods are essential for protecting personal information during data sharing and analysis.

#### Objectives:

1. **Safeguard Personal Information**: Prevent sensitive data disclosures while retaining data usability.
2. **Provide Implementation Insights**: Deliver theoretical knowledge, practical implementations, and performance evaluations.
3. **Guide Privacy Strategy Selection**: Help users identify the most suitable privacy-preserving method for their needs.

By implementing and comparing these techniques, the project aims to promote safer data management practices and enhance public awareness of data privacy.

---

### ⚙️ Methodology

#### **1. Data Preprocessing**

Before applying privacy-preserving techniques, the dataset is cleaned and prepared:

- **Remove Unnecessary Columns**: Exclude irrelevant features.
- **Handle Missing Data**: Eliminate or impute incomplete entries.
- **Clean and Normalize**: Ensure consistency for further analysis.

#### **2. Privacy Preservation Techniques**

The project implements the following methods sequentially:

##### **k-Anonymity**
- Ensures that each record is indistinguishable from at least **k-1 other records**.
- Reduces data granularity to protect individuals.

##### **k-Anonymity + l-Diversity**
- Extends k-anonymity by ensuring that **sensitive attributes** have at least **l diverse values** in each anonymized group.
- Guards against homogeneity and background knowledge attacks.

##### **k-Anonymity + l-Diversity + t-Closeness**
- Adds t-closeness, ensuring the **distribution of sensitive attributes** within each group closely matches the dataset’s overall distribution.
- Prevents skewness and similarity attacks.

#### **3. Model Training and Evaluation**

To assess the impact of privacy-preserving techniques on data utility:

- **Models Used**: Multi-Layer Perceptron (MLP) and Support Vector Machine (SVM).
- **Evaluation Metrics**: Compare accuracy, efficiency, and performance across datasets with varying privacy levels.

---

### 📜 References

#### **k-Anonymity**
- **Paper**: K. LeFevre, D. J. DeWitt, and R. Ramakrishnan, "Mondrian Multidimensional k-Anonymity."  
  [Read the paper](https://personal.utdallas.edu/~mxk055100/courses/privacy08f_files/MultiDim.pdf)

#### **l-Diversity**
- **Paper**: A. Machanavajjhala et al., "l-Diversity: Privacy Beyond k-Anonymity."  
  [Read the paper](https://personal.utdallas.edu/~muratk/courses/privacy08f_files/ldiversity.pdf)

#### **t-Closeness**
- **Paper**: Ninghui Li et al., "t-Closeness: Privacy Beyond k-Anonymity and l-Diversity."  
  [Read the paper](https://www.cs.purdue.edu/homes/ninghui/papers/t_closeness_icde07.pdf)

---

### 🛠️ Steps to Reproduce

1. **Preprocess the Data**: Clean the dataset and handle missing values.
2. **Apply Privacy Techniques**:
   - Implement k-Anonymity, l-Diversity, and t-Closeness.
3. **Train Machine Learning Models**:
   - Use MLP and SVM to evaluate data utility after applying privacy-preserving techniques.
4. **Compare Results**: Analyze the trade-offs between privacy protection and model performance.  
   *Detailed results and analysis are available [here](https://github.com/dyuxiang/Privacy-Preserving/blob/main/Experimental%20Results.md).*

---

### 📩 Contact

For questions or feedback, feel free to reach out:

- **Name**: Ding Yu Xiang  
- **Email**: [dyx2000803a@gmail.com](mailto:dyx2000803a@gmail.com)  
- **GitHub**: [dyuxiang](https://github.com/dyuxiang/Privacy-Preserving)

---

### 🔗 Project Link

[Explore the repository: ](https://github.com/dyuxiang/Privacy-Preserving)
