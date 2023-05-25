"""
Generate a specified number of MT542 messages to issue securities to client accounts. Read contents from a specified .txt file and generate duplicate messages
Auto increased delivering party accounts and auto-decreased receiving party accounts by 1.

"""

import os

def update_content(content, index):
    lines = content.split('\n')
    lines[2] = lines[2].replace("2000", f"{2000 + index}")
    #lines[13] = lines[13].replace("010160", f"{10160 + index:06d}")
    #lines[22] = lines[22].replace("010160", f"{10160 + index:06d}")
    lines[23] = lines[23].replace("2000", f"{2000 + index}")
    lines[28] = lines[28].replace("2000", f"{2000 + index}")
    lines[27] = lines[27].replace("38893", f"{38893 + index:06d}")
    '''
    #in the above line of code, line[2] refers to the 3rd index in the file. 
    e.g. line[2] means that line 3 in the MT542 will be the one being modified.
    This is the modification logic, we are modifying the references in the MT message
    we start with the 2000 incrementally to e.g. 7000 if we are generating 5000 message
    '''
    
    return '\n'.join(lines)

def generate_files(input_file, output_dir, num_files):
    with open(input_file, 'r') as f:
        content = f.read()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    merged_file_content = []
    
    for i in range(num_files):
        new_content = update_content(content, i + 1)
        file_name = os.path.join(output_dir, f"MT542FoP{1 + i + 1}.txt")
        #These are the names of the files to be generated
        
        with open(file_name, 'w') as f:
            f.write(new_content)
            
        merged_file_content.append(new_content)

    with open("merged.txt", 'w') as f:
        f.write('\n\n'.join(merged_file_content))

input_file = "C:/Users/dennis/Desktop/QA/KE_CSD/Python testing/mt542_issuanceFoP.txt"
#path to the input folder where the MT542 message is stored


output_dir = os.path.join(os.path.expanduser("~"), "Desktop", "3kFoPissuanceMessages")
#save the files to the desktop "Desktop". Name of the directory "12kFoPissuanceMessages"
num_files = 1000

generate_files(input_file, output_dir, num_files)


import shutil

# Define the paths of the source file 
src_path = "C:/Users/dennis/Desktop/QA/KE_CSD/Python testing/mt542_issuanceFoP.txt"
dst_folder = "C:/Users/dennis/Desktop/3kFoPissuanceMessages"

# Use the shutil module's copy2() function to copy the file
shutil.copy2(src_path, dst_folder)




# Define path for the destination folder and the destination folder
desktop_path = os.path.expanduser("C:/Users/dennis/Desktop")
folder_path = os.path.join(desktop_path, "C:/Users/dennis/Desktop/3kFoPissuanceMessages")

# Check if the folder exists
if not os.path.exists(folder_path):
    print(f"Folder '{folder_path}' does not exist.")
else:
    # Get a list of all files in the folder
    file_names = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]

    # Set the path for the 'merged11.txt' file
    #name of the new file that will be created
    merged_file_path = os.path.join(folder_path, "3k_FoP_issuance_messages.txt")

    # Merge the contents of the files into 'merged11.txt'
    with open(merged_file_path, "w") as merged_file:
        for file_name in file_names:
            with open(os.path.join(folder_path, file_name), "r") as file_to_merge:
                content_to_merge = file_to_merge.read()
                merged_file.write(content_to_merge)
                merged_file.write("\n")

    print(f"New merged file created: {merged_file_path}")
    print("************************************************")
    print("************************************************")
    print("************************************************")
    print("************************************************")
    print("************************************************")
    print("***************OPERATION DONE*******************")

