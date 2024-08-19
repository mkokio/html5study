#sorting
def sort_chapters_and_questions():
    questions = Question.objects.annotate(
        chapter_number=Cast(Substr('question_code', 1, 1), IntegerField()),
        question_number=Cast(Substr('question_code', 3), IntegerField())
    ).order_by('chapter_number','question_number')

    return questions

#remove duplicates
def remove_duplicates_by_attribute(queryset, attribute):
    seen = set()
    return [item for item in queryset if not (getattr(item, attribute) in seen or seen.add(getattr(item, attribute)))]
        # This list comprehension includes each item in queryset only if its attribute value has not been 'seen' before.
            # Iterate over each item object in queryset and check if the following condition is "not True":
                # Check if the attribute value of the current item is already in the 'seen' set (True):
                    # **If this is True, the entire condition evaluates to True** 
                    # Thus, DON'T ADD this item to the returned list.
                # If the attribute value is not already in the 'seen' set (False):
                    # The 'seen.add(item.attribute)' method is executed, which adds the attribute value to the 'seen' set.
                    # **The add method returns 'None', which is equivalent to 'False' in a boolean context;**
                    # Therefore, the condition evaluates to False, and the item is added to the returned list.

        #seen = set()
        #create an object named 'seen'
        #unique_vocab_list = [vocab for vocab in vocab_list if not (vocab.japanese_word in seen or seen.add(vocab.japanese_word))]
        #this list comprehension includes each vocab in unique_vocab_list only if its japanese_word has not been 'seen' before.
            #iterate over each vocab object in vocab_list and check if the following point is "not True"
                #check if the japanese_word of the current vocab is already in the seen set (True)
                    #**If this is True, the entire condition is True** DON'T ADD vocab.japanese_word to 'unique_vocab_list'
                #if the vocab.japanese_word is not already in the seen set (False)
                    #then seen.add(vocab.japanese_word) is executed
                        # **This will return 'None' which is the same as 'False'; the entire condition is False** ADD vocab.japanese_word to 'unique_vocab_list'