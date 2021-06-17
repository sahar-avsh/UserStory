import spacy
import re

nlp = spacy.load('en_core_web_sm')


def getReason(reason):
    doc = nlp(reason)

    reason_text = ''

    verb_count = 0

    flag_neg = False

    pattern = "[\(\)]"
    p = re.compile(pattern)
    found = re.search(p, reason)

    if found:
        raise ValueError('Please do not specify anything more than a reason to keep requirement minimal.')

    # raise error if first word is not a verb, not, to
    if doc[0].pos_ != 'VERB' and doc[0].dep_ != 'neg' and doc[0].dep_ != 'aux':
        raise ValueError('Reason must start with a verb, "not" or "to".')

    # Scenario 1: first word pos, dep --> PART, aux (to) / second word pos --> AUX, auxpass (get)
    # Scenario 2: first word pos, dep --> PART, aux (to) / second word pos --> VERB, root (any kind of verb)
    if len(doc) > 2:
        if (doc[0].pos_ == 'PART' and doc[0].dep_ == 'aux' and doc[1].pos_ == 'AUX' and doc[1].dep_ == 'auxpass' and doc[2].pos_ == 'VERB') or (doc[0].pos_ == 'PART' and doc[0].dep_ == 'aux' and doc[1].pos_ == 'VERB'):
            pass
        else:
            raise ValueError('Reason must start with a verb, "not" or "to".')

    for i in range(len(doc)):
        token = doc[i]

        if token.pos_ == 'CONJ' or token.pos_ == 'CCONJ':
            raise ValueError('Reason must include single item to achieve atomic property.')

        if i == 0 and token.pos_ == 'PART' and token.dep_ == 'aux':
            continue

        if token.pos_ == 'VERB':
            verb_count += 1
            if verb_count > 1:
                raise ValueError('Reason must include single item.')
            else:
                try:
                    if token.nbor(-1).pos_ == 'AUX':
                        reason_text += token.text + ' '
                    else:
                        reason_text += token.lemma_ + ' '
                except IndexError:
                    reason_text += token.lemma_ + ' '

        else:
            if token.dep_ != 'neg':
                reason_text += token.text + ' '
            else:
                flag_neg = True

    return reason_text[:-1], flag_neg


if __name__ == '__main__':
    print(getReason('to earn money'))

