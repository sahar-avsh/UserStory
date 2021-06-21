import spacy
import re
import numpy as np

nlp = spacy.load('en_core_web_lg')


def getDemand(demand):
    """
     :param demand:
    This function accepts a demand (string) which should either start with a verb, "Auxiliary verb" or "not". The verb should either display as
    simple verb or continuous verb.
    For example earn, earning, to earn, get earned, not earn

    :return:
    It turns (string) continuous form of verb to a simple verb, it removes "to"  and returns the other versions untouched
    For example:
    earn money --> earn money
    earning money --> earn money
    to earn money --> earn money
    get money --> get money
    to get money --> get money
    not earn money --> not earn money

    """
    doc = nlp(demand)

    demand_text = ''

    verb_count = 0
    # This is a pattern to catch the parenthesis
    pattern = "[\(\)]"
    p = re.compile(pattern)
    found = re.search(p, demand)
    # raise error in case there is a parenthesis
    if found:
        raise ValueError('Please do not specify anything more than a demand to keep requirement minimal.')
    # raise error if first word is not a verb, Auxiliary, not
    if doc[0].pos_ != 'VERB' and doc[0].pos_ != 'AUX' and doc[0].dep_ != 'neg' and doc[0].dep_ != 'aux':
        raise ValueError('Demand must start with a verb, "not" or "to".')
    # Scenario 1: first word pos, dep --> PART, aux (to) / second word pos --> AUX, auxpass (get)
    # Scenario 2: first word pos, dep --> PART, aux (to) / second word pos --> VERB, root (any kind of verb)
    # Scenario 3: first word pos, dep --> AUX, auxpass (get) / second word pos --> VERB, root (any kind of verb)
    if len(doc) > 2 and doc[0].pos_ != 'VERB' and doc[0].dep_ != 'neg':
        if (doc[0].pos_ == 'PART' and doc[0].dep_ == 'aux' and doc[1].pos_ == 'AUX' and doc[1].dep_ == 'auxpass' and
            doc[2].pos_ == 'VERB') or (
                doc[0].pos_ == 'PART' and doc[0].dep_ == 'aux' and doc[1].pos_ == 'VERB') or (
                doc[0].pos_ == 'AUX' and doc[1].pos_ == 'VERB'):
            pass
        else:
            raise ValueError('Demand must start with a verb, "not" or "to".')

    flag_split = False
    for token in doc:
        if token.pos_ == 'CONJ' or token.pos_ == 'CCONJ':
            docs = [nlp(i.strip()) for i in demand.split('and')]
            if len(docs) > 1:
                flag_split = True
            else:
                docs = [nlp(i.strip()) for i in demand.split('or')]
                flag_split = True

    if flag_split:
        demands = []
        for j in docs:

            # It iterates over the sentence to test it in case of atomic law
            for i in range(len(j)):
                token = j[i]

                if token.pos_ == 'VERB':
                    verb = token.text
                elif token.text == 'to':
                    continue

                # # Raise an error in case user had used words "and" or "or"
                # if token.pos_ == 'CONJ' or token.pos_ == 'CCONJ':
                #     raise ValueError('Demand must include single item to achieve atomic property.')
                # # Raise an error in case there is multiple verbs
                # if token.pos_ == 'VERB' and token.dep_ != 'compound':
                #     verb_count += 1
                #     if verb_count > 1:
                #         raise ValueError('Demand must include single item to achieve atomic property.')

                # This line of code turns continuous verb into simple verb
                if i == 0:
                    if np.array([t.pos_ != 'VERB' for t in j]).all():
                        demand_text += verb + ' ' + token.text + ' '
                    else:
                        demand_text += token.lemma_ + ' '
                # It adds it untouched otherwise
                else:
                    demand_text += token.text + ' '

            demands.append(demand_text[:-1])
            demand_text = ''

        return demands

    else:
        for i in range(len(doc)):
            token = doc[i]

            if token.text == 'to':
                continue

            # # Raise an error in case user had used words "and" or "or"
            # if token.pos_ == 'CONJ' or token.pos_ == 'CCONJ':
            #     raise ValueError('Demand must include single item to achieve atomic property.')
            # # Raise an error in case there is multiple verbs
            # if token.pos_ == 'VERB' and token.dep_ != 'compound':
            #     verb_count += 1
            #     if verb_count > 1:
            #         raise ValueError('Demand must include single item to achieve atomic property.')

            # This line of code turns continuous verb into simple verb
            if i == 0:
                demand_text += token.lemma_ + ' '
            # It adds it untouched otherwise
            else:
                demand_text += token.text + ' '
        return [demand_text[:-1]]


if __name__ == '__main__':
    print(getDemand('to drink water and not to drink juice'))

