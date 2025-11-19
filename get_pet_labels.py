from os import listdir

def get_pet_labels(image_dir):
    results_dic = {}
    for file_name in listdir(image_dir):
        if file_name.startswith("."):
            continue
        parts = file_name.lower().split("_")
        label = " ".join([w for w in parts if w.isalpha()]).strip()
        if file_name not in results_dic:
            results_dic[file_name] = [label]
    return results_dic
