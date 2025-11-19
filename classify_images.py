from classifier import classifier

def classify_images(images_dir, results_dic, model):
    for key in results_dic:
        path = images_dir + key
        label = classifier(path, model).lower().strip()
        truth = results_dic[key][0]
        match = 1 if truth in label else 0
        results_dic[key].extend([label, match])
