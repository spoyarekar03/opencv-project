import os

def generate_negative_description_file():
    # open the output file for writing. Thiswill overwrite all existing data in there
    with open('neg.txt', 'w') as f:
        # loop over all the filenames
        for filename in os.listdir('negative'):
            f.write('negative/' + filename + '/n')


# --- RUN THE FOLLOWING LINES ON PYTHON INTERPRETER ---
# >>> from cascadeutils import generate_negative_description_file
# >>> generate_negative_description_file()
# >>> exit()

# --- GENERATE POSITIVE DESCRIPTION FILE USING THE FOLLOWING: ---
# $ C:/Users/shrey/Downloads/opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=pos.txt --images=positive/

# You click once to set the upper left corner, then again to set the lower right corner.
# Press 'c' to confirm.
# Or 'd' to undo the previous confirmation.
# When done, click 'n' to move to the next image.
# Press 'esc' to exit.
# Will exit automatically when you've annotated all of the images

# --- GENERATE POSITIVE SAMPLES FROM THE ANNOTATIONS TO GET A VECTOR FILE USING: ---
# $ C:/Users/shrey/Downloads/opencv/build/x64/vc15/bin/opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 1000 -vec pos.vec

# --- TRAIN THE CASCADE CLASSIFIER MODEL USING: ---
# $ C:/Users/shrey/Downloads/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -numPos 200 -numNeg 100 -numStages 10 -w 24 -h 24

# --- MY FINAL CLASSIFIER TRAINING ARGUMENTS: ---
# $ C:/Users/shrey/Downloads/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -precalcValBufSize 6000 -precalcIdxBufSize 6000 -numPos 200 -numNeg 1000 -numStages 12 -w 24 -h 24 -maxFalseAlarmRate 0.4 -minHitRate 0.999