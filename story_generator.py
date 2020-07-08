from random import randint
import copy
#Create a dictionary of words of the type you will use in the story

word_dict = {
    'adjective':['greedy','delicious','super','groovy','rich','harsh','tasty','slow'], 
    'city name':['Bengaluru','Mysuru','Hyderabad','Chennai','Mumbai','Delhi'], 
    'noun':['people','map','music','dog','dosa','ball','pizza','salad'], 
    'action verb':['run','fall','crawl','scurry','cry','watch','swim','jump','bounce'], 
    'sports noun':['football','cricket','hockey','vollyball','baseball','scoreboard','dart']
}



# Select a story and insert placeholders for the words you want to randomly select. You can make your own random story.

story = (
    "One day my {} friend and I decided to go to the {} game in {}. "+
    "We really wanted to see the {} play the {}. So, we {} our {} "+ 
    "down to the {} and bought some {}s. We got into the game and "+
    "it was a lot of fun. We ate some {} {} and also some {} {}. "+
    "We had a great time! We plan to go again next year!"
)



# Create a function that will randomly select a word from the word_dict by type of word

def get_word(type, local_dict):
    ''' get a random word from the word_dict based on word type '''
    words = local_dict[type]
    cnt = len(words)-1
    index = randint(0, cnt)
    return local_dict[type].pop(index)

# Create a function that will insert a random word of the appropriate type into the story

def create_story():
    ''' create a random story from word dict '''
    # create a local copy of the dict so that we can pop words as used
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('adjective', local_dict), 
        get_word('sports noun', local_dict),
        get_word('city name', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('action verb', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict)
)

# Now, you can create any random stories

story1 = create_story()
story2 = create_story()

print("STORY1: \n")
print(story1)
print("STORY2: \n")
print(story2)