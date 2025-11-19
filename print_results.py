def print_results(results_dic, results_stats_dic, model, print_incorrect_dogs=False, print_incorrect_breed=False):
    print("\n*** Results Summary for CNN Model Architecture", model.upper(), "***")
    print("\nNumber of Images:", results_stats_dic['n_images'])
    print("Number of Dog Images:", results_stats_dic['n_dogs_img'])
    print("Number of Not-a-Dog Images:", results_stats_dic['n_notdogs_img'])
    print("\n*** Percentage Statistics ***")
    for key in results_stats_dic:
        if key.startswith('pct_'):
            print("{:20}: {:.2f}".format(key, results_stats_dic[key]))
    if print_incorrect_dogs and (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images']):
        print("\n*** Misclassified Dogs ***")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 1:
                print("Pet Image: {:>26}  Classifier Label: {:>30}".format(results_dic[key][0], results_dic[key][1]))
    if print_incorrect_breed and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']):
        print("\n*** Misclassified Dog Breeds ***")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                print("Pet Image: {:>26}  Classifier Label: {:>30}".format(results_dic[key][0], results_dic[key][1]))
    print("\n*** End of Results ***\n")
