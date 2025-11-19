def adjust_results4_isadog(results_dic, dogfile):
    dognames_dic = {}
    with open(dogfile, "r") as infile:
        for line in infile:
            name = line.strip().lower()
            if name not in dognames_dic:
                dognames_dic[name] = 1
    for key in results_dic:
        pet_label = results_dic[key][0]
        classifier_label = results_dic[key][1]
        pet_is_dog = 1 if pet_label in dognames_dic else 0
        classifier_is_dog = 0
        for w in classifier_label.split(","):
            if w.strip() in dognames_dic:
                classifier_is_dog = 1
                break
        results_dic[key].extend([pet_is_dog, classifier_is_dog])
