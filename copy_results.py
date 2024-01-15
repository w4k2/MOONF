import shutil
import glob
import os


metrics_alias = ["ACC", "BAC", "Gmean", "Gmean2", "Gmean_pr", "F1score", "Recall", "Specificity", "Precision"]

def copy_files_with_pattern(source_folder, method, pattern):
    for metric in metrics_alias:
        file_tree = metric + "/*/" + pattern
        print(os.path.join(source_folder, file_tree))
        for file_path in glob.glob(os.path.join(source_folder, file_tree)):
            filename = "results/" + method + "/" + metric + "/" + file_path.split("/")[-2]
            print(filename)
            if not os.path.exists(filename):
                os.makedirs(filename)
            if os.path.isfile(file_path):
                target_folder = filename + "/" + method + ".csv"
                shutil.copy(file_path, target_folder)

method = "MOONF1"
source_folder = "/home/joannagrzyb/work/DE-Forest/results/experiment1/raw_results"
copy_files_with_pattern(source_folder, method, 'DE_Forest.csv')

method = "MOONF2"
source_folder = "/home/joannagrzyb/work/MOOforest/results/experiment1/raw_results"
copy_files_with_pattern(source_folder, method, 'MOOforest.csv')

# method = "DT"
# source_folder = "/home/joannagrzyb/work/MOOforest/results/experiment1/raw_results"
# copy_files_with_pattern(source_folder, method, 'DT.csv')

# method = "RF"
# source_folder = "/home/joannagrzyb/work/MOOforest/results/experiment1/raw_results"
# copy_files_with_pattern(source_folder, method, 'RF.csv')

# method = "RF_b"
# source_folder = "/home/joannagrzyb/work/MOOforest/results/experiment1/raw_results"
# copy_files_with_pattern(source_folder, method, 'RF_b.csv')