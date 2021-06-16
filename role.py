import spacy

nlp = spacy.load('en_core_web_sm')


def getRole2(role):
    doc = nlp(role)
    nouns = []

    # single word - single role
    if len(doc) == 1:
        token = doc[0]
        if token.pos_ == 'NOUN':
            nouns.append(token.lemma_)

    # multiple word - single role
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
    doc = nlp(role)
    ents = doc.ents
    flag = False

    if len(ents) > 0:
        for ent in ents:
            if ent.label_ not in ['PERSON', 'ORG']:
                roles = [noun_phrase.text for noun_phrase in doc.noun_chunks]
                flag = True
    else:
        roles = [noun_phrase.text for noun_phrase in doc.noun_chunks]
        flag = True

    if flag:
        if len(roles) > 1 or roles is None or len(roles) == 0:
            raise ValueError('You must have a single role')
        else:
            return roles
    else:
        raise ValueError('You must have a single role')


if __name__ == '__main__':
    print(getRole('a crooked dog bed manufacturer'))