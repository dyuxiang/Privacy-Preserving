## Experimental Results

This study evaluates the impact of privacy-preserving methods (k-Anonymity, l-Diversity, and t-Closeness) on data utility and analyzes the performance of Multi-Layer Perceptron (MLP) and Support Vector Machine (SVM) models under varying privacy parameters. The metrics evaluated include Accuracy, Precision, Recall, F1-score, and Area Under the ROC Curve (AUC).

---

### 1. Accuracy under k-Anonymity

<table>
  <tr>
    <td>

   | Privacy Parameter | MLP Accuracy (%) | SVM Accuracy (%) |
   |-------------------|------------------|------------------|
   | Original Dataset  | **84.69**        | **84.49**        |
   | k = 5             | 82.46           | 82.12           |
   | k = 50            | 82.06           | 80.96           |
   | k = 100           | 82.14           | 80.13           |
   | k = 500           | 81.41           | 79.90           |
   | k = 1000          | 80.29           | 77.96           |
   | k = 2000          | 78.63           | 76.78           |

    </td>
    <td>

   <img src="https://github.com/dyuxiang/Privacy-Preserving/blob/main/Figure/compare_k.png" alt="k-Anonymity Accuracy" width="400"/>

   <p style="text-align: center;">Figure 1: Accuracy under k-Anonymity.</p>

    </td>
  </tr>
</table>

**Key Observations**:
- Both MLP and SVM models show a gradual decline in accuracy as the privacy parameter (k-value) increases, indicating that stricter privacy preservation reduces model performance.
- The performance degradation in SVM is slightly more pronounced compared to MLP.

---

### 2. Accuracy under k-Anonymity + l-Diversity**

| K    | L  | MLP Accuracy (%) | SVM Accuracy (%) |
|------|----|------------------|------------------|
| Original Dataset |    | **84.73**        | **84.49**        |
| 5    | 2  | 82.36           | 82.04           |
| 10   | 2  | 81.35           | 81.41           |
| 50   | 2  | 81.84           | 80.93           |
| 100  | 2  | 81.89           | 80.13           |
| 200  | 2  | 81.08           | 79.51           |
| 500  | 2  | 81.04           | 79.91           |
| 1000 | 2  | 79.66           | 77.96           |
| 2000 | 2  | 79.38           | 76.78           |

---

**Key Observations**:
- Both MLP and SVM exhibit the highest accuracy on the original dataset, with **84.73%** for MLP and **84.49%** for SVM.
- As the \( k \)-value increases under \( L = 2 \), accuracy declines progressively for both models.
- MLP consistently outperforms SVM, maintaining higher accuracy across all tested values of \( K \).


---

### 3. Performance under t-Closeness

## 1. Fixed K-Value (K = 5)

| K    | T    | MLP Accuracy (%) | SVM Accuracy (%) |
|------|------|------------------|------------------|
| 5    | 0.3  | 82.23           | 82.12           |
| 5    | 0.2  | 81.61           | 78.36           |
| 5    | 0.1  | 77.69           | 78.03           |
| 5    | 0.09 | 77.60           | 76.99           |

**Key Observations**:
- With \( K \) fixed at 5, as \( T \)-values decrease (indicating stricter privacy), the accuracy of both MLP and SVM drops progressively.
- MLP achieves slightly higher accuracy compared to SVM under most \( T \)-values.

---

## 2. Fixed T-Value (T = 0.1)

| T    | K    | MLP Accuracy (%) | SVM Accuracy (%) |
|------|------|------------------|------------------|
| 0.1  | 5    | 78.63           | 78.03           |
| 0.1  | 50   | 78.33           | 78.03           |
| 0.1  | 200  | 78.17           | 78.31           |
| 0.1  | 500  | 78.43           | 78.31           |
| 0.1  | 1000 | 78.68           | 77.55           |
| 0.1  | 2000 | 77.24           | 77.55           |

**Key Observations**:
- With \( T \) fixed at 0.1, MLP accuracy remains relatively stable across varying \( K \)-values, with only slight fluctuations.
- SVM exhibits consistent performance at lower \( K \)-values but shows minor degradation at higher \( K \)-values.

---

### Conclusion

- **Privacy vs. Utility Trade-off**:
  - Increasing privacy parameters (k, l, or t) consistently reduces model performance across all metrics.
  - It is essential to balance privacy and utility based on the specific use case requirements.
- **Model Performance**:
  - MLP generally outperforms SVM in most cases and is more robust to privacy-preserving techniques.

Detailed experimental data and visualizations are available in the supplementary files within the project repository.
