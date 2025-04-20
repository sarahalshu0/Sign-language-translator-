async function loadModel() {
  const model = await tf.loadLayersModel('web_model/model.json');
  return model;
}

async function predict() {
  const imageInput = document.getElementById('image-upload').files[0];
  const img = new Image();
  img.src = URL.createObjectURL(imageInput);

  img.onload = async () => {
    const model = await loadModel();
    const tensor = tf.browser.fromPixels(img)
      .resizeNearestNeighbor([64, 64])
      .toFloat()
      .expandDims(0);

    const prediction = model.predict(tensor);
    const predictionArray = prediction.arraySync();
    const predictedClassIndex = predictionArray[0].indexOf(Math.max(...predictionArray[0]));

    // قائمة الحروف الأبجدية العربية
    const arabicLetters = ["أ", "ب", "ت", "ث", "ج", "ح", "خ", "د", "ذ", "ر", "ز", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ك", "ل", "م", "ن", "هـ", "و", "ي"];
    
    document.getElementById('prediction').innerText = `الحرف المتوقع: ${arabicLetters[predictedClassIndex]}`;
  };
}
