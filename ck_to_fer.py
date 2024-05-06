ck_to_fer_dict = {
    0: 3,   # 生气 -> 高兴
    1: 4,   # 厌恶 -> 悲伤
    2: 2,   # 害怕 -> 害怕
    3: 0,   # 高兴 -> 生气
    4: 1,   # 悲伤 -> 厌恶
    5: 5,   # 惊讶 -> 惊讶
    6: 6    # 中性 -> 中性
}
import os

for root, dirs, files in os.walk("fer2013/fer2013/ck+.csv"):
    for dir in dirs:
        if dir.isdigit():
            old_path = os.path.join(root, dir)
            new_label = emotion_dict[int(dir)]
            new_folder = "{}/{}".format(new_label, "training")
            new_path = os.path.join(root, new_folder)
            os.renames(old_path, new_path)
