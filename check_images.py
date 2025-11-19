from time import time
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

def main():
    start_time = time()
    print("\n*** Starting Image Classification Pipeline ***\n")
    in_arg = get_input_args()
    print("Command Line Arguments:\n Directory =", in_arg.dir, "\n CNN Model =", in_arg.arch, "\n Dogfile =", in_arg.dogfile, "\n")
    results_dic = get_pet_labels(in_arg.dir)
    print("Total Images Found:", len(results_dic))
    classify_images(in_arg.dir, results_dic, in_arg.arch)
    adjust_results4_isadog(results_dic, in_arg.dogfile)
    results_stats_dic = calculates_results_stats(results_dic)
    print("\n*** Summary of Results Statistics ***")
    for key, value in results_stats_dic.items():
        print(f"{key}: {value}")
    print_results(results_dic, results_stats_dic, in_arg.arch, print_incorrect_dogs=True, print_incorrect_breed=True)
    print("\n*** End of Image Classification Pipeline ***\n")
    end_time = time()
    tot_time = end_time - start_time
    print("\nTotal Elapsed Runtime:", str(int(tot_time / 3600)) + ":" + str(int((tot_time % 3600) / 60)) + ":" + str(int((tot_time % 3600) % 60)))

if __name__ == "__main__":
    main()
