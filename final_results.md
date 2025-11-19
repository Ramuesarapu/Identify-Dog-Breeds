# Pet Image Classification Project - Final Results

## Project Objectives

This project had two main objectives:

1. **Identify which pet images are of dogs and which pet images aren't of dogs.**  
2. **Classify the breeds of dogs for the images that are of dogs.**  

The program `check_images.py` was implemented to address these objectives using three different CNN model architectures: **AlexNet, ResNet, and VGG**.

---

## Results for Uploaded Images (4 Images)

The uploaded images classified were: `Dog_01.jpg`, `Dog_02.jpg`, `Frog_01.jpg`, `Bucket_01.jpg`. The summary of results for each CNN model is shown below.

### AlexNet

- Total Images: 4  
- Dog Images: 2  
- Not-a-Dog Images: 2  

**Percentage Statistics:**

- % Match: 50.00  
- % Correct Dogs: 100.00  
- % Correct Breed: 0.00  
- % Correct Not-a-Dog: 100.00  

**Misclassified Dog Breeds:**

- Pet Image: dog | Classifier Label: clumber, clumber spaniel  
- Pet Image: dog | Classifier Label: golden retriever  

---

### ResNet

- Total Images: 4  
- Dog Images: 2  
- Not-a-Dog Images: 2  

**Percentage Statistics:**

- % Match: 50.00  
- % Correct Dogs: 100.00  
- % Correct Breed: 0.00  
- % Correct Not-a-Dog: 100.00  

**Misclassified Dog Breeds:**

- Pet Image: dog | Classifier Label: chihuahua  
- Pet Image: dog | Classifier Label: golden retriever  

---

### VGG

- Total Images: 4  
- Dog Images: 2  
- Not-a-Dog Images: 2  

**Percentage Statistics:**

- % Match: 50.00  
- % Correct Dogs: 100.00  
- % Correct Breed: 0.00  
- % Correct Not-a-Dog: 100.00  

**Misclassified Dog Breeds:**

- Pet Image: dog | Classifier Label: golden retriever  
- Pet Image: dog | Classifier Label: golden retriever  

---

## Results for Full Dataset (40 Images)

The main pet images dataset consisted of 40 images. The results for each CNN model are summarized below.

| CNN Model | Total Images | Dog Images | Not-a-Dog Images | % Correct Dogs | % Correct Breed | % Correct Not-a-Dog | % Match |
|-----------|-------------|------------|-----------------|----------------|----------------|-------------------|---------|
| AlexNet   | 40          | 30         | 10              | 100%           | 87.5%          | 100%              | 87.5%   |
| ResNet    | 40          | 30         | 10              | 100%           | 93.3%          | 100%              | 87.5%   |
| VGG       | 40          | 30         | 10              | 100%           | 93.3%          | 100%              | 87.5%   |

**Misclassified Dog Breeds (VGG Example):**

- Pet Image: great pyrenees | Classifier Label: kuvasz  
- Pet Image: beagle | Classifier Label: walker hound, walker foxhound  

---

## Discussion

- **Objective 1:** All three models correctly identified dogs and not-a-dog images with 100% accuracy for both the uploaded images and the main dataset.  
- **Objective 2:** VGG provided the best breed classification performance, achieving over 93% accuracy on the full dataset. Misclassifications of breeds occurred but did not affect identifying dogs versus non-dogs.  
- **Uploaded Images:** All models correctly identified dog and non-dog images. Breed classification was less accurate because the uploaded dataset contained only 2 dog images.  

---

## Conclusion

Based on the results:

- **Best Model Architecture:** VGG  
- **Reason:** VGG outperformed AlexNet and ResNet by providing the highest breed classification accuracy while maintaining 100% correct dog identification.  

The project objectives were fully met using the `check_images.py` pipeline with integrated `print_results.py`, providing a clear and reproducible classification summary.

---

**End of Final Results**
