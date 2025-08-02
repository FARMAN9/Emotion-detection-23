
Here’s a **cleaner, more polished** version of your README with better structure, consistent formatting, and a more professional tone:

---

# 🎭 Emotion Detection using Deep Learning

## 📌 Overview

This project classifies **human facial emotions** into one of **seven categories** using a **Deep Convolutional Neural Network (CNN)**.

The model is trained on the **FER-2013 dataset**, published during the **International Conference on Machine Learning (ICML)**.

📊 **Dataset Details**:

* **35,887** grayscale images
* Size: **48×48 pixels**
* **7 Emotion Classes**: 😠 Angry | 🤢 Disgusted | 😨 Fearful | 😄 Happy | 😐 Neutral | 😢 Sad | 😲 Surprised

---

## ⚙️ Dependencies

* 🐍 **Python 3**
* 📦 [OpenCV](https://opencv.org/)
* 🔥 [TensorFlow](https://www.tensorflow.org/) (Keras API)

Install required packages:

```bash
pip install -r requirements.txt
```

---

## 🚀 Getting Started

### 📂 Clone Repository

```bash
git clone 
cd Emotion-detection
```

### 📥 Download Dataset

Place the **FER-2013 dataset** inside the `src/data` folder.

---

## 🏋️ Training the Model

Run the following command to train:

```bash
cd src
python emotions.py --mode train
```

* ✅ Trains the CNN on FER-2013 dataset
* ✅ Saves model weights as **`model.h5`**
* ✅ Generates training **accuracy & loss plots**

---

## 🔍 Using Pre-trained Model


```
emotion_dataset/
   train/
       angry/
           angry1.jpg
           angry2.jpg
           ...
       disgust/
           disgust1.jpg
           disgust2.jpg
           ...
       fear/
           fear1.jpg
           fear2.jpg
           ...
       happy/
           happy1.jpg
           happy2.jpg
           ...
       neutral/
           neutral1.jpg
           neutral2.jpg
           ...
       sad/
           sad1.jpg
           sad2.jpg
           ...
       surprise/
           surprise1.jpg
           surprise2.jpg
           ...
   validation/
       angry/
           angry101.jpg
           ...
       disgust/
           disgust101.jpg
           ...
       fear/
           fear101.jpg
           ...
       happy/
           happy101.jpg
           ...
       neutral/
           neutral101.jpg
           ...
       sad/
           sad101.jpg
           ...
       surprise/
           surprise101.jpg
           ...
```

✅ **What you need to do:**

* Place images of each **emotion** into its correct folder.
* Keep the **same 7 folders** under both `train/` and `validation/`.
* Make sure filenames are **unique** (no duplicates).

---

### 🚀 **Where to get images?**

Here are some free datasets you can download:

* **FER2013** (most popular):
  📥 [Kaggle FER2013 Dataset](https://www.kaggle.com/datasets/msambare/fer2013)

* **CK+ (Cohn-Kanade)**:
  📥 [CK+ Dataset (via Kaggle)](https://www.kaggle.com/datasets/shawon10/ckplus)

* **JAFFE Dataset** (Japanese Female Facial Expression):
  📥 [JAFFE dataset download](https://zenodo.org/record/3451524)

---




You can skip training by downloading the **pre-trained model**:
[📥 Download Model](https://drive.google.com/file/d/1FUn0XNOzf-nQV7QjbBPA6-8GLoHNNgv-/view?usp=sharing)

Then run:

```bash
cd src
python emotions.py --mode display
```

This will:
✔️ Start webcam feed
✔️ Detect faces using **Haar Cascades**
✔️ Classify emotions in **real-time**

---

## 📁 Project Structure

```
Emotion-detection/
│
├── imgs/                   # Plots & visuals
├── src/
│   ├── data/               # FER-2013 dataset
│   ├── emotions.py         # Main script (train/display)
│   ├── haarcascade_frontalface_default.xml
│   ├── model.h5            # Saved model weights
│
├── requirements.txt
└── README.md
```

---

## 📊 Model Performance

* **Architecture**: 4-layer CNN
* **Training Epochs**: 50
* **Test Accuracy**: \~63.2%

📈 *Accuracy Plot Example:*
![Accuracy plot](imgs/accuracy.png)

---

## 🛠 Data Preparation (Optional)

The original [FER-2013 dataset](https://www.kaggle.com/deadskull7/fer2013) is in CSV format.
We converted it into **48×48 PNG images** for training & testing.

* 📜 See `dataset_prepare.py` for conversion code.
* 🧪 Can be modified for **custom datasets**.

---

## 🔬 How It Works

1️⃣ **Face Detection** – Uses **Haar Cascade** to detect faces.
2️⃣ **Preprocessing** – Crops & resizes face to **48×48 grayscale**.
3️⃣ **Prediction** – CNN outputs **softmax probabilities** for 7 emotions.
4️⃣ **Display** – The predicted emotion is displayed on webcam feed.

---

## 📚 References

> Goodfellow, I., Erhan, D., Carrier, P. L., Courville, A., Mirza, M., Hamner, B., ... & Bengio, Y. (2013).
> *Challenges in Representation Learning: A report on three machine learning contests.*
> arXiv preprint arXiv:1307.0414.

---

✅ **Would you like me to:**

* Add **badges** (e.g., Python version, TensorFlow version)?
* Include a **sample webcam output screenshot** section?
* Or convert this into a **fancier GitHub README with emojis & banners**?
