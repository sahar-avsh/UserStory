import spacy

nlp = spacy.load('en_core_web_sm')

# todo: there should not be and/or in the statement --> atomic rule
# todo: there should not be "()" items in the statement --> minimal rule


def getReason(reason):
    doc = nlp(reason)

    reason_text = ''

    verb_count = 0

    flag_neg = False

    flag = False

    # raise error if first word is not a verb
    if not (doc[0].pos_ != 'VERB' or doc[0].dep_ != 'neg' or doc[0].dep_ != 'aux'):
        raise ValueError('Reason must start with a verb, "not" or "to".')
    elif len([chunk.text for chunk in doc.noun_chunks]) == 0:
        if len(doc) > 2:
            if doc[1].pos_ == 'AUX' and doc[1].dep_ == 'ROOT' and doc[0].pos_ == 'PART' and doc[0].dep_ == 'aux' and doc[2].pos_ == 'ADJ':
                flag = True
        else:
            raise ValueError('Reason must either consist a verb and a noun or an auxiliary verb and an adjective to be '
                             'meaningful.')

    flag = True

    if flag:
        for i in range(len(doc)):
            token = doc[i]

            if i == 0 and token.pos_ == 'PART' and token.dep_ == 'aux':
                continue

            if token.pos_ == 'VERB':
                verb_count += 1
                if verb_count > 1:
                    raise ValueError('Reason must include single item.')
                else:
                    reason_text += token.lemma_ + ' '
            else:
                if token.dep_ != 'neg':
                    reason_text += token.text + ' '
                else:
                    flag_neg = True

    return reason_text[:-1], flag_neg


if __name__ == '__main__':
    print(getReason('save time'))
