import spacy

nlp = spacy.load('en_core_web_sm')


def getRole2(role):
    """
     :param reason:
    This function accepts a role (string) as noun or compound nouns.
    For example:
    CEO, user, senior consultant, marketing advisor

    :return:
    It returns the parameter as it is in case it has been written correctly.

    """
    doc = nlp(role)
    nouns = []

    # This if statement checks if the single input is noun
    if len(doc) == 1:
        token = doc[0]
        if token.pos_ == 'NOUN':
            nouns.append(token.lemma_)

    # # This if statement handles the group of words
    else:
        compound_noun = ''
        for i in range(len(doc)):
            token = doc[i]
            # if there is a prepositional word --> ERROR
            if token.dep_ == 'prep':
                raise ValueError('Please provide your job category in its simplest form.')
            if (token.pos_ == 'NOUN' or token.pos_ == 'PROPN') and token.dep_ == 'compound':
                compound_noun += token.text + ' '
            # multiple words - multiple roles --> ERROR
            elif (token.pos_ == 'NOUN' or token.pos_ == 'PROPN') and token.dep_ != 'compound':
                # if it is the first word, add it to nouns
                if i == 0:
                    nouns.append(token.lemma_)
                # if it is not the first word, add it to compound noun
                else:
                    compound_noun += token.text
                    nouns.append(compound_noun)
                    compound_noun = ''

    if len(nouns) > 1 or len(nouns) == 0:
        raise ValueError('You must have a single role.')
    else:
        return nouns
    # return nouns


def getRole(role):
    """
     :param reason:
    This function accepts a role (string) as noun or compound nouns.
    For example:
    CEO, user, senior consultant, marketing advisor

    :return:
    It returns the parameter as it is in case it has been written correctly.

    """
    doc = nlp(role)
    ents = doc.ents
    flag = False
    # This if statement handles the group of words
    if len(ents) > 0:
        for ent in ents:
            # Code doesn't accept personal or organization name, so this line checks fo that
            # For example user can not enter an input as "James" or "apple"
            if ent.label_ not in ['PERSON', 'ORG']:
                roles = [noun_phrase.text for noun_phrase in doc.noun_chunks]
                flag = True
    # This if statement handles the single word
    else:
        roles = [noun_phrase.text for noun_phrase in doc.noun_chunks]
        flag = True

    if flag:
        # This line of code raises an error, in case user does not give any role or more than one role
        if len(roles) > 1 or roles is None or len(roles) == 0:
            raise ValueError('You must have a single role')
        else:
            return roles
    else:
        raise ValueError('You must have a single role')


if __name__ == '__main__':
    print(getRole('a crooked dog bed manufacturer'))