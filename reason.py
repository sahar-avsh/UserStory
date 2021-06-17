import spacy
import re

nlp = spacy.load('en_core_web_lg')


def getReason(reason):
    """
     :param reason:
     :param demand:
    This function accepts a reason (string) which should either start with a verb, "Auxiliary verb" or "not". The verb should either display as
    simple verb or continuous verb.
    For example earn, earning, to earn, get earned, not earn

    :return:
    It turns(String) continuous form of verb to a simple verb, it removes "to" and "not" and returns the other versions untouched
    For example:
    earn money --> earn money
    earning money --> earn money
    to earn money --> earn money
    get money --> get money
    not earn --> earn

    """
    doc = nlp(reason)

    reason_text = ''

    verb_count = 0

    flag_neg = False
    # This is a pattern to catch the parenthesis
    pattern = "[\(\)]"
    p = re.compile(pattern)
    found = re.search(p, reason)
    # If statement to work in case user had added any parenthesis
    if found:
        raise ValueError('Please do not specify anything more than a reason to keep requirement minimal.')
    # raise error if first word is not a verb, not, to
    if doc[0].pos_ != 'VERB' and doc[0].pos_ != 'AUX' and doc[0].dep_ != 'neg' and doc[0].dep_ != 'aux':
        raise ValueError('Reason must start with a verb, "not" or "to".')
    # Scenario 1: first word pos, dep --> PART, aux (to) / second word pos --> AUX, auxpass (get)
    # Scenario 2: first word pos, dep --> PART, aux (to) / second word pos --> VERB, root (any kind of verb)
    # Scenario 3: first word pos, dep --> AUX, auxpass (get) / second word pos --> VERB, root (any kind of verb)
    if len(doc) > 2 and doc[0].pos_ != 'VERB' and doc[0].dep_ != 'neg':
        if (doc[0].pos_ == 'PART' and doc[0].dep_ == 'aux' and doc[1].pos_ == 'AUX' and doc[1].dep_ == 'auxpass' and doc[2].pos_ == 'VERB') or (doc[0].pos_ == 'PART' and doc[0].dep_ == 'aux' and doc[1].pos_ == 'VERB') or (doc[0].pos_ == 'AUX' and doc[1].pos_ == 'VERB'):
            pass
        else:
            raise ValueError('Reason must start with a verb, "not" or "to".')
    # It iterates over the sentence to test it in case of atomic law
    for i in range(len(doc)):
        token = doc[i]
        # Raise an error in case user had used words "and" or "or"
        if token.pos_ == 'CONJ' or token.pos_ == 'CCONJ':
            raise ValueError('Reason must include single item to achieve atomic property.')

        if i == 0 and token.pos_ == 'PART' and token.dep_ == 'aux':
            continue
        if token.pos_ == 'VERB':
            verb_count += 1
            # Raise an error in case there is multiple verbs
            if verb_count > 1:
                raise ValueError('reason must include single item to achieve atomic property.')
            else:
                try:
                    # This line of code adds auxiliary verbs untouched
                    if token.nbor(-1).pos_ == 'AUX':
                        reason_text += token.text + ' '
                    # This line of code turns continuous verb into simple verb
                    else:
                        reason_text += token.lemma_ + ' '
                except IndexError:
                    reason_text += token.lemma_ + ' '
       # This line of code adds reason in case it is not negative
        else:
            if token.dep_ != 'neg':
                reason_text += token.text + ' '
                # This line of code turns not flag true
            else:
                flag_neg = True

    return reason_text[:-1], flag_neg


if __name__ == '__main__':
    print(getReason('dog bed'))
