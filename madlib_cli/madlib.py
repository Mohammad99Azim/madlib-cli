import re ,time


def read_template(path):
    with open(path) as f:
        myText = f.read()
    return myText


def parse_template(file_text):
    result1 = re.findall('\{([A-Za-z0-9_]+)\}', file_text)
    result1 = tuple(result1)

    result2 = re.split('\{.*?\}', file_text)
    result2 = '{}'.join(result2)
    return result2, result1


def merge(the_text_string, text_tup):
    txt3 = the_text_string.format(*text_tup)
    return txt3


def welcoming():
    return ("""
    Hello Welcome in Madlib Game
    The Game Will Ask You To write Some Nouns Adjective Firsts Names etc... 
    Write What The Game Ask You Then Press Enter When You
    Finish You Will Have A Funny Text To Read :)

    Let's Start 
    """)


def get_inputs():
    listWords = []

    listWords += [input("Enter An Adjective: ")]
    listWords += [input("Enter An Adjective: ")]
    listWords += [input("Enter An A First Name: ")]
    listWords += [input("Enter An Past Tense Verb: ")]
    listWords += [input("Enter An A First Name: ")]

    listWords += [input("Enter An Adjective: ")]
    listWords += [input("Enter An Adjective: ")]
    listWords += [input("Enter An Plural Noun: ")]
    listWords += [input("Enter An Large Animal: ")]
    listWords += [input("Enter An Small Animal: ")]

    listWords += [input("Enter An A Girl's Name: ")]
    listWords += [input("Enter An Adjective: ")]
    listWords += [input("Enter An Plural Noun: ")]
    listWords += [input("Enter An Adjective: ")]
    listWords += [input("Enter An Plural Noun: ")]

    listWords += [input("Enter An Number 1-50: ")]
    listWords += [input("Enter An First Name's: ")]
    listWords += [input("Enter An Number: ")]
    listWords += [input("Enter An Plural Noun: ")]
    listWords += [input("Enter An Number: ")]
    listWords += [input("Enter An Plural Noun: ")]
    tuple(listWords)
    return listWords


def write_to_file(text):
    moment = time.strftime("%Y-%b-%d__%H_%M_%S", time.localtime())
    with open(f'../assets/Output_{moment}_text.txt', 'w') as f:
        myText = f.write(text)
    return text


def all_game_functions_play(file_directory):
    print(welcoming())

    the_inputs = get_inputs()

    the_Text = read_template(file_directory)

    file_string, tup = parse_template(the_Text)

    final_text = merge(file_string, the_inputs)

    print(write_to_file(final_text))


if __name__ == "__main__":
    all_game_functions_play('../assets/make_me_a_video_game_template.txt')
