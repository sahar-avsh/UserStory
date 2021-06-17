import spacy
import re

nlp = spacy.load('en_core_web_lg')


def getDemand(demand):
    doc = nlp(demand)

    demand_text = ''

    verb_count = 0

    pattern = "[\(\)]"
    p = re.compile(pattern)
    found = re.search(p, demand)

    if found:
        raise ValueError('Please do not specify anything more than a demand to keep requirement minimal.')

    # raise error if first word is not a verb
    if doc[0].pos_ != 'VERB':
        raise ValueError('Demand must start with a verb.')
    else:
        for i in range(len(doc)):
            token = doc[i]

            if token.pos_ == 'CONJ' or token.pos_ == 'CCONJ':
                raise ValueError('Demand must include single item to achieve atomic property.')

            if token.pos_ == 'VERB' and token.dep_ != 'compound':
                verb_count += 1
                if verb_count > 1:
                    raise ValueError('Demand must include single item to achieve atomic property.')

            if i == 0:
                demand_text += token.lemma_ + ' '
            else:
                demand_text += token.text + ' '

    return demand_text[:-1]


if __name__ == '__main__':
    print(getDemand('sell dog beds (to cats as well)'))