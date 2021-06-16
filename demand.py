import spacy

nlp = spacy.load('en_core_web_lg')

# todo: there should not be and/or in the statement --> atomic rule
# todo: there should not be "()" items in the statement --> minimal rule


def getDemand(demand):
    doc = nlp(demand)

    demand_text = ''

    verb_count = 0

    # raise error if first word is not a verb
    if doc[0].pos_ != 'VERB':
        raise ValueError('Demand must start with a verb.')
    else:
        for i in range(len(doc)):
            token = doc[i]

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
    print(getDemand('sell dog beds'))