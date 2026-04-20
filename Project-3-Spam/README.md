# Project 3 - Naive Bayes Spam Detection

Spam detector for SMS messages using multinomial Naive Bayes with Laplace smoothing (alpha=1). Implementation is in `project3_naive_bayes.ipynb`, dataset is `SMS.txt`.

## Requirements

Python 3 with pandas, numpy, scikit-learn, jupyter.

```
pip install pandas numpy scikit-learn jupyter
```

## Run

Open in Jupyter and run all cells:

```
jupyter notebook project3_naive_bayes.ipynb
```

Or run the whole thing from the command line:

```
python3 -m nbconvert --to notebook --execute project3_naive_bayes.ipynb --output project3_naive_bayes.ipynb
```

## Results

F1 ~ 0.955 on the test set. The bonus cell at the end also runs sklearn's MultinomialNB on the same split for comparison.

## Comparison with Extra Credit (MultinomialNB)

|              | My implementation | sklearn MultinomialNB |
|--------------|-------------------|-----------------------|
| Accuracy     | 0.9883            | 0.9838                |
| Precision    | 0.9653            | 0.9448                |
| Recall       | 0.9456            | 0.9320                |
| F1           | 0.9553            | 0.9384                |

Both use multinomial Naive Bayes with alpha=1 on the same train/test split, so the scores are close. My version scores slightly higher mostly because CountVectorizer drops single-character tokens like "u" and "s", which are actually useful signals in this dataset.

## AI Notice

AI was only used for minor things such as fixing small syntax errors, cleaning up print formatting, and helping word a couple of comments. The algorithm, probability calculation, confusion matrix logic, and analysis were written by me.

