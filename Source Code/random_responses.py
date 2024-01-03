import random

def random_string():
    random_list = [
        "Pasensiya na ngunit hindi ko alam ang iyong nilagay, maaari mo ba itong ulitin?",
        "Sa palagay ko may nasabi kang hindi ko naintindihan, maaari mo ba itong ulitin?",
        "Hindi ko naintindihan ang iyong sinabi, puwede mo bang ulitin ang iyong sagot?",
        "Pasensya na, hindi ko nakuha ang sapat na impormasyon. Pwede mo bang sagutin ulit?"
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]
