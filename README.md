# AutoLocalizationTask

pip install git+https://github.com/alshargi/AutoLocalizationTask.git




from AutoLocalizationTask import CreateTaskFiles

task_path       = "./"
task_path_temp  = "./code/temp/"
task_path_input = "./input/"

#####-  update here

SAMPLES_file = "samples.csv"
DOMAIN_name   = "Travel"
LOCAL_name    = "en-US"
STYLEL_name   = "Localization"
SOURCE_name   = "xxxxxcompny"
MODALITY_name = "Text"
version = "4"
voiceId = "Faisal"
SIM = "https://i.xxxxx.com/issues/AiData-76767698"  # remove it later - test


############################################################ ---------
CreateTaskFiles( task_path, task_path_temp, task_path_input, SAMPLES_file,DOMAIN_name, 
                       LOCAL_name, STYLEL_name, 
                       SOURCE_name, MODALITY_name, 
                       version, voiceId, SIM)
#######################################################################

