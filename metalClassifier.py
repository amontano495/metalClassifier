import os

def imageExtractor(path):
    label = 0

    classes = sorted(os.walk(path).__next__()[1])
    labels = []
    imagepaths = []

    for classID in classes:
        class_dir = os.path.join(path, classID)
        walk = os.walk(class_dir).__next__()

        for sample in walk[2]:
            if sample.endswith('.jpg'):
                imagepaths.append(os.path.join(class_dir,sample))
                labels.append(label)
        label = label + 1

    return labels, imagepaths

labels,images = imageExtractor("./dataset/")


