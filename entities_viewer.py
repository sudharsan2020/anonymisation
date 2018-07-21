from spacy import displacy

import warnings

from generate_trainset.extract_node_values import get_paragraph_from_file
from generate_trainset.match_acora import get_acora_object, get_matches
from generate_trainset.match_patterns import find_address_in_block_of_paragraphs
from generate_trainset.normalize_offset import normalize_offsets
from ner.model_factory import get_empty_model
from resources.config_provider import get_config_default

warnings.filterwarnings('ignore')

config_training = get_config_default()
model_dir_path = config_training["model_dir_path"]
xml_dev_path = config_training["xml_dev_path"]
nlp = get_empty_model(load_labels_for_training=False)
nlp = nlp.from_disk(model_dir_path)

DEV_DATA = get_paragraph_from_file(xml_dev_path,
                                   keep_paragraph_without_annotation=True)

all_docs_to_view = list()
last_case_spans = dict()
last_case_docs = list()
former_case_id = ""
for (case_id, original_text, _, _) in DEV_DATA[0:10000]:
    if case_id != former_case_id:
        last_case_matcher = get_acora_object(content=list(last_case_spans.keys()),
                                             ignore_case=True)
        if len(last_case_docs) > 1:
            doc_text, empty_offsets = zip(*[(doc.text, []) for doc in last_case_docs])
            last_document_offsets = find_address_in_block_of_paragraphs(texts=list(doc_text),
                                                                        offsets=list(empty_offsets))

            for last_case_doc, address_offset in zip(last_case_docs, last_document_offsets):
                matches = get_matches(matcher=last_case_matcher,
                                      text=last_case_doc.text,
                                      tag="UNKNOWN")
                matcher_offsets = list()
                for start_offset, end_offset, _ in matches:
                    span_text = last_case_doc.text[start_offset:end_offset]
                    # print(span_text)
                    type_name = last_case_spans[span_text.lower()]
                    matcher_offsets.append((start_offset, end_offset, type_name))

                matcher_offsets_normalized = normalize_offsets(matcher_offsets + address_offset)

                spacy_matcher_offset = list()
                for start_offset, end_offset, type_name in matcher_offsets_normalized:
                    # https://spacy.io/usage/linguistic-features#section-named-entities
                    span_doc = last_case_doc.char_span(start_offset, end_offset, label=type_name)
                    if span_doc is not None:
                        # span will be none if the word is incomplete
                        spacy_matcher_offset.append(span_doc)
                    else:
                        print("ERROR char offset", last_case_doc.text[start_offset:end_offset])

                all_offsets = set(last_case_doc.ents)
                all_offsets.update(spacy_matcher_offset)
                last_case_doc.ents = all_offsets
                all_docs_to_view.append(last_case_doc)

        last_case_spans.clear()
        last_case_docs.clear()
        former_case_id = case_id
    spacy_doc = nlp(original_text)
    # doc.user_data['title'] = case_id
    all_docs_to_view.append(spacy_doc)
    last_case_docs.append(spacy_doc)
    entities_span = [(ent.text.lower(), ent.label_) for ent in spacy_doc.ents]
    last_case_spans.update(entities_span)


colors = {'PARTIE_PP': '#ff9933',
          'ADRESSE': '#ff99cc',
          'PARTIE_PM': '#00ccff',
          'AVOCAT': '#ccffcc',
          'MAGISTRAT': '#ccccff',
          'GREFFIER': '#ccccff'}
options = {'ents': None, 'colors': colors}
displacy.serve(all_docs_to_view, style='ent', minify=True, port=5000, options=options)